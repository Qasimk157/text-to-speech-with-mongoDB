
from abc import abstractmethod

from app.models.text_to_speech.text_to_speech_request_payload import \
    TextToSpeechRequestPayload
from interface import Interface


class ITextToSpeechManager(Interface):
    @abstractmethod
    async def create_by_tts(self, text_to_speech_request_paylad: TextToSpeechRequestPayload):
        pass
    
    @abstractmethod
    async def create_text_to_speech(self, text_to_speech_request_paylad: TextToSpeechRequestPayload):
        pass
    
    @abstractmethod
    async def create_by_ruth_tts(self, text_to_speech_request_paylad: TextToSpeechRequestPayload):
        pass
    
    @abstractmethod
    async def create_by_tts(self, text_to_speech_request_paylad: TextToSpeechRequestPayload):
        pass

