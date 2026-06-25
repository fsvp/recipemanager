from database import get_connection

conn = get_connection()

recipes = conn.execute(
    "SELECT * FROM recipes"
).fetchall()

for recipe in recipes:
    print(dict(recipe))

conn.close()