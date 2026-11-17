
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# Create Dataset
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2015, 2017, 2019, 2021,
             2016, 2018, 2020, 2021, 2014, 2017, 2019, 2022, 2016, 2020],
    'Kilometers': [50000, 45000, 40000, 35000, 30000, 20000, 70000, 55000,
                   25000, 15000, 60000, 38000, 22000, 10000, 80000, 48000,
                   28000, 8000, 65000, 18000],
    'Price': [350000, 400000, 450000, 500000, 600000, 700000, 300000,
              420000, 650000, 800000, 330000, 520000, 750000, 900000,
              250000, 430000, 620000, 1000000, 310000, 780000]
}

df = pd.DataFrame(data)

# Input and Output
X = df[['Year', 'Kilometers']]
y = df['Price']

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Model Evaluation
predictions = model.predict(X_test)

print("R2 Score:", round(r2_score(y_test, predictions), 2))
print("Mean Absolute Error:", round(mean_absolute_error(y_test, predictions), 2))

# Take User Input
year = int(input("Enter car manufacturing year: "))
km = float(input("Enter kilometers driven: "))

# Predict Car Price
result = model.predict([[year, km]])

print("\nPredicted Used Car Price: Rs.", round(result[0], 2))

# Visualization
plt.scatter(df['Year'], df['Price'], color='blue')
plt.xlabel("Manufacturing Year")
plt.ylabel("Car Price")
plt.title("Used Car Price Dataset")
plt.grid()
plt.show()
