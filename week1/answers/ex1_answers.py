"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
For all three data formats, the model was able to correctly identify the venue.but differed in which valid venue they selected. When multiple answers satisfy constraints, LLMs do not have a stable selection rule.The output depends on how the input format nudges the model’s reasoning style.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
Even after adding the toughest near-miss options, the model still does a good job checking all the conditions and doesn’t get tricked into picking the wrong venues. The tricky part isn’t filtering it’s that there are still multiple correct answers. Because of that, the model’s final choice changes depending on how the data is presented. In structured formats, it tends to pick the first valid option it sees, while in plain text it sometimes lands on a later one. So the difference isn’t about the model getting confused it’s just using different ways to choose between equally valid options.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
In Part C, the smaller model basically stopped reacting to how the data was formatted. No matter whether the input was plain text, XML, or sandwich-style, it kept giving the same answer.That suggests it isn’t really adjusting its reasoning based on structure. Instead, it’s likely relying on simpler shortcuts like picking something that stands out more or appears later in the list(recency) rather than carefully going through each option step by step.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the task is a bit tricky and the model is actually capable of using that structure. If there are multiple conditions or very similar options, a clear format can help guide the model and keep it from getting confused. But this really shows up with larger models, since they can adjust how they reason based on the format. Smaller models, on the other hand, often stick to simpler shortcuts, so changing the format doesn’t affect them as much.
"""
