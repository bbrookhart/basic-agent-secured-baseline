from secured_research_crew.crew import SecuredResearchCrew
from dotenv import load_dotenv

load_dotenv()

def run():
    inputs = {
        "topic": "Latest agentic AI security developments February 2026"
    }
    result = SecuredResearchCrew().crew().kickoff(inputs=inputs)
    print("\nFinal Result:\n")
    print(result)

if __name__ == "__main__":
    run()
