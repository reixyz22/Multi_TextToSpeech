import os
from dotenv import load_dotenv  # pip install python-dotenv

from twitch_bot import TwitchBot


# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build


def main():
    load_dotenv()  # Load environment variables from .env
    # TWITCH
    username = os.getenv('TWITCH_USERNAME')
    channel = os.getenv('TWITCH_CHANNEL')
    token = os.getenv('TWITCH_TOKEN')  # Make sure your .env file has TOKEN defined via https://twitchapps.com/tmi/

    twitch = TwitchBot(username, token, channel)
    twitch.start()

    # YOUTUBE
    '''
    CLIENT_ID = os.getenv('YOUTUBE_CLIENT_ID')
    CLIENT_SECRET = os.getenv('YOUTUBE_CLIENT_SECRET')
    SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secrets.json',
        SCOPES)
    credentials = flow.run_local_server(port=0)
    youtube = build('youtube', 'v3', credentials=credentials)

    request = youtube.liveChatMessages().list(
        liveChatId='YOUR_LIVE_CHAT_ID',
        part='snippet,authorDetails'
    )
    response = request.execute()
    print(response)
    '''


if __name__ == "__main__":
    main()
