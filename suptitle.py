import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])

y1 = np.array([10, 20, 15, 25, 30])
y2 = np.array([5, 15, 10, 20, 25])
y3 = np.array([20, 15, 25, 10, 30])
y4 = np.array([8, 12, 18, 15, 25])

# Common fonts
title_font = 14
label_font = 11

plt.figure(figsize=(10, 8))

# Super Title
plt.suptitle(
    "Student Performance Analysis",
    color="red",
    fontsize=22,
    fontname="Comic Sans MS",
    fontweight="bold"
)

# ---------------- Graph 1 ----------------
plt.subplot(2, 2, 1)

plt.plot(x, y1, 'o-')

plt.title(
    "Monthly Sales",
    fontsize=title_font,
    fontname="Arial",
    fontweight="bold"
)

plt.xlabel(
    "Month",
    fontsize=label_font,
    fontname="Arial"
)

plt.ylabel(
    "Sales",
    fontsize=label_font,
    fontname="Arial"
)

plt.grid(color="red")


# ---------------- Graph 2 ----------------
plt.subplot(2, 2, 2)

plt.plot(x, y2, 'o-')

plt.title(
    "Monthly Profit",
    fontsize=title_font,
    fontname="Arial",
    fontweight="bold"
)

plt.xlabel(
    "Month",
    fontsize=label_font,
    fontname="Arial"
)

plt.ylabel(
    "Profit",
    fontsize=label_font,
    fontname="Arial"
)

plt.grid(color="green")


# ---------------- Graph 3 ----------------
plt.subplot(2, 2, 3)

plt.bar(x, y3)

plt.title(
    "Monthly Expenses",
    fontsize=title_font,
    fontname="Arial",
    fontweight="bold"
)

plt.xlabel(
    "Month",
    fontsize=label_font,
    fontname="Arial"
)

plt.ylabel(
    "Expenses",
    fontsize=label_font,
    fontname="Arial"
)

plt.grid(axis="y", color="yellow")


# ---------------- Graph 4 ----------------
plt.subplot(2, 2, 4)

labels = ["Python", "Java", "C++", "JavaScript"]
values = [30, 25, 20, 25]

plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title(
    "Programming Skills",
    fontsize=title_font,
    fontname="Arial",
    fontweight="bold"
)

# Pie chart doesn't have X/Y axis
plt.grid(color="pink")


plt.tight_layout(rect=[0, 0, 1, 0.93])

plt.show()