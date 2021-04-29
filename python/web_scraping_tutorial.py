# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python [conda env:py37] *
#     language: python
#     name: conda-env-py37-py
# ---

# %%
# some libraries that are used across examples
from pprint import pprint
import re

# %% [markdown]
# # Web scraping with Pandas

# %%
import pandas as pd

# %%
url = 'https://www.espn.com/mens-college-basketball/team/stats/_/id/38/colorado-buffaloes'

# %%
dfs = pd.read_html(url)
print(len(dfs))

# %%
for df in dfs:
    print(df.head())

# %%
url = 'https://cubuffs.com/sports/mens-basketball/stats/2019-20'
url = 'https://en.wikipedia.org/wiki/Colorado_Buffaloes_men%27s_basketball'

# %%
dfs = pd.read_html(url)
print(len(dfs))

# %%
dfs[18]

# %% [markdown]
# # Web Scraping

# %%
import re

# %%
url = 'https://www.time.gov/'

# %% [markdown]
# ## Web scraping using Requests-HTML

# %%
from requests_html import HTMLSession

# %%
session = HTMLSession()
r = session.get(url)

# %%
page_html = r.html.raw_html.decode('utf-8')

# %%
html_body = re.search(r'<body>.+</body>', page_html, flags=re.DOTALL)[0]
lines = re.findall(r'.+', html_body)
for n in range(20):
    print(lines[n])

# %%
r.html.find('time')

# %%
for time in r.html.find('time'):
    if 'id' in time.attrs.keys():
        print(f'UTC Time is: {time.text}')

# %% [markdown]
# ## Web scraping using Selenium and a web browser
#
# For documentation on Selenium, see:
#
# * https://selenium-python.readthedocs.io/index.html
# * https://www.selenium.dev/documentation/en/
#
# For a introductory tutorial, see https://www.scrapingbee.com/blog/selenium-python/
#
# Selenium requires additional webdriver software that allows you to control Chrome, Firefox, etc. via Python.
#
# On macOS, you can use `brew` (https://brew.sh/) to install the dependencies:
#
# ```bash
# brew install geckodriver
# brew install chromedriver
# ```
#
# On Windows 10, you can use `choco` (https://chocolatey.org/) to install the dependencies (Run this in an Administrator shell):
#
# ```pwsh
# choco install selenium-gecko-driver
# choco install selenium-chrome-driver
# ```

# %%
from selenium import webdriver
from IPython.display import Image
from selenium.webdriver.support.select import Select

# %%
from selenium.webdriver.firefox.options import Options as firefoxoptions
options = firefoxoptions()
# comment out this line to see what's happening
# options.headless = True
driver = webdriver.Firefox(options=options)
driver.set_window_size(1024,768)
driver.get(url)
driver.save_screenshot('firefox.png')

# %%
pprint(driver.capabilities)

# %% [markdown]
# Alternatively use Chrome
# ```python
# from selenium.webdriver.chrome.options import Options as chromeoptions
# options = chromeoptions()
# options.headless = True
# driver = webdriver.Chrome(options=options)
# driver.set_window_size(640,480)
# driver.get(url)
# driver.save_screenshot('chrome.png')
# ```

# %%
Image(filename='firefox.png') 

# %%
page_html = driver.page_source

html_body = re.search(r'<body>.+</body>', page_html, flags=re.DOTALL)[0]
lines = re.findall(r'.+', html_body)
for n in range(20):
    print(lines[n])

# %%
driver.find_elements_by_tag_name('time')

# %%
for t in driver.find_elements_by_tag_name('time'):
    if t.get_attribute('id') is not '':
        print(t.text)

# %% [markdown]
# ### A slightly more advanced example
#
# Web scraping requires knowledge of HTML, CSS3, and Javascript. Most

# %%
driver.get('https://www.amazon.com')

# %%
search_box = driver.find_element_by_id('twotabsearchtextbox')
search_box.clear()
search_box.send_keys('512GB sd card\n')
search_box.submit()

# %%
dropdown = driver.find_element_by_class_name('a-dropdown-container')
dropdown.click()

# %%
# sort by 'Price: Low to High'
driver.find_element_by_id('s-result-sort-select_1').click() 

# %%
# despite search terms, some small SDCards are shown
# click on the filter link on the left
li = driver.find_element_by_id('p_n_feature_two_browse-bin/13203835011')
li.find_element_by_class_name('a-link-normal').click()

# %%
product_names = driver.find_element_by_css_selector('.a-size-medium.a-color-base.a-text-normal')

# %%

# %% [markdown]
# ### Cleaning up
#
# When finished, make sure you close the browser. Can either `driver.quit()` or `driver.close()`. `.close()` will close open tabs. If you close the last tab, it is the same as calling `.quit()`

# %%
driver.quit()

# %%
try:
    driver.close()
except Exception:
    print('Already closed')

# %%
