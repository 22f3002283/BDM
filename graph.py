import pandas as pd
import matplotlib.pyplot as p
df=pd.read_csv("graded_sales.csv")
import numpy as np

p.figure(figsize=(8,5))
colors = ['#f94144', '#f8961e', '#43aa8b', '#577590']
revenue= "revenue of sales "
quantity='Quantity of sales '
profit="Profit"
for (month, group), color in zip(df.groupby("Catagory"), colors):

    # scatter points
    x = group["Unit Price of sales"]
    y = group[profit]
    #p.scatter(x, y, s=40, alpha=0.7, edgecolor='black', label=f"{month} (data)")


    p.scatter(group["Unit Price of sales"],
              group[profit],
              label=f"{month} (data)",
              s=40, edgecolor='black', alpha=0.7, color=color)

    # fit a linear trendline: y = m*x + b
    # 
    coeffs = np.polyfit(x, y,1)       # ← linear fit
    x_fit = np.linspace(x.min(), x.max(), 100)
    y_fit = np.polyval(coeffs, x_fit)
    p.plot(x_fit, y_fit, '--', label=f"{month} linear fit",color=color)

p.title("Unit Price vs profit by Category")
p.xlabel("Unit Price of Sales (₹)")
p.ylabel("quantity ")
p.legend(title="Catagory", bbox_to_anchor=(1.05, 1), loc='upper left')
p.grid(True, linestyle='--', alpha=0.6)
p.tight_layout()
p.show()