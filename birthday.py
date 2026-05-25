import streamlit as st
from datetime import date
import streamlit.components.v1 as components
import os
#streamlit run /Users/hersheys/Desktop/python/birthday/birthday.py
os.chdir(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(page_title="Rujji Turns 23 🎂", page_icon="🎉", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Quicksand:wght@400;500;600&display=swap');

* { font-family: 'Quicksand', sans-serif; }
h1, h2, h3 { font-family: 'Playfair Display', serif !important; text-align: center; }

.stApp {
    background: linear-gradient(135deg, #1a0533 0%, #2d1b4e 25%, #1a0533 50%, #0d1a3a 75%, #1a0533 100%);
    min-height: 100vh;
}

/* ✨ Twinkling stars */
.stars-container {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}
.star {
    position: absolute;
    background: white;
    border-radius: 50%;
    animation: twinkle var(--dur) ease-in-out infinite;
}
@keyframes twinkle {
    0%, 100% { opacity: 0.1; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.4); }
}

/* 🔴 String lights */
.lights-row {
    position: fixed;
    top: 0; left: 0;
    width: 100%;
    display: flex;
    justify-content: space-around;
    align-items: flex-start;
    z-index: 10;
    pointer-events: none;
    padding: 0 10px;
}
.bulb-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.wire {
    width: 2px;
    height: 30px;
    background: rgba(255,255,255,0.3);
}
.bulb {
    width: 14px;
    height: 18px;
    border-radius: 50% 50% 40% 40%;
    animation: glow var(--g) ease-in-out infinite alternate;
    box-shadow: 0 0 8px 3px var(--col);
}
@keyframes glow {
    from { opacity: 0.5; }
    to { opacity: 1; }
}

/* 🌸 Floating petals */
.petal {
    position: fixed;
    font-size: 20px;
    animation: floatUp var(--spd) linear infinite;
    z-index: 5;
    pointer-events: none;
    opacity: 0;
}
@keyframes floatUp {
    0% { transform: translateY(110vh) rotate(0deg); opacity: 0; }
    10% { opacity: 0.8; }
    90% { opacity: 0.6; }
    100% { transform: translateY(-10vh) rotate(720deg); opacity: 0; }
}

/* 💌 Note cards */
.note-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 20px;
    padding: 20px 25px;
    margin: 12px 0;
    color: white;
    font-size: 16px;
    line-height: 1.7;
    box-shadow: 0 4px 30px rgba(255,182,193,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    overflow: hidden;
}
.note-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    right: 0; height: 3px;
    background: linear-gradient(90deg, #ff9de2, #ffb347, #ff9de2);
    background-size: 200%;
    animation: shimmer 3s linear infinite;
}
@keyframes shimmer {
    0% { background-position: 0% 50%; }
    100% { background-position: 200% 50%; }
}

/* Pink glowing title */
.main-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 3em;
    text-align: center;
    background: linear-gradient(135deg, #ff9de2, #ffc3e0, #ffb347, #ff9de2);
    background-size: 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientShift 4s ease infinite;
    text-shadow: none;
    margin-bottom: 5px;
}
@keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

.subtitle {
    text-align: center;
    color: rgba(255,220,240,0.85);
    font-size: 15px;
    font-style: italic;
    margin-bottom: 30px;
}

/* Nav buttons */
.nav-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 10px;
    margin: 30px 0;
}
.nav-btn {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 18px;
    padding: 14px 8px;
    text-align: center;
    color: white;
    font-size: 13px;
    cursor: pointer;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
    text-decoration: none;
    display: block;
}
.nav-btn:hover {
    background: rgba(255,182,193,0.2);
    border-color: rgba(255,182,193,0.5);
    transform: translateY(-4px);
    box-shadow: 0 8px 25px rgba(255,182,193,0.2);
}
.nav-icon { font-size: 24px; display: block; margin-bottom: 5px; }

/* Photo frames */
.photo-frame {
    border-radius: 25px;
    overflow: hidden;
    box-shadow: 0 0 30px rgba(255,182,193,0.3), 0 0 60px rgba(255,182,193,0.1);
    border: 2px solid rgba(255,182,193,0.3);
    transition: all 0.4s ease;
}
.photo-frame:hover {
    transform: scale(1.03) rotate(1deg);
    box-shadow: 0 0 50px rgba(255,182,193,0.5);
}

/* Center message */
.center-msg {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,182,193,0.25);
    border-radius: 28px;
    padding: 30px 20px;
    text-align: center;
    color: white;
    font-size: 16px;
    line-height: 2;
    box-shadow: 0 0 40px rgba(255,182,193,0.15);
}

