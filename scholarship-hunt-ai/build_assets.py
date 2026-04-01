import os

css_path = r'C:\Users\EURO COMPUTERS\Desktop\Ai Hub\scholarship-hunt-ai\styles.css'
js_path = r'C:\Users\EURO COMPUTERS\Desktop\Ai Hub\scholarship-hunt-ai\script.js'

css = """
/* =========================================================================
   SaaS PREMIUM THEME VARIABLES & RESET
   ========================================================================= */
:root, .theme-light {
    --bg-main: #f8fafc;
    --bg-surface: rgba(255, 255, 255, 0.75);
    --bg-alt: #f1f5f9;
    --text-main: #0f172a;
    --text-muted: #475569;
    --border-color: rgba(226, 232, 240, 0.8);
    
    --primary: #4f46e5;
    --primary-hover: #4338ca;
    --accent: #ec4899;
    --danger: #ef4444;
    
    --primary-grad: linear-gradient(135deg, #4f46e5 0%, #ec4899 100%);
    
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.05);
    --shadow-md: 0 10px 25px -5px rgba(0,0,0,0.05), 0 8px 10px -6px rgba(0,0,0,0.01);
    --shadow-lg: 0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04);
    --shadow-glow: 0 10px 30px -10px rgba(79, 70, 229, 0.5);
    
    --radius-md: 12px;
    --radius-lg: 20px;
    --radius-full: 9999px;
    
    --transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    
    --glass-bg: rgba(255, 255, 255, 0.6);
    --glass-border: rgba(255, 255, 255, 0.8);
    --glass-blur: blur(16px);
}

.theme-dark {
    --bg-main: #0b0f19;
    --bg-surface: rgba(30, 41, 59, 0.6);
    --bg-alt: #111827;
    --text-main: #f8fafc;
    --text-muted: #94a3b8;
    --border-color: rgba(51, 65, 85, 0.6);
    
    --primary: #6366f1;
    --primary-hover: #818cf8;
    --accent: #f472b6;
    
    --primary-grad: linear-gradient(135deg, #6366f1 0%, #f472b6 100%);
    
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.5);
    --shadow-md: 0 10px 25px -5px rgba(0,0,0,0.5);
    --shadow-lg: 0 20px 25px -5px rgba(0,0,0,0.6);
    --shadow-glow: 0 10px 30px -10px rgba(99, 102, 241, 0.5);
    
    --glass-bg: rgba(15, 23, 42, 0.6);
    --glass-border: rgba(255, 255, 255, 0.05);
}

* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    font-family: 'Inter', sans-serif;
    background-color: var(--bg-main);
    color: var(--text-main);
    line-height: 1.6;
    overflow-x: hidden;
    position: relative;
    transition: background-color 0.4s ease;
}
h1, h2, h3, h4, h5, h6 { font-family: 'Poppins', sans-serif; font-weight: 600; }
a { color: var(--primary); text-decoration: none; transition: var(--transition); }
button, input, select { font-family: inherit; }
.text-muted { color: var(--text-muted) !important; }
.text-dark { color: var(--text-main) !important; }
.text-white { color: white !important; }

/* UTILS */
.container { width: 100%; max-width: 1200px; margin: 0 auto; padding: 0 24px; }
.section { padding: 100px 0; position: relative; }
.grid-2 { display: grid; grid-template-columns: 1fr; gap: 32px; }
.grid-3 { display: grid; grid-template-columns: 1fr; gap: 32px; }
@media(min-width: 768px) { .grid-2 { grid-template-columns: 1fr 1fr; } }
@media(min-width: 1024px) { .grid-3 { grid-template-columns: 1fr 1fr 1fr; gap: 40px; } }
.flex-between { display: flex; justify-content: space-between; align-items: center; }
.flex-left { display: flex; align-items: center; }
.flex-center { display: flex; justify-content: center; align-items: center; }
.mt-2 { margin-top: 8px; } .mb-2 { margin-bottom: 8px; }
.mt-3 { margin-top: 16px; } .mb-3 { margin-bottom: 16px; }
.mt-4 { margin-top: 24px; } .mb-4 { margin-bottom: 24px; }
.mt-5 { margin-top: 32px; } .mb-5 { margin-bottom: 32px; }
.mt-6 { margin-top: 48px; }
.p-0 { padding: 0 !important; }
.p-4 { padding: 24px; }
.p-5 { padding: 32px; }
.p-6 { padding: 40px; }
.w-full { width: 100%; }
.text-center { text-align: center; }
.text-right { text-align: right; }
.relative { position: relative; }
.border-top { border-top: 1px solid var(--border-color); }
.gap-3 { gap: 16px; }

/* BACKGROUND BLOBS */
.blob {
    position: absolute; filter: blur(80px); opacity: 0.4; z-index: -1; 
    border-radius: 50%; pointer-events: none;
    animation: floatBlob 20s infinite alternate;
}
.blob-1 { top: -100px; left: -100px; width: 400px; height: 400px; background: #4f46e5; }
.blob-2 { top: 20%; right: -150px; width: 500px; height: 500px; background: #ec4899; animation-delay: -5s; }
.blob-3 { bottom: 10%; left: 10%; width: 350px; height: 350px; background: #8b5cf6; animation-delay: -10s; }
@keyframes floatBlob {
    0% { transform: translate(0, 0) scale(1); }
    100% { transform: translate(50px, 50px) scale(1.1); }
}

.bg-alt-grad { background-color: var(--bg-alt); }
.pattern-bg {
    background-image: radial-gradient(var(--border-color) 1px, transparent 1px);
    background-size: 24px 24px;
}

/* GLASSMORPHISM */
.glass {
    background: var(--glass-bg);
    backdrop-filter: var(--glass-blur);
    -webkit-backdrop-filter: var(--glass-blur);
    border: 1px solid var(--glass-border);
}
.glass-card {
    background: var(--bg-surface);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    position: relative;
    overflow: hidden;
}

/* HEADINGS & TEXT */
.gradient-text {
    background: var(--primary-grad);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
}
.section-header { text-align: center; margin-bottom: 64px; }
.section-title { font-size: 2.5rem; letter-spacing: -0.5px; margin-bottom: 16px; color: var(--text-main); }
.section-desc { font-size: 1.15rem; color: var(--text-muted); max-width: 600px; margin: 0 auto; }

/* BUTTONS */
.btn {
    display: inline-flex; align-items: center; justify-content: center;
    padding: 12px 24px; border-radius: var(--radius-md); font-weight: 600;
    transition: var(--transition); cursor: pointer; border: none; font-size: 1rem;
}
.btn-lg { padding: 16px 32px; font-size: 1.1rem; }
.btn-primary { background: var(--primary); color: white; }
.btn-primary:hover { background: var(--primary-hover); transform: translateY(-2px); box-shadow: var(--shadow-md); }
.gradient-btn { background: var(--primary-grad); color: white; }
.gradient-btn:hover { box-shadow: var(--shadow-glow); }
.shadow-glow { box-shadow: var(--shadow-glow); }
.btn-outline { background: transparent; border: 1px solid var(--border-color); color: var(--text-main); }
.btn-outline:hover { border-color: var(--primary); color: var(--primary); }
.btn-glass { background: var(--glass-bg); border: 1px solid var(--border-color); color: var(--text-main); backdrop-filter: blur(10px); }
.btn-glass:hover { background: var(--primary); color: white; border-color: var(--primary); }
.btn-icon { padding: 10px; border-radius: 50%; width: 44px; height: 44px; }
.btn-circle { border-radius: 50%; width: 50px; height: 50px; padding: 0; }
.pulse-hover:hover { animation: pulse 1s infinite; }
@keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.05); } 100% { transform: scale(1); } }

/* NAVBAR */
.navbar { position: fixed; top: 0; width: 100%; z-index: 1000; transition: var(--transition); border-bottom: 1px solid transparent; }
.navbar.scrolled { border-bottom: 1px solid var(--border-color); box-shadow: var(--shadow-sm); }
.nav-content { height: 80px; display: flex; justify-content: space-between; align-items: center; }
.logo { display: flex; align-items: center; gap: 12px; font-size: 1.5rem; font-weight: 700; color: var(--text-main); font-family: 'Poppins', sans-serif;}
.logo-icon { width: 40px; height: 40px; border-radius: 10px; background: var(--primary-grad); color: white; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; }
.nav-links { display: flex; gap: 32px; }
.nav-link { color: var(--text-muted); font-weight: 500; font-size: 0.95rem; }
.nav-link:hover { color: var(--primary); }
.nav-controls { display: flex; gap: 12px; align-items: center; }
.mobile-only { display: none; }
@media(max-width: 991px) { .desktop-only { display: none; } .mobile-only { display: inline-flex; } }

/* MOBILE MENU */
.mobile-menu { display: none; position: absolute; top: 80px; left: 0; width: 100%; flex-direction: column; padding: 24px; border-bottom: 1px solid var(--border-color); box-shadow: var(--shadow-md); transform: translateY(-10px); opacity: 0; transition: var(--transition); }
.mobile-menu.active { display: flex; transform: translateY(0); opacity: 1; }
.mobile-link { padding: 16px; border-bottom: 1px solid var(--border-color); color: var(--text-main); font-weight: 600; font-size: 1.1rem; }
.mobile-link:last-child { border-bottom: none; }

/* HERO SECTION */
.hero-section { padding: 180px 0 100px 0; text-align: center; }
.badge-pill { display: inline-flex; align-items: center; gap: 8px; padding: 6px 16px; border-radius: 30px; background: rgba(79, 70, 229, 0.1); color: var(--primary); font-weight: 600; font-size: 0.85rem; margin-bottom: 24px; border: 1px solid rgba(79, 70, 229, 0.2); }
.badge-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--primary); box-shadow: 0 0 10px var(--primary); }
.hero-section .main-title { font-size: 4rem; line-height: 1.1; margin-bottom: 24px; }
.hero-section .subtitle { font-size: 1.25rem; max-width: 700px; margin: 0 auto 40px auto; }
.hero-actions { display: flex; justify-content: center; gap: 16px; flex-wrap: wrap; }
.quote-container { margin-top: 64px; max-width: 800px; margin-left: auto; margin-right: auto; padding: 32px; border-radius: var(--radius-lg); }
.quote { font-size: 1.2rem; font-style: italic; margin-bottom: 12px; color: var(--text-main); }
.quote-author { color: var(--text-muted); font-weight: 500; font-size: 0.95rem; }
@media(max-width: 768px) { .hero-section .main-title { font-size: 2.8rem; } }

/* ROADMAP VISUAL */
.roadmap-section { margin-top: -40px; }
.roadmap-card { padding: 48px; }
.progress-container { position: relative; }
.progress-bar-bg { position: absolute; top: 28px; left: 0; width: 100%; height: 6px; background-color: var(--border-color); border-radius: 3px; z-index: 1; }
.progress-bar-fill { height: 100%; width: 0%; background: var(--primary-grad); border-radius: 3px; transition: width 1s cubic-bezier(0.16, 1, 0.3, 1); box-shadow: var(--shadow-glow); }
.progress-steps { position: relative; z-index: 2; display: flex; justify-content: space-between; }
.step { display: flex; flex-direction: column; align-items: center; gap: 16px; text-align: center; width: 100px; color: var(--text-muted); transition: var(--transition); }
.glass-icon { width: 60px; height: 60px; border-radius: 50%; background: var(--bg-surface); border: 2px solid var(--border-color); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; transition: var(--transition); color: var(--text-muted); }
.step.active .glass-icon, .step.completed .glass-icon { border-color: var(--primary); background: var(--primary-grad); color: white; box-shadow: 0 0 0 8px rgba(79, 70, 229, 0.15); transform: scale(1.1); }
.step.active span, .step.completed span { color: var(--text-main); font-weight: 600; }
@media(max-width: 600px) { .step span {font-size: 0.75rem;} .glass-icon{width:40px;height:40px;font-size:1rem;} .progress-bar-bg{top:18px;} }

/* STEPPER FORM */
.form-tabs { border-bottom: 1px solid var(--border-color); margin-bottom: 32px; display: flex; overflow-x: auto; scrollbar-width: none; }
.form-tab { padding: 16px 24px; font-weight: 600; color: var(--text-muted); cursor: pointer; transition: var(--transition); white-space: nowrap; border-bottom: 3px solid transparent; }
.form-tab span { opacity: 0.5; margin-right: 4px; }
.form-tab.active { color: var(--primary); border-bottom-color: var(--primary); }
.form-progress { height: 4px; background: var(--border-color); width: 100%; margin-top: -33px; margin-bottom: 32px; border-radius: 2px; }
.form-progress-bar { height: 100%; background: var(--primary); width: 25%; transition: width 0.4s ease; border-radius: 2px; }
.form-slide { display: none; animation: slideIn 0.4s ease; }
.form-slide.active { display: block; }
@keyframes slideIn { from { opacity: 0; transform: translateX(20px); } to { opacity: 1; transform: translateX(0); } }

/* MODERN INPUTS */
.input-group label, .doc-item label { display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.9rem; color: var(--text-main); }
.glass-input { width: 100%; padding: 16px 20px; border-radius: var(--radius-md); border: 1px solid var(--border-color); background: rgba(255, 255, 255, 0.05); color: var(--text-main); font-size: 1rem; transition: var(--transition); outline: none; -webkit-appearance: none; }
.glass-input:focus { border-color: var(--primary); box-shadow: 0 0 0 4px rgba(79,70,229,0.1); background: var(--bg-surface); }
.select-wrapper { position: relative; }
.select-icon { position: absolute; right: 20px; top: 50%; transform: translateY(-50%); color: var(--text-muted); pointer-events: none; }

/* CHECKBOXES */
.eligibility-grid { display: grid; gap: 16px; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); }
.custom-checkbox { display: flex; align-items: center; gap: 16px; cursor: pointer; padding: 16px 20px; border: 1px solid var(--border-color); border-radius: var(--radius-md); transition: var(--transition); background: rgba(255,255,255,0.02); }
.custom-checkbox:hover { border-color: var(--primary); background: rgba(79,70,229,0.03); }
.custom-checkbox input { display: none; }
.checkbox-box { width: 24px; height: 24px; border-radius: 6px; border: 2px solid var(--border-color); display: flex; align-items: center; justify-content: center; transition: var(--transition); }
.checkbox-box i { color: white; font-size: 0.8rem; transform: scale(0); transition: var(--transition); }
.custom-checkbox input:checked + .checkbox-box { background: var(--primary); border-color: var(--primary); box-shadow: 0 4px 10px rgba(79,70,229,0.3); }
.custom-checkbox input:checked + .checkbox-box i { transform: scale(1); }
.custom-checkbox span { font-weight: 500; color: var(--text-main); }

/* PROMPTS */
.filter-controls { gap: 12px; flex-wrap: wrap; }
.filter-btn { padding: 10px 20px; border-radius: 30px; border: 1px solid var(--border-color); background: transparent; color: var(--text-muted); font-weight: 600; cursor: pointer; transition: var(--transition); }
.filter-btn:hover, .filter-btn.active { background: var(--primary); color: white; border-color: var(--primary); box-shadow: 0 4px 12px rgba(79,70,229,0.2); }
.prompt-card { display: flex; flex-direction: column; height: 100%; transition: all 0.4s ease; transform: translateY(0); }
.prompt-card.hide { display: none; }
.fancy-hover:hover { transform: translateY(-8px); box-shadow: var(--shadow-lg); border-color: rgba(79, 70, 229, 0.3); }
.category-badge { display: inline-block; padding: 6px 14px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; margin-bottom: 20px; letter-spacing: 0.5px; text-transform: uppercase; align-self: flex-start; }
.badge-discovery { background: rgba(59, 130, 246, 0.1); color: #3b82f6; }
.badge-documents { background: rgba(16, 185, 129, 0.1); color: #10b981; }
.badge-outreach { background: rgba(245, 158, 11, 0.1); color: #f59e0b; }
.badge-interview { background: rgba(139, 92, 246, 0.1); color: #8b5cf6; }
.prompt-card h3 { font-size: 1.35rem; margin-bottom: 12px; }
.prompt-snippet { background: rgba(0,0,0,0.03); padding: 20px; border-radius: var(--radius-md); font-family: monospace; font-size: 0.9rem; margin-bottom: 24px; border: 1px solid var(--border-color); flex-grow: 1; color: var(--text-muted); }
.theme-dark .prompt-snippet { background: rgba(255,255,255,0.02); }

/* CHATBOT */
.chat-container { overflow: hidden; height: 500px; display: flex; flex-direction: column; }
.chat-header { border-bottom: 1px solid var(--border-color); background: rgba(255,255,255,0.02); }
.bot-avatar { width: 44px; height: 44px; border-radius: var(--radius-md); }
.gradient-bg { background: var(--primary-grad); }
.dot-online { display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #10b981; margin-right: 4px; box-shadow: 0 0 8px #10b981; animation: blink 2s infinite; }
@keyframes blink { 0% {opacity:1} 50% {opacity:0.4} 100% {opacity:1} }
.status-online { font-size: 0.8rem; color: var(--text-muted); font-weight: 500; }
.chat-box { flex-grow: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 20px; }
.message-wrapper { display: flex; width: 100%; margin-bottom: 4px; }
.message-wrapper.bot { justify-content: flex-start; }
.message-wrapper.user { justify-content: flex-end; }
.message { max-width: 80%; padding: 14px 20px; font-size: 0.95rem; line-height: 1.5; animation: chatPop 0.3s cubic-bezier(0.16,1,0.3,1); }
@keyframes chatPop { 0% { opacity:0; transform: scale(0.95) translateY(10px); } 100% { opacity:1; transform: scale(1) translateY(0); } }
.glass-msg { background: var(--bg-alt); color: var(--text-main); border-radius: 20px 20px 20px 4px; border: 1px solid var(--border-color); }
.user-msg { background: var(--primary-grad); color: white; border-radius: 20px 20px 4px 20px; box-shadow: var(--shadow-sm); }
.scrollbar::-webkit-scrollbar { width: 6px; }
.scrollbar::-webkit-scrollbar-track { background: transparent; }
.scrollbar::-webkit-scrollbar-thumb { background: var(--border-color); border-radius: 10px; }
.chat-input-area { display: flex; gap: 12px; background: rgba(255,255,255,0.02); }
.chat-input-area input { border-radius: 30px; }

/* TRACKER */
.modern-table { width: 100%; border-collapse: separate; border-spacing: 0; min-width: 600px; }
.table-container { overflow-x: auto; }
.modern-table th { text-align: left; padding: 20px 24px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; color: var(--text-muted); border-bottom: 2px solid var(--border-color); }
.modern-table td { padding: 20px 24px; border-bottom: 1px solid var(--border-color); vertical-align: middle; }
.modern-table tr:last-child td { border-bottom: none; }
.modern-table tr:hover td { background: rgba(255,255,255,0.03); }
.status-badge { padding: 6px 14px; border-radius: 30px; font-size: 0.85rem; font-weight: 600; display: inline-flex; align-items: center; gap: 6px; }
.status-badge::before { content: ''; display: block; width: 6px; height: 6px; border-radius: 50%; }
.status-Planned { background: rgba(245, 158, 11, 0.1); color: #d97706; }
.status-Planned::before { background: #d97706; }
.status-Applied { background: rgba(59, 130, 246, 0.1); color: #2563eb; }
.status-Applied::before { background: #2563eb; }
.status-Completed { background: rgba(16, 185, 129, 0.1); color: #059669; }
.status-Completed::before { background: #059669; }
.btn-delete { background: transparent; border: none; color: var(--danger); width: 36px; height: 36px; border-radius: var(--radius-md); transition: var(--transition); cursor: pointer; display: flex; align-items: center; justify-content: center; }
.btn-delete:hover { background: rgba(239, 68, 68, 0.1); transform: scale(1.1); }
.empty-icon { width: 80px; height: 80px; border-radius: 50%; background: var(--bg-alt); font-size: 2rem; color: var(--text-muted); }

/* RESOURCES CARDS */
.card-feature { display: flex; flex-direction: column; height: 100%; border-top: 4px solid transparent; transition: all 0.4s ease; }
.card-feature:hover { border-top-color: var(--primary); }
.card-icon { width: 56px; height: 56px; border-radius: 16px; font-size: 1.5rem; display: flex; justify-content: center; align-items: center; margin-bottom: 24px; box-shadow: var(--shadow-sm); }
.clean-list { list-style: none; padding: 0; }
.clean-list li { margin-bottom: 16px; border-bottom: 1px dashed var(--border-color); padding-bottom: 16px; }
.clean-list li:last-child { margin-bottom: 0; border-bottom: none; padding-bottom: 0; }
.hover-link { display: flex; justify-content: space-between; align-items: center; font-weight: 600; color: var(--text-main); font-size: 1.05rem; background: transparent; border: none; width: 100%; cursor: pointer; font-family: inherit;}
.hover-link:hover { color: var(--primary); transform: translateX(5px); }
.small-icon { font-size: 0.85rem; opacity: 0.5; transition: var(--transition); }
.hover-link:hover .small-icon { opacity: 1; color: var(--primary); transform: translate(2px, -2px); }

/* FOOTER */
.sao-footer { padding-top: 100px; overflow: hidden; }
.social-pills { display: flex; flex-wrap: wrap; gap: 12px; }
.social-pill { width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white !important; font-size: 1.2rem; transition: transform 0.3s, box-shadow 0.3s; }
.social-pill:hover { transform: translateY(-5px) rotate(8deg); box-shadow: 0 10px 20px rgba(0,0,0,0.15); }
.pill-email { background: #ea4335; }
.pill-linkedin { background: #0a66c2; }
.pill-instagram { background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); }
.pill-facebook { background: #1877f2; }
.creators { font-size: 1.2rem; font-weight: 600; font-family: 'Poppins', sans-serif; color: var(--text-main); }

/* TOAST */
.toast { position: fixed; bottom: 30px; right: 30px; background: var(--bg-surface); backdrop-filter: blur(10px); border: 1px solid var(--border-color); padding: 16px 24px; border-radius: var(--radius-md); box-shadow: var(--shadow-lg); border-left: 4px solid var(--accent); display: flex; align-items: center; gap: 12px; font-weight: 600; z-index: 9999; animation: slideInRight 0.4s ease forwards; color: var(--text-main); }
@keyframes slideInRight { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }

/* ANIMATION UTILS */
.reveal { opacity: 0; transform: translateY(40px); transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1); }
.reveal.active { opacity: 1; transform: translateY(0); }
"""

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)


