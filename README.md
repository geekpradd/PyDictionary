##PyDictionary: A "Real" Dictionary Module for Python

[![Build Status](http://img.shields.io/travis/geekpradd/PyDictionary/master.svg?style=flat-square)
[![Latest Version](http://img.shields.io/pypi/v/PyDictionary.svg?style=flat-square)
[![License](https://img.shields.io/pypi/l/PyDictionary.svg?style=flat-square)](https://pypi.python.org/pypi/PyDictionary/)

PyDictionary is a Dictionary Module for Python 2/3 to get meanings, translations, synonyms and Antonyms of words. It uses WordNet for getting meanings, Google for translations, and thesaurus.com for getting synonyms and antonyms. 

This module uses Python Requests, BeautifulSoup4 and goslate as dependencies

###Installation

Installation is very simple through pip (or easy_install)

For pip

```
pip install PyDictionary
```

For Easy_Install

```
easy_install -U PyDictionary
```

###Usage

PyDictionary can be utilised in 2 ways, either by creating a dictionary instance which can take words as arguments or by creating a dictionary instance with a fixed amount of words.

For example,

```python
from PyDictionary import PyDictionary
dictionary=PyDictionary()
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

dictionary=PyDictionary("hotel","ambush","nonchalant","perceptive")
'There can be any number of words in the Instance'

print(dictionary.printMeanings()) '''This print the meanings of all the words'''
print(dictionary.getMeanings()) '''This will return meanings as dictionaries'''
print (dictionary.getSynonyms())

print (dictionary.translateTo("hi")) '''This will translate all words to Hindi'''

```

Similarly Synonyms and Antonyms can also be printed onto the screen.

##Using the PyDictionary API

I'm very happy to say that the PyDictionary API has been launched.

It's very easy to use and it returns Meanings, Antonyms, Synonyms and Translations in JSON. It runs on Red Hat Open Shift Servers and it uses Flask.

####Usage

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

##PyDictionary for Javascript

Here is a client side implmentation for the PyDictionary API in Javascript:

<a href="https://github.com/geekpradd/PyDictionary-Javascript">PyDictionary for Javascript</a>

##Apps using PyDictionary

Check this awesome pygame windows game created by RajK853 that improves your vocabulary by using PyDictionary: 

<a href="https://github.com/RajK853/Vocab/">Vocab</a>

Download link: <a href="https://raw.githubusercontent.com/RajK853/Vocab/master/Vocab%20(Exe).zip">Vocab</a>
###About

The source is in the source.py file. Feel free to check it out.

Created By Pradipta. Copyright 2014
