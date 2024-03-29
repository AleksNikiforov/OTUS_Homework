from fastapi import FastAPI, Response
from views.ping import router as ping_router

app = FastAPI()

app.include_router(ping_router)
