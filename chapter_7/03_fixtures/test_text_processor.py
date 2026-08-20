from text_processor import extract_sentiment
from text_processor import sentence_contain_word
import pytest

@pytest.fixture
def example_data():
     """Fixture providing test data as shown in the book."""
     return "Today I found a duck and I am happy"


def test_extract_sentiment(example_data):
    """Test sentiment extraction using fixture."""
    sentiment = extract_sentiment(example_data)
    assert sentiment > 0


def test_sentence_contain_word(example_data):
    """Test word containment using fixture."""
    word = "duck"
    assert sentence_contain_word(word, example_data) == True


# testdata= [
#     "I think today will be a great day",
#     "I do not think this will turn out well",
# ]

# @pytest.mark.parametrize("sample", testdata)
# def test_extract_sentiment(sample):
#     """Test basic sentiment extraction."""
#     # text = "I think today will be a great day"
#     sentiment = extract_sentiment(sample)
#     assert sentiment > 0

# testdata_pairs = [
#     ("There is a duck", True), 
#     ("There is nothing here", False)
# ]

# @pytest.mark.parametrize("sample, expected_output", testdata_pairs)
# def test_sentence_contain_word(sample, expected_output):
#     """Test word containment with expected outputs."""
#     word = "duck"
#     assert sentence_contain_word(word, sample) == expected_output



# def test_extract_sentiment_positive():
#     """Test positive sentiment."""
#     text = "I think today will be a great day"
#     sentiment = extract_sentiment(text)
#     assert sentiment > 0

# def test_extract_sentiment_negative():
#     """Test negative sentiment."""
#     text = "I do not think this will turn out well"
#     sentiment = extract_sentiment(text)
#     assert sentiment < 0

