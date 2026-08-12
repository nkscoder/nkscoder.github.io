#!/usr/bin/env python3
"""
Full two-column Enhancv-style CV PDF.
Left: Experience / Education  |  Right: Skills / Projects
Includes complete 12+ years content from original CV.
"""

from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).resolve().parents[1] / "NITESH-KUMAR-SINGH-CV.pdf"
DATE = "10 Aug 2026"

BLUE = (37, 99, 235)
BLACK = (17, 24, 39)
GRAY = (75, 85, 99)
LIGHT = (107, 114, 128)

LX, LW = 14, 118
RX, RW = 136, 60
FW = 182
TOP = 11


class CV(FPDF):
    def footer(self):
        self.set_y(-9)
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*LIGHT)
        self.cell(0, 5, f"Nitesh Kumar Singh  |  {DATE}  |  nkscoder.in  |  statementiq.in", align="C")

    def rule(self, x, w):
        y = self.get_y()
        self.set_draw_color(*BLACK)
        self.set_line_width(0.5)
        self.line(x, y, x + w, y)
        self.set_y(y + 2)

    def section(self, title, x, w):
        self.set_xy(x, self.get_y())
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*BLACK)
        self.cell(w, 4.5, title.upper())
        self.set_y(self.get_y() + 5)
        self.rule(x, w)

    def txt(self, text, x, w, size=8.5, style="", color=BLACK, lh=3.9):
        self.set_xy(x, self.get_y())
        self.set_font("Helvetica", style, size)
        self.set_text_color(*color)
        self.multi_cell(w, lh, text)

    def sub(self, text, x, w):
        self.ln(0.5)
        self.txt(text, x, w, 8.3, "B")

    def bullets(self, x, w, items, size=8.2):
        for item in items:
            self.set_xy(x, self.get_y())
            self.set_font("Helvetica", "", size)
            self.set_text_color(*BLACK)
            self.multi_cell(w, 3.7, f"- {item}")

    def role(self, title, company, meta, x, w):
        self.ln(1.2)
        self.txt(title, x, w, 9.5, "B")
        self.txt(company, x, w, 8.8, "B", BLUE)
        self.txt(meta, x, w, 8, "I", GRAY)

    def at(self, x, y, fn):
        self.set_xy(x, y)
        fn()
        return self.get_y()


SKILLS = [
    "Python", "Django", "Django REST Framework", "FastAPI", "Pandas",
    "REST APIs", "GraphQL", "PostgreSQL", "MySQL", "Celery", "RabbitMQ",
    "Ray", "Docker", "AWS EC2", "GKE", "ElasticSearch", "Algolia", "FCM",
    "Google APIs", "GitHub", "Bitbucket", "Jenkins", "Jira", "Postman",
    "Linux", "CentOS", "HTML", "JavaScript", "jQuery", "PHP", "Laravel",
]


