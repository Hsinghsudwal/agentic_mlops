import pandas as pd
import numpy as np

np.random.seed(42)

# Number of samples
n_samples = 1000

# Numeric features
numeric_data = np.random.randn(n_samples, 10)  # 10 numeric features
numeric_cols = [f"num_feat_{i}" for i in range(10)]

# Categorical features
categories = ["A", "B", "C", "D"]
cat_data = np.random.choice(categories, size=(n_samples, 3))
cat_cols = ["cat_feat_1", "cat_feat_2", "cat_feat_3"]

# Binary labels (optional)
labels = np.random.choice([0, 1], size=n_samples)

# Combine into DataFrame
df = pd.DataFrame(numeric_data, columns=numeric_cols)
for i, col in enumerate(cat_cols):
    df[col] = cat_data[:, i]

df["label"] = labels

# Save CSV for testing
df.to_csv("data/sample.csv", index=False)

# print(df.head())
print(f"Generated dataset with {len(df)} rows and {len(df.columns)} columns")
