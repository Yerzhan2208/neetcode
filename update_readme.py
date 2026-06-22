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
                # Check your specific master string format here
                if 'status: 🟩 Mastered' in content:
                    mastered += 1
        
        total_solved += mastered
        
        # Build a visual progress bar (e.g., 🟩🟩⬜⬜⬜)
        pct = (mastered / total * 10) if total > 0 else 0
        bars = "🟩" * int(pct) + "⬜" * (10 - int(pct))
        
        clean_name = cat.split('_', 1)[-1].replace('_', ' ')
        markdown_table += f"| 📁 {clean_name} | {bars} | {mastered} / {total} |\n"
        
    summary = f"### 📊 Total Progress: **{total_solved}** Problems Mastered\n\n"
    return summary + markdown_table

def update_readme():
    metrics = generate_metrics()
    
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
        
    pattern = r"[\s\S]*"
    replacement = f"\n{metrics}\n"
    
    new_readme = readme, pattern # placeholder logic fix below
    import re
    new_readme = re.sub(pattern, replacement, readme)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme)

if __name__ == "__main__":
    update_readme()