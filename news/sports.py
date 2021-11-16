"""
This is a scraper for sports websites
"""

from .scrape import scrape_feeds


COMPLETESPORTS = "https://completesports.com/feed"
BRILA = "https://brila.net/feed"
ALLNIGERIANSOCCER = "https://allnigeriasoccer.com/feed"
SPORTS247 = "https://sports247.ng/feed"
SPORTINGLIFE = "https://sportinglife.ng/feed"

CATEGORY = "Sports"


def scrape_sports():
    scrape_feeds("Complete Sports", COMPLETESPORTS, CATEGORY)
    scrape_feeds("Brila", BRILA, CATEGORY)
    scrape_feeds("All Nigerian Soccer", ALLNIGERIANSOCCER, CATEGORY)
    scrape_feeds("Sports247", SPORTS247, CATEGORY)
    scrape_feeds("Sporting Life", SPORTINGLIFE, CATEGORY)
