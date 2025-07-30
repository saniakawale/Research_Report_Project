# Research_Report_Project


This project leverages **three AI frameworks** — **LangGraph**, **CrewAI**, and **Google ADK** — to orchestrate a multi-step research paper generation pipeline. The workflow consists of the following agents:

1. **Researcher**

   * Searches the web for academic material and gathers up-to-date, relevant resources.
2. **Outliner**

   * Creates a structured outline detailing what should be included in the research report.
   * Passes the finalized outline back into the Researcher for additional material dump.
3. **Writer**

   * Converts the research outline and gathered material into coherent, well-written paragraphs.
4. **Editor**

   * Edits the draft for grammar, style, and scientific clarity.
5. **Supervisor**

   * Reviews and approves each step, flagging any issues before finalizing the paper.

Each agent runs sequentially under a **SequentialAgent** orchestrator, managed by an **InMemoryRunner** for local execution without external hosting. The final assembled report is saved to `research_report.md`.

---

### Usage

1. Clone or navigate to this repository.
2. Install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the agent script:

   ```bash
   python multi_agent_research/agent.py
   ```
4. View the generated report:

   ```bash
   open research_report.md
   ```
