from database import get_connection

conn = get_connection()

conn.execute("""
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_name TEXT UNIQUE NOT NULL,
    base_quantity REAL NOT NULL,
    calorific_value REAL NOT NULL
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_name TEXT NOT NULL,
    ingredient_list TEXT NOT NULL,
    preparation_steps TEXT NOT NULL,
    serves INTEGER NOT NULL,
    total_calories REAL NOT NULL,
    calorie_per_person REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.execute("INSERT OR IGNORE INTO ingredients (ingredient_name, base_quantity, calorific_value) VALUES ('Rice (cooked)',100,130)")
conn.execute("INSERT OR IGNORE INTO ingredients (ingredient_name, base_quantity, calorific_value) VALUES ('Chicken Breast',100,165)")
conn.execute("INSERT OR IGNORE INTO ingredients (ingredient_name, base_quantity, calorific_value) VALUES ('Whole Egg',100,155)")
conn.execute("INSERT OR IGNORE INTO ingredients (ingredient_name, base_quantity, calorific_value) VALUES ('Olive Oil',100,884)")
conn.execute("INSERT OR IGNORE INTO ingredients (ingredient_name, base_quantity, calorific_value) VALUES ('Onion',100,40)")
conn.execute("INSERT OR IGNORE INTO ingredients (ingredient_name, base_quantity, calorific_value) VALUES ('Tomato',100,18)")
conn.execute("INSERT OR IGNORE INTO ingredients (ingredient_name, base_quantity, calorific_value) VALUES ('Potato',100,77)")
conn.execute("INSERT OR IGNORE INTO ingredients (ingredient_name, base_quantity, calorific_value) VALUES ('Lentils (cooked)',100,116)")
conn.execute("INSERT OR IGNORE INTO ingredients (ingredient_name, base_quantity, calorific_value) VALUES ('Milk (whole)',100,61)")
conn.execute("INSERT OR IGNORE INTO ingredients (ingredient_name, base_quantity, calorific_value) VALUES ('Butter',100,717)")

conn.commit()
conn.close()

print("Database tables created successfully!")