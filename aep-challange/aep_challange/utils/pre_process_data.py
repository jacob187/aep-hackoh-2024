from clean_text import clean
from file_factory import read_aep_csv, save_pk

import pandas as pd

# Read the CSV file
data = read_aep_csv()


print(data.head())

# Clean the text data in the relevant columns
data["PNT_NM"] = data["PNT_NM"].apply(lambda x: clean(x))
data["QUALIFIER_TXT"] = data["QUALIFIER_TXT"].apply(lambda x: clean(x))
data["PNT_ATRISKNOTES_TX"] = data["PNT_ATRISKNOTES_TX"].apply(lambda x: clean(x))

# Format the date
data["DATETIME_DTM"] = pd.to_datetime(
    data["DATETIME_DTM"], format="mixed", dayfirst=True, errors="coerce"
)


save_pk(data, "./files/data.pkl")
