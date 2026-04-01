
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
