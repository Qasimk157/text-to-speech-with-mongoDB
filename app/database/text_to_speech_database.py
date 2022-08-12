import asyncio

from app.config.config import DATABASE_NAME, MONGODB_CON_STR
from app.database.text_to_speech_database_interface import \
    ITextToSpeechDatabase
from app.models.text_to_speech.text_to_speech_request_payload import \
    TextToSpeechRequestPayload
from fastapi.encoders import jsonable_encoder
from interface import implements
from motor.motor_asyncio import AsyncIOMotorClient


class TextToSpeechDatabase(implements(ITextToSpeechDatabase)):
    client = AsyncIOMotorClient(MONGODB_CON_STR)
    client.get_io_loop = asyncio.get_running_loop
    text_to_speech_collection = client[DATABASE_NAME]["text_to_speech"]
    category_history_collection = client[DATABASE_NAME]["history_text_to_speech"]

    async def create(self, text_to_speech_request_paylad: TextToSpeechRequestPayload):
        document = jsonable_encoder(text_to_speech_request_paylad)
        result = await self.text_to_speech_collection.insert_one(document)
        document["_id"] = result.inserted_id
        return document
