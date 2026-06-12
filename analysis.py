import pandas as pd    #Loads the Pandas library
import matplotlib.pyplot as plt  #loads matplot library
df = pd.read_csv("data/sales.csv")  #Reads the CSV file into a DataFrame (like an Excel sheet in Python).
                                            #df["Sales"] --> Selects the Sales column.
print("Total Sales:", df["Sales"].sum())    #add all sales
print("Average Sales:", df["Sales"].mean()) #average of sales
print("Highest Sale:", df["Sales"].max())   #finds maxm sale value

#Which category generated more revenue?
category_sales = df.groupby("Category")["Sales"].sum()  
            #Groups all rows by category #Adds sales within each category
print("\nSales by Category:")
print(category_sales)

plt.figure(figsize=(8,5))

ax = category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

for value in ax.containers:
    ax.bar_label(value)

plt.grid(axis='y')
plt.tight_layout()

plt.savefig("sales_chart.png")
plt.show()
