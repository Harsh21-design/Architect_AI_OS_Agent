import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
ELEVENLABS_AGENT_ID = os.getenv("ELEVENLABS_AGENT_ID")

st.set_page_config(
    page_title="Architecte OS AI",
    page_icon="📐",
    layout="centered",
    initial_sidebar_state="expanded"
)
# DEMO STUDIO & PROJECT
if "studio_id" not in st.session_state:
    st.session_state["studio_id"] = "studio_alpha"
if "active_project_id" not in st.session_state:
    st.session_state["active_project_id"] = "barkly_house"

with st.sidebar:
    st.title("Architecte OS")
    st.markdown("---")
    st.subheader("Current Active Context")
    st.info(f"Studio ID:\n`{st.session_state['studio_id']}`\n\nProject ID:\n`{st.session_state['active_project_id']}`")
    st.markdown("---")
    st.caption("Connected to Architecte Platform (Mock Environment)")

st.title("Workspace Hub")
st.subheader("💬 Project AI Assistant")
st.write(f"I am actively monitoring **{st.session_state['active_project_id']}**.")
st.write("Use the voice orb below to interact with the project context.")

def render_elevenlabs_orb():
    if not ELEVENLABS_AGENT_ID:
        return            
    st.markdown("""
        <style>
            iframe {
                position: fixed !important;
                bottom: 0px !important;
                right: 0px !important;
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
    st.components.v1.html(html_code, height=500, width=350)

render_elevenlabs_orb()
