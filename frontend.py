import streamlit as st
from PIL import Image
from io import BytesIO
import base64

# Set page configuration change 
st.set_page_config(page_title="Data Mapping Tool", layout="centered")

# Apply custom CSS styles
st.markdown(
    """
    <style>
    .custom-dropdown {
        font-size: 16px;
        padding: 12px;
        border-radius: 8px;
        border: 2px solid #0D64D5;
        background-color: white;
        color: #0D64D5;
        cursor: pointer;
        transition: background-color 0.3s, color 0.3s;
        width: 100%; /* Ensure dropdown fills column width */
        margin-bottom: 15px; /* Padding between items */
    }

    .custom-dropdown:hover {
        background-color: #0D64D5;
        color: white;
    }

    /* Styling the page */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #F5F5F5;
        text-align: center;
        margin: 0;
        padding: 0;
    }

    .title {
        font-size: 36px;
        font-weight: bold;
        color: #333;
        text-align: center;
        margin: 40px 0;
    }

    .description {
        font-size: 18px;
        color: #666;
        margin-bottom: 40px;
        text-align: center;
    }

    .card {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin: 20px;
        display: inline-block; /* Adjust for padding between items */
        width: 80%;
    }

    .centered-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 200px; /* Adjusted width */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def resize_image(image_path, width):
    img = Image.open(image_path)
    aspect_ratio = img.height / img.width
    new_height = int(width * aspect_ratio)
    img_resized = img.resize((width, new_height))
    
    # Save the resized image to a BytesIO object
    buffered = BytesIO()
    img_resized.save(buffered, format="PNG")
    
    # Encode the image to Base64
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_base64

# Streamlit app
st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

# Add an image at the top of the app with reduced size
top_image_base64 = resize_image("logo.png", width=200)  # Adjusted width
st.markdown(
    f'<img src="data:image/png;base64,{top_image_base64}" class="centered-image">',
    unsafe_allow_html=True
)

# Page Title and Description
st.markdown('<div class="title">Data Mapping Tool</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Select an option from the dropdown below to be redirected to the relevant page</div>', unsafe_allow_html=True)

# Dropdown for selecting the page
options = {
    "Waste": "https://wastefull.streamlit.app/",
    "Scope 1 Road": "https://scope1-road.streamlit.app/",
    "Scope 2": "https://scope2.streamlit.app/",
    "Ocean": "https://oceanfrieght.streamlit.app/",
    "Scope 3 Category 1": "https://scope3category1.streamlit.app/",
    "Scope 3 Category 6": "https://scope3category6.streamlit.app/",
    "Brsr": "https://brsractivicty.streamlit.app/",
    "Scope 1 Fuel": "https://scope1-fuel.streamlit.app/"
}

selected_option = st.selectbox("Select a page to visit", list(options.keys()), key='page_selector')

# Redirect based on selection
if selected_option:
    st.markdown(f'<a href="{options[selected_option]}" target="_blank" class="custom-dropdown">Go to {selected_option}</a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
