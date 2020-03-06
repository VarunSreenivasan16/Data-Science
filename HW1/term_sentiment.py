import sys

def create_sent_dict(sentiment_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

        Args:
            sentiment_file (string): The name of a tab-separated file that contains
                                     all terms and scores (e.g., the AFINN file).

        Returns:
            dicitonary: A dictionary with schema d[term] = score
        """
    scores = {}
    
    #afinnfile_name = open(sys.argv[1])
    afinnfile = open(sentiment_file, 'r')
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t") # The file is tab-delimited and "\t" means tab character
        scores[term] = int(score) # Conver the score to an integer. It was parsed as a string.
    afinnfile.close()
    #print(scores.items( ))
    
    return scores

def get_tweet_sentiment(tweet, sent_scores):
    """A function that find the sentiment of a tweet and outputs a sentiment score.

            Args:
                tweet (string): A clean tweet
                sent_scores (dictionary): The dictionary output by the method create_sent_dict

            Returns:
                score (numeric): The sentiment score of the tweet
        """
    score = 0

    large_key_list = []
    large_key_size = []
    large_key_dict = {}
    
    for element in sent_scores.keys():
        if (len(element.split()) >= 2):
            large_key_list.append(element)
            large_key_size.append(len(element.split()))
    
    for j in range(1, len(large_key_list)):
        
        k = large_key_size[j]
        temp = large_key_list[j]
        m = j - 1
        
        while m >= 0 and k < large_key_size[m]:
            large_key_size[m+1] = large_key_size[m]
            large_key_list[m+1] = large_key_list[m]
            m = m -1
        large_key_size[m+1] = k
        large_key_list[m+1] = temp
    
   
    i = len(large_key_list) - 1
    while(i >=0):
        large_key_dict[large_key_list[i]] = sent_scores[large_key_list[i]]
        i = i-1
    tweet = "zealot zealous wowww"  
    #print(large_key_dict)
    for large_key in large_key_dict.keys():
        if(large_key in tweet):   
            #print(tweet)
            score += sent_scores[large_key]
            tweet = tweet.replace(large_key, "")
            if("  " in tweet):
                tweet = tweet.replace("  ", " ")
            #print(large_key)
            #print(tweet)
      
    
    senList = tweet.split()
    
    for string in senList:
        if string in sent_scores:
            score += sent_scores[string]
       
    print(score)
    return score


def term_sentiment(sent_scores, tweets_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

            Args:
                sent_scores (dictionary): A dictionary with terms and their scores (the output of create_sent_dict)
                tweets_file (string): The name of a txt file that contain the clean tweets
            Returns:
                dicitonary: A dictionary with schema d[new_term] = score
            """
    new_term_sent = {}
    term_counter = {}
    
    tweets = open(tweets_file, 'r')
    score = 0
    
    for tweet in tweets:
        score = get_tweet_sentiment(tweet, sent_scores)
        tempTweet = tweet.split()
        for string in tempTweet:
            if string not in sent_scores:
               
                if string in new_term_sent:
                    new_term_sent[string] += score
                    term_counter[string] += 1
                else:
                    
                    new_term_sent[string] = score
                    term_counter[string] = 1
    
    for element in new_term_sent:
        new_term_sent[element] = round(float(new_term_sent[element]/term_counter[element]),3)
    
    return new_term_sent


def main():
    sentiment_file = sys.argv[1]
    tweets_file = sys.argv[2]

    # Read the AFINN-111 data into a dictionary
    sent_scores = create_sent_dict(sentiment_file)

    # Derive the sentiment of new terms
    new_term_sent = term_sentiment(sent_scores, tweets_file)
    
    # stdout
    for term in new_term_sent:
        print(term, new_term_sent[term])


if __name__ == '__main__':
    main()