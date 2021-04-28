# bios6642-2021
 
BIOS 6642 Introduction to Python Programming, Spring 2021

Guest lecture on:

* Git
* Web scraping with Python
  * https://news.ycombinator.com/item?id=26090243
  *	https://www.scrapingbee.com/blog/web-scraping-101-with-python/
  * https://requests-html.kennethreitz.org/

Problems with many web scraping tools - no javascript support. 

Other options:
* https://github.com/scrapy/scrapy
* https://github.com/binux/pyspider
*	Beautifulsoup4 - https://www.crummy.com/software/BeautifulSoup/
* Requests-HTML - https://requests-html.kennethreitz.org/ and https://github.com/psf/requests-html Note - this cannot run inside jupyter due to asyncio event loops that conflict. Many bugs currently open with solutions that only work for some.
* https://github.com/pyppeteer/pyppeteer - Python port of puppeteer JavaScript (headless) chrome/chromium browser automation library.


get all csv files from page: https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-crime

Convert HTML table to dataframe:

* See https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html - doesn't support https, few other gotchas
* Data Source https://cubuffs.com/sports/mens-basketball/stats/2019-20
* Data Source https://en.wikipedia.org/wiki/Colorado_Buffaloes_men%27s_basketball
* https://www.espn.com/mens-college-basketball/team/stats/_/id/38/colorado-buffaloes

Download data via google drive:

* API: https://developers.google.com/drive/api/v3/quickstart/python
* Colorado COVID data: https://drive.google.com/drive/folders/1efQVBclGxwnCCYVLbzH96A0QRSWwmTYI

To Do List:
* Feedback form for annual review
* Get details on PyFAST group at CU Denver

### Notes

Do not need to cover Viz., Pandas, Numpy

Can have basic practice, but nothing for grading

80 min Zoom meeting, T/R 10:30 – 11:50

Probably sometime in April

Send lecture notes/outline to Fuyong – previous git repo: https://github.com/magic-lantern/bios6642


