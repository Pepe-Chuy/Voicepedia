import pyttsx3

class TextToSpeech():
    def __init__(self) -> None:
        self.engine = pyttsx3.init()

        # Adjust properties for a more natural voice
        self.engine.setProperty('rate', 150)  # Speed of speech (words per minute)
        self.engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
        self.engine.setProperty('voice', self.engine.getProperty('voices')[1].id)  # English voice index is 1 by default

    # Speak the text
    def speak(self, text, language=1):
        self.engine.setProperty('voice', self.engine.getProperty('voices')[language].id)  # Set voice based on language index
        self.engine.say(text)
        self.engine.runAndWait()

    # Save the text to a WAV file
    def save_to_file(self, text, filename, language=1):
        self.engine.setProperty('voice', self.engine.getProperty('voices')[language].id)  # Set voice based on language index
        self.engine.save_to_file(text, filename)  # Save speech to WAV file
        self.engine.runAndWait()