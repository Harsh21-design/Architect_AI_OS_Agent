import streamlit as st
import os
from dotenv import load_dotenv

# Load environment configurations
load_dotenv()
ELEVENLABS_AGENT_ID = os.getenv("ELEVENLABS_AGENT_ID", "")

# Page configuration for a clean, default dashboard
st.set_page_config(
    page_title="Architecte OS",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- Mock Session State (Simulating Platform Handoff) -----------------
if "studio_id" not in st.session_state:
    st.session_state["studio_id"] = "studio_alpha"
if "active_project_id" not in st.session_state:
    st.session_state["active_project_id"] = "barkly_house"

# ----------------- Sidebar (Context Info) -----------------
with st.sidebar:
    st.title("Architecte OS")
    st.markdown("---")
    st.subheader("Current Active Context")
    st.info(f"Studio ID:\n`{st.session_state['studio_id']}`\n\nProject ID:\n`{st.session_state['active_project_id']}`")
    st.markdown("---")
    st.caption("Connected to Architecte Platform (Mock Environment)")

# ----------------- Main Dashboard -----------------
st.title("Workspace Hub")
st.subheader("💬 Project AI Assistant")
st.write(f"I am actively monitoring **{st.session_state['active_project_id']}**.")

# Simple Chat Placeholder
chat_input = st.chat_input("Ask something about the project...")

# ----------------- ElevenLabs Orb Integration Widget -----------------
def render_elevenlabs_orb():
    if not ELEVENLABS_AGENT_ID:
        return
        
    html_code = f"""
    <div style="position: fixed; bottom: 20px; right: 20px; z-index: 9999;">
        <script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
        <elevenlabs-convai agent-id="{ELEVENLABS_AGENT_ID}"></elevenlabs-convai>
    </div>
    """
    st.html(html_code)

render_elevenlabs_orb()
