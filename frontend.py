import streamlit as st
from PIL import Image
from io import BytesIO
import base64

# Set page configuration change 
st.set_page_config(page_title="Attractive Button Redirect", layout="centered")

# Apply custom CSS styles for buttons and general styling
st.markdown(
    """
    <style>
    .custom-button {
        background-color:#2596BE ; /* blue */
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
        background-color: #2596be; /* Lighter Orange */
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
    """
    <style>
    .centered-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 300px; /* Adjust width as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add an image at the top of the app with reduced size
top_image_base64 = resize_image("logo.png", width=300)  # Adjust width as needed
st.markdown(
    f'<img src="data:image/png;base64,{top_image_base64}" class="centered-image">',
    unsafe_allow_html=True
)

# Page Title and Description
st.markdown('<div class="title">Attractive Button Redirect</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Click the buttons below to be redirected to the relevant pages</div>', unsafe_allow_html=True)

# Function to create a button with a link and inline text color
def create_button(button_name, link, color='white'):
    st.markdown(f'<a href="{link}" target="_blank" class="custom-button" style="color:{color};">{button_name}</a>', unsafe_allow_html=True)

# Create a layout with columns for better alignment
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    create_button("Waste", "https://wastefull.streamlit.app/", color='white')  # Red

with col2:
    create_button("Scope 1 Road", "https://scope1-road.streamlit.app/", color='white')  # Blue

with col3:
    create_button("scope2", "https://scope2.streamlit.app/", color='white')  # Green

# Add more rows of buttons by repeating the structure
col4, col5, col6 = st.columns([1, 1, 1])

with col4:
    create_button("Scope 1 Fuel", "https://example.com/sustainability", color='white')

with col5:
    create_button("scope3 category1", "https://scope3category1.streamlit.app/", color='white')  # Pink

with col6:
    create_button("scope3 category 6", "https://scope3category6.streamlit.app/", color='white')  # Pink
