# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:28:22 2024

@author: USER
"""

import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://theworldtravelguy.com/rock-islands-palau-boat-tour/#Best_Things_To_Do_In_The_Rock_Islands_Of_Palaus']  # Remplacez par l'URL de la page à scraper

    def parse(self, response):
        # Récupérez tout le texte des balises <p>
        paragraphs = response.css('p::text').getall()

        for paragraph in paragraphs:
            print(paragraph)

