import os

def generate_metrics():
    categories = sorted([f for f in os.listdir('.') if os.path.isdir(f) and f[0].isdigit()])
    
    total_solved = 0
    markdown_table = "| Category | Progress Bar | Solved |\n| :--- | :--- | :--- |\n"
    
    for cat in categories:
        folder_path = cat
        files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
        
        total = len(files)
        mastered = 0
        
        for file in files:
            with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
                content = f.read()
                if 'status: 🟩 Mastered' in content:
                    mastered += 1
        
        total_solved += mastered
        
        pct = (mastered / total * 10) if total > 0 else 0
        bars = "🟩" * int(pct) + "⬜" * (10 - int(pct))
        
        clean_name = cat.split('_', 1)[-1].replace('_', ' ')
        markdown_table += f"| 📁 {clean_name} | {bars} | {mastered} / {total} |\n"
        
    summary = f"### 📊 Total Progress: **{total_solved}** Problems Mastered\n\n"
    return summary + markdown_table

def update_readme():
    metrics = generate_metrics()
    
    # The exact static content you want on your repository homepage
    readme_content = (
        "# NeetCode 150 Progress Tracker\n\n"
        "Welcome to my NeetCode tracking repository! This dashboard updates automatically.\n\n"
        f"{metrics}\n"
        "## 🛠️ Tech Stack\n"
        "- Obsidian (Local Notes)\n"
        "- Python (Automation Script)\n"
        "- GitHub Actions (CI/CD)\n"
    )
    
    # Write mode ('w') completely overwrites the file. No regex, no tags, no duplicates.
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

if __name__ == "__main__":
    update_readme()