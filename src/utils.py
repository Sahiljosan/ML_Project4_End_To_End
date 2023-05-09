import os
import sys
import dill # dill can be used to store python objects to a file, but the primary usage is to send python objects across the network as a byte stream

import numpy as np
import pandas as pd
from src.exception import CustomException



def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok= True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)