from abc import ABC, abstractmethod

from telegram import Update
from telegram.ext import CallbackContext


class Handler(ABC):
    @abstractmethod
    def handle(self, update: Update, context: CallbackContext):
        pass
