SHARED_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Quicksand:wght@400;500;600&display=swap');

* { font-family: 'Quicksand', sans-serif; }
h1, h2, h3 { font-family: 'Playfair Display', serif !important; text-align: center; }

.stApp {
    background: linear-gradient(135deg, #1a0533 0%, #2d1b4e 25%, #1a0533 50%, #0d1a3a 75%, #1a0533 100%);
}

.stars-container { position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:0; overflow:hidden; }
.star { position:absolute; background:white; border-radius:50%; animation:twinkle var(--dur) ease-in-out infinite; }
@keyframes twinkle { 0%,100%{opacity:0.1;transform:scale(1);} 50%{opacity:1;transform:scale(1.4);} }

.lights-row { position:fixed; top:0; left:0; width:100%; display:flex; justify-content:space-around; align-items:flex-start; z-index:10; pointer-events:none; }
.bulb-wrap { display:flex; flex-direction:column; align-items:center; }
.wire { width:2px; background:rgba(255,255,255,0.3); }
.bulb { width:14px; height:18px; border-radius:50% 50% 40% 40%; animation:glow var(--g) ease-in-out infinite alternate; box-shadow:0 0 8px 3px var(--col); }
@keyframes glow { from{opacity:0.5;} to{opacity:1;} }

.page-title {
    font-family:'Playfair Display',serif!important;
    font-size:2.5em;
    text-align:center;
    background:linear-gradient(135deg,#ff9de2,#ffc3e0,#ffb347,#ff9de2);
    background-size:300%;
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    animation:gradientShift 4s ease infinite;
    padding-top: 60px;
}
@keyframes gradientShift { 0%,100%{background-position:0% 50%;} 50%{background-position:100% 50%;} }

.card {
    background:rgba(255,255,255,0.07);
    backdrop-filter:blur(20px);
    border:1px solid rgba(255,182,193,0.2);
    border-radius:22px;
    padding:22px 26px;
    margin:14px 0;
    color:rgba(255,230,245,0.92);
    font-size:15.5px;
    line-height:1.8;
    box-shadow:0 4px 30px rgba(255,182,193,0.08);
    transition:transform 0.3s,box-shadow 0.3s;
    position:relative;
    overflow:hidden;
}
.card::before {
    content:'';position:absolute;top:0;left:0;right:0;height:3px;
    background:linear-gradient(90deg,#ff9de2,#ffb347,#ff9de2);
    background-size:200%;
    animation:shimmer 3s linear infinite;
}
@keyframes shimmer { 0%{background-position:0%;} 100%{background-position:200%;} }

.card-icon { font-size:26px; display:block; margin-bottom:8px; }
.card-title { font-family:'Playfair Display',serif; font-size:1.1em; color:#ffc3e0; margin-bottom:6px; }

.tiny-note { display:inline-block; background:rgba(255,182,193,0.1); border:1px solid rgba(255,182,193,0.3); border-radius:10px; padding:6px 14px; margin:4px; color:#ffc3e0; font-size:13px; }

footer{visibility:hidden;}
#MainMenu{visibility:hidden;}
</style>
"""

LIGHTS_JS = """
<div class="stars-container" id="stars"></div>
<div class="lights-row" id="lights"></div>
<script>
const sc=document.getElementById('stars');
for(let i=0;i<60;i++){const s=document.createElement('div');s.className='star';const sz=Math.random()*3+1;s.style.cssText=`width:${sz}px;height:${sz}px;top:${Math.random()*100}%;left:${Math.random()*100}%;--dur:${2+Math.random()*4}s;animation-delay:${Math.random()*5}s;`;sc.appendChild(s);}
const cols=['#ff6b6b','#ffd93d','#6bcb77','#ff9de2','#a29bfe','#fd79a8','#74b9ff','#fdcb6e'];
const lr=document.getElementById('lights');
for(let i=0;i<20;i++){const w=document.createElement('div');w.className='bulb-wrap';const wi=document.createElement('div');wi.className='wire';wi.style.height=(20+Math.random()*20)+'px';const b=document.createElement('div');b.className='bulb';const c=cols[i%cols.length];b.style.cssText=`background:${c};--col:${c};--g:${0.5+Math.random()*2}s;animation-delay:${Math.random()*2}s;`;w.appendChild(wi);w.appendChild(b);lr.appendChild(w);}
</script>
"""