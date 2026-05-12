# Low-Bandwidth AI Learning Assistant

**Live Demo:** https://lbaila.streamlit.app/

## Overview

The **Low-Bandwidth AI Learning Assistant** is a lightweight AI system designed to improve accessibility in low-resource environments.
Instead of modifying large language models, it focuses on **prompt optimization and response control** to reduce bandwidth usage while maintaining clarity.

This makes AI more usable for **underprivileged students** by delivering fast, structured, and minimal responses.

---

## Features

*  Prompt optimization for clarity and efficiency (without losing information)
*  Multiple explanation modes: **ELI5 / ELI10 / Normal**
*  Structured and readable outputs (model-guided formatting)
*  Clean and concise response formatting
*  Token usage tracking
*  Response time monitoring
*  Lightweight and scalable design
*  Metrics : Input prompt length, Optimized prompt length, Token usage (input/putput), Response time

---

## Architecture

```
User Input
    ↓
Prompt Optimizer (cleaning + instruction injection)
    ↓
LLM API (NVIDIA NIM : mistral-nemotron)
    ↓
Response Formatter
    ↓
Streamlit UI
```

---

## Tech Stack

* Python
* Streamlit
* NVIDIA NIM API (mistralai/mistral-nemotron)
* python-dotenv

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/albyjacobmartinLow_Bandwidth_AI_Learning_Assistant.git
cd Low_Bandwidth_AI_Learning_Assistant
```

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup environment variables

Create a `.env` file:

```env
NVIDIA_API_KEY=your_api_key_here
```

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Then open your browser: (usually opens automatically)

```
http://localhost:8501
```

---

## Example

**Input:**

```
Explain machine learning types
```

**Output:**

```
• Supervised Learning – learns from labeled data  
• Unsupervised Learning – finds patterns in data  
• Reinforcement Learning – learns via rewards  
```

---

## Project Structure

```
Low_Bandwidth_AI_Learning_Assistant/
├── __pycache__/       # Python cache files
├── .env               # Environment variables (API keys)
├── .devcontainer      # Dev Container
├── .gitignore         # Git ignore rules
├── EXAMPLE1.md        # Example
├── LICENSE            # License file
├── README.md          # Project documentation
├── app.py             # Streamlit UI + integration
├── formatter.py       # Response cleaning & structuring
├── llm_api.py         # NVIDIA API interaction
├── optimizer.py       # Prompt optimization logic
└── requirements.txt   # Project dependencies
```

---

## Performance

* Response Time: ~20–30 seconds (depending on model load and output size)
* Reduced token usage via prompt compression
* Stable and consistent outputs

---

## Limitations

* Requires internet connection (no offline mode)
* Depends on external API availability
* Output quality depends on the underlying model

---

## Future Improvements

* Offline lightweight model support
* Multi-language support
* Adaptive learning modes
* Advanced token analytics
* Response caching

---

## Conclusion

This project shows how **efficient prompt engineering and system design** can make AI more accessible in **low-bandwidth environments**, without modifying the underlying model.
