import pandas as pd

x = ['a', 'b', 'c', 'd', 'e']

series_x = pd.Series(x, index=["letra1", "letra2", "letra3", "letra4", "letra5"])
print(series_x)

print(series_x['letra1'])

record = {
    'Name': ['Andre', 'Victor', 'Pedro', 'Seb', 'Rafael'],
    'Age': [30, 50, 90, 13, 41],
    'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Commerce'],
    'Percentage': [88, 91, 45, 87, 100]
}

df = pd.DataFrame(record)

print(df)

print(df["Stream"][1])

# Colocando nome na coluna
x = df["Name"]
print(x)

x = df[["Name"]]
print(x)

# Selecionando linha
x = df.loc[0]
print(x)

x = df.loc[[0]]
print(x)


# Selecionando através de condições

x = df.loc[df.Age > 20]
print(x)

x = df.loc[df.Age > 20]['Name'] #Somente os nomes
print(x)


for g in df.index:
    print(df.Name[g])



