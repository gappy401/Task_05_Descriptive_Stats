# scripts/generate_readme.py

readme_content = """
# 🥍 Women's Lacrosse Team Stats Analysis

This project analyzes player and team performance using descriptive statistics from the 2025 season. It includes:

## 📊 Key Metrics
- Total Games Played: 19
- Total Goals: 235
- Total Assists: 112
- Total Points: 347
- Total Shots: 538
- Shot Percentage: 43.7%
- Shots on Goal: 402
- SOG Percentage: 74.7%
- Ground Balls: 295
- Turnovers: 270
- Caused Turnovers: 153
- Draw Controls: 240
- Fouls: 373

## 🧠 LLM Prompts
Stored in `prompts/`:
- `baseline_questions.txt`
- `advanced_prompts.txt`

## 🐍 Scripts
- `descriptive_stats.py`: Computes team and player-level stats
- `player_analysis.py`: Identifies top performers and efficiency metrics

## 📁 Results
- `llm_responses.md`: Answers from LLM
- `evaluation_notes.md`: Comparison of expected vs. actual responses

## 🔍 Goal
Evaluate how well LLMs interpret structured sports data and answer natural language questions.
"""

with open("README.md", "w") as f:
    f.write(readme_content.strip())