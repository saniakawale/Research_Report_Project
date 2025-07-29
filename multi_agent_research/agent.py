import asyncio
from google.adk.agents import Agent, SequentialAgent
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.genai import types


# Researcher Agent: Searches the web
researcher_agent = Agent(
    name="researcher",
    model="gemini-2.0-flash",
    description="Searches the web for academic material",
    instruction="Find up-to-date, relevant resources using web search.",
    tools=[google_search]
)

# Outliner Agent
outliner_agent = Agent(
    name="outliner",
    model="gemini-2.0-flash",
    description="Creates a structured outline for the research report",
    instruction="Organize the research findings into a logical outline for a research paper."
)

# Writer Agent
writer_agent = Agent(
    name="writer",
    model="gemini-2.0-flash",
    description="Drafts research paper sections based on the outline and research dumps",
    instruction="Convert research outline and findings into well-written paragraphs."
)

# Editor Agent
editor_agent = Agent(
    name="editor",
    model="gemini-2.0-flash",
    description="Edits for grammar, style, and scientific clarity",
    instruction="Check and improve grammar, clarity, and style for academic writing."
)

# Supervisor Agent
supervisor_agent = Agent(
    name="supervisor",
    model="gemini-2.0-flash",
    description="Reviews and approves each step before finalizing the paper",
    instruction="Read the outputs from each agent and flag any issues before approving."
)

# Combine into a SequentialAgent
multi_agent_system = SequentialAgent(
    name="research_paper_helper",
    sub_agents=[
        researcher_agent,
        outliner_agent,
        writer_agent,
        editor_agent,
        supervisor_agent
    ]
)

# Set up InMemoryRunner and session

runner = InMemoryRunner(
    agent=multi_agent_system,
    app_name="research_paper_app"
)

session = asyncio.run(
    runner.session_service.create_session(
        app_name="research_paper_app",
        user_id="user"
    )
)

# Prompt and invoke

prompt = "Investigate the latest advances in transformer architectures for NLP."

# Build a Content with Part(text=…) instead of the broken from_text helper
content = types.Content(
    role="user",
    parts=[ types.Part(text=prompt) ]
)

# Run the agent chain, collecting text chunks
full_text = []
for event in runner.run(
    user_id="user",
    session_id=session.id,
    new_message=content
):
    if event.content.parts:
        chunk = event.content.parts[0].text
        full_text.append(chunk)

# Write to Markdown file

output = "\n\n".join(full_text)
with open("research_report.md", "w", encoding="utf-8") as f:
    f.write(output)

print("Research report written!")
