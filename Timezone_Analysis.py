##
# Timezone_Analysis.py
# by Alex Madrzyk
#
# This program runs a sentiment analysis on all four timezones in the continental US, based on specific keywords
# found in tweets from that location. It then prints a happiness score for each timezone.
# This program also contains a graphic histogram that maps out the happiness levels per timezone.
#
# NOTE: happy_histogram.py, graphics.py, tweets.txt and keywords.txt
#   must be in the same folder as this file for it to run properly.
#

import happy_histogram


def main():
    # Initialize variables
    keywords = []
    pacificTotalTweets = 0
    pacificTotalRating = 0
    mountainTotalTweets = 0
    mountainTotalRating = 0
    centralTotalTweets = 0
    centralTotalRating = 0
    easternTotalTweets = 0
    easternTotalRating = 0

    # Get keywords file from user
    keywordsFileName = input("Please enter the name of the keyword file: ")
    try:
        keywordsFile = open(keywordsFileName, "r", encoding="utf-8")
    except IOError as err:
        print("The file was not found. \nError: ", err)
        quit()  # Exit the program

    # Process keywordsFile, store keywords and ratings in the same list
    for line in keywordsFile:
        line = line.strip()
        line = line.split(",")
        keywords.append([line[0], int(line[1])])

    # Get tweets file from user
    tweetFileName = input("Please enter the name of the tweet file: ")
    try:
        tweetsFile = open(tweetFileName, "r", encoding="utf-8")
    except IOError as err2:
        print("The file was not found. \nError: ", err2)
        quit()  # Exit the program

    # Obtain and process each tweet
    for line in tweetsFile:
        line = line.strip()

        # Split each tweet into its components
        componentList = line.split(" ", 5)
        location = [componentList[0], componentList[1]]
        tweet = componentList[5].split()

        # Loop though each word in the tweet for each word in the keywords list, add up total happiness score
        totalScore = 0
        for i in range(len(keywords)):
            for word in tweet:
                word = word.strip(" .,?!/\\:#@'\"")
                if keywords[i][0] in word:
                    totalScore += keywords[i][1]

        # Calculate the tweet's score, ignore tweet if totalScore is 0 (because no keywords appeared in the tweet)
        if len(tweet) != 0 and totalScore != 0:
            tweetScore = totalScore / len(tweet)

            # Get timezone
            latitude = float(location[0].strip("[,"))
            longitude = float(location[1].strip("],"))
            timezone = whichTimezone(latitude, longitude)

            # Add score to respective timezone
            if timezone == "Pacific":
                pacificTotalTweets += 1
                pacificTotalRating += tweetScore
            elif timezone == "Mountain":
                mountainTotalTweets += 1
                mountainTotalRating += tweetScore
            elif timezone == "Central":
                centralTotalTweets += 1
                centralTotalRating += tweetScore
            elif timezone == "Eastern":
                easternTotalTweets += 1
                easternTotalRating += tweetScore

    # Calculate happiness rating, avoid division by zero error
    if pacificTotalTweets != 0:
        pacificHappiness = pacificTotalRating * 10 / pacificTotalTweets
    else:
        pacificHappiness = 0

    if mountainTotalTweets != 0:
        mountainHappiness = mountainTotalRating * 10 / mountainTotalTweets
    else:
        mountainHappiness = 0

    if centralTotalTweets != 0:
        centralHappiness = centralTotalRating * 10 / centralTotalTweets
    else:
        centralHappiness = 0

    if easternTotalTweets != 0:
        easternHappiness = easternTotalRating * 10 / easternTotalTweets
    else:
        easternHappiness = 0

    print("")
    printResult("Pacific", pacificHappiness, pacificTotalTweets)
    printResult("Mountain", mountainHappiness, mountainTotalTweets)
    printResult("Central", centralHappiness, centralTotalTweets)
    printResult("Eastern", easternHappiness, easternTotalTweets)

    # Draw happy histogram if parameters fall within range
    if easternHappiness <= 10 and centralHappiness <= 10 and mountainHappiness <= 10 and pacificHappiness <= 10:
        happy_histogram.drawSimpleHistogram(easternHappiness, centralHappiness, mountainHappiness, pacificHappiness)

    tweetsFile.close()
    keywordsFile.close()


def whichTimezone(lat, long):
    # Latitude boundaries of timezones
    MIN_LATITUDE = 24.660845
    MAX_LATITUDE = 49.189787

    # Longitude boundaries of timezones
    p1 = -67.444574
    p3 = -87.518395
    p5 = -101.998892
    p7 = -115.236428
    p9 = -125.242264

    # If within boundaries: continue, else: return nothing
    if MIN_LATITUDE <= lat <= MAX_LATITUDE:
        if p9 <= long <= p1:
            if p9 <= long < p7:
                return "Pacific"
            elif p7 <= long < p5:
                return "Mountain"
            elif p5 <= long < p3:
                return "Central"
            elif p3 <= long <= p1:
                return "Eastern"
        else:
            return
    else:
        return


def printResult(timeZone, happiness, totalTweets):
    # Prints out the result of the analysis

    happinessRating = round(happiness, 2)
    print("The %s timezone has a happiness rating of %.2f/10 for a total of %d tweets." %(timeZone,
                                                                                          happinessRating, totalTweets))

main()