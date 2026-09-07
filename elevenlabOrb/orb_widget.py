import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
ELEVENLABS_AGENT_ID = os.getenv("ELEVENLABS_AGENT_ID")

def render_elevenlabs_orb():
    if not ELEVENLABS_AGENT_ID:
        return            
    
    # User requested original iframe method with bottom 0px
    st.markdown("""
        <style>
            iframe {
                position: fixed !important;
                bottom: 0px !important;
                right: 0px !important;
                width: 350px !important;
                height: 500px !important;
                z-index: 999999 !important;
                border: none !important;
                pointer-events: auto !important;
            }
        </style>
    """, unsafe_allow_html=True)
    
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                margin: 0;
                padding: 0;
                background-color: transparent !important;
                overflow: hidden;
            }}
        </style>
    </head>
    <body>
        <elevenlabs-convai agent-id="{ELEVENLABS_AGENT_ID}"></elevenlabs-convai>
        <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
    </body>
    </html>
    """
    
    # We keep height=0 here so it doesn't create the 500px scrolling bug on the page
    st.components.v1.html(html_code, height=0)
