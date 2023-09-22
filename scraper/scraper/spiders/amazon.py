import os
import scrapy
import js2xml
from urllib.parse import urlencode
from scraper.items import AmazonProduct
from dotenv import load_dotenv

load_dotenv()


def parse_urls_file(file_path: str) -> list[str]:
    """
    Parse a file of urls into a list of urls

    Args:
        file_path (str): Path to file containing urls
    
    Returns:
        urls (list): List of urls
    """
    with open(file_path, 'r') as f:
        urls = f.read().splitlines()

    return urls

def get_url(url, api_key):
    payload = {'api_key': api_key, 'url': url}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def start_requests(self):
        # Get args to crawler
        urls_file_path = getattr(self, "urls_file", None)
        if urls_file_path is None:
            raise ValueError('No urls_file path provided')

        pages = parse_urls_file(urls_file_path)

        # Get API key from .env file
        try:
            api_key = os.environ.get('PROXY_API_KEY')
        except KeyError:
            EnvironmentError('PROXY_API_KEY not set in .env')

        for page in pages:
            yield scrapy.Request(url = get_url(page, api_key), callback=self.parse)

    def parse(self, response):
        amazon_product = AmazonProduct()
        amazon_product['asin'] = response.xpath('//*[@id="ASIN"]').attrib['value']
        amazon_product['item_name'] = response.xpath('//*[@id="productTitle"]//text()').get().strip()
        bullet_point = response.css('#feature-bullets').css('.a-list-item::text').getall()
        cleaned_bullets = []
        for i in bullet_point:
            if (i != ' ' and i != '\n'):
                cleaned_bullets.append(i)
        amazon_product['bullet_point'] = cleaned_bullets
        js = response.xpath("//script[contains(text(), 'register(\"ImageBlockATF\"')]/text()").extract_first()
        xml = js2xml.parse(js)
        selector = scrapy.Selector(root=xml)
        image_array = selector.xpath('//property[@name="colorImages"]//property[@name="hiRes"]/string/text()').extract()
        amazon_product['images'] = image_array
        amazon_product['image_count'] = len(image_array)
        parsed_details = []
        details = response.xpath('//*[@id="detailBullets_feature_div"]/ul/li').getall()
        if not details:
            details = response.css('.prodDetTable')
            for table in details:
                rows = table.xpath('//tr[not(@id) and not(@class)]')
                for row in rows: 
                    header = row.css('.prodDetSectionEntry::text').get()
                    data = row.css('.prodDetAttrValue::text').get()
                    if header and data:
                        parsed_details.append(header.strip() + ': ' + data.strip())
        amazon_product['product_details'] = parsed_details

        yield amazon_product
