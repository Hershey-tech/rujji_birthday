import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared_style import SHARED_CSS, LIGHTS_JS

st.set_page_config(page_title="💌 Why Rujji is Special", page_icon="💌", layout="centered")
st.markdown(SHARED_CSS, unsafe_allow_html=True)
st.markdown(LIGHTS_JS, unsafe_allow_html=True)

st.markdown("<div class='page-title'>💌 Why Rujji is Special</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; color:rgba(255,200,230,0.7); font-style:italic; margin-bottom:30px;'>lemme mention a few out of infinity 🌸</div>", unsafe_allow_html=True)

reasons = [
    ("🌟", "The way you show up", "You always show up for me when i am messed and sad. This is rare and that's everything for me."),
    ("🌸", "Your laugh", "Your laugh is crazzzyyy in the best way. It fills up my room and makes everything feel lighter."),
    ("💫", "How you care", "The way you care about people — quietly, deeply, without keeping score. Me and all the people you care about are blessed to have you."),
    ("🦋", "Your strength", "You've been through hard things and you still choose to be soft and kind. Still managing everything by yourself, but guess what? You have me by your side, its You n Me v/s The world!"),
    ("🌺", "Your vibe", "There's just something about you, the way you exist, the way you are, your thinking, your voice, your language, your way, your patience, that makes the world a little prettier for me. Because of you i still live in my dreamworld"),
    ("💖", "The little things you do", "The small gestures, the 'kaise ho?' , the remembering things i say. You make me feel existing. "),
    ("✨", "Your dreams", "You dream big and you're willing to work for it. Watching you grow is one of my favorite things."),
    ("🎀", "Simply being you", "You don't even try to be special, you just are. And that's the most special thing of all. THE RUJUL. MY RUJJI"),
]

for icon, title, text in reasons:
    st.markdown(f"""
    <div class='card'>
        <span class='card-icon'>{icon}</span>
        <div class='card-title'>{title}</div>
        {text}
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
if st.button("🏠 Back to Birthday"):
    st.switch_page("birthday.py")
col2, col3  = st.columns(2)
with col2:
    if st.button("📸 Memories"):
        st.switch_page("pages/memories.py")
with col3:
    if st.button("🧸 Cute Notes"):
        st.switch_page("pages/cute_notes.py")
