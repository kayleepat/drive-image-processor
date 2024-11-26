# streamlit interface

# imports
import streamlit as st
import time

st.header('Drive Image Parser')
st.write('This app allows you to process files from a Google Drive folder.')

folder_link = st.text_input("Enter Google Drive folder link:")
# add data validation to this

file_types = st.selectbox(
    'Select file types to process:',
    ["ArcGIS Compatible Images (.jpg, .jpeg)", "All Images (.jpg, .jpeg, .png, .heic, etc)", "Excel Sheets (.xls, .xlsx)", "Text Files (.txt)"]
)

st.radio("Select one:", [1, 2])

st.segmented_control("Filter", ["Open", "Closed"])
st.selectbox("Pick one", ["cats", "dogs"])
st.pills("File Types to Process",['.jpg','.jpeg','.png','.heic','.gif'],selection_mode="multi",default=['.jpg','.jpeg'])

# Show a spinner during a process
with st.spinner(text="In progress"):
    # time.sleep(3)
    st.success("Done")

# Show and update progress bar
bar = st.progress(0)
time.sleep(3)
bar.progress(100)

with st.status("Authenticating...") as s:
    time.sleep(2)
    st.write("Some long response.")
    s.update(label="Response")