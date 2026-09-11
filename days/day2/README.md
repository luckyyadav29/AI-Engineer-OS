# 📘 Day 2 — Python Intermediate

**Date:** August 18, 2026  
**Phase:** 1 — Engineering Foundations

---

## 🎯 What I Learned Today

Object-Oriented Programming, Error Handling, and Python Modules — the building blocks of production code.

| # | Topic | Key Concepts |
|---|-------|-------------|
| 1 | Classes & Objects | `class`, `__init__`, `self`, instance attributes, methods |
| 2 | AI Model Config | Real-world class design, `to_dict()` pattern |
| 3 | Dunder Methods | `__str__`, `__repr__`, `__len__` — making classes work with Python builtins |
| 4 | Inheritance | Parent/child classes, `super()`, method overriding, `isinstance()` |
| 5 | Error Handling | `try/except/finally`, `raise`, catching specific error types |
| 6 | Custom Exceptions | Creating your own exception classes, exception hierarchy |
| 7 | Modules & Imports | `os`, `json`, `random`, `datetime` — essential built-in modules |
| 8 | Full Project | AI Prompt Logger — OOP + error handling + JSON file I/O |

---

## 📂 Files

| File | Description |
|------|-------------|
| `day2_python_intermediate.py` | Guided lesson — 8 exercises covering all topics above |
| `practice.py` | Homework — Student Grade Manager using OOP, inheritance, exceptions & JSON |

---

## 🔨 Mini Projects

### Lesson: AI Prompt Logger
- Logs prompts and responses with timestamps
- Saves/loads from JSON files
- Tracks stats (total prompts, models used, avg length)

### Practice: Student Grade Manager
- `Person` → `Student` inheritance chain
- Custom exceptions (`InvalidGradeError`, `StudentNotFoundError`)
- Add grades, calculate averages, rank students
- Save student data to JSON

---

## ▶️ How to Run

```bash
# Lesson
python day2_python_intermediate.py

# Practice (Student Grade Manager)
python practice.py
```

---

## 💡 Key Takeaways

- **OOP** keeps related data and behavior together — essential for building APIs, AI clients, and tools
- **Inheritance** lets you reuse code while specializing behavior (e.g., base `LLMClient` → `OpenAIClient`)
- **Error handling** prevents crashes — APIs fail, files go missing, users send bad input
- **Custom exceptions** make error handling specific and professional
- **`json` module** is your best friend for working with APIs and storing structured data
- Everything builds on Day 1: lists, dicts, functions, f-strings, and file I/O
