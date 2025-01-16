import streamlit as st

from form.contact import contact_form

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/shrimp.png", width=200)

with col2:
    st.title("Sharon Chen", anchor=False)
    st.write(
        "Grade 10/H2 student in Taiwan"
    )
    if st.button("✉️ Contact Me"):
        contact_form()

st.write("\n")
st.subheader("Education", anchor=False)
st.write(
    """
    - Secondary student in Taipei, Taiwan
    """
)

st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
    - Language: Chinese, English
    - Programming: Python
    """
)