import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    # クロールを開始するURLのリスト。
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        # トップページからカテゴリページへのリンクを抜き出してたどる。
        for url in response.css('ul lia::attr("href")').re('.*/category/.*'):
            yield scrapy.Request(response.urljoin(url), self.parse_titles)

    def parse_titles(self, response):
        # カテゴリページからそのカテゴリの投稿のタイトルをすべて抜き出す。
        for post_title in response.css('div.entries > ul > lia::text').=extract():
            yield {'title': post_title}
