from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pathlib import Path
from datetime import datetime
from .tools import get_secure_tools
from .callbacks import AgentSecurityLogger

def load_prompt(name: str) -> str:
    path = Path(__file__).parent.parent.parent / "prompts" / f"{name}.md"
    return path.read_text(encoding="utf-8").strip()


@CrewBase
class SecuredResearchCrew():
    """Phase 1 Secure Research Crew – security baked in"""

    agents = None
    tasks = None

    @agent
    def researcher(self) -> Agent:
        return Agent(
            role=load_prompt("researcher_role"),
            goal=load_prompt("researcher_goal"),
            backstory=load_prompt("researcher_backstory"),
            verbose=True,
            tools=get_secure_tools(),
            allow_delegation=False,
            max_iter=8,
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            role=load_prompt("analyst_role"),
            goal=load_prompt("analyst_goal"),
            backstory=load_prompt("analyst_backstory"),
            verbose=True,
            allow_delegation=False,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            description=load_prompt("research_task_description"),
            expected_output="Bullet list of 8–12 latest agentic security developments with OWASP ASI mapping",
            agent=self.researcher(),
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            description=load_prompt("reporting_task_description"),
            expected_output="Full professional Markdown report",
            agent=self.reporting_analyst(),
            output_file=str(Path(__file__).parent.parent.parent / "outputs" / "report.md"),
        )

    @crew
    def crew(self) -> Crew:
        global logger
        run_id = f"run_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"
        logger = AgentSecurityLogger(run_id)

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2,
            step_callback=logger.log,
            memory=True,
        )
