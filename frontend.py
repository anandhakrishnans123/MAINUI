# Apply custom CSS styles
st.markdown(
    """
    <style>
    .custom-dropdown {
        font-size: 16px;
        padding: 12px 24px;
        border-radius: 8px;
        border: 2px solid #0D64D5;
        background-color: white;
        color: black; /* Default text color */
        cursor: pointer;
        transition-duration: 0.4s;
        text-decoration: none; /* Remove underline */
        width: 100%; /* Ensure dropdown fills column width */
        display: inline-block; /* Ensure button-like behavior */
    }

    .custom-dropdown:hover {
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

    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit app
st.markdown(
    """
    <style>
    .centered-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 200px; /* Adjusted width */
    }
    </style>
    """,
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

selected_option = st.selectbox("Select a page to visit", list(options.keys()))

# Redirect based on selection
if selected_option:
    st.markdown(f'<a href="{options[selected_option]}" target="_blank" class="custom-dropdown">Go to {selected_option}</a>', unsafe_allow_html=True)
