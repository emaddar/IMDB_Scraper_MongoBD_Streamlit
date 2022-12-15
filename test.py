from icrawler.builtin import GoogleImageCrawler

crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=1,
    downloader_threads=4,
    storage={'root_dir': None},  # Set root_dir to None to prevent image download
)
x = crawler.crawl('cat', max_num=3)
