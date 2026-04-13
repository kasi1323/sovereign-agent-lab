"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  calling to confirm a booking                                                           
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                            
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                                                                   
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £200 deposit                                                                           
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  calling to confirm a booking                                                           
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                             
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                                                                    
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £500 deposit                                                                           
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "a deposit of £500 exceeds the organiser's authorised limit of £300"   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  calling to confirm a booking                                                           
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                             
And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?                                              
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
After the out-of-scope parking question, CALM recognised that the user had moved away from the booking-confirmation flow. It gave a fallback response explaining that it can only help confirm tonight's venue booking, then asked whether the user wanted to continue the confirm booking flow.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
In Exercise 2 Scenario 3, the LangGraph agent did not call any tools, but it also did not really help because no response was shown. That would feel confusing in a real booking assistant, since the user would not know what happened.
Rasa CALM handled the same kind of situation more clearly. When I asked about parking, it said that was outside its scope, explained that it could only help with confirming the venue booking, and then asked if I wanted to continue the booking flow.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I tested it by temporarily setting 'now' to 5:00 PM with
'datetime.datetime.now().replace(hour=17, minute=0)', instead of changing the
condition to always be true. Then I restarted the action server and ran the
booking flow again. The bot escalated instead of confirming the booking, which
showed the cutoff guard was working. After testing, I changed 'now' back to the
real current time.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
CALM reduces the amount of code I have to write because the LLM can understand normal user messages and fill the slots from them. Instead of writing a form validator with regex for every possible way someone might say the guest count or deposit, I can describe the flow and let llm extract the values. The downside is that this part is less exact than plain Python, so I would not want the LLM making the final business decision. I still trust Python more for hard rules like maximum capacity, deposit approval, vegan meal ratio, and the 16:45 cutoff, because those checks need to be consistent every time.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
The extra CALM setup gives the bot a much narrower and more controlled job. Unlike LangGraph, it cannot just decide to branch into a new task, call an undefined tool, check weather, or make a flyer because the user asked for it. That would be a weakness for a general assistant, but it is useful here. For a booking confirmation call, I want the assistant to stay on the agreed process, collect the required details, apply the business rules, and avoid drifting into things it is not supposed to handle.
"""
