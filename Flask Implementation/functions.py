
import pickle
import re

def data_processing(data:str):
    data = data.lower()
    data = re.sub(r"https\S+|www\S+http\S+", '', data)
    data = re.sub(r'\@w+|\#','', data)
    data = re.sub(r'[^\w\s]','',data)
    data = re.sub(r'ð','',data)
    return data
    
def make_prediction(data:str):
    model = pickle.load(open("static/logistic Regression model.pkl", "rb"))
    processed = data_processing(data)
    lst=[]
    lst.append(processed)
    cv = pickle.load(open("static/cv.pickle", "rb"))
    vectorized = cv.transform(lst)
    pred = model.predict(vectorized)
    mapping = {1: 'Thankyou for such a lovely expression', 0: 'Why you gotta be so hatefull'}
    prediction = mapping[pred[0]]
    return data, prediction