js = """
// Premium SaaS Logic Module
document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Theme Logic
    const themeBtn = document.getElementById('theme-toggle');
    const body = document.body;
    const darkIcon = document.querySelector('.dark-icon');
    const lightIcon = document.querySelector('.light-icon');

    const currentTheme = localStorage.getItem('theme') || 'theme-light';
    body.className = currentTheme;
    updateThemeIcon(currentTheme);

    themeBtn.addEventListener('click', () => {
        const isLight = body.classList.contains('theme-light');
        const newTheme = isLight ? 'theme-dark' : 'theme-light';
        body.className = newTheme;
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme);
    });

    function updateThemeIcon(theme) {
        if (theme === 'theme-light') {
            darkIcon.style.display = 'inline-block';
            lightIcon.style.display = 'none';
        } else {
            darkIcon.style.display = 'none';
            lightIcon.style.display = 'inline-block';
        }
    }

    // 2. Mobile Menu Logic
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuIcon = document.querySelector('.menu-icon');
    const closeIcon = document.querySelector('.close-icon');

    mobileBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('active');
        const isActive = mobileMenu.classList.contains('active');
        menuIcon.style.display = isActive ? 'none' : 'inline-block';
        closeIcon.style.display = isActive ? 'inline-block' : 'none';
    });
    
    document.querySelectorAll('.mobile-link').forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.remove('active');
            menuIcon.style.display = 'inline-block';
            closeIcon.style.display = 'none';
        });
    });

    // Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 3. Scroll Reveal Observer
    const revealElements = document.querySelectorAll('.reveal');
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

    revealElements.forEach(el => revealObserver.observe(el));

    // 4. Stepper Form Logic
    const tabs = document.querySelectorAll('.form-tab');
    const slides = document.querySelectorAll('.form-slide');
    const btnNext = document.getElementById('btn-next');
    const btnPrev = document.getElementById('btn-prev');
    const btnSave = document.getElementById('btn-save');
    const formProgress = document.getElementById('stepper-progress');
    let currentStep = 0;
    const totalSteps = slides.length;

    function updateStepper() {
        slides.forEach((slide, idx) => {
            slide.classList.toggle('active', idx === currentStep);
        });
        tabs.forEach((tab, idx) => {
            tab.classList.toggle('active', idx <= currentStep);
        });
        
        formProgress.style.width = `${((currentStep + 1) / totalSteps) * 100}%`;
        
        btnPrev.style.visibility = currentStep === 0 ? 'hidden' : 'visible';
        
        if (currentStep === totalSteps - 1) {
            btnNext.style.display = 'none';
            btnSave.style.display = 'inline-flex';
        } else {
            btnNext.style.display = 'inline-flex';
            btnSave.style.display = 'none';
        }
    }

    btnNext.addEventListener('click', () => {
        if (currentStep < totalSteps - 1) currentStep++;
        updateStepper();
    });

    btnPrev.addEventListener('click', () => {
        if (currentStep > 0) currentStep--;
        updateStepper();
    });

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            currentStep = parseInt(tab.getAttribute('data-target'));
            updateStepper();
        });
    });

    // Form LocalStorage
    const inputs = ['userName', 'fieldOfStudy', 'userGpa', 'achievements', 'targetCountry', 'statusCV', 'statusSOP', 'statusLOR', 'statusTrans', 'statusEng', 'statusInterview', 'statusEmail'];
    const checkboxes = ['reqFinNeed', 'reqMerit', 'reqGpaCheck', 'reqEnglish', 'reqGre'];

    const savedProfile = JSON.parse(localStorage.getItem('scholarProfile'));
    if (savedProfile) {
        inputs.forEach(id => {
            const el = document.getElementById(id);
            if (el && savedProfile[id]) el.value = savedProfile[id];
        });
        checkboxes.forEach(id => {
            const el = document.getElementById(id);
            if (el && savedProfile[id] !== undefined) el.checked = savedProfile[id];
        });
    }

    btnSave.addEventListener('click', () => {
        const profileData = {};
        inputs.forEach(id => {
            const el = document.getElementById(id);
            profileData[id] = el ? el.value : '';
        });
        checkboxes.forEach(id => {
            const el = document.getElementById(id);
            profileData[id] = el ? el.checked : false;
        });

        localStorage.setItem('scholarProfile', JSON.stringify(profileData));
        showToast('Profile Progress Saved!');
        updateGlobalProgress();
    });

    // 5. Advanced Chatbot Logic
    const chatInput = document.getElementById('chat-input');
    const chatBtn = document.getElementById('send-chat');
    const chatBox = document.getElementById('chat-box');

    const botResponses = {
        'cv': "A great CV should be 1-2 pages long, action-oriented, and highlight your research potential, GPA, and key projects.",
        'sop': "Your Statement of Purpose (SOP) is your chance to shine. Focus on 'Why this program?', 'What have I done?', and 'What are my future goals?'.",
        'lor': "Letters of Recommendation (LOR) should come from professors who know you well. Provide them your CV and a summary of achievements.",
        'interview': "Interview prep is crucial. Practice answering 'Why this program?' and 'Tell me about your research'. Use our prompt below!",
        'email': "When cold emailing professors, keep it under 200 words. Mention a specific paper they wrote.",
        'scholarship': "Explore platforms like DAAD, Chevening, Fulbright, or Erasmus+ in Step 5.",
        'default': "I'm your integrated static AI. I can give quick tips on CV, SOP, LOR, emails, interviews, and scholarships."
    };

    function appendMessage(text, isUser) {
        const msgWrapper = document.createElement('div');
        msgWrapper.className = `message-wrapper ${isUser ? 'user' : 'bot'}`;
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${isUser ? 'user-msg' : 'glass-msg bot-message'}`;
        msgDiv.innerText = text;
        msgWrapper.appendChild(msgDiv);
        chatBox.appendChild(msgWrapper);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function processChat() {
        const question = chatInput.value.trim().toLowerCase();
        if (!question) return;

        appendMessage(chatInput.value.trim(), true);
        chatInput.value = '';

        setTimeout(() => {
            let matched = false;
            for (const key in botResponses) {
                if (question.includes(key)) {
                    appendMessage(botResponses[key], false);
                    matched = true;
                    break;
                }
            }
            if (!matched) appendMessage(botResponses['default'], false);
        }, 500);
    }

    chatBtn.addEventListener('click', processChat);
    chatInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') processChat(); });

    // 6. Application Tracker Dashboard
    const addTrackerBtn = document.getElementById('add-tracker-btn');
    const trackerBody = document.getElementById('tracker-body');
    const emptyState = document.getElementById('empty-state');
    const trackerTable = document.getElementById('tracker-table');

    let trackerData = JSON.parse(localStorage.getItem('scholarTracker')) || [];

    function renderTracker() {
        trackerBody.innerHTML = '';
        if (trackerData.length === 0) {
            emptyState.style.display = 'block';
            trackerTable.style.display = 'none';
        } else {
            emptyState.style.display = 'none';
            trackerTable.style.display = 'table';
            
            trackerData.forEach((entry, index) => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td><strong>${entry.name}</strong></td>
                    <td>${entry.country}</td>
                    <td><span class="status-badge status-${entry.status}">${entry.status}</span></td>
                    <td class="text-right"><button class="btn-delete ml-auto" onclick="deleteEntry(${index})"><i class="fa-solid fa-trash"></i></button></td>
                `;
                trackerBody.appendChild(tr);
            });
        }
        updateGlobalProgress();
    }

    addTrackerBtn.addEventListener('click', () => {
        const name = document.getElementById('newA-name').value.trim();
        const country = document.getElementById('newA-country').value.trim();
        const status = document.getElementById('newA-status').value;

        if (name && country) {
            trackerData.push({ name, country, status });
            localStorage.setItem('scholarTracker', JSON.stringify(trackerData));
            document.getElementById('newA-name').value = '';
            document.getElementById('newA-country').value = '';
            renderTracker();
            showToast('Application Tracked!');
        } else {
            alert("Names and Country remain mandatory.");
        }
    });

    window.deleteEntry = function(index) {
        trackerData.splice(index, 1);
        localStorage.setItem('scholarTracker', JSON.stringify(trackerData));
        renderTracker();
    };

    // 7. Global Roadmap Engine
    function updateGlobalProgress() {
        let completedSteps = 0;
        const pData = JSON.parse(localStorage.getItem('scholarProfile'));
        const tData = JSON.parse(localStorage.getItem('scholarTracker'));

        if (pData && (pData.userName || pData.fieldOfStudy)) completedSteps = Math.max(completedSteps, 1);
        if (pData && pData.statusCV === 'Ready' && pData.statusSOP === 'Ready' && pData.statusLOR === 'Ready') completedSteps = Math.max(completedSteps, 2);
        if (tData && tData.length > 0) completedSteps = Math.max(completedSteps, 3);
        if (pData && pData.statusInterview === 'Ready') completedSteps = Math.max(completedSteps, 4);

        for(let i=1; i<=4; i++) {
            const step = document.getElementById(`stepIndicator-${i}`);
            if (i <= completedSteps) step.classList.add('active');
            else step.classList.remove('active');
        }
        
        const pb = document.getElementById('global-progress');
        pb.style.width = completedSteps === 0 ? '0%' : `${((completedSteps - 1) / 3) * 100}%`;
    }

    // 8. Filters for Prompt Library
    const filterBtns = document.querySelectorAll('.filter-btn');
    const promptCards = document.querySelectorAll('.prompt-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const filter = btn.getAttribute('data-filter');

            promptCards.forEach(card => {
                if (filter === 'all' || card.getAttribute('data-category') === filter) {
                    card.classList.remove('hide');
                } else {
                    card.classList.add('hide');
                }
            });
        });
    });

    // 9. Utilities: Copy Prompt & Downloads
    window.copyPrompt = function(id, btn) {
        const text = document.getElementById(id).innerText;
        navigator.clipboard.writeText(text).then(() => {
            const raw = btn.innerHTML;
            btn.innerHTML = '<i class="fa-solid fa-check"></i> Copied';
            btn.classList.add('btn-primary');
            setTimeout(() => { btn.innerHTML = raw; btn.classList.remove('btn-primary'); }, 2000);
        });
    };

    window.downloadTemplate = function(elementId, filename, e) {
        if(e) e.preventDefault();
        const textArea = document.getElementById(elementId);
        if(!textArea) return;
        const blob = new Blob([textArea.value], { type: 'text/plain;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
        showToast('Download Started: ' + filename);
    };

    function showToast(message) {
        const t = document.createElement('div');
        t.className = 'toast';
        t.innerHTML = `<i class="fa-solid fa-circle-check text-accent"></i> <span>${message}</span>`;
        document.body.appendChild(t);
        setTimeout(() => {
            t.style.opacity = '0';
            t.style.transform = 'translateX(100%)';
            t.style.transition = 'all 0.4s';
            setTimeout(() => t.remove(), 400);
        }, 3000);
    }

    // Init
    renderTracker();
    updateGlobalProgress();
});
"""

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("SUCCESS: Assets generated securely.")
