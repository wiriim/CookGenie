import streamlit as st
import subscriptionpage as sp
from utils.st import local_css

def show_subscription():
    local_css("asset/css/style.css")
    st.header("Subscription")
    st.write(f'Welcome to subscription Page')
    st.markdown(sp.PACKAGE, unsafe_allow_html=True) 
    

    