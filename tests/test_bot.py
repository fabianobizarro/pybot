import pytest
from context import PyBot, DummyStemmer


@pytest.fixture
def bot(request):
    bot = PyBot(None)

    def cleanup():
        bot = None

    request.addfinalizer(cleanup)

    return bot


def test_initialize_bot_class(bot):
    # arrange, act
    bot = PyBot(None)

    # assert
    assert bot != None


def test_register_action(bot):
    # arrange
    action_name = 'greeting'

    def action(name): return "Hello {}".format(name)

    # act
    bot.register_action(action_name, action)
    actual_action = bot._get_action(action_name)

    # assert
    assert actual_action == action
    assert actual_action('World') == 'Hello World'


def test_register_actions(bot: PyBot):
    # arrange
    expected_actions_count = 2
    class_name1 = 'action1'

    def action1(): return 'Action 1 Method'

    class_name2 = 'action2'

    def action2(): return 'Action 2 Method'

    # act
    bot.register_actions([
        {'class_name': class_name1, 'method': action1},
        {'class_name': class_name2, 'method': action2}
    ])
    actions_count = len(bot._actions.keys())

    # assert
    assert actions_count == expected_actions_count
    assert class_name1 in bot._actions
    assert class_name2 in bot._actions


def test_set_stemmer_on_success_executes_correctly(bot: PyBot):

    # arrange
    class DummyStemmer(object):
        def stem(self):
            pass

    # act
    bot.set_stemmer(DummyStemmer())

    # assert
    assert bot._stemmer != None


def test_set_stemmer_on_exception_should_throw(bot: PyBot):
    # arrange

    # act
    with pytest.raises(Exception) as ex:
        bot.set_stemmer(None)

    # assert
    assert ex != None


def test_set_stemmer_without_stem_method_throws_exception(bot: PyBot):
    # arrange
    class DummyStemmer:
        pass

    # act
    with pytest.raises(Exception) as ex:
        bot.set_stemmer(DummyStemmer())

    # assert
    assert ex != None


def test_train(bot: PyBot):

    # arrange
    greeting_class = 'greeting'
    train_data = [
        {
            'class': greeting_class,
            'sentences': [
                'hi',
                'hello',
                'hey',
                'whats up',
                'he hello'
            ]
        }
    ]
    bot.set_stemmer(DummyStemmer())

    # act
    bot._train(train_data)

    # assert
    assert bot._corpus_words != {}
    assert 'hi' in bot._corpus_words
    assert 'hey' in bot._corpus_words
    assert 'hello' in bot._corpus_words
    assert bot.corpus_words['hello'] == 2
    assert bot._class_words != {}
    assert greeting_class in bot._class_words
    assert len(bot._class_words[greeting_class]) > 0
