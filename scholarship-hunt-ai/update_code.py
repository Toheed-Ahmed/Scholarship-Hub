import os

html_path = r'C:\Users\EURO COMPUTERS\Desktop\Ai Hub\scholarship-hunt-ai\index.html'
css_path = r'C:\Users\EURO COMPUTERS\Desktop\Ai Hub\scholarship-hunt-ai\styles.css'
js_path = r'C:\Users\EURO COMPUTERS\Desktop\Ai Hub\scholarship-hunt-ai\script.js'

# Update HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<a href="templates/cv_template.txt"', '<button onclick="downloadTemplate(\'cvContent\', \'CV_Template.txt\')"')
html = html.replace('<a href="templates/sop_template.txt"', '<button onclick="downloadTemplate(\'sopContent\', \'SOP_Template.txt\')"')
html = html.replace('<a href="templates/email_template.txt"', '<button onclick="downloadTemplate(\'lorContent\', \'LOR_Template.txt\')"')
html = html.replace('<a href="templates/transcript_guide.txt"', '<button onclick="downloadTemplate(\'transcriptContent\', \'Transcript_Guide.txt\')"')
html = html.replace('<a href="templates/english_tests_guide.txt"', '<button onclick="downloadTemplate(\'englishContent\', \'English_Tests_Guide.txt\')"')

html = html.replace(' title="Download CV"><i class="fa-solid fa-download"></i></a>', ' title="Download CV"><i class="fa-solid fa-download"></i></button>')
html = html.replace(' title="Download SOP"><i class="fa-solid fa-download"></i></a>', ' title="Download SOP"><i class="fa-solid fa-download"></i></button>')
html = html.replace(' title="Download LOR"><i class="fa-solid fa-download"></i></a>', ' title="Download LOR"><i class="fa-solid fa-download"></i></button>')
html = html.replace(' title="Download Transcript Guide"><i class="fa-solid fa-download"></i></a>', ' title="Download Transcript Guide"><i class="fa-solid fa-download"></i></button>')
html = html.replace(' title="Download English Tests Guide"><i class="fa-solid fa-download"></i></a>', ' title="Download English Tests Guide"><i class="fa-solid fa-download"></i></button>')

footer_start = html.find('<!-- Footer -->')
main_logic_start = html.find('<!-- Main Logic -->')

new_footer = """<!-- Footer -->
    <footer class="premium-footer section" id="contact">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <h3><i class="fa-solid fa-graduation-cap"></i> ScholarAI</h3>
                    <p>Your complete AI-powered roadmap to finding and winning scholarships worldwide. Helping students achieve their study abroad dreams.</p>
                    <div class="creator-credits">
                        <p><strong>Developed by:</strong></p>
                        <p>Sindhi Faraz Ahmed & Toheed Ahmed</p>
                    </div>
                </div>
                <div class="footer-socials">
                    <h3>Connect With Us</h3>
                    <div class="social-buttons">
                        <a href="mailto:fk091376@gmail.com" class="social-btn email-btn" aria-label="Email"><i class="fa-solid fa-envelope"></i> Email</a>
                        <a href="https://www.linkedin.com/in/farazahmed-civil/" target="_blank" class="social-btn linkedin-btn" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i> LinkedIn</a>
                        <a href="https://www.instagram.com/ahmed_faraz011/" target="_blank" class="social-btn instagram-btn" aria-label="Instagram"><i class="fa-brands fa-instagram"></i> Instagram</a>
                        <a href="https://www.facebook.com/fraz.ahmed.1253236" target="_blank" class="social-btn facebook-btn" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i> Facebook</a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Scholarship Hunt by AI. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <!-- Hidden Storage for Document Templates (Fixes local download issues) -->
    <div id="template-storage" style="display: none;">
        <textarea id="cvContent">
# ACADEMIC CV/RESUME TEMPLATE
[Your Full Name]
[Your Address]
[Your Email] | [Your Phone Number] | [LinkedIn Profile Link]

# PROFESSIONAL SUMMARY
A highly motivated and dedicated [Your Field of Study] student/graduate seeking a [Master's/PhD] scholarship to further develop my research skills and contribute to [Area of Interest].

# EDUCATION
[Degree Name] in [Major/Field]
[University Name], [City, Country]
[Start Month, Year] - [End Month, Year]
- CGPA: [Your GPA] / [Max GPA]

# RESEARCH & PROJECTS
[Project Title]
[Role/Position], [Institution/Organization]
- [Description of your contribution, methodology, and outcome].

# SKILLS
- Technical: [Skill 1, Skill 2]
- Languages: [English (IELTS X.0), Native Language]
        </textarea>
        <textarea id="sopContent">
STATEMENT OF PURPOSE

[Your Name]
[Your Address]
[Date]

Dear Members of the Admissions Committee,

I am writing to express my strong interest in the [Program Name] program at [University Name]. As a graduate of [Your Previous University] with a degree in [Your Field], I am eager to advance my knowledge in [Specific Area of Study].

[Introduction - Hook the reader]
[Academic Background]
[Professional/Research Experience]
[Why this University?]
[Future Goals]

Thank you for considering my application.

Sincerely,
[Your Name]
        </textarea>
        <textarea id="lorContent">
Subject: Prospective [Master's/PhD] Student Inquiry - [Your Name]

Dear Professor [Professor's Last Name],

My name is [Your Name] and I recently graduated with a degree in [Your Field] from [Your University]. I am writing to express my interest in joining your research group.

I have been following your recent work closely, particularly your publication on "[Title of a Recent Paper]". It strongly aligns with my own research interests in [Your Research Area]. 

I have attached my academic CV and transcripts. I would be incredibly grateful for a brief chat regarding any open positions.

Best regards,
[Your Name]
        </textarea>
        <textarea id="transcriptContent">
ACADEMIC TRANSCRIPT PREPARATION GUIDE

1. WHAT IS IT?
An official document from your university listing all courses and grades.

2. HOW TO OBTAIN IT:
Request it from your university's administrative or registrar office. Maintain both digital and physical official copies.

3. CHECKLIST:
- [ ] Stamped and signed by registrar.
- [ ] Grading scale explanation included.
- [ ] High-quality color scan saved as PDF.
- [ ] Officially translated to English if originally in another language.
        </textarea>
        <textarea id="englishContent">
ENGLISH PROFICIENCY TESTS GUIDE

1. IELTS:
- Minimum overall band 6.5 (no sub-band below 6.0) required for most master's.
- Validity: 2 Years.

2. TOEFL iBT:
- Requirement: 80 to 90+.
- Validity: 2 Years.

3. ENGLISH PROFICIENCY CERTIFICATE (EPC):
- A letter from your previous university stating your degree was taught entirely in English. Accepted widely in Europe/Asia in place of IELTS. (Always verify first!)
        </textarea>
    </div>

    """

