import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

def train():
    columns = ['sentence', 'sentiment']
    df = pd.read_csv('imdb_labelled.txt', sep='\t', header=None)
    df.columns = columns
    X = df['sentence'].values
    Y = df['sentiment'].values
    tfidf = TfidfVectorizer()
    X = tfidf.fit_transform(X)
    x_train, x_test, y_train, y_test = train_test_split(X,y,test_size = 0.25)
    gnb = GaussianNB()
    gnb.fit(x_train, y_train)
    return tfidf, gnb
def test(userInput):
    tfidf, log = train()
    review_tfidf = tfidf.transform([userInput])
    y_pred = log.predict(review_tfidf)
    #print(y_pred)
    if y_pred[0] ==0:
        pred = "Negative"
    else
        pred = "Positive"
    return pred



