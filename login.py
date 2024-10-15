import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator import Authenticate
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
        page_title="NoFoodWaste",
        page_icon="🍲",
        initial_sidebar_state="expanded"
    )

with open('/Users/william/Documents/NoFoodWaste/user.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('main', fields = {'Form name': 'Login'})

if st.session_state["authentication_status"]:
    st.session_state['key'] = config['credentials']['usernames'][st.session_state["username"]]['email']
    authenticator.logout('Logout', 'main')
    st.switch_page("pages/app.py")
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')

if st.button("Register"):
    st.switch_page("pages/register.py")
    

# streamlit run /Users/william/Documents/NoFoodWaste/login.py --client.showSidebarNavigation=False