# Task_05_Descriptive_Stats


## Overview
This repository documents my work for **Research Task 5: Descriptive Statistics and Large Language Models**. The goal is to evaluate how well large language models (LLMs) like Copilot, Claude, and ChatGPT can interpret and answer natural language questions based on a small structured dataset.

I selected the **2023 Syracuse University Women’s Lacrosse cumulative statistics**, sourced from [cuse.com](https://cuse.com/sports/womens-lacrosse/stats/2023). The project involves computing descriptive statistics, designing prompts, querying LLMs, and validating their responses against ground truth.

---

## Objectives
- Clean and prepare a small public dataset for analysis.
- Compute descriptive statistics using Python.
- Design and test natural language prompts across multiple LLMs.
- Evaluate model performance on factual and inferential questions.
- Reflect on how LLMs interpret structured data and generate responses.

---

## Methodology
- Extracted key metrics such as goals, assists, shot percentage, turnovers, and draw controls.
- Developed Python scripts to compute statistics like top scorers, shot accuracy, and turnover rates.
- Created a range of prompts—from simple factual queries to complex judgment-based questions.
- Queried LLMs and compared their answers to computed statistics.
- Documented successes, failures, and insights into model behavior.

---

## Sample Questions Asked
- How many games did the team play?
- Who scored the most goals?
- Which player had the highest shot accuracy?
- Who was the most improved player this season?
- Should the coach focus on offense or defense to win two more games next season?

---

## Reflections
This project helped me understand how transformer-based LLMs process language and structured data. I learned that LLMs tokenize inputs and rely heavily on context and phrasing to infer relationships. They don’t natively “understand” tables, which makes prompt engineering critical. I also explored how statistical truth can diverge from probabilistic language generation, and how to validate model outputs rigorously.



---

## Author
**Nandita Ghildyal**  
Machine Learning Engineer & Data Scientist  
Focused on scalable AI solutions and ethical data science