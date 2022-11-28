import streamlit as st
from pymongo import MongoClient
@st.experimental_singleton(suppress_st_warning=True)
def init_connection():
    return MongoClient("mongodb://localhost:27017/")