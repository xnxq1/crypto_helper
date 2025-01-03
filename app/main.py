from app.application.app import App
from app.di import create_di

container = create_di()
app = container.resolve(App).app