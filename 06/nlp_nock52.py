from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

X_train = pd.read_table("train.feature.txt", sep="\t", header=None)
print(X_train.head())
X_train = X_train.astype(float, errors="raise")
train_df = pd.read_table("train.txt", header=None)
train_df.columns = ["CATEGORY", "TITLE"]

LR = LogisticRegression()
LR.fit(X_train, train_df["CATEGORY"])



