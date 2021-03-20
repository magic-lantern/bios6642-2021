# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.9.1
#   kernelspec:
#     display_name: Python [conda env:py37] *
#     language: python
#     name: conda-env-py37-py
# ---

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

# %%
for df in dfs:
    print(df.head())

# %%
