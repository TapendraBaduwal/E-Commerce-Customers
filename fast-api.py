from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()


@app.get("/items/{item_id}")
def read_item(SessionLength: float,TimeonApp:float,imeonWebsite:float,LengthofMembership:float):
    #Load our model again
    SessionLength = SessionLength
    TimeonApp= TimeonApp
    imeonWebsite = imeonWebsite
    LengthofMembership= LengthofMembership
  
        # assign data of lists.  as key and value 
    data = {'Avg. Session Length': [SessionLength], 'Time on App': [TimeonApp],'Time on Website':[imeonWebsite],'Length of Membership':[LengthofMembership]}  
    
    # Create DataFrame  for converting our data to orginal pandas dataframe.
    df = pd.DataFrame(data) 
    
    model = pickle.load(open("lr_model_pkl","rb"))  #load module
    result = model.predict(df)                      #predict
   
    return {"Yearly Amount Spent prediction is":result[0]}
