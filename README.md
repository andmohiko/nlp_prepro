# nlp_prepro

自然言語処理でよく使う前処理シリーズ

## Install dependent libraries

```bash
pip install -r requirements.txt
```

## What you can do

- word split
- tfidf
- sentence embedding

### Word split

```python
df["word list"] = split_words(make_corpus(df["sentence"]))
```

### Make dictionary
