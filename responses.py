import random


def get_response(username, message: str) -> str:
    p_message = message.lower()  # case sensitive

    if p_message == 'hello':
        return 'Hey there!'

    if message == 'roll':
        return str(random.randint(1, 6))

    if message.endswith('.png'):
        return 'Please do not post pictures in text chat'

    if message == '':
        return 'Please do not post pictures in text chat'


