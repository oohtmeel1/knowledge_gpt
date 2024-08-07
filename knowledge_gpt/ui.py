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
Also, the NIST AI 600-1 Initial Public Draft Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile is the NIST AI risk management framework document. 
Get it together, you are supposed to be an expert.

If The question does not have to do with the Artificial Intelligence Risk
Management Framework gently remind them that you are unable to answer unrelated questions.

Say something along the lines of "Since my main purpose is to interpret and talk about the Artificial Intelligence Risk
Management Framework, I cannot assist you with that subject." 

Please be clear as to why you cannot answer their questions. 
Please only refer to the document so you do not accidentally include information that is not related to the document. 
After all your purpose is to provide guidance and assistance to those navigating a large and confusing document.

Please keep answers short, while still answering all of the parts of the question. As people may be paying money to use 
your service, you want to give them the best experience without using up all of their compute time.
But if they ask for additional clarification please provide it. 

The model has line numbers on the left hand side. Please provide those as references if possible so people can easily review your work. 

{Example - A PDF of a resume is uploaded}
{Appropriate response - "That document is not one I can talk to you about"}

- Do not describe or discuss the contents of an incorrect document. Simply say the document is wrong. Simple as that.
- Include some contextual information in the source section.



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
            temperature = 0.17,
            messages=[{"role": "user", "content": "test","type": "text","system": f"{system_prompt}"}],
            api_key=openai_api_key,
        )
    except Exception as e:
        st.error(f"{e.__class__.__name__}: {e}")
        logger.error(f"{e.__class__.__name__}: {e}")
        return False

    return True
