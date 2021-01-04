from typing import Dict, List

from bs4 import BeautifulSoup


def format_podcast(audio, answer):
    try:
        podcast_link = audio.find("div", {"class": "content"}).find("a")["href"]
        podcast_title = audio.find("div", {"class": "content"}).find("a")["title"]
        podcast_description = (
            audio.find("div", {"class": "content"})
            .find("p", {"class": "description-program"})
            .find("span")
            .text.strip()
        )
        answer.append(
            {
                "podcastTitle": podcast_title,
                "podcastLink": podcast_link,
                "podcastDescription": podcast_description,
            }
        )
    except TypeError:
        pass


def format_response(body) -> List[Dict[str, str]]:
    answer = []
    parser = BeautifulSoup(body, "html.parser")
    banners = parser.findAll("div", {"class": "flipper"})
    for audio in banners:
        try:
            podcast_image_small = audio.find("img", {"class": "mini"}).attrs["data-src"]
            podcast_title = audio.find("p", {"class": "title-wrapper"}).text.strip()
            podcast_author = (
                audio.find("div", {"class": "wrapper"}).find("a")["title"].strip()
            )
            podcast_category = (
                audio.find("div", {"class": "content"})
                .find("a", {"class": "rounded-label"})
                .text.strip()
            )
            podcast_file = (
                audio.find("div", {"class": "content"})
                .find("p", {"class": "title-wrapper"})
                .find("a")["href"]
            ).replace("-mp3_rf", "_mm")
        except AttributeError:
            format_podcast(audio, answer)
            continue
        answer.append(
            {
                "image": podcast_image_small,
                "title": podcast_title,
                "author": podcast_author,
                "category": podcast_category,
                "mp3URL": podcast_file,
            }
        )
    return answer
