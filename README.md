# Grameen shayak call based ChatGPT
## grameen-sahayak is a phone-call based hindi question answering system, developed on top of OpenAi's GPT 3.5 (ChatGPT).
### Use case- 
Users can call the hotline and ask their questions by just verbally speaking the question, their questions are answered in the hindi via SMS sent to their phone number in only 20-30 seconds.
### How Our System Works- 
1. In the protoype, The user has to only call on a designated phone number and ask thier question.
2. We have installed _DriveSync_ app on the android phone where the call is made, it automatically pushes the call recording to _google drive_.
3. The call recording is automatically fetched by _Google Drive Windows App_ to G: drive.
4. Python script _run.py_ is run which first runs _scrapeDrive.py_.
5.  _scrapeDrive.py_ goes through all files in the folder with call recordings, fetches the latest .mp3 recording, its phone number and saves them in local folder.
6.  _Answering.py_ first converts the .mp3 file to .wav file that is then transcribed from speech to text with **Google Web speech API** using speech_recognizer python module.
7.  The transcribed speech (in Devanagri script) is then passed as a question to OpenAi's GPT 3.5 API (can be GPT 4 as well).
8.  GPT 3.5 answers the query in hindi and the answer text is saved in the current folder as response.txt.
9.  _twilio_call.py_ loads response.txt and the phone no., We use _Twilio API_ to message response to the phone number.


<img src="https://github.com/AnilpreetSingh/grameen-sahayak-BlackRockProject/assets/90110629/80b17638-7ddf-4b89-b0bb-963f86e3a0c5" width="500" alt="Description">

### How to Install and run-
  Install DriveSync app on android phone and sync call recordings with your google drive (make sure all calls are recorded by default)
  
  Install Google Drive on server machine
  
  Get API keys from OpenAI and Twilio (OpenAI API is paid)
  
  Install the following modules in pyhton environment
  
      pip install openai
      pip install SpeechRecognition
      pip install twilio
      pip install gTTS
      pip install soundfile
      
### Future -
  We aim to make the system multilingual, support multiple calls at the same time and get response as an incoming call.
  
  1. We aim to use twilio's paid version for a virtual phone number so that multiple calls will be picked up and recorded on their servers.    
    
  2. Multilingual support is easy to address as GPT 3.5/4 understands almost all languages, Google Text-to-speech API call needs to be modified to automatically detect the recording call language and transcribe it.
    
  3. We want to change the way of response from SMS to Call based, We can use Google Web speech API as it supports human-like text to speech conversion in multiple languages, but Twilio API requires the audio file to be hosted onto a public URL, for which we need a paid Web Hosting service.

  
  
  
