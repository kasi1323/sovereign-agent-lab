"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = [
    "check_pub_availability",
    "get_edinburgh_weather",
    "calculate_catering_cost",
    "generate_event_flyer",
]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

TASK_A_NOTES = "Used Qwen/Qwen3.5-397B-A17B model instead of default Llama-3.3-70B-Instruct for potentially better performance."   # optional — anything unexpected

# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = True   # True or False

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-7dbcde71-3499-4ce6-af8d-bd6ba0d193fc_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "  The Haymarket Vaults is confirmed for 160 guests tonight. Generate a promotional flyer with the theme 'Edinburgh AI Meetup, tech professionals, modern venue'."

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
The agent changes course after receiving the result for The Bow Bar, which shows it does not meet the requirements:
{"success": true, "pub_name": "The Bow Bar", "address": "80 West Bow, Edinburgh", "capacity": 80, "vegan": true, "status": "full", "meets_all_constraints": false}
This response indicates that the venue is both full and below the required capacity of 160 guests, meaning it fails to satisfy the constraints. As a result, the agent proceeds to check another venue (The Albanach) that can meet the requirements.
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
After checking all known venues, none meet the requirements for 300 guests with vegan options. The Albanach (capacity 180) and The Haymarket Vaults (capacity 160) are below the required capacity, The Guilford Arms does not provide vegan options, and The Bow Bar is both too small and full. Therefore, no suitable venue is available.
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = "No response is shown"

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
No. In a real booking assistant, simply stopping without responding would not be acceptable. Even if train times are out of scope, the assistant should clearly explain that limitation and either decline politely or direct the user to a more appropriate source instead of giving no answer at all.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent(agent)
        tools(tools)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent;
        agent -.-> __end__;
        agent -.-> tools;
        tools --> agent;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """
The LangGraph graph is just a simple loop where the agent and tools talk back and forth - the model decides everything on the fly. In contrast, Rasa's flows.yml spells out every possible path explicitly. The LLM just picks which flow to start, then Rasa follows the script. LangGraph is more flexible, while Rasa gives you predictable, auditable conversations.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
The agent executed all the tools perfectly - checking venues, getting weather, calculating costs, even generating a real flyer image - but then just stopped without summarizing anything. It gathered all this great information but never actually told me which venue worked or what the total cost would be. Like doing all the research but forgetting to write the conclusion.
"""
