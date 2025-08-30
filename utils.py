from backend import generate_audio

# Example text
text = "Hello! Welcome to Echoverse."

# Generate speech
output_file = generate_audio(text)

print(f"Audio saved to {output_file}")

