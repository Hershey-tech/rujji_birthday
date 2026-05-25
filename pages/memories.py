import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared_style import SHARED_CSS, LIGHTS_JS

st.set_page_config(page_title="📸 Favorite Memories", page_icon="📸", layout="centered")
st.markdown(SHARED_CSS, unsafe_allow_html=True)
st.markdown(LIGHTS_JS, unsafe_allow_html=True)

st.markdown("<div class='page-title'>📸 Favorite Memories</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; color:rgba(255,200,230,0.7); font-style:italic; margin-bottom:30px;'>moments I keep in my heart forever 💕</div>", unsafe_allow_html=True)

# Polaroid-style memory cards
st.markdown("""
<style>
.polaroid {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,182,193,0.25);
    border-radius: 16px;
    padding: 20px 22px 20px 22px;
    margin: 14px 0;
    position: relative;
    overflow: hidden;
    transition: transform 0.3s;
}
.polaroid:hover { transform: rotate(1deg) scale(1.02); }
.polaroid::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, #ff9de2, #a29bfe, #74b9ff, #ff9de2);
    background-size: 200%;
    animation: shimmer 3s linear infinite;
}
@keyframes shimmer { 0%{background-position:0%;} 100%{background-position:200%;} }
.mem-date { font-size: 12px; color: rgba(255,182,193,0.6); margin-bottom: 6px; letter-spacing: 1px; text-transform: uppercase; }
.mem-title { font-family: 'Playfair Display', serif; font-size: 1.15em; color: #ffc3e0; margin-bottom: 8px; }
.mem-text { color: rgba(255,230,245,0.88); font-size: 15px; line-height: 1.75; }
.mem-emoji { font-size: 30px; float: right; margin-left: 12px; }
</style>
""", unsafe_allow_html=True)

memories = [
    ("🌅", "The 13th January 2017", "When we started the journey to this beautiful route. ILOVEYOU"),
    ("📚", "The NIT selection", "when you got MME and later Civil and finally entered NIT!!!! the most proud moment for me. Seeing your 'selected' in the counselling site and running to terrace to wake you uppp!!!!"),
    ("💟", "Late nights 2018", "When we talked late at nights, and see each other in mornings, meet irl, and it wasn't LDR. "),
    ("🚗", "Aureum Ride", "Having you as my passenger prince, and driving on NH without license and thodi si driving practice"),
    ("🍜", "Rajma Date", "While waiting for JEE result, had rajma rice at 3:00 in the morning."),
    ("🌙", "Late night calls", "not exactly a memory but presently as well, but its very relaxing to lie down in bed, cozy, and listening to your talks."),
    ("⚽️", "Goalkeeper Me", "When you motivated me to go for football. I wish we could be together to play. Even tho i have less knowledge about the game but i will full heartedly watch, play and go on football dates with you."),
    ("🎶", "You singing", "Love listenign to each and every song you sing for me, tho i dont understand each and every lyric, but i love it and i wanna keep listening them forever"),
    ("💌", "when you said ILOVEYOU eye contact", "sitting in 17 miles, saying ily first time face to face. and all the upcoming meets"),
]

for emoji, title, text in memories:
    st.markdown(f"""
    <div class='polaroid'>
        <span class='mem-emoji'>{emoji}</span>
        <div class='mem-title'>{title}</div>
        <div class='mem-text'>{text}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><div style='text-align:center; color:rgba(255,182,193,0.5); font-size:13px; font-style:italic;'>I couln't align and add photos to this page, it was very confusing. <br> <br> making more memories day by day</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
cols = st.columns(5)
pages = [("🏠 Home","birthday.py"),("💌 Special","pages/why_rujji_special.py"),("🧸 Notes","pages/cute_notes.py")]
for i,(label,page) in enumerate(pages):
    with cols[i]:
        if st.button(label):
            st.switch_page(page)
