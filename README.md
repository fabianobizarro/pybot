# Pybot


A simple bot package in python.

This project is based on this [post](https://chatbotslife.com/text-classification-using-algorithms-e4d50dcba45)


## How to use

```python

# import the package
import pybot as bot

#define 
def greeting(*params):
    return "Hi!"


def how_are_you(*params):
    return "I'm fine and you?"


bot.train('./data.json')

bot.register_action('greeting', greeting)
bot.register_action('howareyou', how_are_you)

response = bot.interact('Hi')

print(response)

```


## Training data

The training data file used on the package follows the structure:

```json
[
    {
        "class": "greeting",
        "sentences": [
            "hi",
            "hello",
            "hey",
            "what's up"
        ]
    }
    ...
]
```

## Dependencies

[Finish here]

## Stemmer

[Finish Here]