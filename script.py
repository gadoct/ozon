import pandas as pd
df = pd.read_csv("ozon.csv")
df["profit"] = df["cost"]*df["quantity"]
print(pd.DataFrame({"quantity": df.groupby("good_name")["quantity"].sum(), "profit": df.groupby("good_name")["profit"].sum()}))
