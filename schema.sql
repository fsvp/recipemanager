CREATE TABLE ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_name TEXT UNIQUE NOT NULL,
    base_quantity REAL NOT NULL,
    calorific_value REAL NOT NULL
);

CREATE TABLE recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_name TEXT NOT NULL,
    ingredient_list TEXT NOT NULL,
    preparation_steps TEXT NOT NULL,
    serves INTEGER NOT NULL,
    total_calories REAL NOT NULL,
    calorie_per_person REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO ingredients
(ingredient_name, base_quantity, calorific_value)
VALUES
('Rice (cooked)',100,130),
('Chicken Breast',100,165),
('Whole Egg',100,155),
('Olive Oil',100,884),
('Onion',100,40),
('Tomato',100,18),
('Potato',100,77),
('Lentils (cooked)',100,116),
('Milk (whole)',100,61),
('Butter',100,717);