from urlclass import URLClass
import pandas as pd
import numpy as np
import csv
import json

df = pd.read_csv("../webscraping/data/cfascraping_data.csv")
df = df.fillna(np.nan).replace([np.nan], [None])
validate_record_count = 0

urlinstance_list = []

for i, row in df.iterrows():
    try:
        obj = URLClass(topic=row.topic, year=row.year, level=row.level, introduction=row.introduction, learning_outcomes=row.learning_outcomes, summary=row.summary, link_summary=row.link_summary, link_pdf=row.link_pdf)
        urlinstance_list.append(obj)
        validate_record_count += 1
    except Exception as ex:
        print(ex)

def write_to_csv(obj_list):
    fieldnames = list(URLClass.schema()["properties"].keys())
    
    with open("../clean_csv/urlclass_data.csv", "w") as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames, quotechar='"', quoting=csv.QUOTE_STRINGS)
        writer.writeheader()
        for obj in obj_list:
            writer.writerow(obj.model_dump())

if validate_record_count == df.shape[0]:
    print("Successfully validated")
    write_to_csv(urlinstance_list)
else:
    print("Validation failed in some records. Please fix and retry")