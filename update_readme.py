import os
import re

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
        
        # Build progress bar
        pct = (mastered / total * 10) if total > 0 else 0
        bars = "🟩" * int(pct) + "⬜" * (10 - int(pct))
        
        clean_name = cat.split('_', 1)[-1].replace('_', ' ')
        markdown_table += f"| 📁 {clean_name} | {bars} | {mastered} / {total} |\n"
        
    summary = f"### 📊 Total Progress: **{total_solved}** Problems Mastered\n\n"
    return summary + markdown_table

def update_readme():
    metrics = generate_metrics()
    
    # Create file if it doesn't exist
    if not os.path.exists("README.md"):
        with open("README.md", "w", encoding="utf-8") as f:
            f.write("# NeetCode 150 Progress Tracker\n\n\n\n")

    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
        
    # Self-healing: If tags are missing, inject them cleanly at the top
    if "" not in readme or "" not in readme:
        readme = "# NeetCode 150 Progress Tracker\n\n\n\n" + readme
        
    # Use non-greedy dotall matching to strictly target the contents inside the tags
    pattern = r".*?"
    replacement = f"\n{metrics}\n"
    
    new_readme = re.sub(pattern, replacement, readme, flags=re.DOTALL)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme)

if __name__ == "__main__":
    update_readme()