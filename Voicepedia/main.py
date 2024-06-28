from speech_totext import SpeechToText
from text_to_gpt import text, GPTQuery 
from text_to_speech import TextToSpeech
import ffmpeg
from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import tempfile


api_key = 'apikeyhehe'


# #////////////////////FASTAPI

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5555",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount('/static', StaticFiles(directory = 'web-page'), name='static')

@app.get("/")
async def health():
    return {"status": "ok"}


@app.post('/process_audio')
async def process_audio(audio: UploadFile):
    audio_bytes = await audio.read()

    # Define paths for the files
    ogg_file_path = "recorded_audio.ogg"
    wav_file_path = "output_file.wav"

    # Write bytes to an OGG file
    with open(ogg_file_path, "wb") as audio_file:
        audio_file.write(audio_bytes)
    print('Audio saved to OGG format.')

    # Convert OGG to WAV using ffmpeg
    ffmpeg.input(ogg_file_path).output(wav_file_path, y='-y').run(overwrite_output=True)
    print('Audio converted to WAV format.')

    # Speech to text
    Output_stt = SpeechToText().speech_recognition1(wav_file_path).string
    print(f"-User: {Output_stt}")
    print('Speech to text conversion complete.')

    #Text to gpt
    
    Output_gpt = GPTQuery(api_key).query(Output_stt)
    print(f"-GPT:{Output_gpt}")
    print('text to gpt working.')

    #Gpt to speech
    Output_speech = TextToSpeech().save_to_file(Output_gpt,"voice_output.wav")
    print('Gpt to speech: fine.')

    # Example usage:
    return FileResponse('web-page/index.html')

# # Configurar Jinja2 para manejar las plantillas HTML
# app.mount("/static", StaticFiles(directory="webpage"), name="static")
# templates = Jinja2Templates(directory="templates")

# # Ruta para mostrar el formulario HTML
# @app.get("/")
# async def read_form():
#     return {'message': 'Holamundo'}

# @app.get("/home")
# async def home():
#     return FileResponse('webpage/index.html')

# @app.get("/chat/{text}")
# def text_to_chatgpt(text: str, last_message: str = None):
#     last_message = GPTQuery(api_key).query(text)
#     return {'text': last_message}

# @app.get("/gpt/{text}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse(
#         request=request, name="item.html", context={"id": GPTQuery(api_key).query(text)}
#     )



# from pydub import AudioSegment
# @app.post('/process_audio')
# async def process_audio(audio: UploadFile = File(...)):
#     # Save the uploaded audio file temporarily
#     with tempfile.NamedTemporaryFile(delete=False) as tmp_audio:
#         tmp_audio.write(await audio.read())
#         tmp_audio_name = tmp_audio.name
    
#     # Load the audio file using pydub
#     audio_file = AudioSegment.from_file(tmp_audio_name)

#     # Calculate duration in seconds
#     duration_seconds = len(audio_file) / 1000  # Convert milliseconds to seconds

#     # Print the duration
#     print("Duration of the audio:", duration_seconds, "seconds")

#     # Process audio file using SpeechRecognition or other libraries
#     # Example: Convert speech to text
#     text = "Placeholder text: Speech to text processing goes here"

#     return text

