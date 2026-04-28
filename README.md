# Climate Challenge Week 0

## Project Setup

### Clone Repository
git clone https://github.com/redietwogayehu/climate-challenge-week0.git

### Navigate to Project
cd climate-challenge-week0

### Create Virtual Environment
python3 -m venv venv

### Activate Environment
source venv/bin/activate

### Install Dependencies
pip install -r requirements.txt

## Continuous Integration

GitHub Actions runs automatically on pushes to the main branch.



## Project Overview

This project analyzes climate trends across five African countries using NASA climate data. The goal is to support evidence-based insights for COP32 climate discussions.

## Completed Work

### Task 1: Setup
- Repository initialization
- Environment setup using Python venv
- CI pipeline with GitHub Actions

### Task 2: EDA
- Country-level climate profiling
- Data cleaning (-999 handling, duplicates removal)
- Feature engineering (DATE, Month)
- Visual analysis of temperature and rainfall
- Correlation and distribution analysis


## Dashboard

Run locally:

streamlit run app/main.py