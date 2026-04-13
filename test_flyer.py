#!/usr/bin/env python3

import sys
sys.path.insert(0, '.')

from sovereign_agent.tools.venue_tools import generate_event_flyer

# Test the function
result = generate_event_flyer("The Albanach", 160, "AI Meetup, Edinburgh, professional")
print("Result:", result)

# Parse the JSON to check if it's working
import json
parsed = json.loads(result)
print("\nParsed result:")
print(f"Success: {parsed.get('success')}")
print(f"Error: {parsed.get('error', 'None')}")
print(f"Image URL: {parsed.get('image_url', 'None')}")
print(f"Prompt used: {parsed.get('prompt_used', 'None')}")

if "STUB" in str(parsed.get('error', '')):
    print("\n❌ Still contains STUB - implementation not working")
else:
    print("\n✅ STUB removed - implementation working!")
