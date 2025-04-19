import requests

# Replace with your actual API key
api_key = "your_api_key"

# The URL for the text-to-speech API endpoint
url = "https://api.elevenlabs.io/v1/text-to-speech/voice_id"

# The text you want to convert to speech
text = "Hello world"

# The voice ID for the female voice you selected
voice_id = "selected_female_voice_id"

# Headers for the request
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Data payload for the request
data = {
    "text": text,
    "voice_settings": {
        "stability": 0.75,
        "similarity_boost": 0.75
    }
}

# Make the POST request to the API
response = requests.post(f"{url}/{voice_id}", headers=headers, json=data)

# Check the response
if response.status_code == 200:
    with open("output.wav", "wb") as audio_file:
        audio_file.write(response.content)
    print("Audio content saved to output.wav")
else:
    print(f"Failed to generate speech: {response.status_code} - {response.text}")