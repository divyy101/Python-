import pandas as pd

students = pd.Series({
    "name": ["bandhan", "div", "aksh", "abhi", "saurabh"],
    "city": ["unnao", "kanpur", "basti", "lucknow", "bihar"],
    "marks": [18, 20, 60, 40, 90]
})


def count_50(s):
    return sum(m >= 50 for m in s["marks"])


def average(s):
    return sum(s["marks"]) / len(s["marks"])


def above_50(s):
    return [n for n, m in zip(s["name"], s["marks"]) if m > 50]


def from_lucknow(s):
    return [n for n, c in zip(s["name"], s["city"]) if c == "lucknow"]


print(students)

print("Students with 50 or above:", count_50(students))
print("Average marks:", average(students))
print("Students above 50:", above_50(students))
print("Students from Lucknow:", from_lucknow(students)) 