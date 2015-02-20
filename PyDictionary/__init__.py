import requests
import sys
import re
import goslate
from bs4 import BeautifulSoup as bs
__author__ = "Pradipta Bora"
__version__ = "1.3.7"

python2 = False
if list(sys.version_info)[0] == 2:
    python2 = True


class PyDictionary:

    def __init__(self, *args):
        self.args = args

    def printMeanings(self):
        dic = self.getMeanings()
        for key in dic.keys():
            print(key + ':')
            for k in dic[key].keys():
                print(k + ':')
                for m in dic[key][k]:
                    print(m)

            print('\n')

    def getMeanings(self):
        out = {}
        for term in self.args:
            out[term] = self.meaning(term)
        return out

    def translateTo(self, language):
        return [self.translate(term, language) for term in self.args]

    def translate(self, term, language):
        if len(term.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                gs = goslate.Goslate()
                word = gs.translate(term, language)
                return word
            except:
                print("Invalid Word")

    def getSynonyms(self, formatted=True):
        return [self.synonym(term, formatted) for term in self.args]

    def synonym(self, term, formatted=False):
        if len(term.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                link = "http://www.thesaurus.com/browse/{0}".format(term)
                site = requests.get(link).text
                data = bs(site)
                terms = data.select("div#filters-0")[0].findAll("li")
                if len(terms) > 5:
                    terms = terms[:5:]
                li = []
                for t in terms:
                    li.append(t.select("span.text")[0].getText())
                if formatted:
                    return {term: li}
                return li
            except:
                print("{0} has no Synonyms in the API".format(term))

    def __repr__(self):
        return "<PyDictionary Object with {0} words>".format(len(self.args))
    def __getitem__(self,index):
      return self.args[index]
    def __eq__(self):
      return self.args
    def getAntonyms(self, formatted=True):
        return [self.antonym(term, formatted) for term in self.args]

    def antonym(self, word, formatted=False):
        if len(word.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                link = "http://www.thesaurus.com/browse/{0}".format(word)
                site = requests.get(link).text
                data = bs(site)
                terms = data.select("section.antonyms")[0].findAll("li")
                if len(terms) > 5:
                    terms = terms[:5:]
                li = []
                for t in terms:
                    li.append(t.select("span.text")[0].getText())
                if formatted:
                    return {word: li}
                return li
            except:
                print("{0} has no Antonyms in the API".format(word))

    def meaning(self, term):
        if len(term.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                link = "http://wordnetweb.princeton.edu/perl/webwn?s={0}".format(
                    term)
                page = requests.get(link).text
                html = bs(page)
                types = html.findAll("h3")
                length = len(types)
                lists = html.findAll("ul")
                out = {}
                for a in types:
                    reg = str(lists[types.index(a)])
                    meanings = []
                    for x in re.findall(r'\((.*?)\)', reg):
                        if 'often followed by' in x:
                            pass
                        elif len(x) > 5 or ' ' in str(x):
                            meanings.append(x)
                    # meanings = [
                    #     x for x in re.findall(r'\((.*?)\)', reg) if len(x) > 5 or ' ' in str(x) and not 'often followed by' in x]
                    name = a.text
                    
                    out[name] = meanings
                return out
            except:
                print("Error: The Word given is not a valid English Word")

    def googlemeaning(self, term, formatted=True):
        if len(term.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                link = "http://www.google.co.in/search?q=define:%3A%20{0}".format(
                    term)
                page = requests.get(link).text
                html = bs(page)
                body = html.find(
                    "table", {"style": "font-size:14px;width:100%"})
                wordType = body.find(
                    "div", {"style": "color:#666;padding:5px 0"}).getText()
                meaning = body.find("li").getText()
                formated = "{0} : {1} \n{2}\n".format(
                    term.capitalize(), wordType, meaning)
                if not formatted:
                    return meaning
                return formated
            except:
                print("Error: The Word given is not a valid English Word")

if __name__ == '__main__':
   
    print(
        "Hi there, fellow Geek. Good luck on checking the source out. It's both Python 2 and 3 compatible.\n\nPyDictionary is getting many updates and stay tuned for them. \nA Javascript Plugin and a Web API are coming")
