#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import upper
from string import uppercase

EDICT = {'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".",
         'F': "..-.", 'G': "--.", 'H': "....", 'I': "..", 'J': ".---",
         'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.", 'O': "---",
         'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': "...", 'T': "-",
         'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-", 'Y': "-.--", 'Z': "--..",
         "0": "-----", "1": ".----", "2": "..---", "3": "...--",
         "4": "....-", "5": ".....", "6": "-....", "7": "--...",
         "8": "---..", "9": "----.", " ": "-....-"
         }

# print {value: key for key, value in EDICT.items()}

DDICT = {'---': 'O', '--.': 'G', '-...': 'B', '-..-': 'X',
         '.-.': 'R', '--.-': 'Q', '--..': 'Z', '.--': 'W',
         '..---': '2', '.-': 'A', '..': 'I', '-.-.': 'C',
         '..-.': 'F', '-.--': 'Y', '-': 'T', '.': 'E',
         '.-..': 'L', '...': 'S', '..-': 'U', '.----': '1',
         '-----': '0', '-.-': 'K', '-..': 'D', '----.': '9',
         '-....': '6', '.---': 'J', '.--.': 'P', '....-': '4',
         '--': 'M', '-.': 'N', '....': 'H', '---..': '8',
         '...-': 'V', '--...': '7', '.....': '5', '...--': '3',
         '-....-': ' '}


def morseDecode(x):
    return ''.join(map(lambda i: DDICT[i], x.split()))


def morseEncode(x):
    return ' '.join(map(lambda i: EDICT[i], list(filter(lambda i: i in uppercase, upper(x)))))


if __name__ == '__main__':
    print morseEncode('this is a test')
    print morseDecode('.. .-.. --- ...- . -.-- --- ..-')
