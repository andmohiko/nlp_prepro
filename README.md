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
t = "今日は曇りのち晴れです。走りたい気分です。全角！半角!"

# 全品詞
print(get_words(t))
# ['今日', 'は', '曇り', 'のち', '晴れ', 'です', '。', '走り', 'たい', '気分', 'です', '。', '全角', '！', '半角', '!']

# 任意の品詞のみ
print(get_words(t, pos_list=["名詞", "動詞"]))
# ['今日', '曇り', 'のち', '晴れ', '走り', '気分', '全角', '半角', '!']

# 原形
print(get_words(t, pos_list=["名詞", "動詞"], form="origin"))
# ['今日', '曇る', 'のち', '晴れ', '走る', '気分', '全角', '半角', '!']
```

<!-- ```python
df["word list"] = split_words(make_corpus(df["sentence"]))
``` -->

### Make dictionary
