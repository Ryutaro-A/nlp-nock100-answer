import pandas as pd
from sklearn.model_selection import train_test_split

def save_file(df, filename):
    df.to_csv(filename, columns = ["CATEGORY","TITLE"], sep="\t", header=False, index=False)


def main():
    news_corpora = pd.read_csv("NewsAggregatorDataset/newsCorpora.csv", sep="\t", header=None)
    news_corpora.columns = ["ID","TITLE","URL","PUBLISHER","CATEGORY","STORY","HOSTNAME","TIMESTAMP"]

    df = news_corpora[(news_corpora["PUBLISHER"] == "Reuters") \
                    | (news_corpora["PUBLISHER"] == "Huffington Post") \
                    | (news_corpora["PUBLISHER"] == "Businessweek") \
                    | (news_corpora["PUBLISHER"] == "Contactmusic.com") \
                    | (news_corpora["PUBLISHER"] == "Daily Mail")]
    df = df.sample(frac=1)

    train_df, valid_test_df = train_test_split(df, test_size=0.2)
    valid_df, test_df = train_test_split(valid_test_df, test_size=0.5)

    save_file(train_df, "tran.txt")
    save_file(valid_df, "valid.txt")
    save_file(test_df, "test.txt")

if __name__ == "__main__":
    main()
