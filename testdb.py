import sqlite3

conn = sqlite3.connect("recipes.db")

print("RECIPES")
for row in conn.execute("PRAGMA table_info(recipes)"):
    print(row)

print("\nINGREDIENTS")
for row in conn.execute("PRAGMA table_info(ingredients)"):
    print(row)

conn.close()