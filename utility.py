from google import genai

api_key = "AQ.Ab8RN6IHpNcfdEqYxm1E-iXFLx14Va41fTJ6mdPyE0VJH8P6Pw"

#step 1 : authentication

client = genai.Client(api_key=api_key)

prompt = "what is ai agent in simple words"

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

print(response.text)