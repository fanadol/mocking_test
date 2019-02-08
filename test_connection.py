from unittest import mock, TestCase

import app, config


class TestConnection(TestCase):
    @mock.patch("connections.connection")
    def test_connection(self, mockDB):
        valid_credential = config.credential
        app.connect(valid_credential)
        mockDB.assert_called_with(valid_credential)
