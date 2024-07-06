from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from datetime import datetime
import speech_recognition as sr

app = Flask(__name__)

# Set your API key as an environment variable
os.environ['GOOGLE_API_KEY'] = 'AIzaSyB8D2UZJ5uapoygIVy9E286K73Yjk8HzR4'

# Retrieve your API key from the environment variable
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure the Generative AI SDK with your API key
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to create folders if they don't exist
def create_folders():
    # Folder for actual responses
    actual_responses_folder = 'actual_responses'
    if not os.path.exists(actual_responses_folder):
        os.makedirs(actual_responses_folder)
        print(f"Folder '{actual_responses_folder}' created.")

    # Folder for BRF characters with metadata
    brf_characters_folder = 'brf_characters'
    if not os.path.exists(brf_characters_folder):
        os.makedirs(brf_characters_folder)
        print(f"Folder '{brf_characters_folder}' created.")

# Function to generate response
def generate_response(input_text):
    try:
        response = model.generate_content(input_text)
        if response.candidates:
            generated_text = response.candidates[0].content.parts[0].text
            return generated_text.replace("**", "")  # Remove '**' markers from generated text
        else:
            return "No response found"
    except Exception as e:
        print(f"Error occurred: {e}")
        return "Error: Failed to generate response"

# Function to convert text to Braille
def text_to_braille(input_text):
    braille_text = ""
    for char in input_text:
        if char.isalpha():
            braille_text += chr(ord(char.upper()) + 0x2800)  # Convert alphabetic characters to Braille
        elif char.isdigit():
            braille_text += chr(ord(char) + 0x2800)  # Convert digits to Braille
        elif char == ' ':
            braille_text += ' '  # Preserve spaces
        else:
            braille_text += char  # Preserve non-alphanumeric characters as-is
    return braille_text

# Function to store request and responses
def store_request_response(request, spoken_response, braille_response):
    try:
        # Store request and spoken response in actual_responses folder
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(f'actual_responses/{timestamp}_response.txt', 'w', encoding='utf-8') as file:
            file.write(f"Request: {request}\n")
            file.write(f"Spoken Response: {spoken_response}\n")

        # Store Braille response in brf_characters folder as a .brf file
        with open(f'brf_characters/{timestamp}_braille.brf', 'w', encoding='utf-8') as file:
            file.write(braille_response)  # Write the Braille response directly as BRF content

        print(f"Stored request and Braille response for '{request}' successfully.")
    except Exception as e:
        print(f"Error occurred while storing response: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_voice_input', methods=['POST'])
def process_voice_input():
    try:
        voice_command = request.form['voice_input']
        if not voice_command:
            return jsonify({"error": "Voice command cannot be empty"}), 400

        # Generate spoken response
        spoken_response = generate_response(voice_command)

        # Convert spoken response to Braille
        braille_response = text_to_braille(spoken_response)

        # Store request and responses
        store_request_response(voice_command, spoken_response, braille_response)

        return jsonify({"braille_response": braille_response})
    except Exception as e:
        print(f"Error occurred during processing: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    create_folders()
    app.run(debug=True)
