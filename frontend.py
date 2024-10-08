import streamlit as st
from PIL import Image
from io import BytesIO
import base64

# Set page configuration
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
        font-size: 14px; /* Smaller font size */
        padding: 8px 16px; /* Smaller padding */
        border-radius: 8px;
        border: 2px solid #0D64D5;
        background-color: white;
        color: black; /* Default text color */
        cursor: pointer;
        transition-duration: 0.4s;
        text-decoration: none; /* Remove underline */
        display: inline-block; /* Ensure button-like behavior */
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

def create_dropdown_and_redirect():
    """
    Displays a descriptive markdown element, a dropdown with clear labels,
    and handles redirection based on the user's selection.
    """

    st.markdown(
        """
        <div class="description">
            Select an option from the dropdown below to be redirected to the relevant page.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Use a dictionary comprehension for cleaner option definition
    options = {
        "Vessel Waste Data Mapping Tool": "https://wastefull.streamlit.app/",
        "Scope 1 Road Freight Data Mapping Tool": "https://scope1-road.streamlit.app/",
        "Scope 2 Electricity Data Mapping Tool": "https://scope2.streamlit.app/",
        "Scope 3 Ocean Data Mapping Tool": "https://oceanfrieght.streamlit.app/",
        "Scope 3 Category 1 Air Freight Data Mapping Tool": "https://scope3category1.streamlit.app/",
        "Scope 3 Category 6 Business Travel Data Mapping Tool": "https://scope3category6.streamlit.app/",
        "Business Responsibility and Sustainability Reporting": "https://brsractivicty.streamlit.app/",
        "Scope 1 Fuel Data Mapping Tool": "https://scope1-fuel.streamlit.app/"
    }

    selected_option = st.selectbox("Select a page:", list(options.keys()))

    if selected_option:
        url = options[selected_option]
        st.markdown(
            f"""
            <a href="{url}" target="_blank" class="custom-button">Go to {selected_option}</a>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    create_dropdown_and_redirect()
