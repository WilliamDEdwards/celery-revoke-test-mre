pytest_plugins = ("celery.contrib.pytest",)
import pytest

@pytest.fixture(scope="session")
def celery_config() -> dict:
    return {
        "broker_url": "redis://:foobar@127.0.0.1:1432/1",
        "result_backend": "redis://:foobar@127.0.0.1:1432/0",
    }
