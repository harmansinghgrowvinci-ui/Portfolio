/* ── Loader ── */
window.addEventListener('load', function() {
  setTimeout(function() {
    document.getElementById('loader').classList.add('hidden');
  }, 2000);
});

/* ── Background canvas — flowing particles + lines ── */
(function(){
  var canvas = document.getElementById('bgCanvas');
  if(!canvas) return;
  var ctx = canvas.getContext('2d');
  var W, H, particles = [];
  var COUNT = 60;
  var CONNECT_DIST = 150;

  function resize(){
    W = canvas.width  = window.innerWidth;
    H = canvas.height = window.innerHeight;
    canvas.style.width  = W + 'px';
    canvas.style.height = H + 'px';
  }
  resize();
  window.addEventListener('resize', function(){ resize(); particles=[]; init(); });

  function rand(a,b){ return Math.random()*(b-a)+a; }

  function init(){
    particles = [];
    for(var i=0;i<COUNT;i++){
      particles.push({
        x: rand(0,W), y: rand(0,H),
        vx: rand(-0.3,0.3), vy: rand(-0.2,0.2),
        r: rand(1,2.5),
        a: rand(0.15,0.35)
      });
    }
  }
  init();

  function draw(){
    ctx.clearRect(0,0,W,H);
    for(var a=0;a<particles.length;a++){
      var pa = particles[a];
      for(var b=a+1;b<particles.length;b++){
        var pb = particles[b];
        var dx=pa.x-pb.x, dy=pa.y-pb.y;
        var dist=Math.sqrt(dx*dx+dy*dy);
        if(dist<CONNECT_DIST){
          ctx.beginPath();
          ctx.moveTo(pa.x,pa.y);
          ctx.lineTo(pb.x,pb.y);
          ctx.strokeStyle='rgba(230,50,50,'+(0.12*(1-dist/CONNECT_DIST))+')';
          ctx.lineWidth=0.7;
          ctx.stroke();
        }
      }
    }
    for(var i=0;i<particles.length;i++){
      var p=particles[i];
      ctx.beginPath();
      ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
      ctx.fillStyle='rgba(230,50,50,'+p.a+')';
      ctx.fill();
      p.x+=p.vx; p.y+=p.vy;
      if(p.x<-10) p.x=W+10;
      if(p.x>W+10) p.x=-10;
      if(p.y<-10) p.y=H+10;
      if(p.y>H+10) p.y=-10;
    }
    requestAnimationFrame(draw);
  }
  draw();
})();


var sectionColors = {
  hero:    { cur: '#e63232', glow: 'rgba(230,50,50,0.13)' },
  skills:  { cur: '#ff6b35', glow: 'rgba(255,107,53,0.13)' },
  tools:   { cur: '#00c8f0', glow: 'rgba(0,200,240,0.11)' },
  work:    { cur: '#c080ff', glow: 'rgba(192,128,255,0.11)' },
  exp:     { cur: '#ffd700', glow: 'rgba(255,215,0,0.11)'  },
  contact: { cur: '#00c850', glow: 'rgba(0,200,80,0.11)'  }
};
var curColor = '#e63232';

function setCursorColor(id) {
  var c = sectionColors[id] || sectionColors.hero;
  curColor = c.cur;
  document.documentElement.style.setProperty('--cur-color', c.cur);
  document.documentElement.style.setProperty('--glow-color', c.glow);
}

/* ── Custom cursor + magnetic + trail ── */
var dot   = document.getElementById('cursor-dot');
var ring  = document.getElementById('cursor-ring');
var glow  = document.getElementById('cursor-glow');

var mx = -999, my = -999;   // real mouse
var rx = -999, ry = -999;   // ring (lagging)
var lastTrail = 0;
var isMobile = window.matchMedia('(max-width:640px)').matches;

document.addEventListener('mousemove', function(e) {
  mx = e.clientX; my = e.clientY;
  dot.style.left  = mx + 'px';
  dot.style.top   = my + 'px';
  glow.style.left = mx + 'px';
  glow.style.top  = my + 'px';

  /* Particle trail — spawn every 40ms */
  var now = Date.now();
  if (now - lastTrail > 40) {
    lastTrail = now;
    spawnParticle(mx, my);
  }
});

