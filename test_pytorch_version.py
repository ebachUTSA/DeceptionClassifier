import torch
import pandas as pd
import numpy as np
import torch.jit

sampleData = './sampledata/sample.xlsx'
LIWC_xfeatureList = ['Analytic','Clout','Authentic','Sixltr','ppron','ipron','negate','posemo','negemo','anx','anger','sad','cogproc','risk','focuspast','focuspresent','focusfuture','motion','space','time','nonflu','filler']

torch_model = torch.jit.load("./models/Deception Model_torch.pt")

df = pd.read_excel(sampleData)
X = np.array(df.loc[:,LIWC_xfeatureList])
X_tensor = torch.tensor(X)

y_preds = torch_model(X_tensor)

df['y_preds_test'] = y_preds.tolist()

for index,row in df.iterrows():
    print(row['deceptionClass'],'<->',row['y_preds_test'])