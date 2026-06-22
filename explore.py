import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("archive (4)/placement-dataset.csv")


placement_counts = df["placement"].value_counts()

plt.figure(figsize=(7,7))
plt.pie(
    placement_counts,
    labels=["Not Placed", "Placed"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Placement Distribution")
plt.show()

cgpa_bins = pd.cut(
    df["cgpa"],
    bins=[0, 5, 6, 7, 8, 10],
    labels=["<5", "5-6", "6-7", "7-8", "8+"]
)
cgpa_placement = df.groupby(cgpa_bins, observed=False)["placement"].sum()

plt.figure(figsize=(8,5))
cgpa_placement.plot(kind="bar")
plt.title("Placed Students by CGPA Range")
plt.xlabel("CGPA Range")
plt.ylabel("Number of Placed Students")
plt.xticks(rotation=0)
plt.show()


city_placement = df.groupby("city")["placement"].sum()

plt.figure(figsize=(8,5))
city_placement.plot(kind="bar")
plt.title("Placed Students by City")
plt.xlabel("City")
plt.ylabel("Number of Placed Students")
plt.xticks(rotation=45)
plt.show()


numeric_df = df[["cgpa", "iq", "placement"]]

corr = numeric_df.corr()

plt.figure(figsize=(6,5))
plt.imshow(corr)
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        plt.text(
            j,
            i,
            round(corr.iloc[i, j], 2),
            ha="center",
            va="center"
        )

plt.title("Correlation Heatmap")
plt.show()