import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("EducationDataset_2023-24.csv")

# Information about dataset
print(df.info())
print(df.head())


# Q1. Highest and lowest number of schools

print("\nQ1")

max_schools = df["No of Schools - Total"].max()
min_schools = df["No of Schools - Total"].min()

print("Highest number of schools:", max_schools)
print("Lowest number of schools:", min_schools)

print("District with highest schools:",
      df["District"][df["No of Schools - Total"] == max_schools].values)

print("District with lowest schools:",
      df["District"][df["No of Schools - Total"] == min_schools].values)


# Q2. Highest total student enrollment

print("\nQ2")

max_students = df["No of Students - Total"].max()

print("Highest student enrollment:", max_students)

print("District:",
      df["District"][df["No of Students - Total"] == max_students].values)


# Q3. Largest gender difference

print("\nQ3")

difference = np.abs(
    df["No of Students - Boys"] -
    df["No of Students - Girls"]
)

max_difference = difference.max()

print("Largest gender difference:", max_difference)

print("District:",
      df["District"][difference == max_difference].values)


# Graph: Boys vs Girls

plt.plot(
    df["District"],
    df["No of Students - Boys"],
    label="Boys"
)

plt.plot(
    df["District"],
    df["No of Students - Girls"],
    label="Girls"
)

plt.xlabel("District")
plt.ylabel("Students")
plt.title("Boys vs Girls")

plt.xticks(rotation=45)
plt.legend()
plt.grid()

plt.show()



print("\nQ4")

class10 = " PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"

max_class10 = df[class10].max()

print("Highest Class X pass percentage:", max_class10)

print("District:",
      df["District"][df[class10] == max_class10].values)


# Q5. Highest Class XII pass percentage

print("\nQ5")

class12 = " PASS PERCENTAGE IN CLASS XII - \n(Before Compt.) - 2023-24"

max_class12 = df[class12].max()

print("Highest Class XII pass percentage:", max_class12)

print("District:",
      df["District"][df[class12] == max_class12].values)


# Q6. Compare Class X and Class XII

print("\nQ6")

plt.plot(
    df["District"],
    df[class10],
    label="Class X"
)

plt.plot(
    df["District"],
    df[class12],
    label="Class XII"
)

plt.xlabel("District")
plt.ylabel("Pass Percentage")
plt.title("Class X vs Class XII")

plt.xticks(rotation=45)
plt.legend()
plt.grid()

plt.show()


# Q7. Schools vs Class X pass percentage

print("\nQ7")

plt.scatter(
    df["No of Schools - Total"],
    df[class10]
)

plt.xlabel("Number of Schools")
plt.ylabel("Class X Pass Percentage")
plt.title("Schools vs Class X Pass Percentage")

plt.grid()
plt.show()

correlation = np.corrcoef(
    df["No of Schools - Total"],
    df[class10]
)

print("Correlation:")
print(correlation)


# Q8. Students vs Class X pass percentage

print("\nQ8")

plt.scatter(
    df["No of Students - Total"],
    df[class10]
)

plt.xlabel("Total Students")
plt.ylabel("Class X Pass Percentage")
plt.title("Students vs Class X Pass Percentage")

plt.grid()
plt.show()

correlation = np.corrcoef(
    df["No of Students - Total"],
    df[class10]
)

print("Correlation:")
print(correlation)


# Q9. Students per school

print("\nQ9")

df["Students Per School"] = (
    df["No of Students - Total"] /
    df["No of Schools - Total"]
)

max_ratio = df["Students Per School"].max()

print("Highest students per school:", max_ratio)

print("District:",
      df["District"][
          df["Students Per School"] == max_ratio
      ].values)

print("Correlation with Class X:")

print(
    np.corrcoef(
        df["Students Per School"],
        df[class10]
    )
)


# Graph

plt.bar(
    df["District"],
    df["Students Per School"]
)

plt.xlabel("District")
plt.ylabel("Students Per School")
plt.title("Students Per School")

plt.xticks(rotation=45)
plt.grid()

plt.show()


# Q10. Three observations

print("\nQ10")

print("1. Highest student enrollment:",
      df["No of Students - Total"].max())

print("2. Highest Class X pass percentage:",
      df[class10].max())

print("3. Highest students per school:",
      df["Students Per School"].max())