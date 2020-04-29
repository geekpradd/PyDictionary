## PyDictionary: A "Real" Dictionary Module for Python

[![Build Status](http://img.shields.io/travis/geekpradd/PyDictionary/master.svg?style=flat-square)](https://travis-ci.org/geekpradd/PyDictionary)
[![Latest Version](http://img.shields.io/pypi/v/PyDictionary.svg?style=flat-square)](https://pypi.python.org/pypi/PyDictionary/)
[![License](https://img.shields.io/pypi/l/PyDictionary.svg?style=flat-square)](https://pypi.python.org/pypi/PyDictionary/)
[![Downloads](https://img.shields.io/pypi/dm/PyDictionary.svg?style=flat-square)](https://pypi.python.org/pypi/PyDictionary/)

PyDictionary is a Dictionary Module for Python 2/3 to get meanings, translations, synonyms and Antonyms of words. It uses WordNet for getting meanings, Google for translations, and thesaurus.com for getting synonyms and antonyms. 

This module uses Python Requests, BeautifulSoup4 and goslate as dependencies

UPDATE: I will be reworking this plugin to ensure that this works as of May 2020. Please stay tuned! The work of various PRs and some modifications from my side will be pushed to the PyPi repository as well. Thanks!

### Installation

Installation is very simple through pip (or easy_install)

For pip

```
pip install PyDictionary
```

For Easy_Install

```
easy_install  PyDictionary
```

### Usage

PyDictionary can be utilised in 2 ways, either by creating a dictionary instance which can take words as arguments or by creating a dictionary instance with a fixed amount of words.

For example,

```python
from PyDictionary import PyDictionary
dictionary = PyDictionary()
```

This is will create a local instance of the PyDictionary class and now it can be used to get meanings, translations etc.

```python
print (dictionary.meaning("indentation"))
```

This will return a dictionary containing the meanings of the word. 
For example the above code will return:

```
{'Noun': ['a concave cut into a surface or edge (as in a coastline', 'the
 formation of small pits in a surface as a consequence of corrosion', 'th
e space left between the margin and the start of an indented line', 'the 
act of cutting into an edge with toothlike notches or angular incisions']
}                                                                        
```
The dictionary keys are the different types of the word. If a word is both a verb and a noun then there will be 2 keys:'Noun' and 'Verb'.
Each key refers to a list containing the meanings


For Synonyms,

```python
print (dictionary.synonym("Life"))
```

This will return a list containing the Synonyms of the word.

For Antonyms,

```python
print (dictionary.antonym("Life"))
```
This will return a list containing the Antonyms of the word.

For Translations,

```python
print (dictionary.translate("Range",'es'))
```

This will return the Translation of the word "Range" in Spanish. For Language codes consult Google Translate. The return value is String in Python 3 and Unicode in Python 2

Alternatively, you can set a fixed number of words to the PyDictionary Instance. This is useful if you just want to get the meanings of some words quickly without any development need.

Example:

```python
from PyDictionary import PyDictionary

dictionary = PyDictionary("hotel","ambush","nonchalant","perceptive")
'There can be any number of words in the Instance'

print(dictionary.printMeanings()) '''This print the meanings of all the words'''
print(dictionary.getMeanings()) '''This will return meanings as dictionaries'''
print (dictionary.getSynonyms())

print (dictionary.translateTo("hi")) '''This will translate all words to Hindi'''

```

Similarly Synonyms and Antonyms can also be printed onto the screen.

### Using the PyDictionary API

You can use the PyDictionary API for the above functions as well which just outputs the result of the above functions as JSON.

It's very easy to use and it returns Meanings, Antonyms, Synonyms and Translations in JSON. It runs on Red Hat Open Shift Servers and it uses Flask.

#### Usage

For meanings,

```
http://pydictionary-geekpradd.rhcloud.com/api/meaning/[word]
```

For Antonyms,

```
http://pydictionary-geekpradd.rhcloud.com/api/antonym/[word]
```

For Synonyms,

```
http://pydictionary-geekpradd.rhcloud.com/api/synonym/[word]
```
For Translations,

```
http://pydictionary-geekpradd.rhcloud.com/api/translate/[code]/[word]
```

Replace word with the word parameter and 'code' with the Google Translate Language code

You can view the source here: <a href="https://github.com/geekpradd/PyDictionary-Flask-API">PyDictionary Flask</a>



### About

The source is in the source.py file. Feel free to check it out.

Created By Pradipta. Copyright 2019
