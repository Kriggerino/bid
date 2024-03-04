import streamlit as st
import pandas as pd
import numpy as np
import reader
import os


def process_file(uploaded_file):
    # Specify the directory to save the uploaded files
    upload_dir = "./uploaded_files"
    os.makedirs(upload_dir, exist_ok=True)  # Create the directory if it doesn't exist
    
    # Save the uploaded file to the specified directory
    file_path = os.path.join(upload_dir, uploaded_file.name)
    with open(file_path, "wb") as file:
        file.write(uploaded_file.read())

    # Return the file path for further processing or display
    return file_path


def main():
    st.title("File Upload and Processing App")

    # Create a file uploader widget
    uploaded_file = st.file_uploader("Upload a file", type=["docx"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")

        # Display a button to run the function using the uploaded file
        if st.button("Process File"):
            # Call the function to process the file
            processed_result = process_file(uploaded_file)
            
            # Display the result
            st.write("Processed Result:")
            st.write(processed_result)

if __name__ == "__main__":
    main()