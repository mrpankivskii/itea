from telethon import TelegramClient, events, utils


def telegram_client():

    api_id = 719795
    api_hash = '35575fe5979a42e3c6c550fe99c09278'

    client = TelegramClient('test', api_id, api_hash).start()
    #
    # messages = client.get_messages('me')
    # messages[0].download_media()

    # #Відстежування чату
    # @client.on(events.NewMessage(chats=('Остап Т')))
    # async def normal_handler(event):
    #     #print(event.message)
    #     if event.message.to_dict()['message']:
    #         print(event.message.to_dict()['message'])
    #     else:
    #         image = event.message.to_dict()['media']['photo']['file_reference']
    #         image.decode('utf-8')
    #         print(image)
    #         print('image')
    # client.run_until_disconnected()
    #print(client.get_me().stringify())                #-інформація про акаунт
    #client.send_message('me', 'тест Української')     #-надіслати повідомлення
    #client.download_profile_photo('me')               #-загрузити аву
    #for dialog in client.iter_dialogs():
    #    print(dialog.title)                            #-вивести всі чати
    #messages = client.get_entity('Пошта-ССПЗ-ЦІТ')
    #print(messages)


if __name__ == "__main__":
    telegram_client()
#api_id - 719795
#api_hash - 35575fe5979a42e3c6c550fe99c09278