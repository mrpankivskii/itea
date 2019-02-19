from telethon import TelegramClient, events, utils, sync


api_id = 719795
api_hash = '35575fe5979a42e3c6c550fe99c09278'


with TelegramClient('test', api_id, api_hash) as client:
    # Note that you can use 'me' or 'self' to message yourself
    client.send_message('me', 'Hello World from Telethon!')
    # .send_message's parse mode defaults to markdown, so you
    # can use **bold**, __italics__, [links](https://example.com), `code`,
    # and even [mentions](@username)/[mentions](tg://user?id=123456789)
    client.send_message('me', '**Using** __markdown__ `too`!')
    client.send_file('me', 'test.py')
    # The utils package has some goodies, like .get_display_name()
    for message in client.iter_messages('me', limit=10):
        print(utils.get_display_name(message.sender), message.message)
    # Dialogs are the conversations you have open
    for dialog in client.get_dialogs(limit=10):
        print(dialog.name, dialog.draft.text)
    # Default path is the working directory
    client.download_profile_photo('me')

