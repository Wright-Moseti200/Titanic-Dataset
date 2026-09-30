import pandas as pd 
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

df = pd.read_csv("tested.csv")

for col,value in df.isna().sum().items():
    if value == 0:
        continue
    elif value > len(df) * 0.5:
      df = df.drop(columns=col)
    elif pd.api.types.is_numeric_dtype(df[col]):
        df[col]=df[col].fillna(df[col].median())
    else:
        df[col] =df[col].fillna(df[col].mode()[0])

df = df.drop_duplicates()

rates = df.groupby("Embarked")["Survived"].mean()
print(rates)
print(rates.idxmax())
print(df["Embarked"].value_counts())

rates.plot(kind="bar", title="Survival rate by port")
plt.ylabel("Survival rate")
plt.show()

mean_fares = df.groupby("Pclass")["Fare"].mean()
median_fares = df.groupby("Pclass")["Fare"].median()
print(mean_fares[1]-mean_fares[3])
print(median_fares[1]-median_fares[3])

df.groupby("Pclass")["Fare"].agg(["mean", "median"]).plot(kind="bar", title="Fare by class")
plt.ylabel("Fare")
plt.show()

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["isAlone"] = df["FamilySize"]==1
aloneRate = df.groupby("isAlone")["Survived"].mean()
print(aloneRate[True]-aloneRate[False])
print(df.info())

aloneRate.plot(kind="bar", title="Survival: alone vs with family")
plt.ylabel("Survival rate")
plt.show()

df["AgeGroup"] = pd.cut(df["Age"],bins=[0,12,18,35,60,199],labels=["Child", "Teen", "YoungAdult", "Adult", "Senior"])
age_rates = df.groupby("AgeGroup")["Survived"].mean()
print(age_rates)

age_rates.plot(kind="bar", title="Survival rate by age group")
plt.ylabel("Survival rate")
plt.show()

df["Title"] = df["Name"].str.split(",").str.get(1).str.split(".").str.get(0)
print(df["Title"].value_counts())
title_rates = df.groupby("Title")["Survived"].mean()
print(title_rates)

df["Title"].value_counts().plot(kind="bar", title="Passenger count by title")
plt.show()

title_rates.plot(kind="bar", title="Survival rate by title")
plt.ylabel("Survival rate")
plt.show()