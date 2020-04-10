# -*- coding: utf-8 -*-

# Scrapy settings for nlpjob project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'nlpjob'

SPIDER_MODULES = ['nlpjob.spiders']
NEWSPIDER_MODULE = 'nlpjob.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'nlpjob (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 10
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cache-Control': 'max-age=0',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 '
                  'Safari/537.36 ',
    'Cookie': 'lastCity=101020100; sid=sem_pz_bdpc_dasou_title; __c=1584167693; __g=sem_pz_bdpc_dasou_title; __l=l=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDdiHC088qh0KZEgsDcXvkX000007hOm-C00000ImISR2.THdBULP1doZA8QMu1x60UWdBmy-bIy9EUyNxTAT0T1d-nyDdrjTsnW0snjwBP1KB0ZRqnjDLrH77fbNanDcknDPjfH9awHn4wj-7PWnkwj-7fYc0mHdL5iuVmv-b5Hn1PjnvP10knWDhTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8Xh9GTA-8QhPEUitOTv-b5gP-UNqsX-qBuZKWgvw9TvqdgLwGIAk-0APzm1YvnjRYP0%26tpl%3Dtpl_11534_21264_17382%26l%3D1516420953%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DBOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E6%252588%252591%2525E8%2525A6%252581%2525E8%2525B7%25259F%2525E8%252580%252581%2525E6%25259D%2525BF%2525E8%2525B0%252588%2525EF%2525BC%252581%2526xp%253Did(%252522m3343670121_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D140%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%25E5%25AE%2598%25E7%25BD%2591%26issp%3D1%26f%3D3%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26oq%3D%2525E6%2525B1%2525BD%2525E8%2525BD%2525A6%2525E4%2525B9%25258B%2525E5%2525AE%2525B6%26inputT%3D2912%26prefixsug%3Dboss%26rsp%3D0&r=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDdiHC088qh0KZEgsDcXvkX000007hOm-C00000ImISR2.THdBULP1doZA8QMu1x60UWdBmy-bIy9EUyNxTAT0T1d-nyDdrjTsnW0snjwBP1KB0ZRqnjDLrH77fbNanDcknDPjfH9awHn4wj-7PWnkwj-7fYc0mHdL5iuVmv-b5Hn1PjnvP10knWDhTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8Xh9GTA-8QhPEUitOTv-b5gP-UNqsX-qBuZKWgvw9TvqdgLwGIAk-0APzm1YvnjRYP0%26tpl%3Dtpl_11534_21264_17382%26l%3D1516420953%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DBOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E6%252588%252591%2525E8%2525A6%252581%2525E8%2525B7%25259F%2525E8%252580%252581%2525E6%25259D%2525BF%2525E8%2525B0%252588%2525EF%2525BC%252581%2526xp%253Did(%252522m3343670121_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D140%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%25E5%25AE%2598%25E7%25BD%2591%26issp%3D1%26f%3D3%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26oq%3D%2525E6%2525B1%2525BD%2525E8%2525BD%2525A6%2525E4%2525B9%25258B%2525E5%2525AE%2525B6%26inputT%3D2912%26prefixsug%3Dboss%26rsp%3D0&g=%2Fwww.zhipin.com%2Fshanghai%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&friend_source=0&friend_source=0; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3Dnlp%26city%3D101020100%26industry%3D%26position%3D; __zp_seo_uuid__=5820c09b-978b-4dd9-86c9-57d3415d5aec; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1584167693,1586005071,1586341957,1586481823; __a=48821657.1584167693..1584167693.51.1.51.51; __zp_stoken__=f19axPWuAG5hiSFSUJYHL9031RkKiNBaUQSK7qe7Xm7WRgMuDlD8bwN4xrS90Z94zJ1OCmZjopY48HHIblcu579wnmz2ZOJjJQrVsD3YiGXV5MCp%2FOVtfhOLM73O%2F8QkUF%2FI; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1586493350',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'nlpjob.middlewares.NlpwordcloudSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'nlpjob.middlewares.NlpwordcloudDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'nlpjob.pipelines.NlpwordcloudPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
