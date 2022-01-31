# %%
import numpy as np
import pandas as pd
from os import path
from PIL import Image
# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# %%
raw = pd.read_csv('data/raw/RMU2012010FORBOW_DATA_2022-01-27_1507.csv')

raw.head(5)


# %%
df = raw[['ip9', 'ip9_1']]

# %%
df.to_csv('data/processed/df_for_worldcloud.csv')

# %%
df.ip9.value_counts()


# %%
df['ip9'].value_counts(normalize=True).plot(kind='bar', title='Groups')
