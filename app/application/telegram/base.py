import abc
from abc import abstractmethod

from telegram import Update
from telegram.ext import ContextTypes


class BaseTelegramHandler(abc.ABC):

    @abstractmethod
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: ...
