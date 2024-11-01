import pyttsx3


def list_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        print(f"Voice ID: {voice.id}")
        print(f"Name: {voice.name}")
        print(f"Languages: {voice.languages}")
        print(f"Gender: {voice.gender}")
        print(f"Age: {voice.age}")
        print("-" * 30)


list_voices()
