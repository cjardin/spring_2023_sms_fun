from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords # A corpus of stop words to ignore.
from nltk.sentiment import SentimentIntensityAnalyzer

STOP_WORDS = set(stopwords.words('english')) #Building a list of stop words

class ProcessedText:
    """
    Stores useful information about the input message
    """
    def __init__(self, raw_text: str):
        # I haven't ported over the stemming yet becuase I'm not sure that
        # we'll need it. Even then, that information is still useful, so it
        # might be better to do that later in the response cycle.

        # Store lists of words and Penn Treebank tags.
        # For more info on the latter, see https://www.sketchengine.eu/penn-treebank-tagset/
        self.words = []
        self.tags = []
        for (word, tag) in pos_tag(word_tokenize(raw_text)):
            if word in STOP_WORDS: continue
            self.words.append(word)
            self.tags.append(tag)

        # Store the most intense emotion.
        self.intensity = max(
            SentimentIntensityAnalyzer()
                .polarity_scores(raw_text))
