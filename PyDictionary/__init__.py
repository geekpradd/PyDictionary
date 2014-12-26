import requests, sys
import goslate
from bs4 import BeautifulSoup as bs
__author__="Pradipta Bora"
__version__="1.1.2"

python2=False
if list(sys.version_info)[0]==2:
      python2=True

class PyDictionary:
      
      def __init__(self, *args):
            self.args=args
      def getMeanings(self):
            return [self.meaning(term) for term  in self.args]
      def translateTo(self,language):
            return [self.translate(term,language) for term in self.args]
      def translate(self,term,language):
            if len(term.split())>1:
                  print ("Error: A Term must be only a single word")
            else:
                  try:
                        gs=goslate.Goslate()
                        word=gs.translate(term,language)
                        return word
                  except:
                        print ("Invalid Word")
      def getSynonyms(self):
            return [self.synonym(term) for term in self.args]
      def synonym(self,term):
            if len(term.split())>1:
                  print ("Error: A Term must be only a single word")
            else:
                  try:
                        link="http://www.thesaurus.com/browse/{0}".format(term)
                        site=requests.get(link).text
                        data=bs(site)
                        terms=data.select("div#filters-0")[0].findAll("li")
                        if len(terms)>5:
                              terms=terms[:5:]
                        li=[]
                        for t in terms:
                              li.append(t.select("span.text")[0].getText())
                        return {term:li}
                  except:
                        print("{0} has no Synonyms in the API".format(term))
      def __repr__(self):
            return "<PyDictionary Object with {0} words>".format(len(self.args))
      def getAntonyms(self):
            return [self.antonym(term) for term in self.args]
      def antonym(self,word):
            if len(word.split())>1:
                  print ("Error: A Term must be only a single word")
            else:
                  try:
                        link="http://www.thesaurus.com/browse/{0}".format(word)
                        site=requests.get(link).text
                        data=bs(site)
                        terms=data.select("section.antonyms")[0].findAll("li")
                        if len(terms)>5:
                              terms=terms[:5:]
                        li=[]
                        for t in terms:
                              li.append(t.select("span.text")[0].getText())
                        return {word:li}
                  except:
                        print("{0} has no Antonyms in the API".format(word))
      def meaning(self,term):
            if len(term.split())>1:
                  print ("Error: A Term must be only a single word")
            else:
                  try:
                        link="http://www.google.co.in/search?q=define:%3A%20{0}".format(term)
                        page=requests.get(link).text
                        html=bs(page)
                        body=html.find("table",{"style":"font-size:14px;width:100%"})
                        wordType=body.find("div",{"style":"color:#666;padding:5px 0"}).getText()
                        meaning=body.find("li").getText()
                        formated="{0} : {1} \n{2}\n".format(term.capitalize(),wordType,meaning)
                        return formated
                  except:
                        print("Error: The Word given is not a valid English Word")

if __name__=='__main__':
      dictionary=PyDictionary()
      print (dictionary.meaning("Triumph"))
      
     

