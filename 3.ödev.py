import numpy as np
import pandas as pd
df=pd.read_csv("persona.csv")
df.head()
df.describe().T
df.shape
df.info()
df.isnull().values.any()
df.isnull().sum()
df["SOURCE"].nunique()
df["PRICE"].nunique()
df["PRICE"].value_counts()
df["COUNTRY"].value_counts()
df.groupby("COUNTRY").agg({"PRICE":"sum"})
df.groupby("SOURCE").agg({"PRICE":"sum"})
df.groupby("COUNTRY").agg({"PRICE":"mean"})
df.groupby("SOURCE").agg({"PRICE":"mean"})
df.groupby(["COUNTRY","SOURCE"]).agg({"PRICE":"mean"})


df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE":"mean"}).head(4)

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})
agg_df.sort_values(by=["PRICE"],ascending=False,inplace=True)

agg_df.reset_index().head()

age_cat = df["AGE"].astype("category")
age_cat = [18_25,31_37,36_41,41_46,23_29,32_37]
agg_df+=age_cat
agg_df

df["age_cat"]=pd.cut(df["AGE"],[0,18,25,33,37,42,46],labels=["0_18","18_25","25_33","33_37","37_42","42_46"])
df

df["customers_level_based"]=df.groupby(["COUNTRY","SOURCE","SEX","age_cat"]).agg({"PRICE":"count"})
df1["customers_level_based"]
customers_level_based= [col for col in df.columns if "PRICE" not in col if "age_cat" not in col]
customers_level_based