import urllib
import json

urlPrefix = "http://search.twitter.com/search.json?q=microsoft&page="

for p in range(10):
  urlLoad = urlPrefix + str(p + 1)
  #print urlLoad	
  responses = urllib.urlopen(urlLoad)
  pyresponses = json.load(responses)
  results = pyresponses["results"]

  for i in range(len(results)):
    #print i
    unicode_string = results[i]
    print unicode_string
    #unicode_string = results[i]["text"]
    #print unicode_string.encode('utf-8')