import pandas as pd
import numpy as np
from joblib import load

sampleData = './sampledata/sample.xlsx'
LIWC_xfeatureList = ['Analytic','Clout','Authentic','Sixltr','ppron','ipron','negate','posemo','negemo','anx','anger','sad','cogproc','risk','focuspast','focuspresent','focusfuture','motion','space','time','nonflu','filler']

LIWC_modelfile = r'C:/Development/ModelConverter/DeceptionModel.joblib'
sklearn_model = load('./models/DeceptionModel_SKLearn.joblib')

df = pd.read_excel(sampleData)
X = np.array(df.loc[:,LIWC_xfeatureList])
y_preds = sklearn_model.predict_proba(X)
df['y_preds_test'] = y_preds[:, 1]

for index,row in df.iterrows():
    print(row['positiveClassProbability'],'<->',row['y_preds_test'])