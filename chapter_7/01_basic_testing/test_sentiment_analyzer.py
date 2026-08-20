from sentiment_analyzer import extract_sentiment

def test_extract_sentiment():
    """Test basic sentiment extraction."""
    text = "I think today will be a great day"
    sentiment = extract_sentiment(text)
    assert sentiment > 0


def test_extract_sentiment_positive():
    """Test positive sentiment."""
    text = "I think today will be a great day"
    sentiment = extract_sentiment(text)
    assert sentiment > 0

def test_extract_sentiment_negative():
    """Test negative sentiment."""
    text = "I do not think this will turn out well"
    sentiment = extract_sentiment(text)
    assert sentiment < 0

