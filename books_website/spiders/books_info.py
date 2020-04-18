import scrapy


class BooksInfoSpider(scrapy.Spider):
    name = 'books_info'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        yield scrapy.Request(url='http://books.toscrape.com', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
        })

    def parse(self, response):
        path = response.xpath("//article[@class='product_pod']/h3")

        for link in path:
            url = link.xpath(".//a/@href").get()
            name = link.xpath(".//a/text()").get()

            yield response.follow(url=url, callback=self.page_title, meta={'name': name },headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
            })


    def page_title(self, response):
        name = response.request.meta['name']
        
        yield {
            'name': name,
        }

