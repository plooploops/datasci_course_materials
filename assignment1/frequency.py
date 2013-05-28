import sys
import json
import urllib

termOccurrences = {}
totalTerms = 0

def applyScores(tweet_file):
    
    totalTerms = 0
    data = []
    with open(tweet_file) as f:
      for line in f:
        data.append(json.loads(line))
    
    #[# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]
    # number of occurrences of all terms in all tweets can be calculated by looking at the total number of terms in all tweets
    for i in range(len(data)):
      unicode_string = data[i]["text"]
      encodedString = unicode_string.encode('utf-8')     
      termsList = encodedString.split()
      #print termsList
      
      
      for term in termsList:
        totalTerms += 1
        findTerm = term.strip()
        #print findTerm
      	if findTerm in termOccurrences:
      	  #print 'found'
      	  termOccurrences[findTerm] += 1
      	else:
      	  #print 'not found'
      	  termOccurrences[findTerm] = 1
      
    
    #print termOccurrences.items()
    #print totalTerms
    
    for item in termOccurrences.items():
      if len(item[0]) > 0:
        print str(item[0]) + ' ' + str(float((float(item[1])) / float(totalTerms)))

def main():
    tweet_file_path = sys.argv[1]
    applyScores(tweet_file_path)

if __name__ == '__main__':
    main()
