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
            name = link.xpath(".//a/text()").get()
            price = link.xpath("//p[@class='price_color']/text()").get()

            yield {
                'name': name,
                'price': price,
            }

        next_page = response.xpath("//li[@class='next']/a/@href").get()
    
        if next_page :
            # absolute_url = f'http://books.toscrape.com/{next_page}'


            absolute_url = response.urljoin(next_page)
            print(absolute_url)
            print("HELLLLLLDMLSMKSDMSLCKJNDLSCKNSDLCKNDLKSNCLDSKNCSLKDNCSLDKNCSLDKNCSLDNCSLKNDCLSDKNCLKNSD")
            yield scrapy.Request(url=absolute_url, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
            })


    # def page_title(self, response):
    #     name = response.request.meta['name']
    #     price = response.xpath("//p[@class='price_color']/text()").get()
    #     # description = response.xpath("//article/p/text()").get()

    #     # print("Second Function")

    #     yield {
    #         'name': name,
    #         'price': price,
    #         # 'description': description,
    #         # 'next_link': next_link
    #     }

