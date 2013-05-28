import sys
import json
import urllib

scores = {}
    
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
      for term in termsList:
        findTerm = term.strip()
        #print findTerm
      	if findTerm in scores:
      	  #print 'found'
      	  termScore += scores[findTerm]
      	else:
      	  #print 'not found'
          termScore += 0
      print float(termScore)

def main():
    sent_file_path = sys.argv[1]
    tweet_file_path = sys.argv[2]
    applyScores(sent_file_path, tweet_file_path)

if __name__ == '__main__':
    main()
