import streamlit as st

# Load your HTML content
with open("Narender_Kumbala_Portfolio.html", 'r', encoding='utf-8') as f:
    html_content = f.read()

# Display in Streamlit
st.components.v1.html(html_content, height=1500, scrolling=True)
