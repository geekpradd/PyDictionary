##PyDictionary: A "Real" Dictionary Module for Python

PyDictionary is a Dictionary Module for Python 2/3 to get meanings, translations, synonyms and Antonyms of words. It uses Google for getting meanings and translations, and thesaurus.com for getting synonyms and antonyms. 

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

This will print out the meaning along with the name of the word and it's type. Incase, you want to get only the meaning (for development purpose) add a parameter `formatted=False` to get only the meaning.

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

print(dictionary.getMeanings()) '''This print the meanings of all the words'''

print (dictionary.getSynonyms())

print (dictionary.translateTo("hi")) '''This will translate all words to Hindi'''

```

Similarly Synonyms and Antonyms can also be printed onto the screen.

###About

The source is in the source.py file. Feel free to check it out.

Created By Pradipta. Copyright 2014
