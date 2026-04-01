import os

css_path = r'C:\Users\EURO COMPUTERS\Desktop\Ai Hub\scholarship-hunt-ai\styles.css'

fixes_css = """
/* =========================================================================
   FIX: RESPONSIVE & UI/UX OVERRIDES
   ========================================================================= */

/* 1. Global Layout Fixes */
body { overflow-x: hidden; }

.container {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 16px !important; /* FIX: Consistent padding for mobile */
}

/* Fix section formatting */
.section { padding: 60px 0 !important; }
@media(min-width: 768px) { .section { padding: 80px 0 !important; } }
@media(min-width: 1024px) { .section { padding: 100px 0 !important; } }
.section-desc { padding: 0 16px; margin-bottom: 40px !important; }

/* 2. Alignment & Grid Fixes (Cards & Steps) */
/* Reset grid logic based on mobile-first breakpoints */
.grid-2 { display: grid; grid-template-columns: 1fr !important; gap: 24px !important; }
.grid-3 { display: grid; grid-template-columns: 1fr !important; gap: 24px !important; }

@media(min-width: 768px) {
    .grid-2 { grid-template-columns: repeat(2, 1fr) !important; }
    .grid-3 { grid-template-columns: repeat(2, 1fr) !important; }
}
@media(min-width: 1024px) {
    .grid-3 { grid-template-columns: repeat(3, 1fr) !important; }
}

/* Prompt Library Fixes */
.prompt-card { 
    padding: 24px !important; 
    display: flex; 
    flex-direction: column; 
    justify-content: space-between; 
}
.prompt-card h3, .prompt-desc { text-align: left; }
.prompt-snippet {
    flex-grow: 1; /* Pushes button down */
    overflow-x: auto;
    word-break: break-word;
    white-space: pre-wrap;
    text-align: left;
    margin-bottom: 24px !important;
}
.btn-copy { width: 100%; justify-content: center; }

/* 3. Chatbot Fixes */
.chat-container {
    max-width: 800px;
    margin: 0 auto;
    border-radius: var(--radius-lg);
    display: flex !important;
    flex-direction: column !important;
    height: 600px !important; /* Fix collapsed heights */
}
.chat-box {
    padding: 24px !important;
    overflow-y: auto !important;
    flex-grow: 1 !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 16px !important;
}
.message { 
    max-width: 85% !important; 
    padding: 12px 16px !important; 
    word-wrap: break-word; 
    margin-bottom: 0 !important;
}
.message-wrapper { width: 100%; display: flex; margin-bottom: 8px; }
.message-wrapper.bot { justify-content: flex-start; }
.message-wrapper.user { justify-content: flex-end; }

.chat-input-area {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    padding: 16px !important;
    margin-top: auto; /* Fix to bottom */
}
.chat-input-area input { flex: 1 !important; width: 100% !important; min-width: 0 !important; margin: 0 !important; }
.chat-input-area .btn { flex-shrink: 0; }

@media(max-width: 480px) {
    .chat-container { height: 500px !important; border-radius: 12px; }
    .chat-box { padding: 16px !important; }
    .message { max-width: 90% !important; font-size: 0.95rem !important; }
    .chat-input-area { padding: 12px !important; gap: 8px !important; }
}

/* 4. Application Tracker Table Fixes */
.tracker-wrapper { padding: 24px !important; }
@media(min-width: 768px) { .tracker-wrapper { padding: 40px !important; } }

.table-container {
    overflow-x: auto !important;
    width: 100% !important;
    -webkit-overflow-scrolling: touch;
    border-radius: var(--radius-md) !important;
}
.modern-table { min-width: 600px !important; width: 100%; }

/* Mobile controls stack */
.tracker-controls { 
    display: flex !important; 
    flex-direction: column !important; 
    gap: 16px !important; 
}
@media(min-width: 768px) {
    .tracker-controls { 
        flex-direction: row !important; 
        align-items: flex-end !important; 
    }
    .tracker-controls > input {
        flex: 1;
    }
    .tracker-controls > .flex-left {
        flex: 1.5;
        display: flex;
        gap: 16px;
    }
}

/* 5. Mobile Navbar Menu Overlay Fix */
.mobile-menu { max-height: calc(100vh - 80px); overflow-y: auto; }
"""

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Only append if not already there to prevent duplications
if "FIX: RESPONSIVE & UI/UX OVERRIDES" not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(fixes_css)
    print("Fixes successfully appended to CSS.")
else:
    print("Fixes already present.")

