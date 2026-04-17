from fastapi import Fastapi
from fastapi.responses import Jsonresponse
from pydantic import Basemodel , Field , computed_field
from typing import Literal , Annotated
import pickle 
import pandas as pd 

# now importing tye model 
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Fastapi()

