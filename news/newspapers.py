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
TELEGRAPH = "https://www.telegraph.co.uk/rss.xml"
PMNEWS = "https://pmnewsnigeria.com/feed/"
NAIJANEWS = "https://www.naijanews.com/feed/"
INDEPENDENT = "https://independent.ng/feed/"
AUTHORITY = "https://authorityngr.com/feed/"
BLUEPRINT = "https://www.blueprint.ng/feed/"
BREAKINGTIMES = "https://www.thebreakingtimes.com/feed/"
OSUN = "http://www.osundefender.com/feed/"
TIDE = "http://www.thetidenewsonline.com/feed/"
PEOPLESDAILY = "https://www.peoplesdailyng.com/feed/"
NEWSWATCH = "https://www.mydailynewswatchng.com/feed/"
ACCORD = "https://www.nationalaccordnewspaper.com/feed/"
MYSCHOOL = "https://myschool.ng/news/feeds"
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
    scrape_feeds("Telegraph", TELEGRAPH, "Newspaper")
    scrape_feeds("PM NEWS", PMNEWS, "Newspaper")
    scrape_feeds("Naija News", NAIJANEWS, "Newspaper")
    scrape_feeds("Independent", INDEPENDENT, "Newspaper")
    scrape_feeds("Authority", AUTHORITY, "Newspaper")
    scrape_feeds("Blueprint", BLUEPRINT, "Newspaper")
    scrape_feeds("Breaking Times", BREAKINGTIMES, "Newspaper")
    scrape_feeds("Osun Defender", OSUN, "Newspaper")
    scrape_feeds("The Tide", TIDE, "Newspaper")
    scrape_feeds("Peoples Daily", PEOPLESDAILY, "Newspaper")
    scrape_feeds("Newswatch", NEWSWATCH, "Newspaper")
    scrape_feeds("Accord", ACCORD, "Newspaper")
    scrape_feeds("MySchool", MYSCHOOL, "Newspaper")
