import pandas as pd
from io import StringIO
import re
import csv
import sqlite3
from my_ds_babel import csv_to_sql

def clean_csv_1(csv_1):
    df = pd.read_csv(StringIO(csv_1))
    # clean ["Gender"] !!
    df["Gender"] = df["Gender"].replace({"0": "Male", "1": "Female", "M": "Male", "F": "Female"})
    # clean ["FirstName"] , ["LastName"] !!
    df["FirstName"] = df["FirstName"].apply(lambda t: str(t).replace("\\", "").replace("\"", "").title())
    df["LastName"] = df["LastName"].apply(lambda t: str(t).replace("\\", "").replace("\"", "").title())
    # clean ["Email"] !!
    df["Email"] = df["Email"].apply(lambda t: str(t).lower())
    # clean ["City"] !!
    df["City"] = df["City"].apply(lambda t: str(t).replace("-", " ").replace("_", " ").title())
    # clean ["Country"] !!
    df["Country"] = "USA"
    # clean ["Age"] !!
    df["Age"] = df["Age"].apply(lambda t: str(re.findall(r"\d+", str(t))[0]))
    # to csv_1 !!
    #df.to_csv("csv_1_clean.csv", index=False)
    return df
csv_1 = open("only_wood_customer_us_1.csv", "r", encoding="utf-8").read()
# clean_csv_1(csv_1)

def clean_csv_2(csv_2):
    header_2 = "Age;City;Gender;FullName;Email\n"
    csv_content = header_2 + csv_2
    df = pd.read_csv(StringIO(csv_content), sep=";")
    # clean ["Age"] !!
    df["Age"] = df["Age"].apply(lambda t: str(re.findall(r"\d+",str(t))[0]))
    # clean ["City"] !!
    df["City"] = df["City"].apply(lambda t: str(t).replace("-", " ").replace("_", " ").title())
    # clean ["Gender"] !!
    df["Gender"] = df["Gender"].replace({"0": "Male", "1": "Female", "M": "Male", "F": "Female"})
    # clean ["FullName"] to ["FirstName"] , ["LastName"] !!
    df["FullName"] = df["FullName"].apply(lambda t: str(t).replace("\\", "").replace("\"", "").title())
    df[["FirstName","LastName"]] = df["FullName"].str.split(" ",n=1,expand=True)
    df["FirstName"] = df["FirstName"].str.title()
    df["LastName"] = df["LastName"].str.title()
    # ajouter ["Country"] !!
    df["Country"] = "USA"
    # clean ["UserName"] !!
    df["UserName"] = df["FirstName"].str.lower()
    # supprimer ["FullName"] !!
    df = df.drop(columns=["FullName"])
    # clean ["Email"] !!
    df["Email"] = df["Email"].apply(lambda t: str(t).lower())
    # organiser les columes !!
    df = df[["Gender", "FirstName", "LastName", "UserName", "Email", "Age", "City", "Country"]]
    # to csv_2 !!
    #df.to_csv("csv_2_clean.csv", index=False)
    return df   
csv_2 = open("only_wood_customer_us_2.csv", "r", encoding="utf-8").read()
# clean_csv_2(csv_2)

def clean_csv_3(csv_3):
    csv_3 = csv_3.replace(",", "\t")
    df = pd.read_csv(StringIO(csv_3),sep="\t")
    # clean ["Gender"] !!
    df["Gender"] = df["Gender"].apply(lambda t: str(t).replace("string_","").replace("boolean_","").replace("character_",""))
    df["Gender"] = df["Gender"].replace({"0": "Male", "1": "Female", "M": "Male", "F": "Female"})
    # clean ["Name"] !!
    df["Name"] = df["Name"].str.replace("string_","").str.replace("\"", "").str.title()
    df[["FirstName","LastName"]] = df["Name"].str.split(" ", n=1, expand=True)
    # supprimer ["Name"] ["FirstName"] , ["LastName"] !!
    df = df.drop(columns=["Name"])
    # clean ["Email"] !!
    df["Email"] = df["Email"].apply(lambda t: str(t).replace("string_","").lower())
    # clean ["Age"] !!
    df["Age"] = df["Age"].str.replace("integer_","").apply(lambda t: str(re.findall(r"\d+",str(t))[0]))
    # ajouter ["Country"] !!
    df["Country"] = "USA"
    # clean ["City"] !!
    df["City"] = df["City"].str.replace("string_","").str.replace("_"," ").str.replace("-"," ").str.title()
    # clean ["UserName"] !!
    df["UserName"] = df["FirstName"].str.lower()
    # organiser les columes !!
    df = df[["Gender", "FirstName", "LastName", "UserName", "Email", "Age", "City", "Country"]]
    # to csv_3 !!
    #df.to_csv("csv_3_clean.csv", index=False)
    return df
csv_3 = open("only_wood_customer_us_3.csv","r",encoding="utf-8").read()
# clean_csv_3(csv_3)

def my_m_and_a (file_1,file_2,file_3):
    df_1 = clean_csv_1(csv_1)
    df_2 = clean_csv_2(csv_2)
    df_3 = clean_csv_3(csv_3)
    # regrouper les DF !!
    df_all = pd.concat([df_1,df_2,df_3], ignore_index=True)
    # to csv_all !!
    df_all.to_csv("csv_all_clean.csv", index=False)
    return df_all
df = my_m_and_a(csv_1,csv_2,csv_3)

csv_to_sql("csv_all_clean.csv", 'plastic_free_boutique.sql', 'customers')
