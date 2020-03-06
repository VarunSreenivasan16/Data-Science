import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder



train_dataframe = pd.read_csv('train.csv')
test_dataframe = pd.read_csv('test.csv')


train_s = train_dataframe.iloc[:, :-1].apply(LabelEncoder().fit_transform)
train_sI = train_dataframe['Id']

feats = np.array(train_s.iloc[:,1:-1])
labels = np.array(train_s['class'])


test_s = test_dataframe.iloc[:, :-1].apply(LabelEncoder().fit_transform)
test_sI = test_dataframe['Id']

test_feats = np.array(test_s.iloc[:,:-1])


classifier = RandomForestClassifier().fit(feats, labels)

y_hat_prediction = classifier.predict(test_feats)
mydict = dict(zip(test_sI, y_hat_prediction))
for k in mydict:
    if (mydict[k] ==1):
        mydict[k] = 'p'
    else:
        mydict[k] = 'e'

myList = list(mydict.items())
fin_dataframe = pd.DataFrame.from_dict(myList)
temp = ['Id', 'class']
tempInd = False
fin_dataframe.to_csv('varun_results.csv', header = temp, index = tempInd)


