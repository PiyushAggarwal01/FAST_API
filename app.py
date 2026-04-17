from fastapi import Fastapi
from fastapi.responses import Jsonresponse
from pydantic import Basemodel , Field , computed_field
from typing import Literal , Annotated
import Pickle 
import pandas as pd 

# now importing tye model 