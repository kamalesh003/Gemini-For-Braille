# GEMINI FOR BRAILLE


**Connect to Gemini AI API:**

Refer this Link: https://colab.research.google.com/notebooks/snippets/gemini.ipynb

CREATE AND USE YOUR OWN GEMINI-AI API IN 'app.py'

# Braille Ready Format:

* The BRF (Braille Ready Format) file format is specifically designed for storing Braille text content digitally. 
* It typically consists of Unicode Braille characters encoded in UTF-8 or another compatible encoding. 
* BRF files are used to facilitate the distribution and accessibility of Braille documents, allowing visually impaired individuals to read and interact with text through Braille displays or embossers.

**Key characteristics of BRF files include:**

**Text Representation:** BRF files encode Braille characters using Unicode Braille patterns, allowing for accurate representation of Braille text.

**Accessibility:** They enable the distribution of Braille documents in a format compatible with Braille embossers and displays, ensuring accessibility for visually impaired users.

**File Structure:** BRF files are often plain text files (.brf extension) that can be opened and edited using text editors or specialized Braille software.

**Usage:** BRF files are commonly used to archive, share, and produce Braille documents efficiently, maintaining consistency in Braille representation across different devices and platforms.


# BACKEND:

**Backend Flask Application for AI-Powered Braille Conversion**

This Flask application provides a backend service for converting voice commands into Braille using a Generative AI model. 
It utilizes the Google Generative AI SDK for text generation and supports voice input through a simple HTML interface.

**Features:**

* Converts voice commands to spoken responses using a Generative AI model.

* Converts spoken responses into Braille text format.

* Stores user requests and responses locally in separate folders.

**Prerequisites:**

Before running the application, ensure you have the following installed:

* Python (version 3.x recommended)

* Flask framework (pip install Flask)

* Google Generative AI SDK (pip install google-generativeai)

**Usage:**

* Enter manual typed input (or) voice commands in the provided text field and submit.

* The application will generate a spoken response and convert it into Braille.

* Stored responses can be found in the **actual_responses** and **brf_characters** folders.

**Folder Structure:**

* **actual_responses/:** Stores text files containing user requests and spoken responses.
* **brf_characters/:** Stores Braille responses in BRF format.

# FRONTEND:

## Features:

1.)Allows users to input voice or text commands.

2.)Generates spoken responses using Generative AI and converts them into Braille.

3.)Provides a button to download the Braille response in BRF format.

## Voice Input:

* Click **Start Listening (F1) or press F1** to start recording voice input.

* Speak into your microphone. The recognized text will appear in the input field.

## Text Input:

* Alternatively, type directly into the Voice or Text Input field.

## Submit Input:

* Click **Submit (F2) or press F2** to submit the input.

## Braille Response:

* The converted Braille response will appear below the input field.

* Click **Download BRF (F3) or press F3** to download the Braille response as a **.brf** file.

## Integration with Backend:

* Ensure the Flask backend is running (python app.py) before using this interface.

* The backend processes input via **/process_voice_input** endpoint and returns the Braille response in JSON format.

# Empowering Education and Accessibility

Empowering professionals to create accessible educational content and enabling blind individuals to engage actively in learning:

* Effortless Content Creation: Quickly convert educational materials into Braille.
* Interactive Learning: Access content through voice or text input, tailored to individual needs.
* Reliable Translations: AI ensures accurate Braille conversion, maintaining content fidelity.
* Inclusive Education: Promotes independent learning for blind students, fostering inclusivity.
* Professional Impact: Enhances teaching capabilities and supports inclusive practices.


