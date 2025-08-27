# Chain-of-Table: Structured Reasoning over Tabular Data with LLMs

## 🚀 Introduction
**Chain-of-Table (CoTble)** is an approach for enabling **Large Language Models (LLMs)** to reason effectively over **tabular data**.  

Inspired by *Chain-of-Thought* prompting, Chain-of-Table decomposes a query into **step-by-step reasoning operations** aligned with the table’s structure (rows, columns, cells). This improves both **accuracy** and **interpretability** for question answering tasks involving structured data.

This repository contains an implementation of Chain-of-Table as a **LlamaIndex Pack**, making it easy to integrate with RAG pipelines and chatbot frameworks.

---

## 📚 From the Paper
- **Problem**: LLMs are powerful but unreliable when reasoning directly over tables. They often miss key numerical operations or fail to align rows/columns correctly.  
- **Solution (Chain-of-Table)**:  
  - Represent tables in a structured format suitable for LLMs.  
  - Use guided prompting to generate **reasoning chains** over table elements.  
  - Encourage interpretable intermediate steps (like filtering, comparing, aggregating).  
- **Impact**:  
  - Boosts factual correctness in table-based QA tasks.  
  - Produces transparent reasoning chains users can inspect.  
  - Applicable to financial analysis, business intelligence, scientific tables, etc.

---

## 📂 Project Structure
```
.
├── huy/notebook/chain_of_table_pack/
│   └── llama_index/packs/tables/chain_of_table/
│       ├── base.py             # Core Chain-of-Table implementation
│       └── __init__.py
├── examples/                   # Example notebooks & usage
├── requirements.txt            # Dependencies
└── README.md                   # Documentation
```

---

## ⚙️ Installation
```bash
git clone https://github.com/your-username/chain-of-table.git
cd chain-of-table
pip install -r requirements.txt
```

---

## 🧩 Usage Example
```python
from llama_index.packs.tables.chain_of_table import ChainOfTable

# Initialize Chain-of-Table
cot = ChainOfTable()

# Example table
table = [
    ["Year", "Sales", "Profit"],
    ["2021", "1000", "200"],
    ["2022", "1500", "400"],
]

# Example query
query = "What is the profit growth from 2021 to 2022?"

# Run reasoning
result = cot.run(table, query)
print("Answer:", result)
```

---

## 📊 Applications
- **Business Intelligence**: automatic Q&A from spreadsheets or reports.  
- **Financial Analysis**: extracting growth rates, trends, and comparisons.  
- **Research Data**: interpreting structured experimental results.  
- **Chatbots**: allowing conversational interfaces to query tables.  

---
