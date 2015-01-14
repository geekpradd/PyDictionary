from setuptools import setup

setup(name='PyDictionary',
      version="1.1.4",
      description='Python Module to get meanings, translations, synonyms and anotnyms of words',
      author="Pradipta Bora",
      author_email='pradd@outlook.com',
      license='MIT',
      packages=['PyDictionary'],
      url="http://github.com/geekpradd/PyDictionary",
      install_requires=[
            'beautifulsoup4','goslate','requests',],
      zip_safe=False)
