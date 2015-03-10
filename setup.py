from setuptools import setup
try:
    import pypandoc
    with open('readme-pypi.rst','r') as f:
      description = f.read()
    
except:
    description=''
setup(name='PyDictionary',
      version="1.5.2",
      description='Python Module to get meanings, translations, synonyms and antonyms of words',
      long_description=description,
      author="Pradipta Bora",
      author_email='pradd@outlook.com',
      license='MIT',
      packages=['PyDictionary'],
      url="http://github.com/geekpradd/PyDictionary",
      install_requires=[
            'beautifulsoup4','goslate','requests','click'],
      entry_points = {
    'console_scripts': ['pydictionary = PyDictionary.script:script']
    },
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Topic :: Internet",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python"
      ],
      zip_safe=False)
