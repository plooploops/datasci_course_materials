import sys
import json
import urllib
import operator

scores = {}
stateScores = {}    
def applyScores(sent_file, tweet_file):
    #initalize scores
    opFile = open(sent_file)
    scores = {} # initialize an empty dictionary
    for line in opFile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.   

    #print scores.items() # Print every (term, score) pair in the dictionary
    data = []
    with open(tweet_file) as f:
      for line in f:
        data.append(json.loads(line))    

    for i in range(len(data)):
      
      location = data[i].get('place')
      encodedLocation = ""
      #print location
      if location:
        if location["country_code"] == 'US':
          full_name = location["full_name"]
          encodedLocation = full_name[-2:].encode('utf-8')
          if not encodedLocation in stateScores:
            stateScores[encodedLocation] = 0
          #print encodedLocation
      unicode_string = data[i].get('text')
      if unicode_string:
        encodedString = unicode_string.encode('utf-8')     
        termsList = encodedString.split()
        #print termsList
        termScore = 0
        for term in termsList:
          findTerm = term.strip()
          #print findTerm
          if findTerm in scores:
            #print 'found'
      	    termScore += scores[findTerm]
      	  else:
      	    #print 'not found'
            termScore += 0
      
      if encodedLocation in stateScores:
        stateScores[encodedLocation] += float(termScore)

    #print stateScores.items()
    #find the state with maximum happiness
    print max(stateScores.iteritems(), key=operator.itemgetter(1))[0]
def main():
    sent_file_path = sys.argv[1]
    tweet_file_path = sys.argv[2]
    applyScores(sent_file_path, tweet_file_path)

if __name__ == '__main__':
    main()
