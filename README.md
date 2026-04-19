# 🚀 AI Full Stack Learning Dump

A personal knowledge base of **learning guides** and **interview preparation notes** across AI full-stack technologies. Every folder in this repo is auto-indexed in the table below — drop a new markdown file in and the GitHub Action takes care of the rest.

---

## 📂 Contents

<!-- AUTO-GENERATED-START -->

### 🎯 Interview Guides

| # | Topic | File |
|---|-------|------|
| 1 | Python | [`ig_python.md`](interview-guides/ig_python.md) |

### 📚 Learning Guides

| # | Topic | File |
|---|-------|------|
| 1 | Python | [`lg_python.md`](learning-guides/lg_python.md) |

<!-- AUTO-GENERATED-END -->

---

## 🛠️ How the Auto-Index Works

1. Drop a markdown file into any top-level folder (e.g., `learning-guides/lg_javascript.md`).
2. Commit and push to `main`.
3. The **Auto-update README** workflow runs `scripts/update_readme.py`, regenerates the tables above between the `AUTO-GENERATED` markers, and pushes the updated README back.

Content outside the markers is preserved, so you can freely edit this intro, add badges, or extend the "How It Works" section.

### File Naming Convention

Files follow a `<prefix>_<topic>.md` scheme where the prefix identifies the folder:

| Folder              | Prefix | Example                        | Topic Shown     |
| ------------------- | ------ | ------------------------------ | --------------- |
| `learning-guides/`  | `lg_`  | `lg_python.md`                 | Python          |
| `interview-guides/` | `ig_`  | `ig_system-design.md`          | System Design   |

Hyphens in filenames become spaces in the topic name, and each word is title-cased.

### Adding a New Section

Just create a new folder with markdown files — the script picks it up automatically and generates a fresh table for it. To give the folder a prettier display name (with an emoji, etc.), add an entry to `FOLDER_TITLES` in `scripts/update_readme.py`:

```python
FOLDER_TITLES = {
    "learning-guides": "📚 Learning Guides",
    "interview-guides": "🎯 Interview Guides",
    "your-new-folder": "✨ Your New Folder",
}
```

### Running Locally

To preview README changes before pushing:

```bash
python scripts/update_readme.py
```