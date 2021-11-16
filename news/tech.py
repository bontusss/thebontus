from .scrape import scrape_feeds


CATEGORY = "Technology"

TECH_CABAL = "https://techcabal.com/feed/"
NAIJA_TECH_GUIDE = "https://www.naijatechguide.com/feed"
GADGET_STRIPE = "https://gadgetstripe.com/feed/"
TECH_TRENDS = "https://techtrends.com/feed/"
TECH_CITY = "https://www.techcityng.com/feed/"
TECH_POINT = "https://techpoint.africa/feed"
DON_CAPRIO = "https://www.doncaprio.com/feed/"
DISRUPT_AFRICA = "https://disrupt-africa.com/feed"


def scrape_tech():
    scrape_feeds("Tech Cabal", TECH_CABAL, CATEGORY)
    scrape_feeds("Naija Tech Guide", NAIJA_TECH_GUIDE, CATEGORY)
    scrape_feeds("Gadget Stripe", GADGET_STRIPE, CATEGORY)
    scrape_feeds("Tech Trends", TECH_TRENDS, CATEGORY)
    scrape_feeds("Tech City", TECH_CITY, CATEGORY)
    scrape_feeds("Tech Point", TECH_POINT, CATEGORY)
    scrape_feeds("Don Caprio", DON_CAPRIO, CATEGORY)
    scrape_feeds("Disrupt Africa", DISRUPT_AFRICA, CATEGORY)
