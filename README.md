# Twitter Sentiment Analysis

This program performs sentiment analysis on Twitter data. The Twitter data contains tweets from individuals about how they feel about their lives and comes from individuals across the continental United States. The objective is to determine which timezone (Eastern, Central, Mountain, Pacific) is the “happiest”. To do this, the program:
* Analyzes each individual tweet to determine a score – a “happiness score”.
* The “happiness score” for a single tweet is found by looking for certain keywords (given) in a tweet and for each keyword found in that tweet totaling their “sentiment values”. In this assignment, each value is an integer from 1 to 10. The score for the tweet is simply the total of the “sentiment values” divided by the number of keywords found. If there are none of the given keywords in a tweet, it is just ignored.
* The “happiness score” for a timezone is just the total of the scores for all the tweets in that region divided by the number of tweets.

A file called tweets.txt contains the tweets and a file called keywords.txt contains keywords and scores for determining the “sentiment” of an individual tweet.

## Getting Started

Run via terminal by using ```python3 ./Timezone_Analysis.py``` after changing to the directory.

NOTE: happy_histogram.py, graphics.py, tweets.txt and keywords.txt must be in the same folder as this file for it to run properly.

## Built With

* Sublime Text 2

## Acknowledgments

* Western University's CS1026A Course Staff 
