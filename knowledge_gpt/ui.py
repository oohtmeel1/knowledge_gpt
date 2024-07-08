from typing import List
import streamlit as st
from langchain.docstore.document import Document
from knowledge_gpt.core.parsing import File
import openai
from streamlit.logger import get_logger
from typing import NoReturn

logger = get_logger(__name__)

system_prompt = '''
You are an expert on the Artificial Intelligence Risk 4 Management Framework: 5 Generative Artificial Intelligence 6 Profile framework document. 
You answer people's questions about the document and that are related to the Artificial Intelligence Risk
Management Framework.
If the document is **not**  the Artificial Intelligence Risk
Management Framework document or does not have anything to do with responsible AI you gently tell them that you cannot tell them anything about it,
as your job is to be an expert on the Artificial Intelligence Risk 4 Management Framework: 5 Generative Artificial Intelligence 6 Profile framework document.
If The question does not have to do with the Artificial Intelligence Risk
Management Framework please gently remind them that you are unable to answer unrelated questions.
As an expert you provide a clear, but very short explanation as to why you cannot answer questions, without providing more than a few words about the incorrect document.


'''

def wrap_doc_in_html(docs: List[Document]) -> str:
    """Wraps each page in document separated by newlines in <p> tags"""
    text = [doc.page_content for doc in docs]
    if isinstance(text, list):
        # Add horizontal rules between pages
        text = "\n<hr/>\n".join(text)
    return "".join([f"<p>{line}</p>" for line in text.split("\n")])


def is_query_valid(query: str) -> bool:
    if not query:
        st.error("Please enter a question!")
        return False
    return True


def is_file_valid(file: File) -> bool:
    if (
        len(file.docs) == 0
        or "".join([doc.page_content for doc in file.docs]).strip() == ""
    ):
        st.error("Cannot read document! Make sure the document has selectable text")
        logger.error("Cannot read document")
        return False
    return True


def display_file_read_error(e: Exception, file_name: str) -> NoReturn:
    st.error("Error reading file. Make sure the file is not corrupted or encrypted")
    logger.error(f"{e.__class__.__name__}: {e}. Extension: {file_name.split('.')[-1]}")
    st.stop()


@st.cache_data(show_spinner=False)
def is_open_ai_key_valid(openai_api_key, model: str) -> bool:
    if model == "debug":
        return True

    if not openai_api_key:
        st.error("Please enter your OpenAI API key in the sidebar!")
        return False
    try:
        openai.ChatCompletion.create(
            model=model,
            temperature = 0,
            messages=[{"system": f"{system_prompt}","role": "user", "content": "test","type": "text"}],
            api_key=openai_api_key,
        )
    except Exception as e:
        st.error(f"{e.__class__.__name__}: {e}")
        logger.error(f"{e.__class__.__name__}: {e}")
        return False

    return True
