import streamlit as st
from PIL import Image
from io import BytesIO
import base64

# Set page configuration
st.set_page_config(page_title="Data Mapping Tool", layout="centered")

# Apply custom CSS styles for buttons and general styling
st.markdown(
    """
    <style>
    .primary-button {
        background-color:#0D64D5; /* Darker Blue */
        padding: 12px 24px;
        font-size: 18px; /* Larger font size for primary categories */
        margin: 10px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        text-align: center;
        text-decoration: none; /* Remove underlining */
        display: inline-block;
        transition-duration: 0.4s;
    }

    .primary-button:hover {
        background-color: #2596be; /* Lighter Blue */
        text-decoration: none;}

    .secondary-button {
        background-color:#66B2FF; /* Lighter Blue */
        padding: 12px 24px;
        font-size: 14px; /* Slightly smaller font size for secondary categories */
        margin: 10px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        text-align: center;
        text-decoration: none; /* Remove underlining */
        display: inline-block;
        transition-duration: 0.4s;
    }

    .secondary-button:hover {
        background-color: #80C7FF; /* Even lighter Blue */
        text-decoration: none;}

    /* Styling the page */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #FFFEFD;
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

    .centered-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 200px; /* Adjusted width */
    }

    .section {
        margin: 20px 0;
    }

    .section-header {
        font-size: 24px;
        font-weight: bold;
        color: #0D64D5;
        margin-bottom: 10px;
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

# Add an image at the top of the app with reduced size
top_image_base64 = resize_image("logo.png", width=200)  # Adjusted width
st.markdown(
    f'<img src="data:image/png;base64,{top_image_base64}" class="centered-image">',
    unsafe_allow_html=True
)

# Page Title and Description
st.markdown('<div class="title">Data Mapping Tool</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Click the buttons below to be redirected to the relevant pages</div>', unsafe_allow_html=True)

# Create sections
st.markdown('<div class="section"><div class="section-header">Primary Categories</div></div>', unsafe_allow_html=True)

# Primary Categories
cols = st.columns(4)  # Four equal columns per row

with cols[0]:
    st.markdown('<a href="https://wastefull.streamlit.app/" target="_blank" class="primary-button">Waste</a>', unsafe_allow_html=True)

with cols[1]:
    st.markdown('<a href="https://scope1-road.streamlit.app/" target="_blank" class="primary-button">Scope 1 Road</a>', unsafe_allow_html=True)

with cols[2]:
    st.markdown('<a href="https://scope2.streamlit.app/" target="_blank" class="primary-button">Scope 2</a>', unsafe_allow_html=True)

with cols[3]:
    st.markdown('<a href="https://oceanfrieght.streamlit.app/" target="_blank" class="primary-button">Ocean</a>', unsafe_allow_html=True)

# Secondary Categories
st.markdown('<div class="section"><div class="section-header">Secondary Categories</div></div>', unsafe_allow_html=True)

cols = st.columns(4)  # Four equal columns per row

with cols[0]:
    st.markdown('<a href="https://scope3category1.streamlit.app/" target="_blank" class="secondary-button">Scope 3 Category 1</a>', unsafe_allow_html=True)

with cols[1]:
    st.markdown('<a href="https://scope3category6.streamlit.app/" target="_blank" class="secondary-button">Scope 3 Category 6</a>', unsafe_allow_html=True)

with cols[2]:
    st.markdown('<a href="https://brsractivicty.streamlit.app/" target="_blank" class="secondary-button">Brsr</a>', unsafe_allow_html=True)

with cols[3]:
    st.markdown('<a href="https://scope1-fuel.streamlit.app/" target="_blank" class="secondary-button">Scope 1 Fuel</a>', unsafe_allow_html=True)
