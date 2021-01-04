from collections import defaultdict
from typing import Awaitable, Dict, List

import httpx

from .helpers import format_response


class Client:

    base_url: str = "https://www.ivoox.com/"
    url_audios: str = "audios_sa_f_1.html"
    url_podcasts: str = "audios_sc_f_1.html"

    def _complete_url(self, topic: str) -> str:
        return self.base_url + topic + "_sb.html"

    urls = defaultdict(lambda _: "https://www.ivoox.com/audios_sa_f_1.html")
    urls = {
        "audio": base_url + url_audios,
        "podcast": base_url + url_podcasts,
        "search": _complete_url,
    }

    async def _request(self, method="default", **kwargs) -> Awaitable:
        url_endpoint = self.urls[method]
        if kwargs:
            url_endpoint = url_endpoint(self, kwargs["topic"])
        async with httpx.AsyncClient() as client:
            response = await client.get(url=url_endpoint)
        return response

    async def get_audios(self) -> List[Dict[str, str]]:
        response: str = await self._request("audio")
        return format_response(response)

    async def get_podcast(self) -> List[Dict[str, str]]:
        response = await self._request("podcast")
        return format_response(response)

    async def search(self, topic: str) -> List[Dict[str, str]]:
        response: str = await self._request("search", topic=topic)
        return format_response(response)
