# streamlit run streamlit_app.py
# to run

import streamlit as st

# st.title('Hi')

about_page = st.Page(
    "views/about_me.py",
    title="About Me", 
    icon=":material/account_circle:", 
    default=True,
)

project_1_page = st.Page(
    "views/chat_bot.py",
    title="Chat Bot", 
    icon=":material/smart_toy:", 
)

pg = st.navigation(
    {
        "Info": [about_page], 
        "Project": [project_1_page],
    }
)

st.sidebar.text("Made with 🦐 by SC")

pg.run()