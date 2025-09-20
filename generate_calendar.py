import requests
from ics import Calendar, Event
from datetime import datetime
import os

ANILIST_USER = "AkiroZen"

query = """
query ($userName: String) {
  MediaListCollection(userName: $userName, type: ANIME, status: CURRENT) {
    lists {
      entries {
        media {
          title { romaji }
          airingSchedule(notYetAired: true, perPage: 50) {
            nodes {
              episode
              airingAt
            }
          }
        }
      }
    }
  }
}
"""

variables = {"userName": ANILIST_USER}
url = "https://graphql.anilist.co"

response = requests.post(url, json={"query": query, "variables": variables})
data = response.json()

cal = Calendar()

for lst in data["data"]["MediaListCollection"]["lists"]:
    for entry in lst["entries"]:
        media = entry["media"]
        title = media["title"]["romaji"]
        schedule = media.get("airingSchedule", {}).get("nodes", [])

        for ep in schedule:
            airing_date = datetime.utcfromtimestamp(ep["airingAt"]).date()
            ep_number = ep["episode"]

            e = Event()
            e.name = f"{title} - Episodio {ep_number}"
            e.begin = airing_date
            e.make_all_day()
            cal.events.add(e)


with open("anime_calendar.ics", "w", encoding="utf-8") as f:
    f.writelines(cal)

print("✅ anime_calendar.ics generado")