def build():
    pdf = CV(format="A4", unit="mm")
    pdf.set_auto_page_break(auto=False)
    pdf.set_margins(LX, TOP, LX)

    def header():
        pdf.set_xy(LX, TOP)
        pdf.set_font("Helvetica", "B", 19)
        pdf.set_text_color(*BLACK)
        pdf.cell(FW, 8, "NITESH KUMAR SINGH")
        pdf.set_xy(RX, TOP)
        pdf.set_font("Helvetica", "B", 8)
        pdf.set_text_color(*BLUE)
        pdf.multi_cell(RW, 3.8, "12+ Years\nExperience")
        pdf.set_xy(LX, TOP + 9)
        pdf.set_font("Helvetica", "B", 10.5)
        pdf.set_text_color(*BLUE)
        pdf.cell(FW, 5, "Senior Python Developer  |  Fintech, AI & Backend Systems")
        pdf.ln(6)
        for line in [
            "nkscoder@gmail.com  |  +91 7827495599  |  New Delhi, India",
            "Portfolio: https://nkscoder.in  |  Product: https://statementiq.in",
            "LinkedIn: linkedin.com/in/nitesh-kumar-singh-897437a2  |  GitHub: github.com/nkscoder",
            "Experience: 06/2016 - Present (12+ years Python development)",
        ]:
            pdf.set_x(LX)
            pdf.set_font("Helvetica", "", 8.2)
            pdf.set_text_color(*BLACK)
            pdf.multi_cell(FW, 3.8, line)
        pdf.ln(1)
        pdf.set_x(LX)
        y = pdf.get_y()
        pdf.set_draw_color(*BLACK)
        pdf.line(LX, y, LX + FW, y)
        return y + 2.5

    def summary(y):
        pdf.set_xy(LX, y)
        pdf.section("Summary", LX, FW)
        pdf.txt(
            "Senior Python Developer with 12+ years of professional experience (2016-Present) building "
            "production fintech backends, bank statement intelligence, NBFC workflows, and AI-assisted "
            "products. Founder of StatementIQ (statementiq.in). Expert in Python, Django, PostgreSQL, "
            "Celery, RabbitMQ, Ray, Docker, and Linux deployments. Portfolio: nkscoder.in.",
            LX, FW, 8.8, lh=4,
        )
        return pdf.get_y() + 3

    def quess():
        pdf.section("Experience", LX, LW)
        pdf.role(
            "Senior Python Developer",
            "Quess Corp Ltd (Client: Airtel Payments Bank)",
            "02/2025 - Present | New Delhi",
            LX, LW,
        )
        pdf.sub("Large-scale bank statement analysis and financial data processing", LX, LW)
        pdf.bullets(LX, LW, [
            "Designed and implemented scalable pipelines for parsing, normalizing, and validating high-volume bank statements (PDF/CSV/XML).",
            "Built robust data models for transactions, parties, and metadata with accuracy and auditability.",
        ])
        pdf.sub("Distributed processing and messaging", LX, LW)
        pdf.bullets(LX, LW, [
            "Implemented distributed processing using Python, Pandas, Ray, and RabbitMQ for parallel ingestion and transformation.",
            "Optimized CPU/GPU utilization for compute-intensive workloads; implemented back-pressure and retry mechanisms.",
        ])
        pdf.sub("Transaction intelligence and risk indicators", LX, LW)
        pdf.bullets(LX, LW, [
            "Developed transaction indicators, flags, and rules for risk detection, anomaly identification, and categorization.",
            "Automated party extraction and normalization (sender/receiver/merchant) with deduplication and entity resolution.",
        ])
        pdf.sub("Python and Django application development", LX, LW)
        pdf.bullets(LX, LW, [
            "Built backend services using Python and Django/Django REST Framework for data ingestion, processing orchestration, and APIs.",
            "Designed efficient ORM queries, background jobs (Celery/RQ), and secure role-based access.",
            "Implemented file handling, async tasks, and reporting dashboards.",
        ])
        pdf.sub("DevOps, deployment, and reliability", LX, LW)
        pdf.bullets(LX, LW, [
            "Containerized services using Docker; orchestrated deployments with CI/CD pipelines.",
            "Managed environments, secrets, and configurations; implemented logging, monitoring, and alerting.",
            "Deployed and scaled services on Linux servers; optimized performance and reliability for production workloads.",
        ])

    def skills():
        pdf.section("Technical Skills", RX, RW)
        for s in SKILLS:
            pdf.txt(s, RX, RW, 8, lh=3.6)
        pdf.ln(1)
        pdf.section("Operating System", RX, RW)
        pdf.txt("Linux, CentOS, macOS, Windows", RX, RW, 8, lh=3.6)
        pdf.ln(1)
        pdf.section("Languages", RX, RW)
        pdf.txt("English, Hindi", RX, RW, 8, lh=3.6)

    def voxturr():
        pdf.section("Experience", LX, LW)
        pdf.role("Senior Python Developer", "Voxturr Consulting Pvt. Ltd.", "04/2023 - 02/2025 | Gurugram", LX, LW)
        pdf.txt(
            "JM Financial is an integrated and diversified financial services group providing investment banking, "
            "institutional equities, research, private equity, fixed income, syndication, and finance services.",
            LX, LW, 8.2, lh=3.8,
        )
        pdf.sub("Key Contributions", LX, LW)
        pdf.bullets(LX, LW, [
            "Gathered and analyzed business and technical requirements from stakeholders.",
            "Designed and developed REST APIs using Python 3.11 and Django 4.2.",
            "Implemented server-side rendering and dynamic reports using Jinja2 templates.",
            "Built and optimized database schemas and queries using PostgreSQL.",
            "Worked on monolithic architecture applications with high data volume.",
            "Implemented authentication, authorization, and role-based access control.",
            "Integrated third-party services and internal financial systems.",
            "Performed performance optimization and bug fixing for production issues.",
            "Collaborated with QA and business teams for UAT and production releases.",
            "Managed code versioning and pull requests using Bitbucket; tracked tasks in Jira.",
        ])
        pdf.sub("Deployment and Environment", LX, LW)
        pdf.bullets(LX, LW, [
            "Deployed applications on Linux-based servers.",
            "Managed environment configurations for development, staging, and production.",
            "Handled database migrations, release deployments, and post-deployment monitoring.",
            "Worked closely with DevOps teams during release cycles.",
        ])

    def projects_p2():
        pdf.section("Projects", RX, RW)
        pdf.txt("StatementIQ (Own Product)", RX, RW, 8.8, "B")
        pdf.txt("Bank Statement Analyzer for India", RX, RW, 8.2, "B", BLUE)
        pdf.txt("2026 | https://statementiq.in", RX, RW, 7.8, "I", GRAY)
        pdf.txt(
            "Own SaaS product for India: upload bank statement PDF/Excel, FinHealth score in plain English, "
            "Hinglish AI chat, and downloadable PDF report. Supports 15+ banks (HDFC, SBI, ICICI, Axis, Kotak). "
            "First report free, then paid unlock. Built end-to-end: parsing, scoring, reporting, auth, web app.",
            RX, RW, 7.8, lh=3.7,
        )
        pdf.txt("Stack: Python, Django/FastAPI, AI/LLM, PostgreSQL", RX, RW, 7.5, "I", GRAY)
        pdf.ln(1.5)
        pdf.txt("Bank Statement Analysis Platform", RX, RW, 8.5, "B")
        pdf.txt("06/2025 - Present", RX, RW, 7.8, "I", GRAY)
        pdf.sub("Bank Statement Ingestion and Transaction Risk Analysis", RX, RW)
        pdf.bullets(RX, RW, [
            "Designed scalable backend systems for bank statement ingestion and large-scale financial transaction analysis.",
            "Built pipelines to extract, normalize, and deduplicate party entities from multi-source banking datasets.",
            "Implemented transaction indicators, risk flags, and party categorization for compliance and fraud detection.",
            "Developed RESTful APIs using Python and Django; Celery/RabbitMQ for async jobs; Ray for distributed compute.",
            "Optimized PostgreSQL schemas, indexes, and queries for high read/write throughput.",
        ], 7.6)
        pdf.sub("DevOps and Infrastructure", RX, RW)
        pdf.bullets(RX, RW, [
            "Docker containerization, Linux deployments, CI/CD, logging, monitoring, worker auto-scaling.",
        ], 7.6)

    def scaledesk():
        pdf.section("Experience", LX, LW)
        pdf.role("Python Developer", "Scaledesk Web Studio Pvt. Ltd.", "06/2016 - 03/2023 (7 years)", LX, LW)
        pdf.bullets(LX, LW, [
            "Coordinated efficient large-scale software developments across fintech, hospitality, e-commerce, and media.",
            "Evaluated and improved development work of team members; training, constructive criticism, knowledge transfer.",
            "Planned and developed interfaces that simplified overall management and offered ease of use.",
            "Collaborated with fellow engineers to evaluate software and hardware interfaces.",
            "Adjusted design parameters to incorporate new features.",
            "Maintained organized workflow using Bitbucket and project management tools.",
            "Testing to identify bugs and technical issues before and after deploying.",
            "Documented bug reports, tickets, and code changes.",
        ])

    def projects_p3():
        pdf.section("Projects", RX, RW)

        def proj(name, dates, url, desc, tools, bullets=None):
            pdf.txt(name, RX, RW, 8.5, "B")
            meta = dates + (f" | {url}" if url else "")
            pdf.txt(meta, RX, RW, 7.6, "I", GRAY)
            pdf.txt(desc, RX, RW, 7.6, lh=3.6)
            if bullets:
                pdf.bullets(RX, RW, bullets, 7.4)
            if tools:
                pdf.txt(tools, RX, RW, 7.2, "I", GRAY, lh=3.5)
            pdf.ln(1)

        proj(
            "JM Financial",
            "06/2023 - 02/2025",
            "jmfl.com",
            "Investment banking platform for institutional, corporate, and UHNW clients.",
            "Python 3.11, Django 4.2, PostgreSQL, Jinja2, Bitbucket, Jira",
            ["Requirement gathering, REST APIs, Jinja2 reporting."],
        )
        proj(
            "Textile Stock India",
            "06/2021 - 03/2023",
            "textilestockindia.com",
            "Open marketplace for surplus textile stocklots; buy/sell for international clients.",
            "Python 3.9, Django 3.0.8, Algolia, PostgreSQL, Gupshup, Razorpay",
            ["Python integrations, deployment, client communication, application updates."],
        )
        proj(
            "Ujjivan Bank",
            "10/2020 - 06/2021",
            "",
            "Bank employee surveys platform.",
            "Python 3.5, Django 2, MySQL",
            ["Requirement gathering, database design, system design, APIs."],
        )

    def education():
        pdf.section("Education", LX, LW)
        for deg, school, meta in [
            ("BCA", "Kalinga University Raipur", "2016 | Raipur"),
            ("12th", "B.N. College Bhagalpur (B.S.E. Board Bihar)", ""),
            ("10th", "SGG High School, Banka (B.S.E. Board Bihar)", ""),
        ]:
            pdf.txt(deg, LX, LW, 9, "B")
            pdf.txt(school, LX, LW, 8.5, "B", BLUE)
            if meta:
                pdf.txt(meta, LX, LW, 8, "I", GRAY)
            pdf.ln(1.2)
        pdf.section("Certifications", LX, LW)
        pdf.txt("Java 2 Platform, Enterprise Edition (J2EE)", LX, LW, 8.3)
        pdf.ln(1)
        pdf.section("Interests", LX, LW)
        pdf.txt("Traveling, Listening Music, Playing Sports", LX, LW, 8.3)

    def projects_p4():
        pdf.section("Projects", RX, RW)

        def proj(name, dates, url, desc, tools, bullets=None):
            pdf.txt(name, RX, RW, 8.5, "B")
            meta = dates + (f" | {url}" if url else "")
            pdf.txt(meta, RX, RW, 7.6, "I", GRAY)
            pdf.txt(desc, RX, RW, 7.6, lh=3.6)
            if bullets:
                pdf.bullets(RX, RW, bullets, 7.4)
            if tools:
                pdf.txt(tools, RX, RW, 7.2, "I", GRAY, lh=3.5)
            pdf.ln(1)

        proj(
            "goStops",
            "01/2020 - 10/2020",
            "gostops.com",
            "Backpacker hostel chain - online room booking for youth tourism in India.",
            "Python 3.7.1, Django 2.2.8, MySQL, Bitbucket",
            ["APIs, requirement gathering, Jinja2 implementation."],
        )
        proj(
            "Wave Resident App",
            "06/2017 - 01/2020",
            "",
            "Resident app for complaints, bills, polls, gate passes, events, and online payments.",
            "Python 3.6, Django 2/3, MySQL, Oracle, Microservices, FCM, Paytm",
            ["APIs, ERP integration, client communication, configuration updates."],
        )
        proj(
            "Angel One / ANI News / Django Coupons",
            "2016 - 2023",
            "github.com/nkscoder/coupons",
            "Additional fintech and media delivery across client engagements.",
            "Django plugins, REST APIs, production support",
        )

    def links():
        pdf.section("Find Me Online", LX, FW)
        pdf.bullets(LX, FW, [
            "Portfolio: https://nkscoder.in",
            "StatementIQ: https://statementiq.in",
            "StatementIQ login: https://statementiq.in/login",
            "Launch blog: https://nkscoder.in/blog/statementiq-bank-statement-analyzer-launch.html",
            "GitHub: https://github.com/nkscoder",
            "LinkedIn: https://www.linkedin.com/in/nitesh-kumar-singh-897437a2/",
            "JM Financial: https://www.jmfl.com/",
            "Textile Stock: http://textilestockindia.com/",
            "goStops: https://gostops.com/",
        ], 8.3)
        pdf.ln(3)
        pdf.section("Declaration", LX, FW)
        pdf.txt(
            "I hereby declare that the information mentioned above is factual and true to the best of my knowledge.",
            LX, FW, 8.3, lh=3.8,
        )
        pdf.ln(3)
        pdf.txt("Nitesh Kumar Singh", LX, FW, 10, "B")
        pdf.txt(f"New Delhi | {DATE}", LX, FW, 9)

    # Page 1
    pdf.add_page()
    y = header()
    y = summary(y)
    pdf.at(LX, y, quess)
    pdf.at(RX, y, skills)

    # Page 2
    pdf.add_page()
    pdf.at(LX, TOP, voxturr)
    pdf.at(RX, TOP, projects_p2)

    # Page 3
    pdf.add_page()
    pdf.at(LX, TOP, scaledesk)
    pdf.at(RX, TOP, projects_p3)

    # Page 4
    pdf.add_page()
    pdf.at(LX, TOP, education)
    pdf.at(RX, TOP, projects_p4)

    # Page 5
    pdf.add_page()
    pdf.at(LX, TOP, links)

    pdf.output(str(OUT))
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes, 5 pages, full 12+ years content)")


if __name__ == "__main__":
    build()
