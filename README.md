# Аiober

**A**sync**IO**
      vi**BER** – Python library for easy creation of Viber bots
*Currently, Viber bots can only be works using webhooks.*


### Introduction
...

## Let's get started !

### Installing
Creating a viber bot is easy !
1. Install the library with `pip install git+https://github.com/QuaronSoftware/aiober.git` or using git
2. From aiober import Bot and Dispatcher to your projects
3. Build a simple script like in **Example**
4. Make viber bot [here](https://partners.viber.com/account/create-bot-account)
5. Using ngrok make your address global (for webhooks)
6. Run your script
7. Open Postman and make post request to https://chatapi.viber.com/pa/set_webhook with data `{"url":"https://your-domain/update, "auth_token": "auth-token"}` for set webhook to viber bot
**Good, webhook is registred !**

## Example

### Simple echo bot
```python
import asyncio

from aiober import Bot, Dispatcher
from aiober.types import Message

bot = Bot('auth-token')
dp = Dispatcher(bot=bot)

# router
@dp.messages()
async def echo(message: Message):
    await message.copy_to(message.sender.id)


async def main():

    # start webhook
    await dp.start_webhook(
        host='127.0.0.1',
        port=8000,
        path='/update'
    )

asyncio.run(main())
```