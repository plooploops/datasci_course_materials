import sys
import json
import urllib

scores = {}
newScores = {}

def applyScores(sent_file, tweet_file):
    
    #initalize scores
    opFile = open(sent_file)
    scores = {} # initialize an empty dictionary
    for line in opFile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.   

    data = []
    with open(tweet_file) as f:
      for line in f:
        data.append(json.loads(line))
    
    #print scores.items() # Print every (term, score) pair in the dictionary

    for i in range(len(data)):
      unicode_string = data[i]["text"]
      encodedString = unicode_string.encode('utf-8')     
      termsList = encodedString.split()
      #print termsList
      termScore = 0
      
      #find the sentiment of the tweet
      for term in termsList:
        findTerm = term.strip()
        #print findTerm
      	if findTerm in scores:
      	  #print 'found'
      	  termScore += scores[findTerm]
      	else:
      	  #print 'not found'
      	  if term not in newScores:
      	    newScores[term] = 0
      	  else:
      	    if termScore >= 0:
	      newScores[term] += 1
	    else:
      	      newScores[term] -= 1      
          termScore += 0
      
      for term in termsList:
        findTerm = term.strip()
        #print findTerm
        if not findTerm in scores:
          #for each of the terms that aren't found increment their value if they are positive or negative tweets
          if termScore >= 0:
            newScores[term] += 1
          else:
      	    newScores[term] -= 1      
          
      #print float(termScore)
    
    for item in newScores.items():
      if len(item[0]) > 0:
        print str(item[0]) + ' ' + "%.3f" % item[1]

def main():
    sent_file_path = sys.argv[1]
    tweet_file_path = sys.argv[2]
    applyScores(sent_file_path, tweet_file_path)

if __name__ == '__main__':
    main()
