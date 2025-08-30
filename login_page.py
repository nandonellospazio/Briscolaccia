import streamlit as st
#from decouple import config, Config, RepositoryEnv
#import os
import constants as C

#pathenv = C.path + ".env"
#DOTENV_FILE = os.environ.get("DOTENV_FILE", pathenv) # only place using os.environ
#config = Config(RepositoryEnv(DOTENV_FILE))

username = C.user
password = C.password


def login():
    """Returns `True` if the user had a correct password."""
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] == username and st.session_state["password"] == password:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("😕 Utente sconosciuto o password non corretta")
        return False
    else:
        # Password correct.
        return True