"""Vercel FastAPI entrypoint."""

from api.serve import app as create_app

app = create_app()
