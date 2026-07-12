import streamlit as st
from rag import (
    load_pdfs,
    chunk_text,
    create_vector_db,
    ask_question
)

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="StudyAI",
    page_icon="📚",
    layout="wide"
)

# ---------------- SESSION STATE ----------------

if "index" not in st.session_state:
    st.session_state.index = None

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "processed" not in st.session_state:
    st.session_state.processed = False

# ---------------- CSS ----------------

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}

[data-testid="stSidebar"]{
    background:#1E3A8A;
}

[data-testid="stSidebar"] *{
    color:white;
}

.main-title{
    font-size:40px;
    font-weight:bold;
    color:#2563EB;
}

.sub-title{
    color:gray;
    font-size:18px;
}

.chat-box{
    background:#F8FAFC;
    padding:18px;
    border-radius:12px;
    border:1px solid #E5E7EB;
    margin-top:10px;
}

.ai-box{
    background:#EEF4FF;
    padding:18px;
    border-radius:12px;
    border-left:6px solid #2563EB;
    margin-top:10px;
}

div.stButton > button{
    width:100%;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("📚 StudyAI")

    st.write("Intelligent Multi-PDF Study Assistant")

    st.divider()

    st.markdown("""
### 🚀 Features

- 📄 Upload Multiple PDFs
- 💬 Ask Questions
- 🔍 Semantic Search
- 🤖 AI-Powered Answers
""")

    st.divider()

    st.caption("Built using Ollama + Qwen Embeddings + FAISS")

# ---------------- HEADER ----------------

st.markdown(
    "<p class='main-title'>📚 Intelligent Multi-PDF Study Assistant</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='sub-title'>Upload multiple PDFs and ask questions using AI.</p>",
    unsafe_allow_html=True
)

st.write("")

left, right = st.columns([3,1])

# ============================================================
# LEFT SIDE
# ============================================================

with left:

    uploaded_files = st.file_uploader(
        "Upload PDF Files",
        type="pdf",
        accept_multiple_files=True
    )
     # Detect if uploaded PDFs have changed
    current_files = [pdf.name for pdf in uploaded_files] if uploaded_files else []

    if "previous_files" not in st.session_state:
        st.session_state.previous_files = []

    if current_files != st.session_state.previous_files:

        st.session_state.processed = False
        st.session_state.previous_files = current_files

    # ---------------- PROCESS PDF ONLY ONCE ----------------

    if uploaded_files and not st.session_state.processed:

        with st.spinner("Processing PDFs..."):

            text = load_pdfs(uploaded_files)

            chunks = chunk_text(text)

            index = create_vector_db(chunks)

            st.session_state.index = index
            st.session_state.chunks = chunks
            st.session_state.processed = True

        st.success("PDFs Processed Successfully!")

    # ---------------- CHAT ----------------

    query = st.chat_input(
        "Ask anything from your PDFs..."
    )

    if query:

        if st.session_state.index is None:

            st.warning("Please upload PDF(s) first.")

        else:

            with st.spinner("Searching..."):

                answer = ask_question(
                    query,
                    st.session_state.index,
                    st.session_state.chunks
                )

            st.markdown(f"""
<div class="chat-box">
<b>🧑 You</b><br><br>
{query}
</div>
""", unsafe_allow_html=True)

            st.markdown(f"""
<div class="ai-box">
<b>🤖 StudyAI</b><br><br>
{answer}
</div>
""", unsafe_allow_html=True)

    st.write("")

    st.subheader("⚡ Quick Actions")

    c1, c2, c3, c4 = st.columns(4)

    # ---------------- SUMMARY ----------------

    with c1:
        if st.button("📄 Summary"):

            if st.session_state.index is None:
                st.warning("Please upload PDF(s) first.")
            else:

                with st.spinner("Generating Summary..."):

                    answer = ask_question(
                        "Provide a concise summary of all uploaded PDFs.",
                        st.session_state.index,
                        st.session_state.chunks
                    )

                st.markdown(f"""
    <div class="ai-box">
    <b>📄 Summary</b><br><br>
    {answer}
    </div>
    """, unsafe_allow_html=True)


    # ---------------- EXPLAIN ----------------

    with c2:
        if st.button("🧠 Explain"):

            if st.session_state.index is None:
                st.warning("Please upload PDF(s) first.")
            else:

                with st.spinner("Generating Explanation..."):

                    answer = ask_question(
                        """
    Explain the complete contents of the uploaded PDFs in simple language.
    Use headings and examples wherever possible.
    """,
                        st.session_state.index,
                        st.session_state.chunks
                    )

                st.markdown(f"""
    <div class="ai-box">
    <b>🧠 Explanation</b><br><br>
    {answer}
    </div>
    """, unsafe_allow_html=True)


    # ---------------- KEY POINTS ----------------

    with c3:
        if st.button("📌 Key Points"):

            if st.session_state.index is None:
                st.warning("Please upload PDF(s) first.")
            else:

                with st.spinner("Extracting Key Points..."):

                    answer = ask_question(
                        """
    Extract the most important key points from all uploaded PDFs.
    Return them as bullet points.
    """,
                        st.session_state.index,
                        st.session_state.chunks
                    )

                st.markdown(f"""
    <div class="ai-box">
    <b>📌 Key Points</b><br><br>
    {answer}
    </div>
    """, unsafe_allow_html=True)


    # ---------------- QUIZ ----------------

    with c4:
        if st.button("❓ Quiz"):

            if st.session_state.index is None:
                st.warning("Please upload PDF(s) first.")
            else:

                with st.spinner("Creating Quiz..."):

                    answer = ask_question(
                        """
    Generate a quiz from the uploaded PDFs.

    Create:
    - 10 Multiple Choice Questions
    - Provide 4 options
    - Mention the correct answer after each question.
    """,
                        st.session_state.index,
                        st.session_state.chunks
                    )

                st.markdown(f"""
    <div class="ai-box">
    <b>❓ Quiz</b><br><br>
    {answer}
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# RIGHT SIDE
# ============================================================

with right:

    st.subheader("📂 Uploaded PDFs")

    if uploaded_files:

        for pdf in uploaded_files:
            st.success(f"📕 {pdf.name}")

    else:

        st.info("No PDFs Uploaded")

    st.write("")

    st.subheader("📊 Statistics")

    if uploaded_files:
        st.metric("PDFs", len(uploaded_files))
    else:
        st.metric("PDFs", 0)

    if st.session_state.chunks:
        st.metric("Chunks", len(st.session_state.chunks))
    else:
        st.metric("Chunks", 0)

    st.write("")

    st.subheader("💡 Tips")

    st.info("""
✔ Upload multiple PDFs

✔ Ask natural language questions

✔ Compare documents

✔ Generate summaries
""")