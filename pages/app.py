import os

import streamlit as st
from streamlit_navigation_bar import st_navbar

import utils as pg

st.set_page_config(
        page_title="NoFoodWaste",
        page_icon="🍲",
        layout="wide",
        initial_sidebar_state="expanded"
    )

pages = ["Home", "Subscription", "Profile", "Logout"]

styles = {
    "nav": {
        "background-color": "#7BD192",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "padding": "0.4375rem 0.625rem",
        "margin": "0 0.125rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    }
}

options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    styles=styles,
    options=options,
)



def log_out():
    st.session_state["authentication_status"] = None
    st.switch_page("login.py")
    
functions = {
    "Home": pg.show_home,
    "Subscription": pg.show_subscription,
    "Profile": pg.show_profile,
    "Logout": log_out,
}

go_to = functions.get(page)
if go_to:
    go_to()