import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def save_file(filename, datas):
    datas.to_csv(filename, sep='\t', index=False)


def main():
    news_corpora = pd.read_csv("NewsAggregatorDataset/newsCorpora.csv", sep="\t", header=None)
    news_corpora.columns = ["ID", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"]

    df = news_corpora[(news_corpora["PUBLISHER"] == "Reuters") \
                    | (news_corpora["PUBLISHER"] == "Huffington Post") \
                    | (news_corpora["PUBLISHER"] == "Businessweek") \
                    | (news_corpora["PUBLISHER"] == "Contactmusic.com") \
                    | (news_corpora["PUBLISHER"] == "Daily Mail")]
    df = df.sample(frac=1)

    train_df, valid_test_df = train_test_split(df, test_size=0.2)
    valid_df, test_df = train_test_split(valid_test_df, test_size=0.5)

    vec_tfidf = TfidfVectorizer()

    X_train = vec_tfidf.fit_transform(train_df["TITLE"])
    X_valid = vec_tfidf.transform(valid_df["TITLE"])
    X_test = vec_tfidf.transform(test_df["TITLE"])

    X_train = pd.DataFrame(X_train.toarray(), columns=vec_tfidf.get_feature_names())
    X_valid = pd.DataFrame(X_valid.toarray(), columns=vec_tfidf.get_feature_names())
    X_test = pd.DataFrame(X_test.toarray(), columns=vec_tfidf.get_feature_names())

    save_file("train.feature.txt", X_train)
    save_file("valid.feature.txt", X_valid)
    save_file("test.feature.txt", X_test)


if __name__ == "__main__":
    main()