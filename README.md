# YouTube Comment Analytics Pipeline 🚀

An end-to-end, automated pipeline for extracting, classifying, storing, and visualizing YouTube comments using AI, Azure, and Power BI.

## 🔍 Overview

This project enables a user to input any YouTube video URL and receive live insights into the sentiment and toxicity of its comments. Designed as a personal-use tool, the pipeline combines a fine-tuned BERT model, Azure Serverless SQL, Azure Data Factory, and Power BI to process and visualize comment analytics — all triggered on demand.

---

## ⚙️ Pipeline Workflow

1. **User Input** → Paste a YouTube video URL into the Python interface.
2. **Comment Extraction** → YouTube API retrieves up to 100 top-level comments.
3. **AI Classification** → A fine-tuned BERT model classifies each comment by sentiment and toxicity.
4. **Data Storage** → Classified results are inserted into an Azure SQL Serverless database.
5. **Automation** → Azure Data Factory moves new data into a Power BI dataset.
6. **Visualization** → Power BI presents real-time dashboards with trends, toxicity levels, and engagement analytics.
7. **Auto-refreshing** → Dashboards update dynamically without manual intervention.

---

## 🧠 Tech Stack

- **Python** – Comment extraction and classification logic.
- **HuggingFace Transformers (BERT)** – Fine-tuned for sentiment and toxicity classification.
- **YouTube Data API** – Retrieves video comments.
- **Azure SQL Serverless** – Cost-effective, serverless relational storage.
- **Azure Data Factory** – Automates data movement to Power BI.
- **Power BI** – Live dashboard for visualization.
- **Azure Data Studio** – For managing and editing the database schema.

---

## 📦 Features

- Fine-tuned LLM (BERT uncased) for nuanced comment classification.
- On-demand execution keeps cloud usage within the **Azure free tier**.
- No need for manual dashboard updates — fully automated refresh pipeline.
- Lightweight and scalable — ideal for solo use or future multi-user expansion.

---

## 🔒 Requirements

- Python 3.8+
- Azure account (with SQL Serverless and Data Factory setup)
- Power BI (Desktop or Service)
- YouTube Data API Key
- HuggingFace `transformers`, `pandas`, `sqlalchemy`, etc.

---

## 📌 Future Plans

- Add support for replies to comments.
- Enable batching multiple videos.
- Integrate notifications (email/Slack) when new insights are ready.

---

## 📄 License

MIT License


