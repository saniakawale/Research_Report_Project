
from crewai import Task
from agents import researcher, writer, outliner, editor, supervisor
import os
print("GOOGLE_API_KEY is:", os.environ.get("GOOGLE_API_KEY"))

outline_task = Task(
    description="Create a detailed outline for the research report on 'Impact of climate change on rice production in India'.",
    agent=outliner,
    expected_output="A structured, sectioned outline in bullet or numbered format."
)

research_task = Task(
    description="Use the outline to find and summarize reliable sources and data for each section.",
    agent=researcher,
    expected_output="A section-by-section summary of sources, data, citations, and notes."
)

write_task = Task(
    description="Using the outline and research materials, write the main sections of the report.",
    agent=writer,
    expected_output="A draft of the research report with academic structure and citations."
)

edit_task = Task(
    description="Review, edit, and improve the written report for grammar, tone, and clarity.",
    agent=editor,
    expected_output="A polished, grammatically correct, and clear final draft."
)

supervise_task = Task(
    description="Review all stages—outline, research, writing, and editing—to ensure completeness and quality of the research paper.",
    agent=supervisor,
    expected_output="A concise supervision report detailing checks, feedback, and any required revisions."
)