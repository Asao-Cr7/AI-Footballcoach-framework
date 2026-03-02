import os
import google.generativeai as genai
from dotenv import load_dotenv
# This imports your modular prompt pieces from your other file
from prompts import (
    SYSTEM_ROLE,
    INTERACTION_FLOW,
    COACH_LOGIC_FRAMEWORK,
    SESSION_TEMPLATE,
    ADAPTIVE_OPTIONS
)

# 1. Setup & Security
load_dotenv() # Loads your API key from a private .env file
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class FootballSessionGenerator:
    def __init__(self):
        # We combine your modular architecture into one Master System Prompt
        self.master_prompt = f"{SYSTEM_ROLE}\n{INTERACTION_FLOW}\n{COACH_LOGIC_FRAMEWORK}\n{SESSION_TEMPLATE}\n{ADAPTIVE_OPTIONS}"
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_session(self, age_group, skill, player_count):
        """
        Sends the user inputs to Gemini using the modular prompt architecture.
        """
        user_input = f"Age: {age_group}, Skill: {skill}, Players: {player_count}"
        
        # We send the system instructions first, then the user's specific data
        response = self.model.generate_content([self.master_prompt, user_input])
        return response.text

# Simple test block for recruiters to see it works
if __name__ == "__main__":
    generator = FootballSessionGenerator()
    # Mocking a user response to the "Flipped Interaction"
    print(generator.generate_session("U10", "Dribbling", "12"))
