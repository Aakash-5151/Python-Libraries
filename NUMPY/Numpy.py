import numpy as np
import matplotlib.pyplot as plt

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])


print("==== Zomato sales analysis ====")
print("\n Sales data shape", sales_data.shape)

# print("\n Sample data for 1st 3 restaurant: ", sales_data[0:3]) 
print("\n", sales_data[:, 1:]) #sales_data(row, column)

#Total sales per year

# print(np.sum(sales_data, axis=0))

#Yearly total per year
yearly_total = np.sum(sales_data[:, 1:], axis=0)
# print(yearly_total, "\n")

total_sales = np.sum(yearly_total)
# print(total_sales, "\n")

#Minimum sales per restaurant
min_sales = np.min(sales_data[:, 1:], axis= 1)
print(min_sales, "\n")

# Maximum sales per year
max_sales = np.max(sales_data[:, 1:], axis=0)
print(max_sales, "\n")

# Average sales data 
avg_sales = np.average(sales_data[:, 1:], axis=1)
# print(avg_sales)

cumulative_sum = np.cumsum(sales_data[:, 1:], axis=1)
print(cumulative_sum)

plt.figure(figsize= (10, 6))
plt.plot(np.mean(cumulative_sum, axis=1))
plt.title("Average cumulative sales per year accross all restaurent.")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
# plt.show()

vector1 = np.array([1,2, 3, 4, 5])
vector2 = np.array([6, 7, 8, 9, 10])

# print("Vector addition: ", vector1 + vector2)

# print("\n multiplication of vector: ", vector1*vector2)

print("\n dot product: ", np.dot(vector1, vector2))

# Vectorized operation
restaurant_types = np.array(['biryani', 'dalBhat', 'Rice', 'Panir', 'burger'])
vectorized_upper = np.vectorize(str.upper)

print("vectorized upper", vectorized_upper(restaurant_types))

monthly_avg = sales_data[:, 1:] / 12
print(monthly_avg)