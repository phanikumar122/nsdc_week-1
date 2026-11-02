# Week 1: Data Science Project Planning and Strategy Design

## TelePulse AI — Customer Churn Prediction & Proactive Retention Strategy

### Project Overview
This deliverable presents a comprehensive data science project plan for **TelePulse Communications**, a telecommunications provider servicing 120,000 active subscribers facing an annualized churn rate of 26.5% (~$3.24M in lost recurring revenue). The plan outlines the end-to-end strategy to build, deploy, and operationalize an intelligent churn prediction engine using Python.

### Deliverable Contents
- **Project Background & Motivation** — Business context, problem statement, and strategic value proposition
- **Project Objectives & Scoping Matrix** — Quantitative targets (PR-AUC ≥ 0.82, Sensitivity ≥ 85%, $1.84M net ARR), in-scope vs out-of-scope boundary
- **Methodology & CRISP-DM Strategy** — 7-phase data science lifecycle with iterative validation loops
- **35-Hour Work Breakdown Schedule** — Gantt timeline with milestone gates across 6 sprint phases
- **Technology Stack** — Python libraries (Pandas, Scikit-Learn, LightGBM, XGBoost, Optuna, MLflow, FastAPI, Docker)
- **Risk Assessment & Mitigation** — Class imbalance, data leakage, feature drift, cold-start, stakeholder trust

### Strategic Diagrams (Embedded in Report)
| Figure | Description |
|--------|-------------|
| `figures/w1_fig1_ds_lifecycle.png` | End-to-End CRISP-DM Project Lifecycle Flowchart |
| `figures/w1_fig2_gantt_chart.png` | 35-Hour Work Breakdown Gantt Timeline |
| `figures/w1_fig3_architecture.png` | Enterprise ML System Architecture |

### Tools & Technologies
Python 3.13 · Pandas · NumPy · Scikit-Learn · LightGBM · XGBoost · Optuna · MLflow · FastAPI · Docker · Great Expectations · SHAP

### How to Regenerate
```bash
pip install python-docx matplotlib seaborn numpy
python generate_week1_doc.py
```
