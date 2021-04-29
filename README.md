# bios6642-2021
 
BIOS 6642 Introduction to Python Programming, Spring 2021

Guest lecture on:

* Git
* Web scraping with Python

## To Setup a similar Python environment to what is used in the presentations, run:

`conda env create -f ./environment.yml`

Command to enable `conda` in VSCode `pwsh` shell:

```powershell
pwsh -ExecutionPolicy ByPass -NoExit -Command "& 'C:\Anaconda3\shell\condabin\conda-hook.ps1'"
# now modify powershell startup to always make conda available
conda init powershell
```

## Notes and useful information


Web scraping tutorial
  *	https://www.scrapingbee.com/blog/web-scraping-101-with-python/


Problems with many web scraping tools - no javascript support.

Some python web scraping options:
* https://github.com/scrapy/scrapy
* https://github.com/binux/pyspider
*	Beautifulsoup4 - https://www.crummy.com/software/BeautifulSoup/
* Requests-HTML - https://requests-html.kennethreitz.org/ and https://github.com/psf/requests-html Note - this cannot run inside jupyter due to asyncio event loops that conflict. Many bugs currently open with solutions that only work for some.
* https://github.com/pyppeteer/pyppeteer - Python port of puppeteer JavaScript (headless) chrome/chromium browser automation library.


Besides the above, there are also APIs that allow you to download data from more specialized web services. For example to download data from google drive:

* API: https://developers.google.com/drive/api/v3/quickstart/python
* Colorado COVID data: https://drive.google.com/drive/folders/1efQVBclGxwnCCYVLbzH96A0QRSWwmTYI
