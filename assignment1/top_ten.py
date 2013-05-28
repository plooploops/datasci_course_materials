import sys
import json
import urllib
import operator


hashTags = {}    
def applyScores(tweet_file):
    data = []
    with open(tweet_file) as f:
      for line in f:
        data.append(json.loads(line))    

    for i in range(len(data)):      
      entities = data[i].get('entities')
      encodedHashtag = ""
      #print entities
      hashtags = entities["hashtags"]
      if hashtags:
        for j in range(len(hashtags)):
          hashtagText = hashtags[j]["text"]
          if hashtagText:
            encodedHashtag = hashtagText.encode('utf-8')
            if not encodedHashtag in hashTags:
              hashTags[encodedHashtag] = 1
            else: 
              hashTags[encodedHashtag] += 1
            #print encodedHashtag

    sortedTop = sorted(hashTags.iteritems(), key=lambda x:-x[1])[:10]
    #sortedTop = sorted(hashTags.iteritems(), key=operator.itemgetter(1))[:10]
    #print sortedTop
    for topHashtag in sortedTop:
      print str(topHashtag[0]) + ' ' + str(float(topHashtag[1]))
    #find the state with maximum happiness
    #print max(encodedHashtag.iteritems(), key=operator.itemgetter(1))[0]
def main():
    tweet_file_path = sys.argv[1]
    applyScores(tweet_file_path)

if __name__ == '__main__':
    main()
