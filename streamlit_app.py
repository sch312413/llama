# streamlit run streamlit_app.py
# to run

import streamlit as st

# st.title('Hi')
st.set_page_config(layout='wide')

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

project_2_page = st.Page(
    "views/web_scraper.py",
    title="AI Web Scraper", 
    icon=":material/search:", 
)

project_3_page = st.Page(
    "views/pdf_to_png.py",
    title="PDF to PNG Converter",
    icon=":material/picture_as_pdf:"
)

pg = st.navigation(
    {
        "Info": [about_page], 
        "Project": [project_1_page, project_2_page, project_3_page]
    }
)

st.sidebar.text("Made with 🦐 by SC")

pg.run()