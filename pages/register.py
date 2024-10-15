import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator import Authenticate
import yaml
from yaml.loader import SafeLoader
from streamlit_authenticator.utilities.exceptions import (CredentialsError,
                                                          ForgotError,
                                                          LoginError,
                                                          RegisterError,
                                                          ResetError,
                                                          UpdateError) 

st.markdown("Register")

with open('/Users/william/Documents/NoFoodWaste/user.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

(email_of_registered_user,
        username_of_registered_user,
        name_of_registered_user) = authenticator.register_user(pre_authorization=False)
if email_of_registered_user:
    st.success('User registered successfully')

     

with open('/Users/william/Documents/NoFoodWaste/user.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(config, file, default_flow_style=False)

if st.button("Login"):
    st.switch_page("login.py")