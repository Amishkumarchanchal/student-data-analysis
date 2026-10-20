import pandas as pd

# 1. REad student data
df=pd.read_csv("CSV/students.csv")
print("=== STUDENT DATA ===")
print(df)

# 2. Calculate statistics
print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

# 3. Students scoring above 80
print("\n=== STUDENTS ABOVE 80 ===")
print(df[df["Marks"] > 80])

# 4. Rank students by marks
print("\n=== RANKING ===")
ranking = df.sort_values(
    by="Marks", ascending=False
)
print(ranking)

# 5. Save the ranking
ranking.to_csv("CSV/student_ranking.csv", index=False)
print("\nRanking saved successfully!")