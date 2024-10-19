import re


def clean(text):
    text = re.sub("https?://\S+|www\.\S+", "", text)
    text = re.sub("\n", "", text)
    text = re.sub(r"\[NAME\]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"(?<!\S)(\w)(\s)(?=\w\s)", r"\1", text)

    return text
