"""
Scrape entertainment websites
"""

from .scrape import scrape_feeds

RIPPLES = "https://ripplesnigeria.com/feed"
GISTREEL = "https://gistreel.com/feed"
NAIJA_LOADED = "https://www.naijaloaded.com.ng/feed"
YNAIJA = "https://ynaija.com/feed/"
NETNAIJA = "https://www.thenetnaija.com/feed"
NAIJA_FLAVER = "https://9jaflaver.com/feed/"
BELLA_NAIJA = "https://www.bellanaija.com/feed/"
NOTJUSTOK = "https://notjustok.com/feed/"

CATEGORY = "Entertainment"


def scrape_entertainment():
    scrape_feeds("Ynaija", YNAIJA, CATEGORY)
    scrape_feeds("Ripples", RIPPLES, CATEGORY)
    scrape_feeds("Gistreel", GISTREEL, CATEGORY)
    scrape_feeds("NaijaLoaded", NAIJA_LOADED, CATEGORY)
    scrape_feeds("Notjustok", NOTJUSTOK, CATEGORY)
    scrape_feeds("Bella Naija", BELLA_NAIJA, CATEGORY)
    scrape_feeds("Naija Flaver", NAIJA_FLAVER, CATEGORY)
