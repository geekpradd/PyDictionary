from setuptools import setup
import PyDictionary as module
setup(name='PyDictionary',
      version=module.__version__,
      description='Python Module to get meanings, translations, synonyms and anotnyms of words',
      author=module.__author__,
      author_email='pradd@outlook.com',
      license='MIT',
      packages=['PyDictionary'],
      url="http://github.com/geekpradd/PyDictionary",
      install_requires=[
            'beautifulsoup4','goslate','requests',],
      zip_safe=False)
