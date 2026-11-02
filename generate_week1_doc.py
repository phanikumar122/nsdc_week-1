import os
from docx.shared import Inches, Pt, RGBColor
from doc_builder import (
    create_base_document, add_header_banner, add_heading_1, add_heading_2,
    add_heading_3, add_paragraph, add_bullet, add_callout, add_styled_table, add_figure
)

def build_week1_document():
    doc = create_base_document()
    
    # Header Banner
    add_header_banner(
        doc,
        title="TelePulse AI: Customer Churn Prediction & Proactive Retention Strategy",
        subtitle="Comprehensive Data Science Project Plan, Architectural Strategy, and 35-Hour Execution Blueprint",
        task_badge="Week 1 Deliverable | Strategic Project Charter"
    )

    # 1. Executive Summary & Problem Background
    add_heading_1(doc, "1. Executive Summary & Problem Background")
    
    add_paragraph(doc, 
        "In the contemporary subscription telecommunications and digital services landscape, customer retention serves as the primary engine of sustainable profitability. Industry empirical benchmarks establish that acquiring a replacement subscriber costs between five to seven times more than retaining an existing account. TelePulse Communications—a hypothetical mid-to-large tier telecommunications provider servicing approximately 120,000 active subscribers across residential broadband, digital voice, streaming entertainment, and mobile services—is currently confronting an annualized churn rate of 26.5%. This rate significantly surpasses the healthy industry median benchmark of 14% to 16%, translating into a direct top-line recurring revenue attrition of approximately $3.24 million annually.",
        bold_prefix="Business Context: "
    )
    
    add_paragraph(doc,
        "Historically, TelePulse has relied on passive, reactive customer service retention tactics. Customers only encounter retention counter-offers after voluntarily placing a cancellation request with call center representatives, at which stage customer sentiment is irreparably degraded and success rates fall below 12%. Furthermore, uncoordinated promotional discounting without risk segmentation has eroded average revenue per user (ARPU) by granting unnecessary discounts to loyal subscribers who had zero churn propensity.",
        bold_prefix="Problem Statement: "
    )

    add_callout(
        doc,
        "Transitioning from reactive churn firefighting to proactive, algorithmic risk mitigation will allow TelePulse to identify at-risk subscribers 30 to 60 days before contract expiry or cancellation, yielding an estimated net annual revenue preservation of $1.84M after accounting for intervention costs.",
        title="Strategic Value Proposition"
    )

    add_paragraph(doc,
        "The primary justification for leveraging a Python-based data science architecture lies in Python's industry-standard machine learning ecosystem (Pandas, Scikit-Learn, LightGBM, XGBoost, Optuna), flexible ETL pipeline integration, and robust open-source API serving capabilities (FastAPI). This document outlines the strategic roadmap, technical architecture, 35-hour work breakdown structure, and governance protocols necessary to build, deploy, and operationalize the TelePulse AI churn mitigation engine.",
        bold_prefix="Technical Justification: "
    )

    # 2. Project Objectives & Detailed Scope
    add_heading_1(doc, "2. Project Objectives & Scoping Matrix")
    
    add_paragraph(doc,
        "To ensure precise operational alignment across data science, data engineering, business intelligence, and customer success stakeholders, the project defines rigid primary technical and financial objectives alongside a strict scoping boundary.")

    add_heading_2(doc, "2.1 Primary Quantitative & Business Objectives")
    add_bullet(doc, "Achieve an Area Under the Precision-Recall Curve (PR-AUC) >= 0.82 and ROC-AUC >= 0.88 across 5-fold stratified cross-validation on holdout test cohorts, reflecting high discriminative power under class imbalance.", bold_prefix="Discriminative Predictive Accuracy: ")
    add_bullet(doc, "Identify and flag at least 85% of churn-prone accounts (Sensitivity/Recall >= 0.85) at an operational false-positive tolerance threshold below 15%.", bold_prefix="Early Warning Lead Time: ")
    add_bullet(doc, "Deliver calibrated churn risk probability deciles (0.00 to 1.00) paired with SHAP (SHapley Additive exPlanations) local feature contribution attributions for every customer scored.", bold_prefix="Explainable Risk Scoring: ")
    add_bullet(doc, "Reduce annualized subscriber churn from 26.5% to below 18.0% within the initial 12-month post-deployment production lifecycle, generating an estimated gross revenue recovery of $2.15M.", bold_prefix="Enterprise Financial ROI: ")
    add_bullet(doc, "Maintain sub-50 millisecond inference response latency for real-time CRM API queries, coupled with a nightly batch scoring pipeline handling 120,000 active records in under 15 minutes.", bold_prefix="Engineering Latency & Throughput: ")

    add_heading_2(doc, "2.2 In-Scope vs. Out-of-Scope Boundary Matrix")
    add_paragraph(doc, "A definitive boundary is crucial to avoid scope creep within the allocated 35-hour engineering sprint.")

    scope_headers = ["Project Dimension", "In-Scope (Confirmed Deliverables)", "Out-of-Scope (Deferred to Future Sprints)"]
    scope_rows = [
        ["Data Sources", "CRM subscriber records, relational billing logs, call center ticket summaries, network usage aggregates", "Raw audio speech-to-text transcription of call center recordings; external social media sentiment scraping"],
        ["Modeling Methodology", "Supervised classification algorithms (Logistic Regression, Random Forest, XGBoost, LightGBM, CatBoost)", "Deep neural networks (Transformers, LSTMs); unexplainable black-box models violating consumer credit explainability"],
        ["Feature Engineering", "Tenure tenure-to-charge ratios, service bundling counts, support escalation frequency, payment method stability", "Real-time edge IoT router telemetry packet inspection; dynamic GPS geolocation tracking of cellular devices"],
        ["Inference Strategy", "Scheduled nightly batch database scoring + RESTful FastAPI microservice container for ad-hoc agent lookup", "Embedded on-device mobile client scoring; decentralized federated edge learning models"],
        ["Downstream Actions", "Scored customer risk tiers pushed to Salesforce CRM queues and automated email/SMS marketing workflows", "Direct automated algorithmic contract cancellations or unmonitored financial credit adjustments"]
    ]
    add_styled_table(doc, scope_headers, scope_rows, [Inches(1.5), Inches(2.6), Inches(2.6)])

    # 3. Methodology & Strategy
    add_heading_1(doc, "3. Methodology, Lifecycle Strategy & Architectural Blueprint")
    add_paragraph(doc,
        "The project strictly adheres to the Cross-Industry Standard Process for Data Mining (CRISP-DM) framework, enriched with contemporary MLOps best practices to facilitate iterative feedback loops, auditability, and production reliability.")

    add_figure(doc, "figures/w1_fig1_ds_lifecycle.png", "TelePulse AI End-to-End Data Science Project Lifecycle & CRISP-DM Workflow", width=Inches(6.5))

    add_heading_2(doc, "3.1 End-to-End Architectural Pipeline")
    add_paragraph(doc,
        "The architecture is modularized into four decoupled enterprise tiers: Data Ingestion & Storage, Feature Store & Transformation, Model Development & Experiment Tracking, and Inference & Operational Action Serving.")

    add_figure(doc, "figures/w1_fig3_architecture.png", "Enterprise ML System Architecture: From Ingestion to Retention Action Tier", width=Inches(6.5))

    add_heading_2(doc, "3.2 Detailed Phase-by-Phase Technical Strategy")
    add_bullet(doc, "Connect to source relational databases (PostgreSQL, Snowflake) and extract historical transactional tables. Implement Great Expectations validation suites to enforce schema validation, nullity bounds, and data type assertions.", bold_prefix="Data Acquisition & Integrity Verification: ")
    add_bullet(doc, "Audit missingness mechanisms (MCAR vs MAR), treat anomalies via robust IQR thresholding, assess distribution skewness, calculate multicollinearity variance inflation factors (VIF), and generate bivariate churn relationship profiles.", bold_prefix="Exploratory Data Analysis & Data Cleaning: ")
    add_bullet(doc, "Engineer behavioral velocity features (e.g., 30-day ticket velocity vs 90-day baseline), aggregate service tier indices, encode categorical attributes via Target Encoding and One-Hot Encoding, and standardize numerical scales via RobustScaler.", bold_prefix="Feature Engineering & Selection: ")
    add_bullet(doc, "Address the ~26% minority class distribution utilizing Stratified 5-Fold Cross Validation combined with Synthetic Minority Over-sampling (SMOTE-NC) applied strictly inside cross-validation training folds to prevent data leakage.", bold_prefix="Class Balancing & Sampling Strategy: ")
    add_bullet(doc, "Benchmark candidate algorithms ranging from interpretable baselines (ElasticNet Logistic Regression) to high-performance tree ensembles (Random Forest, XGBoost, LightGBM). Optimize hyperparameter spaces via Optuna Bayesian optimization.", bold_prefix="Model Zoo Benchmarking & Hyperparameter Tuning: ")
    add_bullet(doc, "Evaluate calibrated probabilities using Brier Score, Cost-Benefit Matrix optimization, PR-AUC, and ROC-AUC. Deconstruct model logic using SHAP TreeExplainer to deliver both global variable rankings and local customer-level risk explanations.", bold_prefix="Performance Diagnostics & Explainability: ")

    # 4. Timeline & 35-Hour Work Breakdown Structure
    add_heading_1(doc, "4. Work Breakdown Schedule (WBS) & 35-Hour Sprint Allocation")
    add_paragraph(doc,
        "To guarantee execution rigor within the prescribed 30 to 35-hour internship timeframe, the project is structured across six sequential phases, each equipped with explicit deliverables and milestone verification gates.")

    add_figure(doc, "figures/w1_fig2_gantt_chart.png", "Gantt Timeline Chart: 35-Hour Sprint Milestone and Resource Allocation Plan", width=Inches(6.4))

    timeline_headers = ["Phase", "Sprint Activity Description", "Key Milestones & Deliverables", "Allocated Hours"]
    timeline_rows = [
        ["Phase 1", "Problem Definition, Stakeholder Scoping & Architecture Design", "Approved Project Charter, KPI Target Definitions, Scope Matrix", "5.0 Hours"],
        ["Phase 2", "Data Pipeline Ingestion, Schema Auditing & Quality Verification", "Validated Extraction Scripts, Great Expectations Assertion Suite", "6.0 Hours"],
        ["Phase 3", "Exploratory Data Analysis (EDA) & Data Preprocessing Protocol", "Statistical Profiling Report, Outlier & Missing Data Treatment", "7.0 Hours"],
        ["Phase 4", "Feature Engineering, Velocity Transformation & Selection", "Feature Store Dataset, VIF Multicollinearity Reduction Matrix", "5.0 Hours"],
        ["Phase 5", "Model Benchmarking, Bayesian Optimization (Optuna) & Tuning", "MLflow Run Logs, Tuned LightGBM Model Artifact, Calibration Curve", "6.0 Hours"],
        ["Phase 6", "Model Evaluation, Explainability (SHAP) & Final Report Prep", "Cost-Benefit Evaluation Matrix, Executive Insights Documentation", "6.0 Hours"],
        ["Total", "Comprehensive End-to-End Data Science Project Plan Execution", "Complete Production Strategy, Tested Scripts & Final DOCX Report", "35.0 Hours"]
    ]
    add_styled_table(doc, timeline_headers, timeline_rows, [Inches(0.9), Inches(2.7), Inches(2.3), Inches(0.8)])

    # 5. Technology Stack & Python Tooling
    add_heading_1(doc, "5. Technology Stack & Python Tooling Specification")
    add_paragraph(doc, "The project relies strictly on stable, battle-tested Python libraries and supporting ecosystem tools:")

    tools_headers = ["Domain / Layer", "Python Library / Tool", "Version", "Role & Justification in Architecture"]
    tools_rows = [
        ["Data Processing", "Pandas & NumPy", ">= 2.2.0", "In-memory tabular data manipulation, vectorized arithmetic, and schema management"],
        ["Data Quality", "Great Expectations", ">= 0.18.0", "Declarative automated data validation, schema constraint checking, and quality alerting"],
        ["Visualization", "Matplotlib & Seaborn", ">= 3.8.0", "High-resolution publication-grade statistical charts, distribution plots, and correlation matrices"],
        ["Interactive EDA", "Plotly Express", ">= 5.20.0", "Dynamic web-based multidimensional exploration charts and interactive drill-down dashboards"],
        ["Machine Learning", "Scikit-Learn", ">= 1.4.0", "Core preprocessing pipelines, ColumnTransformer, baseline models, and cross-validation metrics"],
        ["Gradient Boosting", "LightGBM & XGBoost", ">= 4.3.0", "State-of-the-art tree ensembles offering high throughput, categorical support, and accuracy"],
        ["Class Imbalance", "Imbalanced-Learn (imblearn)", ">= 0.12.0", "SMOTE-NC synthetic data generation tailored for mixed numerical-categorical subscriber data"],
        ["Hyperparameter Opt.", "Optuna", ">= 3.6.0", "Next-generation Bayesian hyperparameter search using Tree-structured Parzen Estimator (TPE)"],
        ["Explainable AI", "SHAP (SHapley Additive exPlanations)", ">= 0.45.0", "Local and global feature attribution ensuring enterprise interpretability and fair lending compliance"],
        ["MLOps Tracking", "MLflow", ">= 2.12.0", "Experiment tracking, parameter logging, artifact serialization, and model registry lifecycle"],
        ["API Serving", "FastAPI & Uvicorn", ">= 0.110.0", "Asynchronous, low-latency REST API microservice exposing `/predict` endpoint for CRM integration"],
        ["Containerization", "Docker & Docker Compose", ">= 26.0", "Standardized container packaging ensuring environment reproducibility and cloud portability"]
    ]
    add_styled_table(doc, tools_headers, tools_rows, [Inches(1.4), Inches(1.8), Inches(0.8), Inches(2.7)])

    # 6. Expected Outcomes, Risks & Mitigation Strategies
    add_heading_1(doc, "6. Expected Outcomes, Strategic Risks & Mitigation Protocol")
    
    add_heading_2(doc, "6.1 Expected Business & Operational Outcomes")
    add_bullet(doc, "Direct preservation of approximately 2,800 at-risk subscribers within the first operational year, translating to $1.84M in net retained ARR after incentive costs.", bold_prefix="Tangible Financial Savings: ")
    add_bullet(doc, "Front-line customer success reps receive prioritized daily queues of high-risk accounts alongside top three localized churn drivers (e.g., 'Frequent Fiber Outages + Month-to-Month Contract').", bold_prefix="Optimized Customer Success Efficiency: ")
    add_bullet(doc, "Elimination of blanket promotional discounting, preserving baseline revenue and targeting budget strictly where intervention changes customer decision.", bold_prefix="Smarter Marketing Budget Allocation: ")

    add_heading_2(doc, "6.2 Anticipated Project Challenges and Robust Mitigation Plan")
    
    risk_headers = ["Identified Challenge / Risk", "Probability / Impact", "Concrete Engineering & Governance Mitigation Strategy"]
    risk_rows = [
        ["Class Imbalance (26.5% churn minority)", "High / High", "Apply SMOTE-NC strictly within training cross-validation folds; utilize PR-AUC instead of standard accuracy; tune decision threshold based on cost matrix."],
        ["Data Leakage from Temporal Features", "Medium / Critical", "Enforce strict temporal out-of-time validation splits; calculate features using historical backward-looking rolling windows only."],
        ["Feature Drift & Changing Behavior", "High / Medium", "Deploy Evidently AI monitor in production to continuously compute Population Stability Index (PSI) and Kolmogorov-Smirnov tests on input feature distributions."],
        ["Cold-Start Problem (New Subscribers)", "Medium / Low", "Develop fallback heuristic rule-engine based on demographic and initial onboarding setup until 60-day transactional history accumulates."],
        ["Stakeholder Model Mistrust", "Medium / High", "Integrate SHAP visual waterfall explanations directly into CRM screens, allowing account reps to see plain-English justifications for risk scores."]
    ]
    add_styled_table(doc, risk_headers, risk_rows, [Inches(1.8), Inches(1.3), Inches(3.6)])

    add_callout(
        doc,
        "By enforcing strict phase milestones, standardized Python tooling, explainable gradient-boosted models, and cost-sensitive threshold optimization, TelePulse AI provides an enterprise-grade blueprint capable of achieving predictable, high-ROI retention outcomes.",
        title="Project Planning Conclusion"
    )

    # Save document
    os.makedirs("deliverables", exist_ok=True)
    out_path = "deliverables/Week_1_Data_Science_Project_Planning_and_Strategy_Design.docx"
    doc.save(out_path)
    print(f"Successfully generated: {out_path}")

if __name__ == '__main__':
    build_week1_document()
