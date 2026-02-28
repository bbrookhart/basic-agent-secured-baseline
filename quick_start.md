# 1. Clone & prepare environment
git clone https://github.com/YOUR_GITHUB_USERNAME/basic-agent-secured-baseline.git
cd basic-agent-secured-baseline

# 2. Install dependencies
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Set API keys (never commit them!)
cp .env.example .env
# → edit .env  (TAVILY_API_KEY=...)

# 4. Run the secured research crew
python src/secured_research_crew/main.py
