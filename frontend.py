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
        padding: 8px 16px; /* Smaller padding for dropdown */
        border-radius: 8px;
        border: 2px solid #0D64D5;
        background-color: white;
        color: black; /* Default text color */
        cursor: pointer;
        transition-duration: 0.4s;
        text-decoration: none; /* Remove underline */
        width: 33%; /* Dropdown width */
        display: inline-block; /* Ensure dropdown behaves like a button */
    }

    .custom-dropdown:hover {
        background-color: #0D64D5;
        color: white; /* Text color on hover */
        text-decoration: none; /* Remove underline on hover */
    }

    .custom-button {
        font-size: 14px; /* Smaller font size for button */
        padding: 8px 16px; /* Smaller padding for button */
        border-radius: 8px;
        border: 2px solid #0D64D5;
        background-color: white;
        color: black; /* Default text color */
        cursor: pointer;
        transition-duration: 0.4s;
        text-decoration: none; /* Remove underline */
        width: 33%; /* Button width */
        display: inline-block; /* Ensure button-like behavior */
        margin-top: 20px; /* Add space above the button */
    }

    .custom-button:hover {
        background-color: #0D64D5;
        color: white; /* Text color on hover */
        text-decoration: none; /* Remove underline on hover */
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
st.markdown('<div class="description">Select an option from the dropdown below to be redirected to the relevant page</div>', unsafe_allow_html=True)

# Create a custom dropdown
dropdown_html = """
<select id="custom-dropdown" class="custom-dropdown" onchange="window.location.href=this.value;">
<option value="" selected>Select a page to visit</option>
<option value="https://wastefull.streamlit.app/">Waste</option>
<option value="https://scope1-road.streamlit.app/">Scope 1 Road</option>
<option value="https://scope2.streamlit.app/">Scope 2</option>
<option value="https://oceanfrieght.streamlit.app/">Ocean</option>
<option value="https://scope3category1.streamlit.app/">Scope 3 Category 1</option>
<option value="https://scope3category6.streamlit.app/">Scope 3 Category 6</option>
<option value="https://brsractivicty.streamlit.app/">Brsr</option>
<option value="https://scope1-fuel.streamlit.app/">Scope 1 Fuel</option>
</select>
"""

st.markdown(dropdown_html, unsafe_allow_html=True)

# Button for action
if st.button('Go to Selected Page', key='button'):
    selected_page = st.session_state.get('selected_option')
    if selected_page:
        st.write(f'<script>window.location.href="{selected_page}"</script>', unsafe_allow_html=True)

# JavaScript to handle dropdown change
st.markdown(
    """
    <script>
    document.getElementById('custom-dropdown').addEventListener('change', function() {
        window.location.href = this.value;
    });
    </script>
    """,
    unsafe_allow_html=True
)
