from .scrape import scrape_feeds

BUSINESS_DAY = 'https://businessday.ng/feed'
NAIRAMETRICS = 'https://nairametrics.com/feed'
BUSINESS_NEWS = 'https://businessnews.com.ng/feed'
VENTURES_AFRICA = "https://venturesafrica.com/feed/"
SME_DIGEST = "https://smedigest.com.ng/feed"
BUSINESSDAILYAFRICA = "https://www.businessdailyafrica.com/service/rss/bd/1939132/feed.rss"
BIZMAG = "https://bizmag.co.za/feed/"
HWMIIA = "https://www.howwemadeitinafrica.com/feed/"
SMALLSTARTER = "https://www.smallstarter.com/feed/"
BUSINESSELITE = "https://businesselitesafrica.com/feed/"
MATRIXLIVE = "https://matrixliveng.com/feed/"

CATEGORY = 'Business'


def scrape_business():
    scrape_feeds("Business Day", BUSINESS_DAY, CATEGORY)
    scrape_feeds("Nairametrics", NAIRAMETRICS, CATEGORY)
    scrape_feeds('Business News', BUSINESS_NEWS, CATEGORY)
    scrape_feeds("Business Africa", BUSINESSDAILYAFRICA, CATEGORY)
    scrape_feeds("SME Digest", SME_DIGEST, CATEGORY)
    scrape_feeds("Ventures Africa", VENTURES_AFRICA, CATEGORY)
    scrape_feeds("Bizmag", BIZMAG, CATEGORY)
    scrape_feeds("HWMIIA", HWMIIA, CATEGORY)
    scrape_feeds("Small Starter", SMALLSTARTER, CATEGORY)
    scrape_feeds("Business Elite", BUSINESSELITE, CATEGORY)
    scrape_feeds("Matix Live", MATRIXLIVE, CATEGORY)
