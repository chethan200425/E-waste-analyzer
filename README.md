
# ♻️ CMRIT E-Waste Analyzer

An **AI-powered web application** that analyzes uploaded e-waste images to identify **useful materials** and **hazardous substances**, along with **safe disposal guidelines**.  
Developed as part of an academic project at **CMR Institute of Technology (CSE Department)**.

---

## 🌍 Project Overview

Electronic waste (E-Waste) contains valuable materials like gold, copper, and silver, but also harmful elements such as lead and mercury.  
This project helps users and organizations **analyze e-waste components** and understand **how to safely dispose of hazardous materials**.

---

## ✨ Features

✅ Upload an e-waste image (e.g., battery, PCB, phone, etc.)  
✅ AI model identifies useful & hazardous materials  
✅ Provides safe disposal tips for hazardous items  
✅ Generates a detailed analysis report (with CMRIT branding)  
✅ Simple and responsive user interface  
✅ Runs locally using Flask  

---

## 🏫 Institution Information

**CMR Institute of Technology (CMRIT)**  
Department of Computer Science and Engineering  
Project by: **Chethan Kumar V**  
Semester: **7th Sem, B.E. CSE**

---

## 🧠 How It Works

1. User uploads an image of an e-waste item.  
2. The backend AI module analyzes the file name and simulates material detection.  
3. The system classifies materials as:
   - **Useful materials** (can be recycled/reused)
   - **Hazardous materials** (need safe disposal)
4. The system provides **safe disposal guidelines** for each hazardous item.  
5. A detailed **report (.txt)** is generated for download.

---

## 🖥️ Tech Stack

| Component | Technology Used |
|------------|-----------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python (Flask) |
| **AI Logic** | Simple rule-based classification (can be extended with ML) |
| **Report Format** | Text (with future support for PDF) |

---

## 🚀 Local Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/cmrit-e-waste-analyzer.git
cd cmrit-e-waste-analyzer

project structure 
cmrit-e-waste-analyzer/
│
├── app.py                # Flask backend
├── templates/
│   └── index.html        # Frontend HTML
├── static/
│   └── style.css         # Styling
├── uploads/              # Uploaded images
├── reports/              # Generated reports
└── README.md             # Project documentation
