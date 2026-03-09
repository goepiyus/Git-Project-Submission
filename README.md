
# Simple Calculator Application
A beginner-friendly Python calculator for the Git & GitHub Capstone Project.

## 5 Functions
1. add() - Addition
2. subtract() - Subtraction
3. multiply() - Multiplication
4. divide() - Division with zero check

5. modulus() - Remainder operation

# 🐙 Git & GitHub Capstone Project
### Sharing a Local Project to an Open-Source Platform (GitHub)

---

## 📌 About This Project

This is a beginner-level Git & GitHub project created as part of the **Tamilnadu Advanced Technical Training Institute** course.

The goal is simple:
- Create a project on your computer (local repository)
- Use Git commands to track changes
- Work with multiple branches
- Resolve merge conflicts
- Push everything to GitHub (remote repository)

---

## 🛠️ Tools & Software Used

| Tool | Purpose |
|------|---------|
| Git | Version control system |
| GitHub | Remote repository hosting |
| VS Code | Code editor / IDE |
| Terminal / Command Prompt | Running Git commands |

---

## 🌿 Branch Structure

This project uses **3 branches**:

```
main          → The main/base branch
developer1    → Branch for Developer 1's changes
developer2    → Branch for Developer 2's changes
```

---

## ⚙️ Git Concepts Used

- ✅ Git Configuration (`git config`)
- ✅ Git Initialization (`git init`)
- ✅ File Creation & Tracking (`git add`)
- ✅ Commits (`git commit`)
- ✅ Branch Creation & Switching (`git branch`, `git checkout`)
- ✅ Merging Branches (`git merge`)
- ✅ Resolving Merge Conflicts
- ✅ Connecting to Remote Repository (`git remote add origin`)
- ✅ Pushing to GitHub (`git push`)
- ✅ Checking Logs & Status (`git log`, `git status`)

---

## 📋 Step-by-Step Process

### 🔧 Step 1 – Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

### 📁 Step 2 – Initialize Local Repository
```bash
mkdir my-project
cd my-project
git init
```

### 📝 Step 3 – Create Files & First Commit (main branch)
```bash
# Create your project files
git add .
git commit -m "Initial commit on main branch"
```

### ☁️ Step 4 – Connect & Push to GitHub
```bash
git remote add origin https://github.com/your-username/your-repo.git
git push -u origin main
```

### 🌿 Step 5 – Create & Work on developer1 Branch
```bash
git checkout -b developer1
# Make some changes to your files
git add .
git commit -m "Second commit - changes by developer1"
```

### 🌿 Step 6 – Create & Work on developer2 Branch (from main)
```bash
git checkout main
git checkout -b developer2
# Make some changes to your files
git add .
git commit -m "Third commit - changes by developer2"
```

### 🔀 Step 7 – Merge Branches into Main
```bash
# First, merge developer1
git checkout main
git merge developer1

# Then, try merging developer2 (conflict will happen here!)
git merge developer2
```

### ⚠️ Step 8 – Resolve Merge Conflict
When a conflict happens, Git will mark the conflicting file like this:
```
<<<<<<< HEAD (main branch version)
This is the content from main/developer1
=======
This is the content from developer2
>>>>>>> developer2
```

👉 **Keep only the latest change** (developer2's version), delete the conflict markers, then:
```bash
git add .
git commit -m "Merge conflict resolved - kept latest changes"
```

### 🚀 Step 9 – Push All Branches to GitHub
```bash
git push origin developer1
git push origin developer2
```

---

## 📂 Project Files

```
my-project/
│
├── README.md          → Project description (this file)
├── main.py            → Main project file
├── function1.py       → Function 1
├── function2.py       → Function 2
├── function3.py       → Function 3
├── function4.py       → Function 4
└── function5.py       → Function 5
```

> 📌 The project contains **5 functions** as required by the assignment.

---

## 🖼️ Screenshots

> *(Add your screenshots here — terminal outputs, VS Code views, GitHub repository pages, etc.)*

---

## 🎥 Demo Video

> *(Attach your screen recording link or file here)*

---

## 📚 Skills & Techniques Learned

- Setting up Git for the first time
- Understanding what a repository is
- How branching works in team projects
- What merge conflicts are and how to fix them
- Pushing local work to GitHub for open-source sharing

---

## 👨‍💻 Author

- **Name:** *(Your Name)*
- **Course:** Git & GitHub — Tamilnadu Advanced Technical Training Institute
- **GitHub:** *(Your GitHub Profile Link)*

---

> 💡 *This project was built as a learning exercise to understand how real-world developers use Git and GitHub for collaboration.*
