from .scrape import scrape_feeds

BUSINESS_DAY = 'https://businessday.ng/feed'
NAIRAMETRICS = 'https://nairametrics.com/feed'
BUSINESS_NEWS = 'https://businessnews.com.ng/feed'
VENTURES_AFRICA = "https://venturesafrica.com/feed/"
SME_DIGEST = "https://smedigest.com.ng/feed"

CATEGORY = 'Business'


def scrape_business():
    scrape_feeds("Business Day", BUSINESS_DAY, CATEGORY)
    scrape_feeds("Nairametrics", NAIRAMETRICS, CATEGORY)
    scrape_feeds('Business News', BUSINESS_NEWS, CATEGORY)
