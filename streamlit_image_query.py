import streamlit as st
from PIL import Image
from generate_response import generate_response

def main():
    """Main Streamlit application for querying images."""
    st.title("Image Query App")
    
    # File uploader for image input
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Open and display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)  # Updated parameter
        
        # Text area for user to input a query regarding the image
        prompt = st.text_area("Ask a question about the image")
        
        # Button to generate a response based on the image and query
        if st.button("Generate Response"):
            with st.spinner("Generating response..."):
                # Convert image to bytes
                image_bytes = uploaded_file.getvalue()
                
                # Call the function to generate a response
                response = generate_response(image_bytes, prompt)
                
                # Display the generated response
                st.write(response)

if __name__ == "__main__":
    main()
