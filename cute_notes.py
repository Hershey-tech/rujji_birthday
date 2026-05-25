import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared_style import SHARED_CSS, LIGHTS_JS

st.set_page_config(page_title="🧸 Tiny Cute Notes", page_icon="🧸", layout="centered")
st.markdown(SHARED_CSS, unsafe_allow_html=True)
st.markdown(LIGHTS_JS, unsafe_allow_html=True)

st.markdown("<div class='page-title'>🧸 Tiny Cute Notes</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; color:rgba(255,200,230,0.7); font-style:italic; margin-bottom:30px;'>little notes from my heart 💌</div>", unsafe_allow_html=True)

st.markdown("""
<style>
.sticky-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin: 16px 0;
}
.sticky {
    border-radius: 4px 4px 4px 4px;
    padding: 20px 18px 24px 18px;
    font-size: 14px;
    line-height: 1.7;
    color: rgba(30,10,40,0.92);
    position: relative;
    box-shadow: 3px 4px 20px rgba(0,0,0,0.3), 0 0 0 1px rgba(255,255,255,0.05);
    transition: transform 0.3s ease;
    min-height: 140px;
}
.sticky:hover {
    transform: rotate(2deg) scale(1.04);
    z-index: 2;
}
.sticky::before {
    content: '';
    position: absolute;
    top: -6px; left: 50%; transform: translateX(-50%);
    width: 30px; height: 10px;
    background: rgba(255,255,255,0.35);
    border-radius: 3px;
}
.sticky-pink { background: linear-gradient(135deg, #ffb3d9, #ff85c1); }
.sticky-yellow { background: linear-gradient(135deg, #fff3a3, #ffe066); }
.sticky-lavender { background: linear-gradient(135deg, #d4b3ff, #b88aff); }
.sticky-mint { background: linear-gradient(135deg, #b3f0d4, #7fe5b2); }
.sticky-peach { background: linear-gradient(135deg, #ffd4b3, #ffb380); }
.sticky-blue { background: linear-gradient(135deg, #b3d4ff, #80b3ff); }

.sticky-note-emoji { font-size: 22px; display:block; margin-bottom:8px; }
.sticky-text { font-family:'Quicksand',sans-serif; font-weight:500; }

/* Big romantic note */
.love-note {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,182,193,0.3);
    border-radius: 22px;
    padding: 30px;
    text-align: center;
    color: rgba(255,230,245,0.9);
    font-size: 16px;
    line-height: 2;
    font-style: italic;
    box-shadow: 0 0 50px rgba(255,182,193,0.1);
    margin: 20px 0;
    position: relative;
}
.love-note::before {
    content: '💌';
    font-size: 30px;
    display: block;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

notes = [
    ("sticky-pink", "🌸", "you are loved more than you know"),
    ("sticky-yellow", "⭐", "your existence is the best thing"),
    ("sticky-lavender", "🦋", "on bad days remember: you've handled me since 9 years now, you are strong."),
    ("sticky-mint", "🌿", "drink water."),
    ("sticky-peach", "🍑", "someone out there feels blessed to have your presence in their life"),
    ("sticky-blue", "🌙", "you deserve lots of love and kind people"),
    ("sticky-pink", "💕", "your laugh is genuinely one of the best sounds"),
    ("sticky-yellow", "✨", "you are the best."),
    ("sticky-lavender", "🎀", "I hope today felt as special as you are"),
    ("sticky-mint", "🌱", "keep growing, keep glowing"),
    ("sticky-peach", "🧡", "someone out there thinks of you and smiles"),
    ("sticky-blue", "💙", "you make the world warmer just by being in it"),
]

# Render grid
for i in range(0, len(notes), 3):
    cols = st.columns(3)
    for j in range(3):
        if i+j < len(notes):
            cls, emoji, text = notes[i+j]
            with cols[j]:
                st.markdown(f"""
                <div class='sticky {cls}'>
                    <span class='sticky-note-emoji'>{emoji}</span>
                    <div class='sticky-text'>{text}</div>
                </div>
                """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Big love note at bottom
st.markdown("""
<div class='love-note'>
    <span style='font-family: Playfair Display, serif; font-size:1.3em; color:#ffc3e0; font-style:normal;'>
        A note from Harshu 💖
    </span><br>
    Happy birthday, Rujji. I could write a thousand pages and still not capture
    everything I want to say. So I'll just say this: I'm so glad you exist.
    I'm so glad I know you. Have the most beautiful 23rd year.<br><br>
    <span style='color:#ff9de2; font-style:normal; font-weight:600;'>✨ ILOVEYOURUJULKAUSHAL ✨</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
cols = st.columns(3)
pages = [("🏠 Home","birthday.py"),("💌 Special","pages/why_rujji_special.py"),("📸 Memories","pages/memories.py")]
for i,(label,page) in enumerate(pages):
    with cols[i]:
        if st.button(label):
            st.switch_page(page)