import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64

model = pickle.load(open('model.pkl','rb'))
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))

st.title("Student Performance Prediction")

gender = st.selectbox("Please select gender",
                      ('male','female'))

race_ethnicity = st.selectbox("Select ethnicity of students",
                              ('group A','group B','group C','group D', 'group E'))


parental_level_of_education = st.selectbox("Select parental_level_of_education",
                                           ("associate's degree", "bachelor's degree","high school","master's degree","some college", "some high school"))

lunch = st.selectbox("Select lunch",
                     ("standard","free/reduced"))

test_preparation_course = st.selectbox("Select test_preparation_course",
                                       ('none','completed'))


reading_score = st.text_input("Enter reading_score", 65)

writing_score = st.text_input("Enter writing_score", 75)

l = {}
l['gender'] = gender
l['race_ethnicity'] = race_ethnicity
l['parental_level_of_education'] = parental_level_of_education
l['lunch'] = lunch
l['test_preparation_course'] = test_preparation_course
l['reading_score'] = reading_score
l['writing_score'] = writing_score

df = pd.DataFrame(l,index=[0])

df = preprocessor.transform(df)
y_pred = model.predict(df)


if st.button("Show Math's Score"):
    st.header(f"{round(y_pred[0], 2)}")


# insert Background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('stud_performance.jpg')   
