from dotenv import load_dotenv
load_dotenv() # to load env

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Config api
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load model res sql query
def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text


# function to retrive data from sql db
def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION and MARK \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]


# streamlit App

st.set_page_config(page_title="Text to SQL LLM")
st.header("Gemini AI Powered Application to retrieve SQL Data by natural Language")

question = st.text_input("Input : ",key="input")

submit = st.button("Query it")

# If Submit clicked

if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    data = read_sql_query(response,"student.db")
    st.header("The Response is")
    for row in data:
        print(row)
        st.json(row)