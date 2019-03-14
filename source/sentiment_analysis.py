import re
from textblobl import TextBlob


def clean_text():
    """
    Utility function to clean text by removing links, special characters using
    regex statement.

    :return: None
    """

    return ' '.join(re.sub(
        "(@[A-Za-z0-9]+) | ([ ^ 0-9A-Za-z \t]) | (\w+: \/\/\S+)",
        " ", tweet).split())


def get_text_sentiment(text):
    """
    Pass text as a parameter, which gets split into paragraphs/sentences and
    passed onto TextBlob for analysis.

    :return: tuple(positive, negative, neutral)
    """

    text = text.split("\n")
    
    positive = 0
    negative = 0
    neutral = 0

    for sentence in text:
        analysis = TextBlob(clean_text(sentence))

        if analysis.sentiment.polarity > 0:
            positive += 1
        elif analysis.sentiment.polarity < 0:
            negative += 1
        else:
            neutral += 1

    return (positive, negative, neutral)


def display_analysis(positive, negative, neutral):
    """
    Interprets the values from TextBlob and displays it on the shell.

    :param positive: number of positive results after analysis
    :param negative: number of negative results after analysis
    :param neutral: number of neutral results after analysis

    :return: None
    """
    total = positive + negative + neutral

    positive_percentage = (positive / total) * 100
    negative_percentage = (negative / total) * 100
    neutral_percentage = (neutral / total) * 100

    print("Positive: {}%\nNegative: {}%\n Neutral: {}%".format(
        positive_percentage, negative_percentage, neutral_percentage))
