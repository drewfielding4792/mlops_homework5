import re

def clean_text(text: str) -> str:
    """
    Lowercases, removes non-alphanumeric characters (except spaces), and trims whitespace.
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text