/* Smooth lagging ring via rAF */
function animateRing() {
  rx += (mx - rx) * 0.12;
  ry += (my - ry) * 0.12;
  ring.style.left = rx + 'px';
  ring.style.top  = ry + 'px';
  requestAnimationFrame(animateRing);
}
animateRing();

/* Magnetic effect on hover targets */
var magnetTargets = 'button, a, .wc, .sk, .tc, .stat, .ec, .float-btn';
document.querySelectorAll(magnetTargets).forEach(addMagnet);

/* Also apply to dynamically relevant elements */
function addMagnet(el) {
  el.addEventListener('mouseenter', function() {
    ring.classList.add('hovering');
    dot.style.transform = 'translate(-50%,-50%) scale(0.4)';
  });
  el.addEventListener('mousemove', function(e) {
    var r   = el.getBoundingClientRect();
    var cx  = r.left + r.width  / 2;
    var cy  = r.top  + r.height / 2;
    var dx  = (e.clientX - cx) * 0.28;
    var dy  = (e.clientY - cy) * 0.28;
    el.style.transform = 'translate(' + dx + 'px,' + dy + 'px)';
  });
  el.addEventListener('mouseleave', function() {
    ring.classList.remove('hovering');
    dot.style.transform = 'translate(-50%,-50%) scale(1)';
    el.style.transform = '';
  });
}

/* Spawn a single trail particle */
function spawnParticle(x, y) {
  if (isMobile) return;
  var p = document.createElement('div');
  p.className = 'trail-dot';
  var size = Math.random() * 5 + 3;
  p.style.cssText = 'width:' + size + 'px;height:' + size + 'px;left:' + x + 'px;top:' + y + 'px;background:' + curColor + ';';
  document.body.appendChild(p);
  setTimeout(function() { p.remove(); }, 600);
}

/* ── Typing effect ── */
var typedEl = document.getElementById('typed');
var roles = ['Visual Storyteller & Brand Designer', 'Graphic Designer & Video Editor'];
var ri = 0, ci = 0, deleting = false;
function type() {
  var word = roles[ri];
  if (!deleting) {
    ci++;
    typedEl.textContent = word.slice(0, ci);
    if (ci === word.length) { deleting = true; setTimeout(type, 1600); return; }
  } else {
    ci--;
    typedEl.textContent = word.slice(0, ci);
    if (ci === 0) { deleting = false; ri = (ri + 1) % roles.length; }
  }
  setTimeout(type, deleting ? 40 : 80);
}
type();

/* ── Nav scroll + active nav + section color shift ── */
var sections = ['hero','skills','tools','work','exp','contact'];
window.addEventListener('scroll', function() {
  var nav = document.getElementById('nav');
  if (window.scrollY > 60) nav.classList.add('scrolled');
  else nav.classList.remove('scrolled');

  var scrollY = window.scrollY + 160;
  sections.forEach(function(id) {
    var el = document.getElementById(id);
    if (!el) return;
    if (el.offsetTop <= scrollY && el.offsetTop + el.offsetHeight > scrollY) {
      /* Active nav link */
      document.querySelectorAll('.nav-links a').forEach(function(a) { a.classList.remove('active'); });
      var link = document.querySelector('.nav-links a[onclick*="' + id + '"]');
      if (link) link.classList.add('active');
      /* Cursor color shift */
      setCursorColor(id);
    }
  });
});

