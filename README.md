# Voice-Enabled ChatGPT  

This project extends ChatGPT's functionality by providing voice access, enabling use by a wider range of individuals, such as the elderly, visually impaired, and others who benefit from voice interaction.  

## Features  

- **Voice-to-Text Conversion**: Uses the Google Web Speech API to record voice input on a webpage and convert it into text.  
- **ChatGPT Integration**: The converted text is sent to ChatGPT via the GPT API for generating responses.  
- **Text-to-Speech Output**: Leverages the `pyttsx3` library to convert ChatGPT's responses into speech, providing a fully voice-enabled interaction.  
- **Webpage Interface**: A user-friendly HTML-based webpage built with JavaScript for handling file exchanges between components and displaying outputs seamlessly.  

## Pipeline Overview  

1. **Voice Input**:  
   - The Google Web Speech API captures voice input directly from the browser.  
   - Converts voice into text and sends it to the ChatGPT API for processing.  

2. **ChatGPT Processing**:  
   - The text is processed by ChatGPT to generate a meaningful response.  

3. **Voice Output**:  
   - The response is converted back into speech using the `pyttsx3` library, making the interaction accessible to users who prefer or require auditory output.  

## Benefits  

This project aims to enhance accessibility by bridging the gap between text-based AI and users who may have difficulty reading or typing. By integrating voice capabilities, it ensures a broader audience can benefit from AI technology.  

## Technologies Used  

- **Google Web Speech API**: For voice-to-text conversion.  
- **ChatGPT API**: For generating intelligent responses.  
- **pyttsx3**: For text-to-speech conversion.  
- **HTML & JavaScript**: To build the interactive webpage interface and handle data exchange.  

## Getting Started  

### Prerequisites  

- Python 3.x  
- `pyttsx3` library (`pip install pyttsx3`)  
- A web browser with Google Web Speech API support  
- A GPT API key (available from OpenAI)  

### Installation  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-repository.git  
   cd your-repository  
   ```  

2. Install required Python libraries:  
   ```bash  
   pip install pyttsx3  
   ```  

3. Set up your GPT API key in the appropriate configuration file or environment variable.  

4. Open the `index.html` file in your preferred browser.  

### Usage  

1. Navigate to the webpage interface.  
2. Click the **Record** button to provide voice input.  
3. The text output from ChatGPT will appear on the page and will also be read aloud using the text-to-speech system.  

## Contributions  

Contributions are welcome! If you’d like to enhance the project or fix issues, feel free to submit a pull request.  

## License  

This project is licensed under the [MIT License](LICENSE).  

---  

Let me know if you'd like further tweaks!
