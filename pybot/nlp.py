import nltk
from nltk.stem import RSLPStemmer
from .util import read_json_file

stemmer = RSLPStemmer()

TRAINING_DATA = []
CORPUS_WORDS = {}
CLASS_WORDS = {}


def train(train_data_file):
    data = read_json_file(train_data_file)

    for item in data:
        class_name = item['class']
        sentences = item['sentences']
        for sentence in sentences:
            TRAINING_DATA.append({'class': class_name, 'sentence': sentence})

    classes = list(set([a['class'] for a in TRAINING_DATA]))

    for c in classes:
        CLASS_WORDS[c] = []

    for data in TRAINING_DATA:
        for word in nltk.word_tokenize(data['sentence']):
            if word not in ["?", "'s"]:
                stemmed_word = stemmer.stem(word.lower())
                if stemmed_word not in CORPUS_WORDS:
                    CORPUS_WORDS[stemmed_word] = 1
                else:
                    CORPUS_WORDS[stemmed_word] += 1

                CLASS_WORDS[data['class']].extend([stemmed_word])


def calculate_class_score(sentence, class_name, show_details=False):
    score = 0

    for word in nltk.word_tokenize(sentence):

        if stemmer.stem(word.lower()) in CLASS_WORDS[class_name]:

            score += (1 / CORPUS_WORDS[stemmer.stem(word.lower())])

            if show_details:
                print("   match: %s (%s)" % (stemmer.stem(word.lower()),
                                             1 / CORPUS_WORDS[stemmer.stem(word.lower())]))
    return score


def classify(sentence):
    high_class = None
    high_score = 0
    # loop through our classes
    for c in CLASS_WORDS.keys():
        # calculate score of sentence for each class
        score = calculate_class_score(sentence, c)
        # keep track of highest score
        if score > high_score:
            high_class = c
            high_score = score

    return high_class, high_score
