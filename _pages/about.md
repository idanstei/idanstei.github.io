Here are the updated files to build your portfolio.

### 1. Main Configuration (`_config.yml`)

I have updated the main site configuration to include your name, contact details, standard GitHub Pages URL formatting, and Google Scholar parsing variables.

*Note: I have only included the sections that required changes to keep this concise. You can replace these specific blocks in your original file.*

```yaml
# -----------------------------------------------------------------------------
# Site settings
# -----------------------------------------------------------------------------

title: Idan Steinberg # the website title (if blank, full name will be used instead)
first_name: Idan
middle_name: 
last_name: Steinberg
contact_note: >
  You can reach me directly via email or connect with me on LinkedIn.
description: > # the ">" symbol means to ignore newlines until "footer_text:"
  Dynamic, highly innovative engineer and Vice President of Research and Development specializing in medical devices and medical imaging.
footer_text: >
  Powered by <a href="https://jekyllrb.com/" target="_blank">Jekyll</a> with <a href="https://github.com/alshedivat/al-folio">al-folio</a> theme.
  Hosted by <a href="https://pages.github.com/" target="_blank">GitHub Pages</a>.
keywords: jekyll, jekyll-theme, academic-website, portfolio-website, biomedical-engineering, medical-devices
lang: en # the language of your site (for example: en, fr, cn, ru, etc.)
icon: ⚕️ # the emoji used as the favicon (alternatively, provide image name in /assets/img/)
apple_touch_icon: # image name in /assets/img/ (or a rooted path / absolute URL) used for iOS home-screen bookmarks; needs a real 180x180 PNG, since Safari ignores the emoji favicon above. Left empty, iOS falls back to a screenshot of the page.

url: https://idanstei.github.io # the base hostname & protocol for your site
baseurl: "" # the subpath of your site, e.g. /blog/. Leave blank for root
last_updated: false # set to true if you want to display last updated in the footer
impressum_path: # set to path to include impressum link in the footer, use the same path as permalink in a page, helps to conform with EU GDPR
back_to_top: true # set to false to disable the back to top button

# ... [Keep intervening sections exactly as they are in your original file] ...

# -----------------------------------------------------------------------------
# Jekyll Scholar
# -----------------------------------------------------------------------------

scholar:
  last_name: [Steinberg]
  first_name: [Idan, I.]

  style: apa
  locale: en

```

---

### 2. The Resume Page (`_pages/cv.md`)

I have updated the CV page settings to point to your specific resume file. You will need to save your `.docx` file as a `.pdf`, rename it to `Idan_Steinberg_Resume.pdf`, and upload it to the `assets/pdf/` directory.

```yaml
---
layout: cv
permalink: /cv/
title: CV
nav: true
nav_order: 5
cv_pdf: /assets/pdf/Idan_Steinberg_Resume.pdf # you can also use external links here
cv_format: rendercv # options: rendercv, jsonresume
description: A comprehensive overview of my professional experience in medical devices, imaging, and research and development leadership.
toc:
  sidebar: left
---

```

---

### 3. The Home / About Page (`_pages/about.md`)

I have updated the homepage structure with your contact information, location, and the professional biography we drafted earlier. Ensure you upload a photo named `prof_pic.jpg` to the `assets/img/` folder.

```markdown
---
layout: about
title: about
permalink: /
subtitle: Vice President of Research and Development | Biomedical Engineer

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false # crops the image to make it circular
  more_info: >
    <p>Ann Arbor, MI</p>
    <p><a href="mailto:idanstei@gmail.com">idanstei@gmail.com</a></p>
    <p>(650) 469-6437</p>

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: false # Disabled since this is a static portfolio, change to true if you want a news feed

latest_posts:
  enabled: false # Disabled since you are not running a blog
---

I am a dynamic, highly innovative engineer with over 25 years of hands-on experience in research positions at internationally renowned institutions. My core expertise spans medical devices, medical imaging, and signal processing, and I excel at identifying product opportunities for emerging technologies. 

Currently, I serve as the Vice President for Research and Development at Endra Life Sciences Inc. in Ann Arbor, Michigan, where I have operational and execution responsibility for all company products. My recent work includes proposing a system design that reduced console size by 5x, decreased probe weight by 5x, and reduced overall costs by one-third. 

My academic foundation includes a Ph.D. in Biomedical Engineering from Tel Aviv University, where I focused on acoustic instrumentation development, biophotonics, and fiber optics. I later spent five years at Stanford University's School of Medicine as a Postdoctoral Fellow and Team Leader, developing complex photoacoustic and ultrasound prostate imaging systems. Recently, I completed an Accelerated Management Development Certificate from the University of Michigan's Ross School of Business to further refine my skills in strategic decision-making and digital innovation.

### Technical Fabrication & Workflow Automation
Beyond clinical hardware development, I maintain a dedicated workspace for technical DIY fabrication. I actively operate a V1 Engineering Primo MPCNC machine and a Creality CR laser engraver, frequently utilizing custom G-code generation and software routing. To optimize operational tracking and financial metrics, I also regularly develop custom automation tools using Excel VBA and Google Sheets Apps Script.

```
