import streamlit as st


def show_profile():
    st.header("Profile")
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.write(f'*{st.session_state["key"]}*')
    # st.write(st.session_state)
    # st.write(f'Welcome *{st.session_state["name"]}*')
    