import streamlit as st

from knowledge_gpt.components.faq import faq
from dotenv import load_dotenv
import os

load_dotenv()


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "2. Upload a pdf, docx, or txt file📄\n"
            "3. Ask a question about the document💬\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
            value=os.environ.get("OPENAI_API_KEY", None)
            or st.session_state.get("OPENAI_API_KEY", ""),
        )

        st.session_state["OPENAI_API_KEY"] = api_key_input

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖NIST AI 600-1 Helper allows you to ask questions about the "
            "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile and get accurate answers with instant citations. "
			"The most recent version of the document can be found here.[Source](https://www.nist.gov/itl/ai-risk-management-framework)"
   )
        st.markdown("# What is the purpose of the Artificial Intelligence Risk Management Framework document?")
        st.markdown(
            "In collaboration with the private and public sectors, "
            "NIST has developed a framework to better manage risks to individuals, organizations, and society" 
            "associated with artificial intelligence (AI). The NIST AI Risk Management Framework (AI RMF) is intended"
            " for voluntary use and to improve the ability to incorporate trustworthiness considerations into the design," 
            "development, use, and evaluation of AI products, services, and systems.[Source](https://www.nist.gov/itl/ai-risk-management-framework)"
        )
        st.markdown(
            "This tool is a work in progress. "
            "My fork of the project is located on [GitHub](https://github.com/oohtmeel1/knowledge_gpt) "  # noqa: E501
            "You can contribute to the main project on [GitHub](https://github.com/mmz-001/knowledge_gpt) " 
            "with your feedback and suggestions💡"
        )
        st.markdown("Changes Made by [Oohtmeel1](https://oohtmeel1.github.io/)")
        st.markdown("Gotta give credit to - Originally Made by [mmz_001](https://twitter.com/mm_sasmitha)")
        st.markdown("---")

        faq()
