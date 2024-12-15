import sys
import logging
import asyncio

from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import Message, BotCommand
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from req import parsLink


load_dotenv()


bot = Bot(token=getenv('API_TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML)) 
dp = Dispatcher()

@dp.message(Command(commands='start'))
async def start_bot(message: Message) -> None:
    await message.answer(f'Hello, {message.from_user.full_name}!')


@dp.message(Command(commands='info'))
async def about_bot(message: Message) -> None:
    await message.answer('Этот бот создан, чтобы помогать вам находить и поддерживать надёжные благотворительные организации. ' + 
                         'Мир благотворительности порой сложно разобрать. ' +
                         'Этот бот упрощает процесс, предоставляя список организаций, которым можно доверять,' +
                         'чтобы ваши пожертвования точно оказали помощь тем, кто в этом нуждается.')


@dp.message(Command(commands='orgs'))
async def print_orgs(message: Message) -> None:
     fonds = parsLink()
    
     for fond in fonds:
         await message.answer(f'<a href="{fond}"> {fond.split('/')[-2]} </a>')


async def setup_bot_commands():
    bot_commands = [
        BotCommand(command='/start', description='Start'),
        BotCommand(command='/info', description='Информация о боте'),
        BotCommand(command='/orgs', description='Список благотворителных фондов')
    ]
    await bot.set_my_commands(bot_commands)


async def main() -> None:
    await setup_bot_commands()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

    