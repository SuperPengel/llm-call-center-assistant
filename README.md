# LLM Call Center Assistant

## 📌 Project Overview

This project demonstrates a mini end-to-end pipeline for customer support automation using LLMs.

It processes customer service call transcripts, retrieves relevant knowledge base articles, and generates summaries and advisor suggestions.

The goal is to simulate a real-world LLM-based application for improving advisor productivity.

---

## 🎯 Problem

Customer service agents spend significant time:

* Reading long call transcripts
* Searching for the correct knowledge base article
* Deciding on next actions

This leads to inefficiencies and inconsistent service quality.

---

## 💡 Solution

This project builds a simplified system that:

* Summarizes customer calls
* Retrieves relevant knowledge base documents
* Suggests next actions for advisors
* Tracks basic performance metrics

---

## ⚙️ Features

* 📥 Data ingestion from JSON files
* 🔄 Data transformation and feature engineering
* 🔎 Knowledge base retrieval (rule-based)
* 🤖 Call summarization (LLM / placeholder)
* 👩‍💼 Advisor recommendation system
* 📊 Monitoring and evaluation metrics

---

## 🏗️ Project Structure

```
llm-call-center-assistant/
│
├── data/
│   ├── raw/
│   └── output/
│
├── notebooks/
│   ├── 01_ingestion.ipynb
│
├── src/
│   ├── ingest.py
│   ├── transform.py
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

## 🧪 Tech Stack

* Python
* Pandas
* PySpark (planned / optional)
* Jupyter Notebook

---

## 📊 Example Use Case

Input:

> Customer received an incorrect invoice and asks for clarification.

Output:

* Summary: Customer questions incorrect invoice charges
* Suggested KB: Facturatiebeleid
* Advisor Action: Explain billing structure and verify invoice

---

## 🚀 How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Start Jupyter:

```
jupyter notebook
```

3. Open:

```
notebooks/01_ingestion.ipynb
```

---

## 📈 Future Improvements

* Add embedding-based retrieval (vector search)
* Integrate real LLM API for summarization
* Add Databricks job scheduling
* Improve monitoring and evaluation metrics
* Build a simple API or UI

---

## ⚠️ Disclaimer

This project uses **synthetic data** for demonstration purposes only.

---

## 👤 Author

Mark Pengel
