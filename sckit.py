from sklearn.ensemble import ExtraTreesClassifier
from sklearn import preprocessing
import pandas as pd
import numpy as np
import pickle


#params=[str soil type, int whc, int rainmin, int rainmax,
#int tempmin, int tempmax, float phmin, floatphmax]

def predict_crop(params):
    data = pd.read_csv('CropData.csv')
    X = data.drop(["Crop"], axis=1)
    y = pd.DataFrame(data["Crop"])
    le1 = preprocessing.LabelEncoder()
    le2 = preprocessing.LabelEncoder()
    X["Soil"] = le1.fit_transform(X["Soil"])
    y["Crop"] = le2.fit_transform(y["Crop"])
    clf = ExtraTreesClassifier()
    clf = pickle.load(open("model.sav", 'rb'))
    feature_vector = np.array([le1.transform([params[0]]), params[1], params[2], params[3], params[4], params[5], params[6], params[7]]).reshape(1,-1)
    return((le2.inverse_transform(clf.predict(feature_vector))))

if __name__ == "__main__":
    predict_crop(["clayey loamy", 2, 600, 1100, 27, 35, 6.7, 7.7])

"""
data = pd.read_csv('CropData.csv')
X = data.drop(["Crop"], axis=1)
y = pd.DataFrame(data["Crop"])

le1 = preprocessing.LabelEncoder()
le2 = preprocessing.LabelEncoder()
X["Soil"] = le1.fit_transform(X["Soil"])
y["Crop"] = le2.fit_transform(y["Crop"])

clf = ExtraTreesClassifier()
clf.fit(X.values, y.values.reshape(-1))

filename = "model.sav"
pickle.dump(clf, open(filename,'wb'))
clf = pickle.load(open(filename, 'rb'))
X_t = np.array([le1.transform(["clayey loamy"]),2,600,1100,27,35,6.7,7.7])
predict = clf.predict(X=X_t.reshape(1,-1))

print(predict)
print(le2.inverse_transform(predict))
print(clf.score(X,y))
"""