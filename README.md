# AI Full Stack Prep Guide

A personal knowledge base covering AI, full-stack engineering, and system design — built while learning in public. All notes, guides, and cheat sheets are openly available. Feel free to reference, fork, or share anything here.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sarvesh%20Talele-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sarveshtalele/) [![Medium](https://img.shields.io/badge/Medium-@sarveshtalele-000000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@sarveshtalele)


## About This Repo

This is my personal learning dump. Every time I study a new concept, go through interview prep, or summarise a topic, I drop a file here. The goal is to build a structured, searchable reference I can return to — and that others might find useful too.

Topics span the full AI engineering stack:

- **AI & ML fundamentals** — models, training, inference, RAG, agents
- **Backend & APIs** — Python, REST, async patterns, databases
- **System design** — architecture patterns, scalability, trade-offs
- **Interview prep** — concept walkthroughs, common questions, answers

There is no course or curriculum here — just honest notes from someone learning in the open.



## Contents

<!-- AUTO-GENERATED-START -->

### 📚 Learning Guides

| # | Topic | File |
|---|-------|------|
| 1 | Api Guide | [`api-guide.md`](learning-guides/api-guide.md) |
| 2 | Python Guide | [`python-guide.md`](learning-guides/python-guide.md) |

### 🎯 Interview Guides

| # | Topic | File |
|---|-------|------|
| 1 | Python Interview Guide | [`python-interview-guide.md`](interview-guides/python-interview-guide.md) |

### 📋 Cheat Sheets

| # | Topic | File |
|---|-------|------|
| 1 | Python Cheatsheet | [`python-cheatsheet.md`](cheatsheets/python-cheatsheet.md) |

<!-- AUTO-GENERATED-END -->



## Folder Structure

```
ai-fullstack-prep-guide/
├── learning-guides/      # Deep-dive notes on a topic
├── interview-guides/     # Interview-focused walkthroughs
├── cheatsheets/          # Quick-reference sheets
└── scripts/
    └── update_readme.py  # Auto-generates the tables above
```

New folders are picked up automatically — drop a markdown file in and the index updates on the next push.


## How the Auto-Index Works

A GitHub Action runs on every push that touches a `.md` file or the generator script:

1. `scripts/update_readme.py` scans all content folders for markdown files.
2. It derives the topic name directly from the filename — hyphens become spaces, words are title-cased.
3. The tables between the `AUTO-GENERATED` markers in this file are rewritten.
4. The updated README is committed back automatically with `[skip ci]` to prevent loops.

To preview locally before pushing:

```bash
python3 scripts/update_readme.py
```



## File Naming

Files use descriptive, hyphenated names that map directly to table entries:

| Filename | Displayed as |
|----------|-------------|
| `python-guide.md` | Python Guide |
| `system-design-basics.md` | System Design Basics |
| `transformer-architecture.md` | Transformer Architecture |



## Contributing / Using This

This is a personal repo, but you are welcome to:

- **Reference** any notes for your own study
- **Fork** the repo and adapt the structure for your own learning
- **Open an issue** if you spot an error or want to suggest a topic

---

*Maintained by [Sarvesh Kishor Talele](https://github.com/sarveshtalele) — learning in public.*
