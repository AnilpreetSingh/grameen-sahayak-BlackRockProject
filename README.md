# Grameen Sahayak: Phone-based Question Answering with ChatGPT

Grameen Sahayak is a cutting-edge phone-call based Hindi question answering system, leveraging the power of OpenAI's GPT 3.5 (ChatGPT).
This project won 3rd place in BlackRock BlackKnight Hackathon
## Use Case

Grameen Sahayak offers a seamless user experience through a hotline where users can verbally ask their questions. Our system promptly responds by sending SMS answers in Hindi to their registered phone numbers, typically within 20-30 seconds.

## How Our System Works

1. To initiate the process, users simply call a designated phone number and voice their questions.
2. Our system incorporates the "DriveSync" app on the Android device, automatically syncing call recordings to Google Drive.
3. Google Drive Windows App retrieves the call recordings to the local G: drive.
4. The heart of the system, the `run.py` Python script, is executed, initiating the `scrapeDrive.py` script.
5. `scrapeDrive.py` scans through the call recording folder, selecting the latest .mp3 recording and its associated phone number for processing.
6. The `Answering.py` script transcribes the .mp3 file into a .wav file, utilizing the Google Web Speech API via the `speech_recognizer` Python module.
7. Transcribed speech, now in Devanagri script, is then presented as a query to the OpenAI GPT 3.5 API.
8. GPT 3.5 responds in Hindi, and the answer is stored in the current folder as `response.txt`.
9. To deliver the response, the `twilio_call.py` script loads `response.txt` along with the phone number. Using the Twilio API, the response is sent back to the user's phone.

<img src="https://github.com/AnilpreetSingh/grameen-sahayak-BlackRockProject/assets/90110629/80b17638-7ddf-4b89-b0bb-963f86e3a0c5" width="500" alt="SMS ss">

## Installation and Usage

To set up and run Grameen Sahayak:

1. Install and configure DriveSync on your Android phone to synchronize call recordings with Google Drive (ensure call recording is enabled).
2. Install Google Drive on your server machine to access the synchronized call recordings.
3. Obtain API keys from OpenAI and Twilio (note that OpenAI's API is a paid service).
4. Install necessary Python modules using the following commands:
   ```bash
   pip install openai
   pip install SpeechRecognition
   pip install twilio
   pip install gTTS
   pip install soundfile
   
## Future Developments
We are committed to enhancing Grameen Sahayak's capabilities in the following ways:

1. Multiple Calls: Transitioning to Twilio's premium service to handle multiple calls simultaneously and record them on their servers.
2. Multilingual Support: Leveraging GPT 3.5/4's inherent multilingual capabilities, with modifications to automatically detect call languages and transcribe them.
3. Speech based call Response: Evolving from SMS to call-based responses using Google Web Speech API's human-like text-to-speech conversion. Note that Twilio requires audio files to be hosted on a public URL, necessitating a paid web hosting service.
> We're excited about the potential of Grameen Sahayak. Feel free to contibute to the code, reach out to me at asingh9_be20@thapar.edu
