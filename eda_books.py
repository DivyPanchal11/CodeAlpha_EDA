import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================
# LOAD DATASET
# ==========================

df = pd.read_csv("books_data.csv")

print("=" * 50)
print("FIRST 5 ROWS")
print("=" * 50)
print(df.head())

# ==========================
# DATASET INFORMATION
# ==========================

print("\n" + "=" * 50)
print("DATASET INFO")
print("=" * 50)
print(df.info())

print("\n" + "=" * 50)
print("DATASET SHAPE")
print("=" * 50)
print(df.shape)

print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())

# ==========================
# CLEAN PRICE COLUMN
# ==========================

print("\nOriginal Price Values:")
print(df["Price"].head())

# Extract only numbers from the price
df["Price"] = df["Price"].str.extract(r'(\d+\.\d+)')
df["Price"] = df["Price"].astype(float)

print("\nCleaned Price Values:")
print(df["Price"].head())

# ==========================
# STATISTICAL SUMMARY
# ==========================

print("\n" + "=" * 50)
print("STATISTICAL SUMMARY")
print("=" * 50)
print(df["Price"].describe())

# ==========================
# MOST EXPENSIVE BOOK
# ==========================

most_expensive = df.loc[df["Price"].idxmax()]

print("\n" + "=" * 50)
print("MOST EXPENSIVE BOOK")
print("=" * 50)
print(most_expensive)

# ==========================
# CHEAPEST BOOK
# ==========================

cheapest = df.loc[df["Price"].idxmin()]

print("\n" + "=" * 50)
print("CHEAPEST BOOK")
print("=" * 50)
print(cheapest)

# ==========================
# AVERAGE PRICE
# ==========================

avg_price = df["Price"].mean()

print("\n" + "=" * 50)
print("AVERAGE PRICE")
print("=" * 50)
print(round(avg_price, 2))

# ==========================
# VISUALIZATIONS
# ==========================

sns.set_style("whitegrid")

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=10)
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.savefig("histogram_price_distribution.png")
plt.show()

# Box Plot
plt.figure(figsize=(8, 5))
sns.boxplot(y=df["Price"])
plt.title("Book Price Box Plot")
plt.savefig("boxplot_price.png")
plt.show()

# Top 10 Expensive Books
top10 = df.sort_values(by="Price", ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(
    x="Price",
    y="Title",
    data=top10
)

plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.tight_layout()
plt.savefig("top10_expensive_books.png")
plt.show()

# ==========================
# CONCLUSION
# ==========================

print("\n" + "=" * 50)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 50)

print(f"\nTotal Books: {len(df)}")
print(f"Average Price: £{avg_price:.2f}")
print(f"Highest Price: £{df['Price'].max():.2f}")
print(f"Lowest Price: £{df['Price'].min():.2f}")