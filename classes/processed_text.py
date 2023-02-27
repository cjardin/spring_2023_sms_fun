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
        self.og_text = raw_text
        raw_text = raw_text.lower()
        raw_text = raw_text.translate(str.maketrans('','', string.punctuation)) # removes punctuation to match more in corpus

        # Remove Contractions

        raw_text.replace("aren't", "are not")
        raw_text.replace("can't", "can not")
        raw_text.replace("couldn't", "could not")
        raw_text.replace("didn't", "did not")
        raw_text.replace("doesn't", "does not")
        raw_text.replace("don't", "do not")
        raw_text.replace("hadn't", "had not")
        raw_text.replace("hasn't", "has not")
        raw_text.replace("haven't", "have not")
        raw_text.replace("he'd", "he would")
        raw_text.replace("he'll", "he will")
        raw_text.replace("he's", "he is")
        raw_text.replace("i'd", "i would")
        raw_text.replace("i'll", "i will")
        raw_text.replace("i'm", "i am")
        raw_text.replace("i've", "i have")
        raw_text.replace("isn't", "is not")
        raw_text.replace("let's", "let us")
        raw_text.replace("she'd", "she would")
        raw_text.replace("she'll", "she will")
        raw_text.replace("she's", "she is")
        raw_text.replace("shouldn't", "should not")
        raw_text.replace("that's", "that is")
        raw_text.replace("there's", "there is")
        raw_text.replace("they'd", "they would")
        raw_text.replace("they'll", "they will")
        raw_text.replace("they're", "they are")
        raw_text.replace("they've", "they have")
        raw_text.replace("we'd", "we would")
        raw_text.replace("we're", "we are")
        raw_text.replace("we've", "we have")
        raw_text.replace("weren't", "were not")
        raw_text.replace("what're", "what are")
        raw_text.replace("what's", "what is")
        raw_text.replace("what've", "what have")
        raw_text.replace("where's", "where is")
        raw_text.replace("who'd", "who would")
        raw_text.replace("who'll", "who will")
        raw_text.replace("who're", "who are")
        raw_text.replace("who's", "who is")
        raw_text.replace("won't", "will not")
        raw_text.replace("you'd", "you would")
        raw_text.replace("you're", "you are")
        raw_text.replace("you've", "you have")

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
