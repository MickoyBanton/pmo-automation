# 🚀 PMO Automation Platform

## 📌 Overview
The PMO Automation Platform is a backend system designed to **automate project reporting and compliance auditing**.

This system simulates real-world enterprise workflows by aggregating project data, generating performance reports, and identifying governance issues to improve operational efficiency and decision-making.

---

## 🎯 Key Features

### 📊 Automated Reporting
- Generates real-time project status reports
- Calculates:
  - Completion percentage
  - Total and overdue tasks
  - Risk count
- Provides structured, decision-ready insights

---

### 🔍 Audit Engine (Compliance & Governance)
- Detects:
  - Overdue tasks
  - Missing deadlines
  - Projects without owners
  - Missing risk logs
- Produces a **compliance score (0–100)** to quantify project health
- Highlights critical issues affecting project delivery

---

### 🧠 Decision Intelligence Layer
- Translates audit results into clear project health statuses:
  - 🟢 Healthy  
  - 🟡 At Risk  
  - 🔴 Critical  
- Enables faster stakeholder decision-making

---

### 🔗 Unified Reporting Endpoint
- Combines reporting and audit insights into a single API response


---

## 🧱 Tech Stack

- **Backend:** Flask  
- **Database:** PostgreSQL  
- **ORM:** SQLAlchemy  
- **Language:** Python  

---

## 📡 API Endpoints

### 🔹 Get All Projects
GET /projects

### 🔥 Full Project Insights
GET /full-report/<project_id>


Returns:
- Project performance metrics
- Compliance audit results
- Health status classification

---

## 📊 Sample Output

```json
{
  "project": "Website Upgrade",
  "status": "At Risk",
  "report": {
    "completion_percentage": 66.67,
    "total_tasks": 3,
    "overdue_tasks": 1,
    "risk_count": 1
  },
  "audit": {
    "compliance_score": 80,
    "issue_count": 2,
    "issues": [
      "Task 'Testing' is overdue",
      "Project deadline passed but tasks are still incomplete"
    ]
  }
}
```

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/MickoyBanton/pmo-automation
cd pmo-automation
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure database

Update `config.py`:
```text
postgresql://<username>:<password>@localhost:5432/pmo_db
```

### 5. Initialize database
```bash
python init_db.py
```

### 6. Seed data
```bash
python seed_db.py
```

### 7. Run the application
```bash
python app.py
```
