import streamlit as st
from genai.db import fetch_documents

# Page for viewing the MongoDB data
st.subheader("MongoDB Data Viewer")
collection_name = st.text_input("Collection name", value="my_collection")

if st.button("Fetch Documents"):
    try:
        docs = fetch_documents(collection_name)
        st.json(docs)
    except Exception as e:
        st.error(str(e))