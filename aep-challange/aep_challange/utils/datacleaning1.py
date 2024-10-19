import re


def clean(text):
    text = str(text).lower()
    text = re.sub("https?://\S+|www\.\S+", "", text)
    text = re.sub("<.*?>+", "", text)
    text = re.sub("\n", "", text)
    text = re.sub(r"\[NAME\]", "", text)
    text = " ".join(text)
    return text
