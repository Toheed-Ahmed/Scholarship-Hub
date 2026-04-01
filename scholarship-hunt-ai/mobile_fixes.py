import os

css_path = r'C:\Users\EURO COMPUTERS\Desktop\Ai Hub\scholarship-hunt-ai\styles.css'

mobile_css = """
/* =========================================================================
   EXTREME MOBILE VIP FIXES (iPhone, Android Small Screens - Max 480px)
   ========================================================================= */
@media (max-width: 480px) {

    /* 1. GLOBAL MOBILE FIXES */
    html, body {
        overflow-x: hidden !important;
        width: 100% !important;
        max-width: 100vw !important;
    }
    .container {
        width: 100% !important;
        max-width: 100vw !important;
        padding: 0 16px !important;
        overflow-x: hidden !important;
    }
    .section, .hero-section {
        padding-top: 60px !important;
        padding-bottom: 40px !important;
    }
    .hero-section { padding-top: 120px !important; }
    
    /* 2. TYPOGRAPHY SCALING */
    h1, .main-title { font-size: 26px !important; line-height: 1.2 !important; margin-bottom: 16px !important; }
    h2, .section-title { font-size: 22px !important; margin-bottom: 12px !important; }
    h3, .card-title { font-size: 18px !important; }
    p, .section-desc, .subtitle { font-size: 14px !important; }

    /* 3. LAYOUT COERCION (Single Column Base) */
    .grid-2, .grid-3, .footer-grid, .doc-status-flex {
        grid-template-columns: 1fr !important;
        display: grid !important;
        gap: 16px !important;
    }
    .card, .glass-card, .prompt-card, .card-feature, .framework-wrapper, .tracker-wrapper {
        width: 100% !important;
        margin-bottom: 16px !important;
        padding: 20px 16px !important;
    }
    .form-slide { padding: 0 !important; }

    /* 4. BUTTONS & INPUTS (Prevent iOS Zoom) */
    .btn {
        width: 100% !important;
        padding: 14px 16px !important;
        margin-bottom: 8px !important;
        font-size: 16px !important; /* Prevents iOS Zoom */
        justify-content: center !important;
    }
    input, select, .glass-input {
        width: 100% !important;
        font-size: 16px !important; /* Prevents iOS Zoom */
        padding: 14px !important;
    }

    /* 5. STEP 3: CHATBOT MOBILE FIX */
    .chat-container {
        width: 100% !important;
        height: 70vh !important;
        max-height: 550px !important;
        display: flex !important;
        flex-direction: column !important;
        margin: 0 !important;
        border-radius: 12px !important;
    }
    .chat-box {
        padding: 16px !important;
        flex-grow: 1 !important;
    }
    .message {
        padding: 10px 14px !important;
        font-size: 14px !important;
        max-width: 90% !important;
    }
    .chat-input-area {
        position: sticky !important;
        bottom: 0 !important;
        width: 100% !important;
        padding: 12px !important;
        flex-direction: column !important; /* Stack input and button */
        gap: 8px !important;
    }
    .chat-input-area .btn {
        width: 100% !important;
        border-radius: 8px !important;
        height: 48px !important;
    }

    /* 6. STEP 4: TRACKER MOBILE FIX (Table to Cards) */
    .table-container {
        overflow-x: hidden !important; 
        background: transparent !important;
        padding: 0 !important;
    }
    .modern-table, .modern-table thead, .modern-table tbody, .modern-table th, .modern-table td, .modern-table tr {
        display: block !important;
        width: 100% !important;
    }
    .modern-table thead tr {
        position: absolute !important;
        top: -9999px !important;
        left: -9999px !important;
    }
    .modern-table tr {
        margin-bottom: 16px !important;
        background: rgba(255,255,255,0.02) !important;
        border-radius: 12px !important;
        border: 1px solid var(--border-color) !important;
        padding: 16px !important;
        display: flex !important;
        flex-direction: column !important;
        gap: 8px !important;
    }
    .modern-table td {
        border: none !important;
        padding: 0 !important;
        text-align: left !important;
        display: block !important;
        width: 100% !important;
    }
    .modern-table td:nth-child(1) { font-size: 1.1rem !important; color: var(--primary) !important; font-weight: 600 !important; margin-bottom: 4px !important;}
    .modern-table td:nth-child(2) { font-size: 0.9rem !important; color: var(--text-muted) !important; margin-bottom: 8px !important;}
    .modern-table td:nth-child(3) { margin-bottom: 12px !important; }
    .modern-table td:last-child {
        margin-top: 8px !important;
        width: 100% !important;
    }
    .modern-table td .btn-delete {
        width: 100% !important;
        height: 44px !important;
        background: rgba(239, 68, 68, 0.1) !important;
        border-radius: 8px !important;
        color: var(--danger) !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }

    /* 7. ROADMAP & FILTERS FIX */
    .progress-steps { gap: 8px !important; padding: 0 8px !important; }
    .step span { font-size: 10px !important; font-weight: 500 !important; }
    .glass-icon { width: 36px !important; height: 36px !important; font-size: 0.9rem !important; }
    .progress-bar-bg { top: 16px !important; }
    .roadmap-card { padding: 24px 12px !important; }
    
    .filter-controls { flex-direction: column !important; width: 100% !important; gap: 8px !important; }
    .filter-btn { width: 100% !important; text-align: center !important; margin: 0 !important; }

    /* Navbar exact fixing */
    .navbar { width: 100vw !important; overflow: hidden !important; }
    .logo-text { font-size: 1.2rem !important; }
}
"""

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Only append if not already there to prevent duplications
if "EXTREME MOBILE VIP FIXES" not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(mobile_css)
    print("Mobile VIP Fixes successfully appended to CSS.")
else:
    print("Fixes already present.")

