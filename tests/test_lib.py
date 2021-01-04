import asyncio
from unittest import TestCase, mock, skip

from src.ivoox_client import client
from src.ivoox_client.helpers import format_response

from tests.fixtures.response import response as mock_response


class TestLib(TestCase):
    def setUp(self) -> None:
        self.loop = asyncio.new_event_loop()
        self.loop.set_debug(True)

    def tearDown(self) -> None:
        self.loop.close()

    def test_client(self):
        with mock.patch("src.ivoox_client.client._request") as mock_call:
            mock_call.return_value = True
            response = self.loop.run_until_complete(client._request("audio"))
            self.assertTrue(response)

    def test_format(self):
        formatted_response = format_response(mock_response)
        self.assertTrue(formatted_response)
        self.assertEqual(len(formatted_response), 36)

    @skip("Skipping due it makes real request")
    def test_audios_endpoint(self):
        response = self.loop.run_until_complete(client.get_audios())
        self.assertTrue(response)

    @skip("Skipping due it makes real request")
    def test_podcast_endpoint(self):
        response = self.loop.run_until_complete(client.get_podcast())
        self.assertTrue(response)

    @skip("Skipping due it makes real request")
    def test_search_endpoint(self):
        response = self.loop.run_until_complete(client.search("mystery"))
        self.assertTrue(response)
