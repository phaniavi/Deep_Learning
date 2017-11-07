import pandas as pd #for dataframes
import quandl   #for data
import math
import numpy as np  #for arrays
from sklearn import preprocessing   #for scaling(i.e, to make the values of features in between -1 and +1) the data
from sklearn import cross_validation    #for dividing the data into partitions for training,testing after shuffling
from sklearn import svm
from sklearn.linear_model import LinearRegression   #for applying linear regression
import pickle   #Instead of training everytime we use the model for prediction, we can train and save it for future use

df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100
df['PCT_CHANGE'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100

df = df[['Adj. Close', 'HL_PCT', 'PCT_CHANGE', 'Adj. Volume']]

forecast_col = 'Adj. Close'

forecast_out = int(math.ceil(.01*len(df)))
df.fillna(-99999, inplace=True)

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

X = np.array(df.drop('label',1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

y = np.array(df['label'])
y = y[:-forecast_out]

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
#save the classifier
with open('stock prices.pickle', 'wb') as f:
    pickle.dump(clf, f)

#load the classifier
pickle_in = open('stock prices.pickle', 'rb')
clf = pickle.load(pickle_in)

accuracy = clf.score(X_test, y_test)
#predict the output on the data in X_lately
forecast_set = clf.predict(X_lately)

print(forecast_set, accuracy, forecast_out)