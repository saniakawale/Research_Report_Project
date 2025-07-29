from crewai import Agent
from gemini_llm import GeminiLLM

gemini_llm = GeminiLLM()
researcher = Agent(
    role="Researcher",
    goal="Find and summarize research sources for a report",
    backstory=(
        "You are an expert at conducting efficient and thorough online research. "
        "You find accurate and reliable sources to support an academic report."
    ),
    llm=gemini_llm
)

writer = Agent(
    role="Writer",
    goal="Draft a clear, factual, and structured research report using provided materials",
    backstory=(
        "You are a skilled content writer who transforms research material into "
        "cohesive and engaging academic sections."
    ),
    llm=gemini_llm
)

outliner = Agent(
    role="Outliner",
    goal="Create a detailed outline for a research report based on topic input",
    backstory=(
        "You are an expert academic strategist. You know how to organize research into "
        "a logical, well-structured academic report outline."
    ),
    llm=gemini_llm
)

editor = Agent(
    role="Editor",
    goal="Polish grammar, structure, and improve clarity of the final report",
    backstory=(
        "You are an experienced professional editor. You enhance readability, correctness, "
        "and adjust tone for academic and professional readability."
    ),
    llm=gemini_llm
)

supervisor = Agent(
    role="Supervisor",
    goal="Oversee the entire research process and ensure high quality at all steps",
    backstory=(
        "You are a senior research project manager. Your job is to oversee every agent's "
        "work, provide feedback, and ensure each step meets expected standards."
    ),
    llm=gemini_llm
)
