from matplotlib import pyplot as plt 

# matplot is used for data visualization.
# Here simple plot is created using matplotlib to show sales through years.

years = [2000, 2001, 2002, 2003]
sales = [2.5, 3.3, 3.2, 4.1]

plt.plot(years, sales, color="purple", linestyle="solid")
plt.title("Sales by Years")

plt.xlabel("Years")
plt.ylabel("Sales")

plt.show()