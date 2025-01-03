from fastapi import FastAPI
from dataclasses import dataclass


@dataclass
class App:

    def setup(self, app: FastAPI) -> None:
        pass

    @property
    def app(self):
        app = FastAPI(title="Crypto Helper")
        self.setup(app)
        return app
