import scrapy


class BooksInfoSpider(scrapy.Spider):
    name = 'books_info'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        yield scrapy.Request(url='http://books.toscrape.com', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
        })

    def parse(self, response):
        path = response.xpath("//article[@class='product_pod']/h3")

        for link in path:
            name_link = link.xpath(".//a/@href").get()

            yield response.follow(url=name_link, callback=self.page_title, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
            })

        next_page = response.xpath("//li[@class='next']/a/@href").get()
    
        if next_page :
            absolute_url = response.urljoin(next_page)
            print(absolute_url)
            print("HELLLLLLDMLSMKSDMSLCKJNDLSCKNSDLCKNDLKSNCLDSKNCSLKDNCSLDKNCSLDKNCSLDNCSLKNDCLSDKNCLKNSD")
            yield scrapy.Request(url=absolute_url, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
            })

    def page_title(self, response):
        name = response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get()
        price = response.xpath("//div[@class='col-sm-6 product_main']/p[position()=1]/text()").get()

        yield {
            'name': name,
            'price': price,
        }

