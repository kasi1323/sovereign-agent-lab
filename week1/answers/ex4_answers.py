"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Albanach"
QUERY_1_VENUE_ADDRESS = "2 Hunter Square, Edinburgh"
QUERY_2_FINAL_ANSWER  = "No available Edinburgh venue matches those requirements."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
After I changed The Albanach from available to full in the MCP venue server, the same client query returned a different best match. Before the change, search_venues returned both The Albanach and The Haymarket Vaults, so the agent picked The Albanach. After the change, The Albanach was filtered out and only The Haymarket Vaults matched. I did not need to change the LangGraph client, because it discovered and called the same MCP tools.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 4   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 0   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP is useful because the agent does not need to know the tool code directly. It can connect to the server, discover what tools are available, and call them through the same interface. In this exercise, the venue data changed on the MCP server side and the client still worked. That feels better than copying the same tool functions into every agent, because one shared tool layer can serve different clients.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- The LangGraph research agent would handle open-ended venue research because it can decide which tools to call, react when a venue is unavailable, and change direction as it learns more.
- The Rasa CALM call agent would handle booking confirmation calls because the conversation needs a fixed process, clear boundaries, and business rules that the LLM cannot override.
- The MCP venue server would act as the shared tool layer because both the research agent and the call agent should use the same venue data and search logic.
- The vector store and CLAUDE.md memory layer would store past context because the agent should remember previous venue choices, preferences, and failed checks across sessions.
- The Python business-rule actions would enforce constraints like capacity, deposit amount, vegan ratio, and cutoff time because those decisions need to be predictable every time.
- The LangSmith observability layer would track traces, token costs, tool latency, and failures because a real agent needs to be debugged and monitored after it is running.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
I would use LangGraph for the research work and Rasa CALM for the phone-style confirmation call. LangGraph fits research because it can choose tools and change direction, like in Exercise 2 when The Bow Bar did not meet the requirements and the agent moved on to another venue. Rasa CALM fits the call because in my run it collected 160 guests, about 50 vegan meals, and a £200 deposit in a fixed flow. When I asked about parking, it did not try to solve that side request; it said it was out of scope and asked whether I wanted to continue. Swapping them feels wrong because research needs flexibility, while confirmation needs boundaries and predictable rules.
"""
