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

# from dotenv import load_dotenv
# load_dotenv()
# import os
# import google.generativeai as genai
# from langchain_google_genai import ChatGoogleGenerativeAI
# from crewai import Crew

# from agents import researcher, writer, outliner, editor, supervisor
# from tasks import outline_task, research_task, write_task, edit_task, supervise_task

# # ✅ Set up Gemini
# genai.configure(api_key=os.getenv("AIzaSyBHeqBtwDslD7kFXrfUDhk2r731DpQHzPg"))
# llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

# # ✅ Assign LLM to all agents
# for agent in [researcher, writer, outliner, editor, supervisor]:
#     agent.llm = llm

# # ✅ Create the crew
# crew = Crew(
#     agents=[researcher, writer, outliner, editor, supervisor],
#     tasks=[
#         outline_task,
#         research_task,
#         write_task,
#         edit_task,
#         supervise_task
#     ],
#     verbose=True
# )

# # ✅ Run the crew
# if __name__ == "__main__":
#     result = crew.kickoff()
#     print("\n\n✅ Final Report Output:\n")
#     print(result)