import asyncio
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


@pytest.fixture
def run_async():
    return asyncio.run


@pytest.fixture
def user_schema():
    from app.models.user_schema import UserSchema

    now = datetime.now(timezone.utc)
    return UserSchema(
        id=1,
        name="Alice",
        email="alice@example.com",
        password="secret",
        created_at=now,
        updated_at=now,
    )
