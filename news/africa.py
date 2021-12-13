from .scrape import scrape_feeds

AFRICANEWS = "https://www.africanews.com/feed/"
AFRICANREPORTER = "https://africanreporter.co.za/feed"

CATEGORY = "Africa"


def scrape_africa():
    scrape_feeds("Africa news", AFRICANEWS, CATEGORY)
    scrape_feeds("African reporters", AFRICANREPORTER, CATEGORY)
