import scrapy
import re


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        """Собирает ссылки на документы PEP"""
        index = response.xpath('//*[@id="numerical-index"]').css("tbody")
        all_hrefs = index.css("a::attr(href)").getall()
        for href in all_hrefs:
            yield response.follow(href, callback=self.parse_pep)

    def parse_pep(self, response):
        """Парсит страницы с документами и формирует Items"""
        pep = response.css("section[id='pep-content']")
        pattern = re.compile(r"^PEP\s(?P<number>\d+)[\s–]+(?P<name>.*)")
        h1_tag = pattern.search(pep.css("h1::text").get())
        if h1_tag:
            number, name = h1_tag.group("number", "name")
        yield {
            'number': number,
            'name': name,
            'status': pep.css("dt:contains('Status') + dd::text").get()
        }
