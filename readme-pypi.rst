PyDictionary: A "Real" Dictionary Module for Python

---------------------------------------------------



PyDictionary is a Dictionary Module for Python 2/3 to get meanings,

translations, synonyms and Antonyms of words. It uses WordNet for

getting meanings, Google for translations, and synonyms.com for getting

synonyms and antonyms.



This module uses Python Requests, BeautifulSoup4 and goslate as

dependencies



Installation

~~~~~~~~~~~~



Installation is very simple through pip (or easy\_install)



For pip



::



    pip install PyDictionary



For Easy\_Install



::



    easy_install -U PyDictionary



Usage

~~~~~



PyDictionary can be utilised in 2 ways, either by creating a dictionary

instance which can take words as arguments or by creating a dictionary

instance with a fixed amount of words.



For example,



.. code:: python



    from PyDictionary import PyDictionary

    dictionary=PyDictionary()



This is will create a local instance of the PyDictionary class and now

it can be used to get meanings, translations etc.



.. code:: python



    print (dictionary.meaning("indentation"))



This will return a dictionary containing the meanings of the word. For

example the above code will return:



::



    {'Noun': ['a concave cut into a surface or edge (as in a coastline', 'the

     formation of small pits in a surface as a consequence of corrosion', 'th

    e space left between the margin and the start of an indented line', 'the 

    act of cutting into an edge with toothlike notches or angular incisions']

    }                                                                        



The dictionary keys are the different types of the word. If a word is

both a verb and a noun then there will be 2 keys:'Noun' and 'Verb'. Each

key refers to a list containing the meanings



For Synonyms,



.. code:: python



    print (dictionary.synonym("Life"))



This will return a list containing the Synonyms of the word.



For Antonyms,



.. code:: python



    print (dictionary.antonym("Life"))



This will return a list containing the Antonyms of the word.



For Translations,



.. code:: python



    print (dictionary.translate("Range",'es'))



This will return the Translation of the word "Range" in Spanish. For

Language codes consult Google Translate. The return value is String in

Python 3 and Unicode in Python 2



Alternatively, you can set a fixed number of words to the PyDictionary

Instance. This is useful if you just want to get the meanings of some

words quickly without any development need.



Example:



.. code:: python



    from PyDictionary import PyDictionary



    dictionary=PyDictionary("hotel","ambush","nonchalant","perceptive")

    'There can be any number of words in the Instance'



    print(dictionary.printMeanings()) '''This print the meanings of all the words'''

    print(dictionary.getMeanings()) '''This will return meanings as dictionaries'''

    print (dictionary.getSynonyms())



    print (dictionary.translateTo("hi")) '''This will translate all words to Hindi'''



Similarly Synonyms and Antonyms can also be printed onto the screen.


Created By Pradipta 2020.

