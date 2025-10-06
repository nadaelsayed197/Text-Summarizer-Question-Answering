# 🧠 Text Summarizer & Question Answering App

This project is a **Streamlit web application** that performs two NLP tasks using pre-trained Hugging Face models:

1. **Text Summarization** — generates concise summaries for long texts.
2. **Question Answering** — provides answers to questions based on a given context paragraph.

---

## 🚀 Features

* Interactive web interface built with **Streamlit**
* Uses **Facebook BART Large CNN** for summarization
* Uses **DistilBERT (SQuAD)** for question answering
* Lightweight and easy to deploy

---

## 🧩 Tech Stack

* **Python**
* **Streamlit**
* **Transformers (Hugging Face)**
* **PyTorch**

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/text-summarizer-qa-app.git
cd text-summarizer-qa-app
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate  # on Windows
# or
source venv/bin/activate  # on macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app locally

```bash
streamlit run app.py
```

---

## 💡 Usage

### 📝 Summarization

1. Choose **Summarization** from the sidebar.
2. Paste or type a long text.
3. Click **Summarize** to generate a concise summary.

### ❓ Question Answering

1. Choose **Question Answering** from the sidebar.
2. Enter a **context paragraph** and a **question**.
3. Click **Get Answer** to see the model's prediction.

---

## 🌐 Deployment

You can deploy the app easily on **Streamlit Cloud**:

1. Push your code to GitHub.
2. Go to [https://share.streamlit.io](https://share.streamlit.io).
3. Connect your GitHub account and select the repository.
4. Set the main file to `app.py`.
5. Click **Deploy**.

---

## 📚 Example Inputs

**Summarization Example**

```
Artificial Intelligence (AI) refers to the simulation of human intelligence in machines...
```

**Question Answering Example**

```
Context: The Eiffel Tower was designed by Gustave Eiffel and built in 1889.
Question: Who designed the Eiffel Tower?
Answer: Gustave Eiffel
```

---

## 🧠 Acknowledgments

* [Hugging Face Transformers](https://huggingface.co/transformers/)
* [Streamlit](https://streamlit.io/)