/* Small cute note boxes */
.tiny-note {
    display: inline-block;
    background: rgba(255,182,193,0.12);
    border: 1px solid rgba(255,182,193,0.3);
    border-radius: 12px;
    padding: 8px 16px;
    margin: 5px;
    color: #ffc3e0;
    font-size: 14px;
}

footer { visibility: hidden; }
#MainMenu { visibility: hidden; }
</style>

<!-- Twinkling Stars -->
<div class="stars-container" id="stars"></div>

<!-- String Lights -->
<div class="lights-row" id="lights"></div>

<!-- Floating Petals -->
<div id="petals"></div>

<script>
// Stars
const starsContainer = document.getElementById('stars');
for (let i = 0; i < 80; i++) {
    const star = document.createElement('div');
    star.className = 'star';
    const size = Math.random() * 3 + 1;
    star.style.cssText = `
        width:${size}px; height:${size}px;
        top:${Math.random()*100}%;
        left:${Math.random()*100}%;
        --dur:${2 + Math.random()*4}s;
        animation-delay:${Math.random()*5}s;
    `;
    starsContainer.appendChild(star);
}

// String Lights
const colors = ['#ff6b6b','#ffd93d','#6bcb77','#ff9de2','#a29bfe','#fd79a8','#74b9ff','#fdcb6e'];
const lightsRow = document.getElementById('lights');
for (let i = 0; i < 20; i++) {
    const wrap = document.createElement('div');
    wrap.className = 'bulb-wrap';
    const wire = document.createElement('div');
    wire.className = 'wire';
    wire.style.height = (20 + Math.random()*20) + 'px';
    const bulb = document.createElement('div');
    bulb.className = 'bulb';
    const col = colors[i % colors.length];
    bulb.style.cssText = `background:${col}; --col:${col}; --g:${0.5 + Math.random()*2}s; animation-delay:${Math.random()*2}s;`;
    wrap.appendChild(wire);
    wrap.appendChild(bulb);
    lightsRow.appendChild(wrap);
}

// Petals
const petalsContainer = document.getElementById('petals');
const petalEmojis = ['🌸','🌷','✨','💕','🌺','🌼','💫','🩷'];
for (let i = 0; i < 15; i++) {
    const p = document.createElement('div');
    p.className = 'petal';
    p.innerText = petalEmojis[Math.floor(Math.random()*petalEmojis.length)];
    p.style.cssText = `
        left:${Math.random()*100}%;
        --spd:${8 + Math.random()*10}s;
        animation-delay:${Math.random()*12}s;
        font-size:${14 + Math.random()*14}px;
    `;
    petalsContainer.appendChild(p);
}
</script>
""", unsafe_allow_html=True)

st.balloons()

# Main Title
st.markdown("<div class='main-title'>🎀 Happy Birthday Rujji 🎀</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>✨ May 26 · Turning 23 · The most special day ✨</div>", unsafe_allow_html=True)

# Cute tag pills
st.markdown("""
<div style='text-align:center; margin-bottom:25px;'>
    <span class='tiny-note'>🌸 23 & blooming 🌸</span>
    <span class='tiny-note'>💖 forever loved 💖</span>
    <span class='tiny-note'>✨ my man ✨</span>
    <span class='tiny-note'>🎂 happy birthday 🎂</span>
