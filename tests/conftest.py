from unittest.mock import Mock

import pytest


@pytest.fixture
def mock_flask():
    flask_app = Mock()
    return flask_app
