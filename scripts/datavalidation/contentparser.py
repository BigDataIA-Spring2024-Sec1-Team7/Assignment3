import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
from contentclass import ContentClass
import csv
import json
import re


from pydantic import BaseModel

def parse_my_files(file_path, Title, level):
# Parse the XML
    tree = ET.parse(file_path)
    root = tree.getroot()
    df = pd.DataFrame(columns=['level','title', 'topic', 'learning_outcomes'])  
    div_elements = root.findall(".//")
    count = 0 
    x = 0
    while x < len(div_elements):
        
        if div_elements[x].tag == "{http://www.tei-c.org/ns/1.0}p" or div_elements[x].tag == "{http://www.tei-c.org/ns/1.0}head" :
          
            print("-------------------------------------------------")
            if div_elements[x].tag == "{http://www.tei-c.org/ns/1.0}head":
                head =div_elements[x].text
                j = x+1
                description = ""
                while div_elements[j].tag == "{http://www.tei-c.org/ns/1.0}p":
                    print(f"value of j -------> {j}")
                    description = description + " " + str(div_elements[j].text)
                    j = j + 1
                x = j
               
                
                if description != "":
                   
                   df.loc[len(df), df.columns] = level,Title,head, description
                   count = count + 1
                   print(f"level: {level},title: {Title},topic:{head}, learning_outcomes:{description}")
                else:
                    if head != "LEARNING OUTCOMES" :
                        Title = head
                        print(f"Title:{head}")
                    else:
                        pass
                    
                print(f"count:{count}")
                continue
                

            
        
        x = x + 1
    # df.to_csv(output_path,index=False)
    return df
list_df = []
x = 1
while x < 4:
  
  if x == 1:
      Level = "Level I"
      new_df=parse_my_files(file_path=f"../../sourcedata/2024-l{x}-topics-combined-2.grobid.tei.xml", Title="Derivatives",level=Level)
  if x == 2:
      Level = "Level II"
      new_df=parse_my_files(file_path=f"../../sourcedata/2024-l{x}-topics-combined-2.grobid.tei.xml", Title="Quantitative Methods",level=Level)
  if x == 3:
      Level = "Level III"
      new_df=parse_my_files(file_path=f"../../sourcedata/2024-l{x}-topics-combined-2.grobid.tei.xml", Title="Economics",level=Level)
  list_df.append(new_df)
  x = x+1        

final_df = pd.concat(list_df, ignore_index=True)
# final_df.to_csv("../clean_csv/contentdata.csv",index=False)





df = final_df
df = df.fillna(np.nan).replace([np.nan], [None])
df['learning_outcomes'] = df['learning_outcomes'].apply(lambda v: re.sub(r'[\'"‘’”“]|<.*?>', '', str(v)))

validate_record_count = 0

contentinstance_list = []

for i, row in df.iterrows():
    try:
        obj = ContentClass(level = row.level, title= row.title, topic= row.topic ,learning_outcomes= row.learning_outcomes)
        contentinstance_list.append(obj)
        validate_record_count += 1
    except Exception as ex:
        print(ex)

def write_to_csv(obj_list):
    fieldnames = list(ContentClass.schema()["properties"].keys())
    
    with open("../clean_csv/content_data.csv", "w") as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        for obj in obj_list:
            writer.writerow(json.loads(obj.json()))

if validate_record_count == df.shape[0]:
    print("Successfully validated")
    write_to_csv(contentinstance_list)
else:
    print("Validation failed in some records. Please fix and retry")











