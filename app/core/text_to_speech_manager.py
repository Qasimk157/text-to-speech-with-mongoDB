from app.core.text_to_speech_manager_interface import ITextToSpeechManager
from app.database.text_to_speech_database import TextToSpeechDatabase
from app.models.logger import Logger
from app.models.text_to_speech.text_to_speech_request_payload import \
    TextToSpeechRequestPayload
from app.models.text_to_speech.text_to_speech_response_payload import \
    TextToSpeechResponsePayload
from text_to_speech import speak
from fastapi.encoders import jsonable_encoder
import pyttsx3

import gtts
from playsound import playsound
from interface import implements


class TextToSpeechManager(implements(ITextToSpeechManager)):
    def __init__(self):
        self.database = TextToSpeechDatabase()
        self.logger = Logger()

    async def create_by_tts(self, text_to_speech_request_paylad: TextToSpeechRequestPayload):
        
        create_text_to_speech_request = jsonable_encoder(
            text_to_speech_request_paylad)
        response = await self.database.create(create_text_to_speech_request)
        
        response["id"] = str(response["_id"])
        api_response = TextToSpeechResponsePayload(**response)
        print(type(api_response.enter_text))
        
        engine = pyttsx3.init()
        engine.setProperty('rate', 125)
        engine.setProperty('volume',1.0)  
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(api_response.enter_text)
        engine.save_to_file(api_response.enter_text, 'pyttsx.mp3')
        engine.runAndWait()
        engine.stop()
        
        api_response.id = response["id"]
        return api_response
    
    
    async def create_by_gTTS(self, text_to_speech_request_paylad: TextToSpeechRequestPayload):
        
        create_text_to_speech_request = jsonable_encoder(
            text_to_speech_request_paylad)
        response = await self.database.create(create_text_to_speech_request)
        
        response["id"] = str(response["_id"])
        api_response = TextToSpeechResponsePayload(**response)
        print(api_response.enter_text)

        tts = gtts.gTTS(api_response.enter_text, lang="en")
        tts.save("gtts.mp3")
        playsound("gtts.mp3")
        
        api_response.id = response["id"]
        return api_response
    
    
    
    async def create_text_to_speech(self, text_to_speech_request_paylad: TextToSpeechRequestPayload):
        
        create_text_to_speech_request = jsonable_encoder(
            text_to_speech_request_paylad)
        response = await self.database.create(create_text_to_speech_request)
        
        response["id"] = str(response["_id"])
        api_response = TextToSpeechResponsePayload(**response)
        print(api_response.enter_text)

        # speak(api_response.enter_text, "en", save=True, file="text-to-speech.mp3", speak=True)
        
        api_response.id = response["id"]
        return api_response
    
    
    
    async def create_by_ruth_tts(self, text_to_speech_request_paylad: TextToSpeechRequestPayload):
        
        create_text_to_speech_request = jsonable_encoder(
            text_to_speech_request_paylad)
        response = await self.database.create(create_text_to_speech_request)
        
        response["id"] = str(response["_id"])
        api_response = TextToSpeechResponsePayload(**response)
        print(api_response.enter_text)

        # from ruth_tts.api import Tts
        # converter = Tts("eastus", 'How are you doing', "gabby")
        # converter.convert("file_name.wav")
        
        api_response.id = response["id"]
        return api_response
