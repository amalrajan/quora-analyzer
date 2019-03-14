import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def generate_word_cloud():
    """
    Generates a word cloud based on the text.

    :return: None
    """

    with open("answer_blob.txt", "r", encoding="utf-8") as text_blob_file:
        text_blob = text_blob_file.read()

    stopwords = set(STOPWORDS)

    word_cloud = WordCloud(width=1000, height=1000,
                           background_color="White",
                           stopwords=stopwords,
                           min_font_size=10).generate(text_blob)

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.show()


generate_word_cloud()
