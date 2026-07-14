import json
from urllib.parse import parse_qs

from fastapi import Request


def from_urlencoded(body: bytes) -> dict:
    """Parse from application/x-www-form-urlencoded body."""
    return {k: v[0] for k, v in parse_qs(body.decode()).items()}


async def from_urlencoded_or_json(request: Request) -> dict:
    body = await request.body()
    content_type = request.headers.get("content-type", "")
    if "application/x-www-form-urlencoded" in content_type:
        parsed = from_urlencoded(body)
    else:
        parsed = json.loads(body)
    return parsed