html = html[:footer_start] + new_footer + html[main_logic_start:]
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)


# Update CSS
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

footer_css_start = css.find('/* Footer */')
if footer_css_start != -1:
    css = css[:footer_css_start]

new_footer_css = """/* Premium Footer */
.premium-footer {
    background-color: var(--bg-surface);
    border-top: 1px solid var(--border-color);
    padding: 80px 0 40px 0;
    margin-top: 60px;
}
.footer-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 48px;
    margin-bottom: 60px;
}
@media(min-width: 900px) {
    .footer-grid { grid-template-columns: 1fr 1.2fr; gap: 60px; }
}
.footer-brand h3 {
    font-size: 1.8rem;
    color: var(--primary);
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 12px;
}
.footer-brand p {
    color: var(--text-muted);
    margin-bottom: 32px;
    max-width: 400px;
    font-size: 1.05rem;
}
.creator-credits {
    background: var(--bg-alt);
    padding: 24px;
    border-radius: var(--radius-md);
    border-left: 4px solid var(--primary);
}
.creator-credits p {
    margin-bottom: 4px;
    color: var(--text-main);
    font-size: 1.15rem;
}
.footer-socials h3 {
    font-size: 1.4rem;
    margin-bottom: 24px;
    color: var(--text-main);
}
.social-buttons {
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px;
}
@media(min-width: 500px) {
    .social-buttons { grid-template-columns: 1fr 1fr; }
}
.social-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    padding: 14px 20px;
    border-radius: var(--radius-md);
    font-weight: 600;
    font-size: 1.05rem;
    color: white !important;
    transition: transform 0.2s, box-shadow 0.2s, background-color 0.2s;
    text-decoration: none;
}
.social-btn:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 15px -3px rgba(0,0,0,0.2);
    color: white !important;
}
.email-btn { background-color: #ea4335; }
.linkedin-btn { background-color: #0a66c2; }
.instagram-btn { background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); }
.facebook-btn { background-color: #1877f2; }
.footer-bottom {
    text-align: center;
    padding-top: 32px;
    border-top: 1px solid var(--border-color);
    color: var(--text-muted);
    font-size: 0.95rem;
}
"""
css = css + new_footer_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Update JS
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Only add downloadTemplate if it's not already there
if 'window.downloadTemplate' not in js:
    download_js = """
    // --- 7. Local File Downloader ---
    window.downloadTemplate = function(elementId, filename) {
        const textArea = document.getElementById(elementId);
        if(!textArea) {
            console.error('Text area not found:', elementId);
            return;
        }
        const textContent = textArea.value;
        const blob = new Blob([textContent], { type: 'text/plain;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    };

    // Initial renders"""
    js = js.replace('// Initial renders', download_js)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Update complete!")
