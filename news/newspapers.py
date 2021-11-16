"""
This file scrapes only headlines from different newspapers
"""


from .scrape import scrape_feeds


PUNCH = 'https://rss.punchng.com/v1/category/latest_news'
VANGUARD = 'https://vanguardngr.com/feed'
PREMUIM_TIMES = 'https://premiumtimesng.com/feed'
GUARDIAN = 'https://guardian.ng/feed'
THISDAYLIVE = 'https://thisdaylive.com/feed'
SAHARA_REPORTERS = 'https://saharareporters.com/feed'
DAILY_TRUST = 'https://dailytrust.com/feed'
DAILY_POST = 'https://dailypost.ng/feed'
THE_NATION = 'https://thenationonlineng.net/feed'
TRIBUNE = 'https://tribuneonlineng.com/feed'
LEADERSHIP = 'https://leadership.ng/feed'
NAIRALAND = "https://www.nairaland.com/feed"


# scrapes the leadership newspaper's headlines and stores it in the database

def scrape_newspapers():
    scrape_feeds("Punch", PUNCH, "Newspaper")
    scrape_feeds("Leadership", LEADERSHIP, "Newspaper")
    scrape_feeds('Tribune', TRIBUNE, "Newspaper")
    scrape_feeds("The Nation", THE_NATION, "Newspaper")  # Not working
    scrape_feeds("Premuim Times", PREMUIM_TIMES, "Newspaper")
    scrape_feeds("Daily Post", DAILY_POST, "Newspaper")  # Not working
    scrape_feeds("Daily Trust", DAILY_TRUST, "Newspaper")
    scrape_feeds("Sahara Reporters", SAHARA_REPORTERS, "Newspaper")
    scrape_feeds("This Daylive", THISDAYLIVE, "Newspaper")
    scrape_feeds("Vanguard", VANGUARD, "Newspaper")
    scrape_feeds("Nairaland", NAIRALAND, "Newspaper")
