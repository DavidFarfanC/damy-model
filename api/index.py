"""Vercel serverless entrypoint for the FastAPI application."""

from __future__ import annotations

from api.serve import app as create_app

try:
    app = create_app()
except Exception:  # pragma: no cover - runtime diagnostics
    import traceback
    import sys

    print("[vercel] Failed to initialize FastAPI application:", file=sys.stderr)
    traceback.print_exc()
    raise
