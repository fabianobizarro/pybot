import nltk
from .util import read_json_file


class PyBot:

    def __init__(self, stemmer, class_words: dict = {}, corpus_words: dict = {}):

        self._actions = {}
        self._stemmer = stemmer

        self._training_data = []
        self._corpus_words = corpus_words
        self._class_words = class_words

    def register_action(self, class_name: str, method: callable):
        self._actions[class_name] = method

    def register_actions(self, actions_list: list):
        for action in actions_list:
            self.register_action(**action)

    def _get_action(self, class_name: str):
        if class_name in self._actions.keys():
            return self._actions[class_name]
        else:
            return None

    def interact(self, phrase: str):

        classification = self.classify(phrase)
        action = self._get_action(classification[0])
        response = action([phrase])

        if response is None:
            raise ValueError('Action must return a response')

        return response

    def set_stemmer(self, stemmer):
        if callable(stemmer.stem):
            self._stemmer = stemmer
        else:
            raise AttributeError("Stemmer does not have a stem() method")

    def load_data(self, class_words: dict, corpus_words: dict):
        self._class_words = class_words
        self._corpus_words = corpus_words

    @property
    def class_words(self):
        return self._class_words

    @property
    def corpus_words(self):
        return self._corpus_words

    def _calculate_class_score(self, sentence: str, class_name: str, show_details: bool = False):
        score = 0

        for word in nltk.word_tokenize(sentence):
            stemmed_word = self._stemmer.stem(word.lower())
            if stemmed_word in self._class_words[class_name]:
                score += (1 / self._corpus_words[stemmed_word])

                if show_details:
                    print("   match: %s (%s)" % stemmed_word, 1 / self._corpus_words[stemmed_word])
        return score

    def _train(self, train_data) -> None:
        """
        Train the model with the train_data
        :param train_data: A dictionary wit the training data in the format:
            {
                'class': 'your class name',
                sentences: [
                    'your sentences'
                ]
            }
        :return: None
        """
        for item in train_data:
            class_name = item['class']
            sentences = item['sentences']
            for sentence in sentences:
                self._training_data.append({'class': class_name, 'sentence': sentence})

        classes = list(set([a['class'] for a in self._training_data]))

        for c in classes:
            self._class_words[c] = []

        for data in self._training_data:
            for word in nltk.word_tokenize(data['sentence']):
                if word not in ["?", "'s"]:
                    stemmed_word = self._stemmer.stem(word.lower())
                    if stemmed_word not in self._corpus_words:
                        self._corpus_words[stemmed_word] = 1
                    else:
                        self._corpus_words[stemmed_word] += 1

                    self._class_words[data['class']].extend([stemmed_word])

    def train_file(self, train_data_file):
        data = read_json_file(train_data_file)
        self._train(data)

    def train_sentence(self, sentence, class_name):
        train_data = {
            'class': class_name,
            'sentences': [sentence]
        }
        self._train(train_data)

    def classify(self, sentence: str):
        high_class = None
        high_score = 0
        # loop through our classes
        for c in self._class_words.keys():
            # calculate score of sentence for each class
            score = self._calculate_class_score(sentence, c)
            # keep track of highest score
            if score > high_score:
                high_class = c
                high_score = score

        return high_class, high_score

