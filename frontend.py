import streamlit as st

# Set page configuration
st.set_page_config(page_title="Attractive Button Redirect", layout="centered")

# Apply custom CSS styles
st.markdown(
    """
    <style>
    .custom-button {
        background-color: #2D80ED; /* Blue */
        color: white; /* Button text color */
        padding: 12px 24px;
        font-size: 16px;
        margin: 10px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        transition-duration: 0.4s;
    }

    .custom-button:hover {
        background-color: #64b5f6; /* Light Blue */
    }

    /* Styling the page */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #FFFEFD;
        text-align: center;
    }

    .title {
        font-size: 40px;
        font-weight: bold;
        color: #333; /* Keep title color as it is */
        text-align: center;
        margin-bottom: 40px;
    }

    .description {
        font-size: 18px;
        color: #666; /* Keep description color as it is */
        margin-bottom: 40px;
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# Page Title and Description
st.markdown('<div class="title">Attractive Button Redirect</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Click the buttons below to be redirected to the relevant pages</div>', unsafe_allow_html=True)

# Function to create a button with a link
def create_button(button_name, link):
    st.markdown(f'<a href="{link}" target="_blank" class="custom-button">{button_name}</a>', unsafe_allow_html=True)

# Create a layout with columns for better alignment
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    create_button("Waste", "https://wastefull.streamlit.app/")

with col2:
    create_button("Scope 1 Road", "https://scope1-road.streamlit.app/")

with col3:
    create_button("scope2", "https://scope2.streamlit.app/")

# Add more rows of buttons by repeating the structure
col4, col5, col6 = st.columns([1, 1, 1])

with col4:
    create_button("Scope 1 Fuel", "https://example.com/sustainability")

with col5:
    create_button("scope3 category1", "https://scope3category1.streamlit.app/")

with col6:
    create_button("scope3 category 6", "https://scope3category6.streamlit.app/")
