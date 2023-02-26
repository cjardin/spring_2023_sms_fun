import string
from nltk import pos_tag, word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

class ProcessedText:
    """Stores useful information about the input text."""
    def __init__(self, raw_text: str):
        """Performs a preliminary analysis of the text."""
        # There are some transformations here, like removing punctuation and stop words.
        # Consider handling them later. They're noisy, but they might still be useful information.
        # It would be better to ignore them in analysis rather than discard them outright.
        self.og_text = raw text
        raw_text = raw_text.lower()
        raw_text = raw_text.translate(str.maketrans('','', string.punctuation)) # removes punctuation to match more in corpus

        # Store lists of words and Penn Treebank tags.
        # For more info on the latter, see https://www.sketchengine.eu/penn-treebank-tagset/
        self.words = []
        self.tags = []
        for (word, tag) in pos_tag(word_tokenize(raw_text)):
            self.words.append(word)
            self.tags.append(tag)

        # Store the most intense emotion.
        self.intensity = max(
            SentimentIntensityAnalyzer()
                .polarity_scores(raw_text))
