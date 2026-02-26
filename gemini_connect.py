from google import genai

# Initialize client
client = genai.Client(api_key="AIzaSyApv1Ed8s5LZg34Z4_ipdsWZD27zU6VDw0")

def create_prompt(income, rent, travel, food, shopping):
    prompt = f"""
    You are a financial AI.
    Monthly Income: {income}
    Rent: {rent}
    Travel: {travel}
    Food: {food}
    Shopping: {shopping}

    Generate a detailed budget plan, total expenses, savings, and money-saving suggestions.
    """
    return prompt

def get_response(prompt):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[prompt]   # IMPORTANT: use a list
    )
    return response.candidates[0].content.parts[0].text

# -------------------------
# Example input
# -------------------------

income = 50000
rent = 12000
travel = 3000
food = 6000
shopping = 4000

prompt = create_prompt(income, rent, travel, food, shopping)
response = get_response(prompt)

print("\n--- AI Budget Plan ---\n")
print(response)