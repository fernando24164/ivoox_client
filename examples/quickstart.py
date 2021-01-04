"""
This example script imports the ivoox_client package and
retrieve audios information
"""

import asyncio
from ivoox_client import client

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    response = loop.run_until_complete(client.get_audios())
    # response will be a list of python object with audios information
    # [{
    #             "image": 'https://example.com/media?url=fsdfsd',
    #             "title": 'Awesome podcast',
    #             "author": 'Awesome podcast author',
    #             "category": 'Mystery',
    #             "mp3URL": 'https://example.com',
    #         }]