</div>
""", unsafe_allow_html=True)

# Navigation buttons
st.markdown("""
<div class='nav-grid'>
    <div class='nav-btn'>
        <span class='nav-icon'>💌</span>Why Rujji is Special
    </div>
    <div class='nav-btn'>
        <span class='nav-icon'>📸</span>Favorite Memories
    </div>
    <div class='nav-btn'>
        <span class='nav-icon'>🌸</span>Little Things About You
    </div>
    <div class='nav-btn'>
        <span class='nav-icon'>✨</span>Reasons You Make Life Better
    </div>
    <div class='nav-btn'>
        <span class='nav-icon'>🧸</span>Tiny Cute Notes
    </div>
</div>
""", unsafe_allow_html=True)

# Photos + center message
left, center, right = st.columns([100.5, 300, 100.5])
with left:
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    st.image("1610288754796.jpeg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with center:
    st.markdown("""
    <div class='center-msg'>
        <div style='font-family:Playfair Display,serif; font-size:1.4em; color:#ffc3e0; margin-bottom:15px;'>
            🎂 Happy Birthday Rujji ✨
        </div>
        You’re the boy I used to wish for without saying it out loud. Your nature, your heart and your love is the best place I could ever be at. 
                I hope life feels like a warm sunrise you can always be happy in. 🌸<br><br>
                 Another year of you is another year I’m grateful for the simplest things — your hand finding mine, your patience on my hard days, your brain that I eat daily, 
                your laugh that fills my ears, the coziness you have, your scent that blossoms everywhere, the way you are with me, your softest voice, your cool and compose nature, the way you handle things nicely and I am so proud of you.
                You are THE best.<br><br>
        Wishing you endless happiness, soft moments,
        success, and all years
        full of unforgettable memories 💖<br><br>
        bestestestestestestetststtsttststs wishes✨
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    st.image("IMG_0019.jpeg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Note cards
st.markdown("### 🌟 Little Birthday Notes 🌟")

notes = [
    ("🌸", "You deserve laughter that hurts your stomach, people who genuinely care, and days that feel lighter than today."),
    ("💖", "Hope this year becomes your successful one. Happy Graduation and touchwood soon Job."),
    ("🎈", "ILOVEYOURUJULKAUSHAL — always, in every universe, on every birthday and every ordinary day too, forever and ever and ever 💕"),
     ("🌸", "And when two people live together for so long time, they do fight daily, boil each other's blood, annoy each other, and the urge to give up on each other. "
     "But its never lesser love, lesser care. We started the relationship when we were young and naive, its okay to have mistakes done, its okay to fight daily, its okay to have space time to time, "
     "but whats not okay is loving less. I continue loving you daily irrespective the way we are talking. You are always gonna be MY THE FIRST LOVE and the Person I cherish always. I AM LUCKIEST BECAUSE I HAVE YOU!!!"),
]

for icon, text in notes:
    st.markdown(f"""
    <div class='note-card'>
        <span style='font-size:22px;'>{icon}</span>
        <span style='color:rgba(255,230,245,0.9); margin-left:10px;'>{text}</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Streamlit nav buttons
col1, col2, col3  = st.columns(3)
with col1:
    if st.button("💌 Why Special"):
        st.switch_page("pages/why_rujji_special.py")
with col2:
    if st.button("📸 Memories"):
        st.switch_page("pages/memories.py")

with col3:
    if st.button("🧸 Cute Notes"):
        st.switch_page("pages/cute_notes.py")

st.markdown("---")
st.markdown("<div style='text-align:center; color:rgba(255,182,193,0.7); font-size:14px;'>Made with love by Your Harshu · Just for My Rujji 🎀</div>", unsafe_allow_html=True)