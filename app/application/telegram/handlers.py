from telegram import Update
from telegram.ext import ContextTypes

from app.application.telegram.base import BaseTelegramHandler


class Test(BaseTelegramHandler):

    async def handle(self) -> None:
        print('hello world')