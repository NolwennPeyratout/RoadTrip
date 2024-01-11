import scrapy
from functools import partial


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        
        urls = [
            "https://theworldtravelguy.com/nudey-beach-on-fitzroy-island-best-beach-in-australia/",
            "https://theworldtravelguy.com/best-things-to-do-in-japan-what-to-do-for-fun/",
            "https://theworldtravelguy.com/kyoto-temple-shrine-japan/",
            "https://theworldtravelguy.com/japanese-temple-guide-best-traditional-shrines-temples-to-visit-in-japan/",
            "https://theworldtravelguy.com/best-things-to-do-in-tokyo-japan/",
            "https://theworldtravelguy.com/the-taj-mahal-india-history-location-pictures-from-agra/",
            "https://theworldtravelguy.com/destinations/india-travel-tips-complete-india-travel-guide/",
            "https://theworldtravelguy.com/destinations/egypt-travel-guide-the-best-egypt-travel-tips-blog/" , 
            "https://theworldtravelguy.com/best-things-to-do-in-egypt-adventure-fun-history/" ,
            "https://theworldtravelguy.com/colossi-of-memnon-giant-statues-in-luxor-egypt/ ", 
            "https://theworldtravelguy.com/karnak-temple-egypt-the-ancient-temple-of-amun-in-luxor/ ",
            "https://theworldtravelguy.com/abu-simbel-temple-egypt-epic-tomb-statue-of-ramses-ii/", 
            "https://theworldtravelguy.com/montserrat-spain-monastery-mountain-national-park-day-trip-from-barcelona/" ,
            "https://theworldtravelguy.com/basilica-de-santa-maria-del-mar-church-in-barcelona-spain/",
            "https://theworldtravelguy.com/destinations/new-zealand-travel-guide-best-travel-tips-blog/" , 
            "https://theworldtravelguy.com/roys-peak-new-zealand-epic-hike-in-wanaka-nz/ ", 
            "https://theworldtravelguy.com/tongariro-crossing-alpine-volcano-hike-national-park-in-new-zealand/ ",
            "https://theworldtravelguy.com/tasman-glacier-walk-lake-view-in-mount-cook-new-zealand/" , 
            "https://theworldtravelguy.com/hooker-valley-track-new-zealand-in-mount-cook-nz/ ",
            "https://theworldtravelguy.com/devils-punchbowl-waterfall-short-walk-in-arthurs-pass-new-zealand/",
            "https://theworldtravelguy.com/santorini-greece-island/ ",
            "https://theworldtravelguy.com/navagio-beach-greece-shipwreck/" , 
            "https://theworldtravelguy.com/kefalonia-greece-island/ ", 
            "https://theworldtravelguy.com/zakynthos-greece-island/" , 
            "https://theworldtravelguy.com/melissani-cave-lake/"

        ]
        country=[
            "Australia", "Japan", "Japan", "Japan", "Japan",  "India", "India", "Egypt",
            "Egypt","Egypt","Egypt","Egypt","Spain", "Spain","New Zealand", "New Zealand",
            "New Zealand", "New Zealand","New Zealand","New Zealand", "Greece","Greece",
            "Greece","Greece","Greece"
        ]
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for i in range(len(urls)):
            callback_with_country = partial(self.parse, country=country[i])
            yield scrapy.Request(url=urls[i], callback=callback_with_country, headers=headers)

    def parse(self, response, country):
        # Récupérez tout le texte des balises <p>
        
        paragraphs = response.css('p::text').getall()
        filename = f"../paragraph/paragraph-{country}.txt"
        with open(filename, 'a', encoding='utf-8') as file:
            file.write('\n'.join(paragraphs) + '\n')