/* ── Scroll reveal + skill bars ── */
var revealObserver = new IntersectionObserver(function(entries) {
  entries.forEach(function(entry) {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      var fill = entry.target.querySelector('.skill-fill');
      if (fill) fill.style.transform = 'scaleX(' + (fill.dataset.w / 100) + ')';
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.15 });
document.querySelectorAll('.reveal').forEach(function(el) { revealObserver.observe(el); });

/* ── Nav goTo ── */
function goTo(id, el) {
  var t = document.getElementById(id);
  if (t) t.scrollIntoView({ behavior: 'smooth' });
  if (el) {
    document.querySelectorAll('.nav-links a').forEach(function(a) { a.classList.remove('active'); });
    el.classList.add('active');
  }
}

/* ── Lightbox ── */
function openLightbox(title, cat, tool, desc, bg) {
  document.getElementById('lbContent').innerHTML =
    '<div class="lb-preview" style="background:' + bg + ';">' +
      '<div style="text-align:center;padding:1rem"><div style="font-size:32px;font-weight:900;color:rgba(255,255,255,0.15);text-transform:uppercase;letter-spacing:-2px;">' + title.split('—')[0].trim() + '</div></div>' +
    '</div>' +
    '<div class="lb-body">' +
      '<div class="lb-cat">' + cat + '</div>' +
      '<div class="lb-title">' + title + '</div>' +
      '<div class="lb-tool">Made with ' + tool + '</div>' +
      '<div class="lb-desc">' + desc + '</div>' +
    '</div>';
  document.getElementById('lightboxBg').classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeLightbox() {
  document.getElementById('lightboxBg').classList.remove('open');
  document.body.style.overflow = '';
}
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') { closeLightbox(); closeModal(); }
});

/* ── Contact form ── */
function submitForm(e) {
  e.preventDefault();
  var form = e.target;
  var name    = form.querySelector('[name=name]').value.trim();
  var email   = form.querySelector('[name=email]').value.trim();
  var subject = form.querySelector('[name=subject]').value.trim() || 'Portfolio Contact';
  var message = form.querySelector('[name=message]').value.trim();
  var btn = form.querySelector('.form-submit');
  btn.textContent = 'Sending...';
  btn.disabled = true;

  /* mailto fallback — always works without a backend */
  var body = 'Name: ' + name + '\nEmail: ' + email + '\n\n' + message;
  var mailto = 'mailto:hs5153210@gmail.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
  window.open(mailto, '_blank');

  form.reset();
  btn.textContent = 'Send Message ↗';
  btn.disabled = false;
  showToast();
}

function showToast() {
  var overlay = document.getElementById('toastOverlay');
  overlay.classList.remove('hiding');
  overlay.classList.add('show');
  document.body.style.overflow = 'hidden';
}

function closeToast() {
  var overlay = document.getElementById('toastOverlay');
  overlay.classList.add('hiding');
  setTimeout(function() {
    overlay.classList.remove('show', 'hiding');
    document.body.style.overflow = '';
  }, 300);
}


function openModal() { document.getElementById('modalBg').classList.add('open'); document.body.style.overflow = 'hidden'; }
function closeModal() { document.getElementById('modalBg').classList.remove('open'); document.body.style.overflow = ''; }

async function generateMsg() {
  var box = document.getElementById('msgBox');
  var dots = document.getElementById('loadDots');
  box.value = '';
  dots.classList.add('show');
  var fallback = "Hey! I'm Harman Singh, a graphic designer & video editor from Ludhiana with 1 year of professional experience.\n\nI specialize in social media creatives, reels, product ads, and print design using Photoshop, Canva & Filmora.\n\nLooking to level up your brand? Let's connect! 🎨\n\n📞 +91 98775-57408";
  try {
    var res = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 1000,
        messages: [{ role: 'user', content: 'Write a short friendly professional Instagram DM for Harman Singh, graphic designer and video editor from Ludhiana Punjab, 1 year experience at Growvinci IT Solutions and Eduwings Global. Skilled in Photoshop CorelDraw Canva Filmora. Message is for attracting freelance clients for graphic design social media posts and video editing. Under 120 words, conversational not salesy, end with clear CTA. Write only the message no preamble.' }]
      })
    });
    var data = await res.json();
    box.value = data.content && data.content[0] ? data.content[0].text : fallback;
  } catch (e) { box.value = fallback; }
  dots.classList.remove('show');
}

function copyMsg() {
  var box = document.getElementById('msgBox');
  if (box.value) {
    navigator.clipboard.writeText(box.value).then(function() {
      var btn = document.querySelectorAll('.copy-btn')[0];
      btn.textContent = 'Copied!';
      setTimeout(function() { btn.textContent = 'Copy Message'; }, 2000);
    });
  }
}
