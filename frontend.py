import streamlit as st

# Set page configuration
st.set_page_config(page_title="Redirect Links", layout="centered")

# Apply custom CSS styles
st.markdown(
    """
    <style>
    .link-button {
        background-color: #4CAF50; /* Green */
        color: white;
        padding: 12px 24px;
        font-size: 16px;
        margin: 10px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        text-decoration: none;
    }

    .link-button:hover {
        background-color: #45a049;
    }

    body {
        font-family: 'Arial', sans-serif;
        background-color: #f0f2f6;
        text-align: center;
    }

    .title {
        font-size: 40px;
        font-weight: bold;
        color: #333;
        text-align: center;
        margin-bottom: 40px;
    }

    .description {
        font-size: 18px;
        color: #666;
        margin-bottom: 40px;
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# Page Title and Description
st.markdown('<div class="title">Redirect Links</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Click the links below to be redirected to the relevant pages</div>', unsafe_allow_html=True)

# Links as buttons
st.markdown('<a href="https://wastefull.streamlit.app/" target="_blank" class="link-button">Waste</a>', unsafe_allow_html=True)
st.markdown('<a href="https://scope1-road.streamlit.app/" target="_blank" class="link-button">Scope 1 Road</a>', unsafe_allow_html=True)
st.markdown('<a href="https://scope2.streamlit.app/" target="_blank" class="link-button">Scope 2</a>', unsafe_allow_html=True)
