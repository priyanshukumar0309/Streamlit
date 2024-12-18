import streamlit as st
import json
import os

def app():
    st.header("Notion Azure Devops Sync ")
    st.markdown("""
            - This app integrates **Notion** and **Azure DevOps (ADO)** to automate the synchronization of work items, 
            ensuring that both systems are up-to-date. It fetches and updates work items between ADO and Notion, creates 
            missing items, and synchronizes descriptions. The app also facilitates the addition of required columns in Notion 
            and tracks the sync status of items.
    """)

    st.write("### Why")
    st.markdown("""
            - At Volvo Cars, maintaining accurate data across various platforms is critical. This application bridges the gap 
            between ADO, used for tracking development work, and Notion, used for documentation. It automates updates, reduces 
            errors, and ensures real-time consistency between the two systems.
    """)

    st.write("### Created by")
    st.markdown("""
            - **[Kumar Priyanshu](https://teams.microsoft.com/l/chat/0/0?users=kumar.priyanshu@volvocars.com)**, Digital Payments Product Manager at Volvo Cars, created this app as a side project to streamline workflows 
            and improve data consistency between ADO and Notion. 

            Reach out if you find any bugs or have suggestions for improvements!

    **Connect with me:**
    - [Teams](https://teams.microsoft.com/l/chat/0/0?users=kumar.priyanshu@volvocars.com)
    """)
    
   
        
