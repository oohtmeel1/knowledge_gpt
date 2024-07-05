# flake8: noqa
from langchain.prompts import PromptTemplate

## Use a shorter template to reduce the number of tokens in the prompt
template = """Create a final answer to the given questions using the provided document excerpts (given in no particular order) as sources. ALWAYS include a "SOURCES" section in your answer citing only the minimal set of sources needed to answer the question. If you are unable to answer the question, simply state that you do not have enough information to answer the question and leave the SOURCES section empty. Use only the provided documents and do not attempt to fabricate an answer.

---------

QUESTION: What is the best way to ensure my GenAI is safe?
=========
Content: To ensure your GenAI is safe, it is recommended to practice and follow incident response plans for addressing the generation of inappropriate or harmful content, conduct post-mortem analyses of incidents, provide external stakeholders with regular updates, simulate various scenarios to test system responses, use visualizations to represent model behavior, and manage incidents and errors by communicating with relevant AI actors.
SOURCES: Overview of Risks Unique to or Exacerbated by GAI ............................................................................ 3 4 5 6 7 8 9 10 11 12 13 14 15 16
Content: Additionally, ensure information security for GAI models and systems, evaluate feedback loops, and document training data sources to trace the origin and provenance of AI-generated content.
SOURCES: Actions to Manage GAI Risks ...................................................................................................................... 11 17
=========
FINAL ANSWER: To ensure your GenAI is safe, it is recommended to practice and follow incident response plans for addressing the generation of inappropriate or harmful content, conduct post-mortem analyses of incidents, provide external stakeholders with regular updates, simulate various scenarios to test system responses, use visualizations to represent model behavior, and manage incidents and errors by communicating with relevant AI actors. Additionally, ensure information security for GAI models and systems, evaluate feedback loops, and document training data sources to trace the origin and provenance of AI-generated content.
SOURCES: Introduction ........................................................................................................................................................ 1 2 3
Overview of Risks Unique to or Exacerbated by GAI ............................................................................ 3 4 5 6 7 8 9 10 11 12 13 14 15 16
Actions to Manage GAI Risks ...................................................................................................................... 11 17 
Appendix A. Primary GAI Considerations ........................................................................................................ 63 18 Appendix

---------

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""

STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
