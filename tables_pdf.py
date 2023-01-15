import pdfplumber
import pandas as pd
from PIL import Image

pdf = pdfplumber.open("ex900942130")
po = pdf.pages[0]
Image.open("page_o.png")

table = p0.extract_table()

df = pd.DataFrame(table[1:], columns=table[0])
for column in ["Effective", "Received"]:
    df[column] = df[column].str.replace("","")
df.head()
