import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = dict()

    def add_app(self, title, func):
        self.apps[title] = func

    def run(self):
        pages = self.apps

        # If 'page' is present, update session_state with itself to preserve
        # values when navigating from Home to Others.
        if "page" in st.session_state:
            st.session_state.update(st.session_state)

        # If 'page' is not present, setup default values for settings widgets.
        else:
            st.session_state.update({
                # Default page
                "page": "Home",

                # Radio, selectbox and multiselect options
                "options": ["Hello", "Everyone", "Happy", "Streamlit-ing"],

                # Default widget values
                "text": "",
                "slider": 0,
                "checkbox": False,
                "radio": "Hello",
                "selectbox": "Hello",
                "multiselect": ["Hello", "Everyone"],
            })


        with st.sidebar:
            page = st.radio("Select your page", tuple(pages.keys()))

        pages[page]()
