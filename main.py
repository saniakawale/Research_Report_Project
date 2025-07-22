from crewai import Crew, Process
from agents import researcher, writer, outliner, editor, supervisor
from tasks import outline_task, research_task, write_task, edit_task, supervise_task

crew = Crew(
    agents=[outliner, researcher, writer, editor, supervisor],
    tasks=[outline_task, research_task, write_task, edit_task, supervise_task],
    process=Process.sequential
)

if __name__ == "__main__":
    final_result = crew.kickoff()
    result_text = str(final_result)
    print("\n Final Output:\n")
    print(result_text)

with open("final_output.md", "w") as f:
    f.write(result_text)