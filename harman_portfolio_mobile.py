<!-- 
<style>
*{margin:0;padding:0;box-sizing:border-box;}
body{background:#080808;color:#fff;font-family:system-ui,sans-serif;overflow-x:hidden;}

.bg-gif{position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none;}
.bg-gif img{width:100%;height:100%;object-fit:cover;opacity:0.07;filter:hue-rotate(200deg) saturate(2);}
.bg-overlay{position:fixed;top:0;left:0;width:100%;height:100%;z-index:1;background:linear-gradient(135deg,rgba(8,8,8,0.9) 0%,rgba(8,8,8,0.78) 50%,rgba(20,0,0,0.9) 100%);pointer-events:none;}

nav{position:sticky;top:0;z-index:999;display:flex;justify-content:space-between;align-items:center;padding:.85rem 1.2rem;background:rgba(8,8,8,0);transition:all .4s;border-bottom:1px solid transparent;}
nav.scrolled{background:rgba(8,8,8,0.97);border-bottom:1px solid rgba(230,50,50,0.4);box-shadow:0 4px 30px rgba(230,50,50,0.12);}
.nav-logo{font-size:20px;font-weight:900;letter-spacing:3px;color:#fff;cursor:pointer;}
.nav-logo span{color:#e63232;}

.hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:4px;z-index:1001;}
.hamburger span{display:block;width:24px;height:2px;background:#fff;border-radius:2px;transition:all .3s;}
.hamburger.open span:nth-child(1){transform:translateY(7px) rotate(45deg);}
.hamburger.open span:nth-child(2){opacity:0;}
.hamburger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg);}

.nav-links{display:flex;gap:2rem;list-style:none;}
.nav-links a{color:rgba(255,255,255,0.65);text-decoration:none;font-size:13px;letter-spacing:1.5px;text-transform:uppercase;cursor:pointer;transition:all .25s;position:relative;padding-bottom:4px;}
.nav-links a::after{content:'';position:absolute;bottom:0;left:0;width:0;height:2px;background:#e63232;transition:width .3s;}
.nav-links a:hover,.nav-links a.active{color:#fff;}
.nav-links a:hover::after,.nav-links a.active::after{width:100%;}

.wrap{position:relative;z-index:2;}

.hero{min-height:90vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:5rem 1.5rem 3rem;}
.htag{font-size:11px;letter-spacing:4px;color:#e63232;text-transform:uppercase;margin-bottom:1rem;}
.hname{font-size:clamp(48px,14vw,130px);font-weight:900;text-transform:uppercase;line-height:.88;margin-bottom:.25em;}
.hname .script{display:block;font-family:Georgia,serif;font-style:italic;font-weight:400;color:#e63232;font-size:.5em;text-transform:none;}
.hrole{font-size:clamp(13px,3.5vw,22px);font-weight:700;text-transform:uppercase;letter-spacing:2px;color:rgba(255,255,255,0.8);margin-bottom:1.2rem;}
.hdesc{font-size:clamp(14px,3.5vw,17px);color:rgba(255,255,255,0.65);line-height:1.85;max-width:580px;margin:0 auto 2rem;}
.btns{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;}
.btn-r{background:#e63232;color:#fff;border:none;padding:13px 28px;font-size:13px;letter-spacing:1.5px;text-transform:uppercase;cursor:pointer;border-radius:4px;font-weight:700;transition:all .25s;}
.btn-r:hover{background:#ff4444;transform:translateY(-2px);box-shadow:0 8px 24px rgba(230,50,50,0.4);}
.btn-g{background:transparent;color:#fff;border:1.5px solid rgba(255,255,255,0.35);padding:13px 28px;font-size:13px;letter-spacing:1.5px;text-transform:uppercase;cursor:pointer;border-radius:4px;font-weight:700;transition:all .25s;}
.btn-g:hover{border-color:#e63232;color:#e63232;}

.stats{display:flex;justify-content:center;gap:1rem;flex-wrap:wrap;margin-top:2.5rem;}
.stat{background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);border-radius:12px;padding:1.2rem 1.5rem;text-align:center;transition:all .3s;min-width:80px;}
.stat:hover{border-color:rgba(230,50,50,0.5);background:rgba(230,50,50,0.1);transform:translateY(-4px);}
.snum{font-size:clamp(26px,6vw,38px);font-weight:900;color:#e63232;}
.slbl{font-size:11px;color:rgba(255,255,255,0.5);letter-spacing:1.5px;text-transform:uppercase;margin-top:4px;}

.sec{padding:4rem 1.5rem;max-width:1100px;margin:0 auto;text-align:center;}
.stag{font-size:11px;letter-spacing:4px;color:#e63232;text-transform:uppercase;margin-bottom:.6rem;display:block;}
.stitle{font-size:clamp(28px,8vw,62px);font-weight:900;text-transform:uppercase;line-height:1;margin-bottom:.5rem;color:#fff;}
.stitle .dim{color:rgba(255,255,255,0.35);}
.divbar{width:50px;height:3px;background:#e63232;margin:1.2rem auto 2.5rem;border-radius:2px;}

.skills-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:1rem;text-align:left;}
.sk{background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);border-radius:14px;padding:1.4rem;transition:all .35s;}
.sk:hover{border-color:#e63232;background:rgba(230,50,50,0.1);transform:translateY(-4px);}
.sk-ico{width:44px;height:44px;background:rgba(230,50,50,0.18);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:.8rem;}
.sk-n{font-size:15px;font-weight:700;color:#fff;margin-bottom:.4rem;}
.sk-d{font-size:13px;color:rgba(255,255,255,0.6);line-height:1.65;}

.tools-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1rem;}
.tc{background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);border-radius:14px;padding:1.2rem;display:flex;align-items:center;gap:12px;transition:all .3s;}
.tc:hover{border-color:#e63232;transform:scale(1.03);background:rgba(230,50,50,0.09);}
.tl{width:44px;height:44px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:900;flex-shrink:0;}
.tl.ps{background:#001e36;color:#31a8ff;}
.tl.cd{background:#003d20;color:#7cfc00;}
.tl.cv{background:#5b21b6;color:#e9d5ff;}
.tl.fm{background:#0a1628;color:#00c8f0;}
.tl.cc{background:#1a1a1a;color:#eee;}
.tn{font-size:14px;font-weight:700;color:#fff;}
.tu{font-size:12px;color:rgba(255,255,255,0.5);margin-top:2px;}

.work-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.2rem;text-align:left;}
.wc{background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.14);border-radius:14px;overflow:hidden;transition:all .35s;cursor:pointer;}
.wc:hover{transform:translateY(-6px);border-color:#e63232;box-shadow:0 16px 40px rgba(0,0,0,0.6);}
.wi{height:180px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;}
.wbadge{position:absolute;top:10px;right:10px;font-size:10px;padding:3px 9px;border-radius:20px;font-weight:700;letter-spacing:.5px;}
.bps{background:rgba(49,168,255,0.2);color:#31a8ff;border:1px solid rgba(49,168,255,0.3);}
.bcv{background:rgba(160,100,255,0.2);color:#c080ff;border:1px solid rgba(160,100,255,0.3);}
.winfo{padding:1rem 1.2rem;}
.wcat{font-size:11px;letter-spacing:2px;color:#e63232;text-transform:uppercase;margin-bottom:4px;}
.wtitle{font-size:16px;font-weight:700;color:#fff;margin-bottom:4px;}
.wdesc{font-size:13px;color:rgba(255,255,255,0.55);line-height:1.65;}

.exp-list{display:flex;flex-direction:column;gap:1.2rem;max-width:820px;margin:0 auto;text-align:left;}
.ec{background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.13);border-left:3px solid #e63232;border-radius:0 14px 14px 0;padding:1.6rem 1.6rem;transition:all .4s;}
.ec:hover{background:rgba(230,50,50,0.08);border-color:rgba(230,50,50,0.5);}
.er{font-size:clamp(15px,4vw,19px);font-weight:700;color:#fff;}
.eco{font-size:clamp(13px,3.5vw,16px);color:#e63232;margin:.3rem 0;}
.ep{font-size:11px;color:rgba(255,255,255,0.4);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:.7rem;}
.ed{font-size:clamp(13px,3.5vw,15px);color:rgba(255,255,255,0.6);line-height:1.85;}

.contact-sec{border-top:1px solid rgba(230,50,50,0.25);padding:4rem 1.5rem;text-align:center;background:rgba(230,50,50,0.05);}
.c-items{display:flex;justify-content:center;gap:1.5rem;flex-wrap:wrap;margin:1.8rem 0 2rem;}
.ci{font-size:clamp(13px,3.5vw,16px);color:rgba(255,255,255,0.7);}
.ci strong{color:#fff;}

.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.88);z-index:9999;align-items:center;justify-content:center;padding:1rem;}
.modal-bg.open{display:flex;}
.modal{background:#111;border:1px solid rgba(230,50,50,0.4);border-radius:16px;padding:2rem 1.5rem;width:100%;max-width:520px;position:relative;}
.modal h3{font-size:20px;font-weight:900;color:#fff;margin-bottom:.4rem;}
.modal p{font-size:13px;color:rgba(255,255,255,0.5);margin-bottom:1.2rem;}
.modal textarea{width:100%;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.15);border-radius:8px;color:#fff;font-size:14px;padding:.9rem;line-height:1.7;resize:none;height:200px;outline:none;font-family:system-ui,sans-serif;}
.modal textarea:focus{border-color:#e63232;}
.modal-actions{display:flex;gap:.8rem;margin-top:1rem;flex-wrap:wrap;}
.close-btn{position:absolute;top:.9rem;right:1.1rem;background:none;border:none;color:rgba(255,255,255,0.5);font-size:22px;cursor:pointer;}
.close-btn:hover{color:#e63232;}
.copy-btn{background:rgba(255,255,255,0.08);color:#fff;border:1px solid rgba(255,255,255,0.2);padding:10px 18px;border-radius:6px;font-size:13px;cursor:pointer;letter-spacing:.5px;transition:all .2s;}
.copy-btn:hover{border-color:#e63232;color:#e63232;}
.gen-btn{background:#e63232;color:#fff;border:none;padding:10px 20px;border-radius:6px;font-size:13px;cursor:pointer;letter-spacing:.5px;font-weight:700;transition:all .2s;}
.gen-btn:hover{background:#ff4444;}
.loading-dots{display:none;align-items:center;gap:6px;margin-top:.8rem;}
.loading-dots.show{display:flex;}
.dot{width:8px;height:8px;background:#e63232;border-radius:50%;animation:bounce .8s infinite;}
.dot:nth-child(2){animation-delay:.15s;}
.dot:nth-child(3){animation-delay:.3s;}
@keyframes bounce{0%,80%,100%{transform:scale(.8);opacity:.5;}40%{transform:scale(1.2);opacity:1;}}

.sec-divider{border-top:1px solid rgba(255,255,255,0.08);}
.footer{font-size:12px;color:rgba(255,255,255,0.2);padding:1.2rem;text-align:center;}

@media(max-width:640px){
  .hamburger{display:flex;}
  .nav-links{display:none;position:fixed;top:0;left:0;width:100%;height:100vh;background:rgba(8,8,8,0.98);flex-direction:column;align-items:center;justify-content:center;gap:2.5rem;z-index:1000;}
  .nav-links.open{display:flex;}
  .nav-links a{font-size:18px;letter-spacing:3px;}
  .nav-links a::after{display:none;}
  .btns{flex-direction:column;align-items:center;}
  .btn-r,.btn-g{width:100%;max-width:280px;text-align:center;}
  .stats{gap:.8rem;}
  .stat{padding:1rem 1.2rem;min-width:70px;}
  .skills-grid{grid-template-columns:1fr 1fr;}
  .tools-grid{grid-template-columns:1fr 1fr;}
  .work-grid{grid-template-columns:1fr;}
  .c-items{flex-direction:column;align-items:center;gap:1rem;}
  .modal-actions{flex-direction:column;}
  .copy-btn,.gen-btn{width:100%;text-align:center;}
}

@media(max-width:380px){
  .skills-grid{grid-template-columns:1fr;}
  .tools-grid{grid-template-columns:1fr;}
  .hname{font-size:42px;}
}
</style>

<div class="bg-gif">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDd4NW83Y3JyNzJ6Y3E2dTBhc3ZuczBpZXBiNXQ5NHpzMnVsM3drbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/077i6AULCXc0FKTj9s/giphy.gif" alt="tech bg"/>
</div>
<div class="bg-overlay"></div>

<div class="wrap">

<nav id="nav">
  <div class="nav-logo">HS<span>.</span></div>
  <div class="hamburger" id="ham" onclick="toggleMenu()">
    <span></span><span></span><span></span>
  </div>
  <ul class="nav-links" id="navLinks">
    <li><a class="active" onclick="goTo('hero',this)">Home</a></li>
    <li><a onclick="goTo('skills',this)">Skills</a></li>
    <li><a onclick="goTo('tools',this)">Tools</a></li>
    <li><a onclick="goTo('work',this)">Work</a></li>
    <li><a onclick="goTo('exp',this)">Experience</a></li>
    <li><a onclick="goTo('contact',this)">Contact</a></li>
  </ul>
</nav>

<div class="hero" id="hero">
  <span class="htag">Graphic Designer & Video Editor — Ludhiana, Punjab</span>
  <h1 class="hname">HARMAN<span class="script">Singh</span>CREATIVE</h1>
  <p class="hrole">Visual Storyteller & Brand Designer</p>
  <p class="hdesc">Creative and performance-driven designer with 1 year of professional experience. Skilled in crafting visually compelling content across digital, print, and video — from brand shoots to final delivery.</p>
  <div class="btns">
    <button class="btn-r" onclick="openModal()">Generate Outreach Message ↗</button>
    <button class="btn-g" onclick="goTo('work',null)">View Work ↓</button>
  </div>
  <div class="stats">
    <div class="stat"><div class="snum">1+</div><div class="slbl">Years Exp</div></div>
    <div class="stat"><div class="snum">2</div><div class="slbl">Companies</div></div>
    <div class="stat"><div class="snum">5+</div><div class="slbl">Tools</div></div>
    <div class="stat"><div class="snum">76%</div><div class="slbl">BCA Score</div></div>
  </div>
</div>

<div class="sec-divider"><div class="sec" id="skills">
  <span class="stag">What I Do</span>
  <h2 class="stitle">SKILLS & <span class="dim">EXPERTISE</span></h2>
  <div class="divbar"></div>
  <div class="skills-grid">
    <div class="sk"><div class="sk-ico">🎨</div><div class="sk-n">Graphic Design & Brand Identity</div><div class="sk-d">Cohesive visual identities for digital and print.</div></div>
    <div class="sk"><div class="sk-ico">📱</div><div class="sk-n">Social Media Creatives</div><div class="sk-d">Scroll-stopping posts for Instagram, Facebook & YouTube.</div></div>
    <div class="sk"><div class="sk-ico">🎬</div><div class="sk-n">Video Editing & Reels</div><div class="sk-d">Promo videos, reels, and testimonials with motion.</div></div>
    <div class="sk"><div class="sk-ico">🖨️</div><div class="sk-n">Print Media Design</div><div class="sk-d">Flex banners, stickers, standees & visiting cards.</div></div>
    <div class="sk"><div class="sk-ico">✍️</div><div class="sk-n">Typography & Composition</div><div class="sk-d">Bold layouts and balanced visual hierarchy.</div></div>
    <div class="sk"><div class="sk-ico">📷</div><div class="sk-n">Photography & Videography</div><div class="sk-d">Product shoots and AI-based image enhancement.</div></div>
  </div>
</div></div>

<div class="sec-divider"><div class="sec" id="tools">
  <span class="stag">My Toolkit</span>
  <h2 class="stitle">SOFTWARE & <span class="dim">TOOLS</span></h2>
  <div class="divbar"></div>
  <div class="tools-grid">
    <div class="tc"><div class="tl ps">Ps</div><div><div class="tn">Photoshop</div><div class="tu">Posters & photo editing</div></div></div>
    <div class="tc"><div class="tl cd">Cd</div><div><div class="tn">CorelDraw</div><div class="tu">Print & cards</div></div></div>
    <div class="tc"><div class="tl cv">Ca</div><div><div class="tn">Canva</div><div class="tu">Digital designs</div></div></div>
    <div class="tc"><div class="tl fm">Fm</div><div><div class="tn">Filmora</div><div class="tu">Video & reels</div></div></div>
    <div class="tc"><div class="tl cc">CC</div><div><div class="tn">CapCut PC</div><div class="tu">Short-form content</div></div></div>
  </div>
</div></div>

<div class="sec-divider"><div class="sec" id="work">
  <span class="stag">Selected Work</span>
  <h2 class="stitle">PORTFOLIO <span class="dim">SHOWCASE</span></h2>
  <div class="divbar"></div>
  <div class="work-grid">
    <div class="wc">
      <div class="wi" style="background:linear-gradient(135deg,#5a0000,#cc0000);">
        <span class="wbadge bps">Photoshop</span>
        <div style="text-align:center"><div style="font-size:40px;font-weight:900;color:rgba(255,255,255,0.13);text-transform:uppercase;letter-spacing:-2px;line-height:1;">FERRARI<br>LUXURY</div><div style="font-size:12px;color:#ffd700;letter-spacing:3px;margin-top:8px;">◆ FERRARI ◆</div></div>
      </div>
      <div class="winfo"><div class="wcat">Social Media Ad</div><div class="wtitle">Ferrari Luxury Campaign</div><div class="wdesc">Bold automotive brand poster with dramatic typography.</div></div>
    </div>
    <div class="wc">
      <div class="wi" style="background:linear-gradient(135deg,#1a0800,#7b2800);">
        <span class="wbadge bps">Photoshop</span>
        <div style="text-align:center"><div style="font-size:58px;font-weight:900;color:#e63232;text-transform:uppercase;letter-spacing:-3px;line-height:.9;">ALIVE</div><div style="font-size:11px;color:rgba(255,255,255,0.55);letter-spacing:2px;text-transform:uppercase;margin-top:10px;">Sahil Birla · JDT</div></div>
      </div>
      <div class="winfo"><div class="wcat">Music Poster</div><div class="wtitle">Alive — Song Cover</div><div class="wdesc">Cinematic music poster with atmospheric treatment.</div></div>
    </div>
    <div class="wc">
      <div class="wi" style="background:linear-gradient(135deg,#050018,#200060);">
        <span class="wbadge bps">Photoshop</span>
        <div style="text-align:center"><div style="font-size:50px;font-weight:900;color:rgba(255,255,255,0.12);letter-spacing:-2px;">NOISE</div><div style="font-size:10px;color:rgba(255,255,255,0.5);letter-spacing:2px;margin:4px 0;">FEEL EVERY BEAT</div><div style="background:rgba(230,50,50,0.9);color:#fff;padding:5px 16px;border-radius:4px;font-size:15px;font-weight:700;display:inline-block;margin-top:4px;">50% OFF</div></div>
      </div>
      <div class="winfo"><div class="wcat">Product Ad</div><div class="wtitle">JBL Noise Speaker Ad</div><div class="wdesc">Product ad with bold type and purple color grading.</div></div>
    </div>
    <div class="wc">
      <div class="wi" style="background:linear-gradient(135deg,#0a0010,#200040);">
        <span class="wbadge bcv">Canva</span>
        <div style="text-align:center;padding:1rem"><div style="font-size:12px;color:rgba(255,255,255,0.45);letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;">The</div><div style="font-size:26px;font-weight:900;color:#fff;text-transform:uppercase;letter-spacing:-1px;">VINCI TALKS</div><div style="font-family:Georgia,serif;font-style:italic;color:rgba(255,255,255,0.55);font-size:14px;margin-top:8px;">Coming Soon</div></div>
      </div>
      <div class="winfo"><div class="wcat">Event Promo</div><div class="wtitle">Vinci Talks — Coming Soon</div><div class="wdesc">Event teaser poster with spotlight effect for Growvinci.</div></div>
    </div>
    <div class="wc">
      <div class="wi" style="background:linear-gradient(135deg,#0a001a,#300070);">
        <span class="wbadge bcv">Canva</span>
        <div style="text-align:center;padding:1rem"><div style="font-size:22px;font-weight:700;color:#fff;">grow<span style="color:#c080ff;">with</span></div><div style="font-size:28px;font-weight:900;text-transform:uppercase;letter-spacing:-1px;color:#fff;">growvinci</div><div style="font-size:11px;color:rgba(255,255,255,0.45);margin-top:8px;letter-spacing:1px;">WE STRATEGIZE YOU SHINE</div></div>
      </div>
      <div class="winfo"><div class="wcat">Brand Post</div><div class="wtitle">Growvinci Brand Campaign</div><div class="wdesc">Brand awareness post with neon frame and bold typography.</div></div>
    </div>
    <div class="wc">
      <div class="wi" style="background:linear-gradient(135deg,#002800,#006600);">
        <span class="wbadge bcv">Canva</span>
        <div style="text-align:center;padding:1rem"><div style="font-size:11px;color:rgba(255,255,255,0.7);letter-spacing:2px;text-transform:uppercase;margin-bottom:4px;">Independence Day</div><div style="font-size:52px;font-weight:900;color:#ff9933;line-height:1;">50%</div><div style="font-size:20px;font-weight:700;color:#138808;">OFF</div></div>
      </div>
      <div class="winfo"><div class="wcat">Promotional</div><div class="wtitle">Independence Day Special</div><div class="wdesc">Festive promotional creative in tricolor scheme.</div></div>
    </div>
  </div>
</div></div>

<div class="sec-divider"><div class="sec" id="exp">
  <span class="stag">Where I've Worked</span>
  <h2 class="stitle">WORK <span class="dim">EXPERIENCE</span></h2>
  <div class="divbar"></div>
  <div class="exp-list">
    <div class="ec"><div class="er">Graphic Designer · Video Editor · Videographer</div><div class="eco">Growvinci IT Solutions & Eduwings Global</div><div class="ep">2025 – Present · 1 Year</div><div class="ed">Designed social media creatives, product ads, and marketing materials. Executed brand-aligned visual campaigns, conducted promotional shoots with full lighting setup, and edited reels for Instagram, Facebook, and YouTube.</div></div>
    <div class="ec"><div class="er">Creative Associate</div><div class="eco">Jwelogy — Jewellery Brand</div><div class="ep">2025</div><div class="ed">Conducted professional jewellery product shoots. Performed AI-based image enhancement and background refinement for e-commerce. Designed website banners and promotional visuals.</div></div>
    <div class="ec"><div class="er">Freelance Designer</div><div class="eco">Independent Projects</div><div class="ep">Ongoing</div><div class="ed">Delivered song posters, visiting cards, banners, logos, and flex prints for clients across music, retail, and events.</div></div>
  </div>
</div></div>

<div class="contact-sec" id="contact">
  <span class="stag" style="display:block;margin-bottom:.5rem;">Let's Connect</span>
  <h2 class="stitle">GET IN <span class="dim">TOUCH</span></h2>
  <div class="divbar"></div>
  <div class="c-items">
    <div class="ci"><strong>📞</strong> +91 98775-57408</div>
    <div class="ci"><strong>✉️</strong> hs5153210@gmail.com</div>
    <div class="ci"><strong>📍</strong> Ludhiana, Punjab</div>
  </div>
  <button class="btn-r" onclick="openModal()">Generate Outreach Message ↗</button>
  <div class="footer">© 2025 Harman Singh · All Rights Reserved</div>
</div>

</div>

<div class="modal-bg" id="modalBg" onclick="if(event.target===this)closeModal()">
  <div class="modal">
    <button class="close-btn" onclick="closeModal()">✕</button>
    <h3>✉️ Outreach Message</h3>
    <p>AI-generated Instagram DM to attract freelance clients. Click Generate to create one.</p>
    <textarea id="msgBox" placeholder="Click 'Generate' to create your outreach message..."></textarea>
    <div class="loading-dots" id="loadDots"><div class="dot"></div><div class="dot"></div><div class="dot"></div><span style="font-size:13px;color:rgba(255,255,255,0.5);margin-left:6px;">Generating...</span></div>
    <div class="modal-actions">
      <button class="gen-btn" onclick="generateMsg()">Generate ↗</button>
      <button class="copy-btn" onclick="copyMsg()">Copy Message</button>
      <button class="copy-btn" onclick="closeModal()">Close</button>
    </div>
  </div>
</div>

<script>
function toggleMenu(){
  var h=document.getElementById('ham');
  var n=document.getElementById('navLinks');
  h.classList.toggle('open');
  n.classList.toggle('open');
}
function goTo(id,el){
  var ham=document.getElementById('ham');
  var nl=document.getElementById('navLinks');
  ham.classList.remove('open');
  nl.classList.remove('open');
  var t=document.getElementById(id);
  if(t) t.scrollIntoView({behavior:'smooth'});
  if(el){
    document.querySelectorAll('.nav-links a').forEach(function(a){a.classList.remove('active');});
    el.classList.add('active');
  }
}
window.addEventListener('scroll',function(){
  var nav=document.getElementById('nav');
  if(window.scrollY>60) nav.classList.add('scrolled');
  else nav.classList.remove('scrolled');
});
function openModal(){document.getElementById('modalBg').classList.add('open');}
function closeModal(){document.getElementById('modalBg').classList.remove('open');}
async function generateMsg(){
  var box=document.getElementById('msgBox');
  var dots=document.getElementById('loadDots');
  box.value='';
  dots.classList.add('show');
  try{
    var res=await fetch('https://api.anthropic.com/v1/messages',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({
        model:'claude-sonnet-4-20250514',
        max_tokens:1000,
        messages:[{role:'user',content:'Write a short friendly professional Instagram DM for Harman Singh, graphic designer and video editor from Ludhiana Punjab, 1 year experience at Growvinci IT Solutions and Eduwings Global. Skilled in Photoshop CorelDraw Canva Filmora. Message is for attracting freelance clients for graphic design social media posts and video editing. Under 120 words, conversational not salesy, end with clear CTA. Write only the message no preamble.'}]
      })
    });
    var data=await res.json();
    box.value=data.content&&data.content[0]?data.content[0].text:"Hey! I'm Harman Singh, a graphic designer & video editor from Ludhiana with 1 year of professional experience.\n\nI specialize in social media creatives, reels, product ads, and print design using Photoshop, Canva & Filmora.\n\nIf you're looking to level up your brand's visual presence, I'd love to help! Drop me a message and let's talk. 🎨\n\n— Harman Singh\n📞 +91 98775-57408";
  }catch(e){
    box.value="Hey! I'm Harman Singh, a graphic designer & video editor from Ludhiana with 1 year of professional experience.\n\nI specialize in social media creatives, reels, product ads, and print design using Photoshop, Canva & Filmora.\n\nLooking to level up your brand? Let's connect! 🎨\n\n📞 +91 98775-57408";
  }
  dots.classList.remove('show');
}
function copyMsg(){
  var box=document.getElementById('msgBox');
  if(box.value){
    navigator.clipboard.writeText(box.value).then(function(){
      var btns=document.querySelectorAll('.copy-btn');
      btns[0].textContent='Copied!';
      setTimeout(function(){btns[0].textContent='Copy Message';},2000);
    });
  }
}
</script> -->
