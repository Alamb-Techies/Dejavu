import requests
from decouple import config

class TelegramBot():

    def __init__(self) -> None:
        self.bot_token = config('TELEGRAM_BOT_TOKEN')
        self.bot_chatID = config('TELEGRAM_CHAT_ID')
        
    
    def send(self, data:str) -> None:
        bot_token = self.bot_token
        bot_chatID = self.bot_chatID
        bot_message = str(data)
        send =  'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        
        response =  requests.get(send)
        return response.json()


if __name__ == "__main__":
    TelegramBot.test("What's up?")  