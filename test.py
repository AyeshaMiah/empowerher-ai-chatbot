from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6Ix5Z6KHLNfZk57UmsqRpTPTohy9TYICeNx9fxz3G_F2A"
)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Say Hello"
)

print(response.text)