import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '6240577285:AAHqH6Nbf3pIk6xsTex_reweasjbaftQrwk'
openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler()
async def send(message: types.Message):
    """
    Модель давинчи 3 для диалогов
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    await bot.send_message(message.chat.id, response.choices[0].text)


executor.start_polling(dp, skip_updates=True)
