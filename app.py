import streamlit as st
from transformers import pipeline

# --- App Title ---
st.title("Text Summarizer & Question Answering App")

# --- Load Models ---
@st.cache_resource
def load_models():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    return summarizer, qa_model

summarizer, qa_model = load_models()

# --- Sidebar Task Selection ---
option = st.sidebar.selectbox("Choose task:", ["Summarization", "Question Answering"])

# --- Summarization Section ---
if option == "Summarization":
    st.subheader("Text Summarizer")
    text = st.text_area("Enter text to summarize:")
    if st.button("Summarize"):
        if text.strip():
            summary = summarizer(
                text,
                max_length=130,
                min_length=30,
                do_sample=False
            )[0]['summary_text']
            st.success(summary)
        else:
            st.warning("Please enter some text.")

# --- Question Answering Section ---
elif option == "Question Answering":
    st.subheader("Question Answering")
    context = st.text_area("Enter context paragraph:")
    question = st.text_input("Enter your question:")
    if st.button("Get Answer"):
        if context.strip() and question.strip():
            answer = qa_model(question=question, context=context)
            st.success(f"Answer: {answer['answer']}")
        else:
            st.warning("Please enter both context and question.")
