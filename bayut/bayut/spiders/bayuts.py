# from  typing import Any
# import scrapy
# # from scrapy.http import Response





#
#             

import scrapy

class MySpider(scrapy.Spider):
    
    name='bayut'
#     name='bayut'
    start_urls =   ['https://www.bayut.com/to-rent/property/dubai/'] # Replace with your target URL

    def parse(self, response):
        
        for item in response.css('li.a37d52f0'):  # R_5254c99eplace with the correct item container
            yield {
                'name': item.css('div._301c67f2::text').get(),  # Adjust selector for name
                'price': item.css('.dc381b5::text').get(), # Adjust selector for price
                # 'location': item.css('span.location::text').get(),  # Adjust selector for location
                'link': item.css('a.d40f2294::attr(href)').get(),  # Adjust to get the link
                'label': item.css('h2.f0f13906::text').get(),  # Page title (if needed)
                ' image_url' : item.css('picture.a659dd2e::attr(src)').get()
            }
        