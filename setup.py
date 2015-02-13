from setuptools import setup
try:
    import pypandoc
    description=pypandoc.convert('README.md','rst')
except:
    description=''
setup(name='PyDictionary',
      version="1.3.7",
      description='Python Module to get meanings, translations, synonyms and antonyms of words',
      long_description=description,
      author="Pradipta Bora",
      author_email='pradd@outlook.com',
      license='MIT',
      packages=['PyDictionary'],
      url="http://github.com/geekpradd/PyDictionary",
      install_requires=[
            'beautifulsoup4','goslate','requests',],
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Topic :: Internet",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python"
      ],
      zip_safe=False)
