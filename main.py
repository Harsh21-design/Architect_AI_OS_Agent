import streamlit as st
from elevenlabOrb import orb_widget

st.set_page_config(
    page_title="Architecte OS AI",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to shift content and avoid Orb overlap
st.markdown("""
    <style>
        /* Push the main content left and create a massive 350px empty space on the right for the Orb */
        [data-testid="block-container"] {
            padding-right: 350px !important;
            padding-left: 40px !important;
        }
        /* Make the Chat Input physically smaller by adding a huge right margin */
        [data-testid="stChatInput"] {
            margin-right: 250px !important;
            width: auto !important;
        }
        [data-testid="stBottomBlockContainer"] {
            padding-right: 250px !important;
        }
    </style>
""", unsafe_allow_html=True)

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
st.caption("Use the chat box below for silent text mode, or the voice orb in the corner for voice mode.")
st.markdown("---")

# MOCK CHAT INTERFACE (Text-only UI Demo)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": f"Hello! I am connected to `{st.session_state['active_project_id']}`. Ask me anything via text, or use the Orb below for voice!"}
    ]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user text input
if prompt := st.chat_input("Type your message here (Text-only mode)..."):
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Mock AI response (Later this will connect to our Multi-LLM Adapter)
    mock_reply = f"*(This is a mock text reply)*. You said: {prompt}"
    with st.chat_message("assistant"):
        st.markdown(mock_reply)
    st.session_state.messages.append({"role": "assistant", "content": mock_reply})

# # Render the orb
orb_widget.render_elevenlabs_orb()
