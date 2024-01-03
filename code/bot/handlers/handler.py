from abc import abstractmethod, ABC

from telegram import Update
from telegram.ext import CallbackContext


class Handler(ABC):
    @abstractmethod
    async def handle(self, update: Update, context: CallbackContext):
        pass
