# End To End ML Project Implementation

## Table of Content
- [Day 1](#day-1)
- [Day 2](#day-2)
- [Day 3](#day-3)
- [Day 4](#day-4)


## Day 1
### Create Basic Setup
1 : Create Environment
```
conda create -p venv python==3.8 -y
```
2 : Set up the github repository
```
git init
git add Readme.md
git commit -m "Readme commit"
git branch -M main
git remote add origin https://github.com/Sahiljosan/ML_Project4_End_To_End.git
git remote -v
git config --global user.name "Sahil Josan"
git config --global user.email sahiljosan50@gmail.com
git push -u origin main 
```
3 : Create .gitignore file in repository <br>
pull .gitignore file in vs code 
```
git pull
```
4 : Create setup.py file and requirement.txt file in vs code 

5 : Create src(source) directory and create __init__.py file in it

6 : Write code in setup.py and install requirements.txt
```
pip install -r requirements.txt
```
- After this we get mlproject.egg-info, in which we have different different packages

[Back To Top](#table-of-content)

## Day 2 
### Entire Project Structure Logging, Exceptional Handling
1 : Create components folder in src (source) folder <br>
Components are all the modules that we are going to create like Data Ingestion, data_transformation, model_trainer


2 : Create another folder pipeline in src folder <br>
Inside this pipeline we will have tranining_pipeline and prediction_pipeline <br>
train_pipeline will have code for training pipeline itself, and from this training pipeline will trigger and call all data components <br>
Predict_pipeline for the prediction purpose <br>
One more file in src folder will be __init__.py so that we can import both train and predict pipelines


3 : Now we create 3 important files 
    - logger.py : logging
    - exception.py : For Exceptional Handling
    - utils.py : any functionality that will be usefull in the entire application can we written here 


4 : Write code in exception.py
```
import sys
import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))

    return error_message

    


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail = error_detail)

    
    def __str__(self):
        return self.error_message
    

if __name__ =="__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)
```

5: Write code for logger.py

```
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,


)

if __name__ =="__main__":
    logging.info("Logging has started")
```
to check where the logger is working or not <br>
Open cmd in Terminal and write
```
python src/logger.py
```
[Back To Top](#table-of-content)

## Day 3 
Perfrom EDA and Model Training in Jupyter Notebook using student performance dataset

## Day 4
Written code for data_ingestion.py <br>
After Executing the code we get artifacts folder which includes
- raw_data.csv
- test.csv
- train.csv
<br><br>
Add this artifacts folder in .gitignore/Environments