import requests
from decouple import config

class TelegramBot():

    def __init__(self, data:str) -> None:
        self.bot_token = config('TELEGRAM_BOT_TOKEN')
        self.bot_chatID = config('TELEGRAM_CHAT_ID')
        self.bot_message = self.data
    
    def test(data:str) -> None:
        bot_token = config('TELEGRAM_BOT_TOKEN')
        bot_chatID = config('TELEGRAM_CHAT_ID')
        bot_message = data
        send =  'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        
        response =  requests.get(send)
        print(response.json())


if __name__ == "__main__":
    TelegramBot.test("What's up?")  