import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Voice IDs
korean_voice_id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_KO-KR_HEAMI_11.0'
english_voice_id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'  # Example English voice ID
japanese_voice_id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0'  # Placeholder, replace with actual ID


def is_korean(text):
    """Check if the text contains any Hangul syllables or letters."""
    for char in text:
        if '\uAC00' <= char <= '\uD7A3':  # Hangul Syllables range
            return True
        if '\u1100' <= char <= '\u11FF':  # Hangul Jamo range
            return True
        if '\u3130' <= char <= '\u318F':  # Hangul Compatibility Jamo range
            return True
        if '\uA960' <= char <= '\uA97F':  # Hangul Jamo Extended-A range
            return True
        if '\uD7B0' <= char <= '\uD7FF':  # Hangul Jamo Extended-B range
            return True
    return False


def is_english(text):
    """Check if the text contains any English alphabetic characters."""
    return any('A' <= char <= 'Z' or 'a' <= char <= 'z' for char in text)


def speak(text, voice_id=None):
    # Determine the language of the text
    if is_english(text):
        voice_id = english_voice_id
    elif is_korean(text):
        voice_id = korean_voice_id
    else:
        voice_id = japanese_voice_id

    # Set the voice based on detected language
    engine.setProperty('voice', voice_id)

    # Speak the text
    engine.say(text)
    engine.runAndWait()


# Example usage
speak("Hello")  # Will use English voice
speak("안녕하세요")  # Will use Korean voice
speak("こんにちは")  # Will use Japanese voice
