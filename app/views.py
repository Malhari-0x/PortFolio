from django.shortcuts import render

def home(request):
    context = {
        "profile": {
            "name": "Malhari Patil",
            "title": "Python & Django Developer",
            "tagline": "Building clean, reliable web experiences with strong backend logic and thoughtful UI.",
            "about": (
                "BCA graduate focused on Python, Django, and modern web development. "
                "I enjoy turning ideas into practical applications that are fast, accessible, and user-centered."
            ),
            "email": "malharpatil7975@gmail.com",
            "phone": "+91 79751 70121",
            "location": "Belagavi, Karnataka, India",
            "resume_url": "resume/MalharCV.pdf",
            "photo": "images/DSC_503211.JPG",
        },
        "stats": [
            {"value": "1+", "label": "Years Learning & Building"},
            {"value": "20+", "label": "Hands-on Mini Projects"},
            {"value": "5x", "label": "Pratibha Puraskar Award"},
        ],
        "skills": [
            {"name": "Python", "icon": "fa-brands fa-python", "level": "Advanced"},
            {"name": "Django", "icon": "fa-solid fa-code", "level": "Advanced"},
            {"name": "HTML5", "icon": "fa-brands fa-html5", "level": "Advanced"},
            {"name": "CSS3", "icon": "fa-brands fa-css3-alt", "level": "Advanced"},
            {"name": "JavaScript", "icon": "fa-brands fa-js", "level": "Intermediate"},
            {"name": "Bootstrap", "icon": "fa-brands fa-bootstrap", "level": "Intermediate"},
            {"name": "SQL (Oracle)", "icon": "fa-solid fa-database", "level": "Intermediate"},
        ],
        "projects": [
            {
                "title": "Weather Forecasting Website",
                "description": (
                    "A dynamic weather application that provides real-time conditions with a clean, "
                    "mobile-friendly interface to help users plan daily activities."
                ),
                "highlights": [
                    "Real-time weather data rendering",
                    "Responsive UI for desktop and mobile",
                    "Clear visual presentation for quick decisions",
                ],
                "stack": ["HTML", "CSS", "JavaScript"],
                "link": "https://weather-app-vercel-app.vercel.app/",
            },
            {
                "title": "Portfolio Website (Django)",
                "description": (
                    "A personal portfolio application built with Django to present profile, skills, "
                    "projects, and achievements in a structured single-page experience."
                ),
                "highlights": [
                    "Template-driven architecture",
                    "Reusable styling system",
                    "Production-ready section layout",
                ],
                "stack": ["Python", "Django", "CSS"],
                "link": "https://port-folio-4ex2.vercel.app/",
            },
        ],
        "education": [
            {
                "qualification": "BCA",
                "score": "85.05%",
                "year": "2024",
                "institution": "KLS Gogte College of Commerce, Belagavi",
            },
            {
                "qualification": "PUC Science",
                "score": "86.6%",
                "year": "2021",
                "institution": "Maratha Mandal's PU College",
            },
            {
                "qualification": "SSLC",
                "score": "93.44%",
                "year": "2019",
                "institution": "Ranzunzar High School",
            },
        ],
        "achievements": [
            "Pratibha Puraskar Award recipient (5 times)",
            "Special Prize in College Designing Event",
        ],
        "social_links": [
            {"name": "LinkedIn", "url": "https://www.linkedin.com/in/malhar-patil-b57817311", "icon": "fa-brands fa-linkedin"},
            {"name": "GitHub", "url": "https://github.com/Malhari-0x", "icon": "fa-brands fa-github"},
        ],
    }

    return render(request, "home.html", context)

