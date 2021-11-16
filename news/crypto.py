from .scrape import scrape_feeds

CATEGORY = "Crypto"

BITCOIN_NG = "https://bitcoin.ng/feed/"
KRAKEN_BLOG = "https://blog.kraken.com/feed/"
NEWSBTC = "https://www.newsbtc.com/feed/"
COINBASE_BLOG = "https://blog.coinbase.com/feed"
CRYPTO_NINJAS = "https://www.cryptoninjas.net/feed/"


def scrape_crypto():
    scrape_feeds("Bitcoin NG", BITCOIN_NG, CATEGORY)
    scrape_feeds("Kraken Blog", KRAKEN_BLOG, CATEGORY)
    scrape_feeds("News BTC", NEWSBTC, CATEGORY)
    scrape_feeds("Coinbase Blog", COINBASE_BLOG, CATEGORY)
    scrape_feeds("Crypto Ninjas", CRYPTO_NINJAS, CATEGORY)
