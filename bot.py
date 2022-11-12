import discord
import responses


async def send_message(username, message, user_message, is_private):
    try:
        response = responses.get_response(username, user_message)
        await message.author.send(response) if is_private else await message.channel.send(
            response)  # sends message to use privatly if its a private message or sends into channel if not
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA0MDY5MTMxNDA4MzI1NDI3Mg.GZP7B9.A5JSKcjFZB0gKGERNBWs5wOIJQb5TwmnG5k8p8'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event  #
    async def on_ready():  # triggers each time we run code when bot is ready to be used on server
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):  # takes in all the messages on the server
        if message.author == client.user:  # necessary. client.user is the bot and we want the bot to be client author
            return  # just return and ignore

        username = str(message.author)  # holds username
        user_message = str(message.content)  # make sure its a string holds user message
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        await send_message(username, message, user_message, is_private=False)

    client.run(TOKEN)
