from .scrape import scrape_feeds

CATEGORY = "Crypto"

BITCOIN_NG = "https://bitcoin.ng/feed/"
KRAKEN_BLOG = "https://blog.kraken.com/feed/"
NEWSBTC = "https://www.newsbtc.com/feed/"
COINBASE_BLOG = "https://blog.coinbase.com/feed"
CRYPTO_NINJAS = "https://www.cryptoninjas.net/feed/"
COINTELEGRAPH = "https://cointelegraph.com/feed"
BITCOIN = "https://news.bitcoin.com/feed/"
BITFLYER = "https://blog-eu.bitflyer.com/rss/"
COINSTATS = "https://coinstats.app/blog/feed/"
U_TODAY = "https://u.today/rss"
CRYPTOSLATE = "https://cryptoslate.com/feed/"
CRYPTO_POTATO = "https://cryptopotato.com/feed"
CHALENG = "https://changelly.com/blog/feed/"
BRIEF = "https://cryptobriefing.com/feed/"
BITCOIN_MAGAZINE = "https://bitcoinmagazine.com/.rss/full/"
BITCOINIST = "https://bitcoinist.com/feed/"
COINCHECKUP = "https://coincheckup.com/blog/feed/"
CRYPTONEWSZ = "https://www.cryptonewsz.com/feed/"
ZYCRYPTO = "https://zycrypto.com/feed/"
COINQUORA = "https://coinquora.com/latest-post/feed/"


def scrape_crypto():
    scrape_feeds("Bitcoin NG", BITCOIN_NG, CATEGORY)
    scrape_feeds("Kraken Blog", KRAKEN_BLOG, CATEGORY)
    scrape_feeds("News BTC", NEWSBTC, CATEGORY)
    scrape_feeds("Coinbase Blog", COINBASE_BLOG, CATEGORY)
    scrape_feeds("Crypto Ninjas", CRYPTO_NINJAS, CATEGORY)
    scrape_feeds("Coin Telegraph", COINTELEGRAPH, CATEGORY)
    scrape_feeds("Bitcoin", BITCOIN, CATEGORY)
    scrape_feeds("Bitflyer", BITFLYER, CATEGORY)
    scrape_feeds("Coin Stats", COINSTATS, CATEGORY)
    scrape_feeds("U Today", U_TODAY, CATEGORY)
    scrape_feeds("Crypto Slate", CRYPTOSLATE, CATEGORY)
    scrape_feeds("Crypto Potato", CRYPTO_POTATO, CATEGORY)
    scrape_feeds("Changelly", CHALENG, CATEGORY)
    scrape_feeds("Crypto Briefing", BRIEF, CATEGORY)
    scrape_feeds("Bitcoin Magazine", BITCOIN_MAGAZINE, CATEGORY)
    scrape_feeds("Bitcoinist", BITCOINIST, CATEGORY)
    scrape_feeds("Coin Checkup", COINCHECKUP, CATEGORY)
    scrape_feeds("Crypto Newsz", CRYPTONEWSZ, CATEGORY)
    scrape_feeds("Zycrypto", ZYCRYPTO, CATEGORY)
    scrape_feeds("Coin Quora", COINQUORA, CATEGORY)
