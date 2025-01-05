from dataclasses import field, dataclass
from typing import Dict

from black.trans import defaultdict

from app.application.telegram.base import BaseTelegramHandler
from app.domain.mediators.base import BaseMediator, R


@dataclass
class ButtonMediator(BaseMediator):
    buttons_map: Dict[str, BaseTelegramHandler] = field(default_factory=lambda: defaultdict(object), kw_only=True)

    async def handle(self, query: str) -> R:
        await self.buttons_map[query].handle()

    def bind(self, query: str, handler: BaseTelegramHandler) -> None:
        self.buttons_map[query] = handler