import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pybot.bot import PyBot


class DummyStemmer(object):
    def stem(self, word):
        return word