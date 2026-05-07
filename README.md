# Campus Recruitment Management System

A desktop GUI application built with **Python + Tkinter + SQLite3** to automate and manage campus placement activities.

---

## 📁 Project Structure

```
campus_recruitment/
├── main.py               ← Entry point
├── campus_recruitment.db ← Auto-created on first run
├── modules/
│   ├── login.py          ← Login screen
│   ├── register.py       ← Registration (Student / Recruiter)
│   ├── admin.py          ← Admin dashboard
│   ├── student.py        ← Student dashboard
│   └── recruiter.py      ← Recruiter dashboard
└── utils/
    ├── database.py       ← SQLite setup & helpers
    ├── theme.py          ← UI theming & reusable widgets
    └── helpers.py        ← Utility functions
```

---

## ⚙️ Requirements

- Python 3.10 or higher  
- **No third-party packages** — only the standard library is used (`tkinter`, `sqlite3`, `hashlib`, `os`)

---

## 🚀 How to Run

```bash
cd campus_recruitment
python main.py
```

---

## 🔐 Default Credentials

| Role    | Username | Password  |
|---------|----------|-----------|
| Admin   | admin    | admin123  |

Students and recruiters must register first via the **Register** link on the login screen.  
Recruiter accounts require **Admin approval** before they can log in.

---

## 🎯 Module Summary

### Admin
- Add / view / delete students  
- Add / delete companies  
- Manage all job postings (toggle active / delete)  
- View all applications across the system  
- Approve or reject recruiter registrations  

### Student
- Register & login  
- Update profile (name, CGPA, skills, resume file path)  
- Browse and filter available jobs (by skill / min CGPA)  
- Apply for jobs & withdraw applications  
- Track application status (Applied → Shortlisted → Selected / Rejected)  

### Recruiter
- Register & login (requires admin approval)  
- Post job openings (title, skills, CGPA cut-off, package, location, etc.)  
- Manage own job postings  
- View applicants per job, shortlist / select / reject candidates  

---

## 💡 Features

| Feature | Details |
|---|---|
| Authentication | SHA-256 hashed passwords |
| Job Filtering | By skill keywords and minimum CGPA |
| Application Tracking | Real-time status updates |
| Resume Upload | File-picker stores the local file path |
| Placement Marking | Admin can mark students as placed |
| Recruiter Approval | Two-step account activation |

---

## 📸 UI Theme

Dark navy colour scheme with vivid accent colours — designed for long recruitment sessions without eye strain.
