import streamlit as st

# Title
st.title("Narender Kumbala Portfolio")

# Resume download
with open("Narender_Kumbala_Resume.pdf", "rb") as file:
    btn = st.download_button(
        label="📄 Download My Resume",
        data=file,
        file_name="Narender_Kumbala_Resume.pdf",
        mime="application/pdf"
    )

# Display portfolio content
with open("Narender_Kumbala_Portfolio.html", 'r', encoding='utf-8') as f:
    html_content = f.read()

st.components.v1.html(html_content, height=1500, scrolling=True)
