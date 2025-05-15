# Verificar os valores nulos em df_sup
print("Colunas com valores nulos em df_sup:")
print(df_sup.isnull().sum())

# Analisar as colunas categóricas e numéricas
print("\nColunas categóricas:")
for col in cat_cols:
    print(f"{col}: {df_sup[col].isnull().sum()} valores nulos")

print("\nColunas numéricas:")
for col in num_cols:
    print(f"{col}: {df_sup[col].isnull().sum()} valores nulos")

# Verificar também os dados de treinamento
print("\nValores nulos em X_train:")
print(X_train.isnull().sum())
