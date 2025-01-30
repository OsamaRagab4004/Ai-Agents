
import os
from openai import OpenAI


client = OpenAI(
        api_key=os.getenv("API_KEY"),
        )
response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input="""
        The optimal solution for storing JSON in a database depends on your specific use case:

    For simple, infrequently queried JSON data, storing it as a string in a TEXT field might be sufficient.
    For more complex use cases, where querying specific fields inside the JSON is important, use databases with native JSON support like PostgreSQL or MySQL.
    For structured, highly queried data, decomposing JSON into relational tables or using a hybrid approach will give you the best performance and flexibility.""",
    )
response.stream_to_file("output.mp3")