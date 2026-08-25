import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
ELEVENLABS_AGENT_ID = os.getenv("ELEVENLABS_AGENT_ID")

st.set_page_config(
    page_title="Architecte OS",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)
# DUMMY STUDIO & PROJECT
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
        
    html_code = f"""
    <div style="display: flex; justify-content: flex-end; padding: 5px;">
        <script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
        <elevenlabs-convai agent-id="{ELEVENLABS_AGENT_ID}"></elevenlabs-convai>
    </div>
    <style>
        body {{ background-color: transparent !important; }}
    </style>
    """
    st.components.v1.html(html_code, height=600, width=400)

render_elevenlabs_orb()
