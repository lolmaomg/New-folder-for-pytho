

import pandas as pd

# 1. 读取
df = pd.read_csv("titanic.csv")

# 2. 初步观察
print(df.head())
print(df.shape)
df.info()

# 3. 检查缺失值
print(df.isnull().sum())

print(df["Age"].isnull().sum())
print("this is the number of missing values in Age column")

# 4. 填补 Age
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)

# 5. 创建新特征
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
print(df.head())

# 6. 查看性别分布
print(df["Sex"].value_counts())

# 7. 找成年人
adults = df[df["Age"] >= 18]
print(adults.head())

# 8. 比较男女存活率
survival = df.groupby("Sex")["Survived"].mean()
print(survival)

# 9. 保存
df.to_csv("titanic_cleaned.csv", index=False)