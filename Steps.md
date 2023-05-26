# End To End ML Project Implementation

## Table of Content
- [Day 1](#day-1)
- [Day 2](#day-2)
- [Day 3](#day-3)
- [Day 4](#day-4)
- [Day 5](#day-5)
- [Day 6](#day-6)
- [Day 7](#day-7)
- [Day 8](#day-8)
- [Day 9](#day-9)


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

[Back To Top](#table-of-content)

## Day 5
data_transformation.py <br>
The main aim of data_transformation is to do 
- feature engineering 
- data cleaning, 
- Change our dataset
- change our categorical features into numerical features
- Handle the missing values

## Day 6 
model_trainer.py <br>
The main aim of model_trainer.py is to train model using different different algorithms and store the best model in model.pkl file

[Back To Top](#table-of-content)

## Day 7 
Model Hyperparameter Tuning <br>
For Hyperparameter tuning we have to add this code in utils
```
 model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train) # Train Model
```

and This code in Model Trainer
```
 models = {
                "Linear Regression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor()
            }

            params={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boosting":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "CatBoosting Regressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                }
                
            }

            model_report:dict = evaluate_models(X_train = X_train, y_train = y_train, X_test = X_test, y_test = y_test , 
                                               models = models, param = params)
```
[Back To Top](#table-of-content)

## Day 8
Create Prediction Pipeline <br>
In Prediction Pipeline we will try to create the web application, which will be interating with pickle files, in web applicaton there will be a form where we give input data to predict the student performance
`Step1` Create app.py
`Step2` Right code in prefict_pipeline.py


## Day 9
Project Deployment in AWS Cloud using CICD Pipelines <br>
Elastic Beanstalk <br>
Here 2 important configuration we need to setup <br>
`step1` create .ebextensions folder <br>
`step2` create python.config file <br>
python.config file is mainly to tell the elastic beanstalk instance that what is the entry point of your application. <br>
By Default While searching in eleastic beanstalk documentation page, they are giving this type of configuration
```
option_settings:
    "aws:eleasticbeanstalk:container:python":
        WSGIPath: application:application
```
This configuration is for python only , not for dockers.. while using dockers there is different configuration

Steps of Deployment
---------------------------------------------------------
`step1` Have an AWS account <br>
`step2` Go to elastic beanstalk in search bar and click on applications <br> <br>
![](https://i.imgur.com/KLhrH1G.png)


`step3` Click on create application
![](https://i.imgur.com/5a91s9x.png)

`step4` write application name in tab of application name
<br>
![](https://i.imgur.com/K4lK1FB.png)
<br>
Write python in tab of platform and click on sample application because we want to integrate with our github repository
![](https://i.imgur.com/PnTQAVl.png)
<br>
and click on the next and wait for the environment to create
![](https://i.imgur.com/HlUDDNJ.png)
<br>
Now open another tab for AWS and search for CodePipeline
![](https://i.imgur.com/22jy42U.png) <br>
Click on create pipeline
![](https://i.imgur.com/TWRFd3X.png) <br>
Write pipeline name and dont do any advance settings and click Next
![](https://i.imgur.com/nmGx3lE.png) <br>
In source provider click on Github (Version1)
![](https://i.imgur.com/Coju3wA.png) <br>
and connect with your local github , select repository and branch and detection option will be github webhooks (recommended) and click next
![](https://i.imgur.com/O5eLFIr.png) <br>
Then it comes Build provider - lets say you create project before for creating artifacts and all for doing that any steps we can use build provider. right now we will skip build stage
![](https://i.imgur.com/kM2XmWU.png) <br>
This is important Deploy Stage 
![](https://i.imgur.com/URV2bmR.png) <br>
Now wait till our environment is created 
![](https://i.imgur.com/xbbebXu.png) <br>






