# Question 1 Answer

poem = """ Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.

When the blazing sun is set, and the grass with dew is wet. Then you show your little
light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
are.

Then the traveler in the dark thanks you for your tiny spark. How could he see where to
go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.

As your bright and tiny spark lights the traveler in the dark, though I know not what you
are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are.  """

print(poem)

# Question 2 Answer

multiple = (1,2,3,4,5,6,7,8,9,10)

multipied_by = int(input("Please choose a Number of which you want to know the table = "))

for m in multiple : 
    print(m*multipied_by)

# Question 3 Answer. I will install openai wisper for this question 

import os
import queue
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import whisper

# Audio settings
SAMPLE_RATE = 16000  # Whisper explicitly requires 16kHz audio
DURATION = 5         # Records in 5-second chunks
FILENAME = "temp_live_audio.wav"

print("📦 Loading Whisper model...")
model = whisper.load_model("base")
print("✅ Model loaded! Start speaking now...")

try:
    while True:
        print("\n🎤 Listening... for 5 second")
        # Record raw audio from microphone into a numpy array
        recording = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
        sd.wait()  # Wait until the 5-second recording finish
        
        # Save the recording to a temporary audio file
        write(FILENAME, SAMPLE_RATE, recording)
        
        # Run your original Whisper transcription code on the file
        result = model.transcribe(FILENAME, fp16=False) # fp16=False prevents CPU warnings
        text = result["text"].strip()
        
        # Only print if something meaningful was captured
        if text:
            print(f"🗣️ Transcribed: {text}")
            
except KeyboardInterrupt:
    print("\n👋 Stopping live transcription.")
finally:
    # Clean up the temporary file from your hard drive
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
