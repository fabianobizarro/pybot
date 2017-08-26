#!/usr/local/bin/python
import sys
import json
from nlp import train, classify


def main():
    input =  ' '.join(sys.argv[1:])
    score = classify(input)
    print(score)


def initialize():
    train()


if __name__ == '__main__':
    initialize()
    main()
