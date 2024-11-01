import irc.bot
from text_to_speech import speak


class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, token, channel):
        self.token = token
        self.channel = '#' + channel
        server = 'irc.chat.twitch.tv'
        port = 6667
        print(f'Connecting to {server} on port {port}...')
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, token)], username, username)

    def on_welcome(self, c, e):
        print(f'Joining {self.channel}')
        c.join(self.channel)

    @staticmethod
    def on_pubmsg(c, e):
        sender = e.source.nick
        message = e.arguments[0]
        speak(f'Message from {sender}: {message}')