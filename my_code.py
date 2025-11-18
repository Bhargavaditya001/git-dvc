import os
import pandas as pd

data = {"name":["A","B","C"],
        "age":[20,30,40]}

df = pd.DataFrame(data)

data_dir = "data"
os.makedirs(data_dir,exist_ok=True)
file_path = os.path.join(data_dir,"sample.csv")
df.to_csv(file_path,index=False)
print(f"CSV file saved to {file_path}")