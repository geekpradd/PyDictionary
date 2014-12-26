import requests
import goslate
from bs4 import BeautifulSoup

class PyDictionary:
      def __init__(self, *args):
            self.args=args
      def getMeaning(self):
            return [self.getResults(term) for term  in self.args]
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
      def __repr__(self):
            return "<PyDictionary Object with {0} words>".format(len(self.args))
      def getResults(self,term):
            if len(term.split())>1:
                  print ("Error: A Term must be only a single word")
            else:
                  try:
                        link="http://www.google.co.in/search?q=define:%3A%20{0}".format(term)
                        page=requests.get(link).text
                        html=BeautifulSoup(page)
                        body=html.find("table",{"style":"font-size:14px;width:100%"})
                        wordType=body.find("div",{"style":"color:#666;padding:5px 0"}).getText()
                        meaning=body.find("li").getText()
                        formated="{0} : {1} \n{2}\n".format(term.capitalize(),wordType,meaning)
                        return formated
                  except:
                        print("Error: The Word given is not a valid English Word")

if __name__=='__main__':
      dictionary=PyDictionary("Morning")
      results=dictionary.getMeaning()
      for result in results:
           print (result)
      
     

