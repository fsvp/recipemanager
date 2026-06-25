from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import get_connection

app = Flask(__name__)
app.secret_key = "secret123"

USERNAME = "admin"
PASSWORD = "recipe123"


@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("recipe_form"))
        else:
            flash("Invalid username or password")

    return render_template("login.html")

@app.route("/delete/<int:recipe_id>", methods=["POST"])
def delete_recipe(recipe_id):

    if not session.get("logged_in"):
        return redirect(url_for("login"))

    conn = get_connection()

    conn.execute(
        "DELETE FROM recipes WHERE id = ?",
        (recipe_id,)
    )

    conn.commit()
    conn.close()

    flash("Recipe deleted successfully!")

    return redirect(url_for("recipe_list"))
@app.route("/recipe", methods=["GET", "POST"])
def recipe_form():

    if not session.get("logged_in"):
        return redirect(url_for("login"))

    conn = get_connection()

    ingredients = conn.execute(
        "SELECT * FROM ingredients ORDER BY ingredient_name"
    ).fetchall()

    field_errors = {}

    if request.method == "POST":

        recipe_name = request.form.get("recipe_name", "").strip()
        preparation_steps = request.form.get("preparation_steps", "").strip()
        serves = request.form.get("serves", "").strip()

        ingredient_lines = []
        selected_count = 0
        total_calories = 0
        selected_ingredient_ids = []

        if len(recipe_name) < 3:
            field_errors["recipe_name"] = "Recipe Name is required and must contain at least 3 characters."

        existing_recipe = conn.execute(
            "SELECT id FROM recipes WHERE LOWER(recipe_name) = LOWER(?)",
            (recipe_name,)
        ).fetchone()

        if existing_recipe:
            field_errors["recipe_name"] = f"Recipe Name '{recipe_name}' already exists. Please enter a different recipe name."

        if not preparation_steps:
            field_errors["preparation_steps"] = "Preparation Steps cannot be empty."

        elif preparation_steps.isdigit():
            field_errors["preparation_steps"] = "Preparation Steps must contain meaningful text and cannot be only numbers."

        if not serves.isdigit() or int(serves) <= 0:
            field_errors["serves"] = "Serves must be a whole number greater than 0."

        for i in range(1, 11):

            ingredient_id = request.form.get(f"ingredient{i}")
            quantity = request.form.get(f"quantity{i}", "").strip()

            if ingredient_id:

                if ingredient_id in selected_ingredient_ids:
                    ingredient = conn.execute(
                        "SELECT ingredient_name FROM ingredients WHERE id = ?",
                        (ingredient_id,)
                    ).fetchone()

                    field_errors[f"ingredient{i}"] = f"Ingredient '{ingredient['ingredient_name']}' has already been selected."
                    continue

                selected_ingredient_ids.append(ingredient_id)
                selected_count += 1

                ingredient = conn.execute(
                    "SELECT * FROM ingredients WHERE id = ?",
                    (ingredient_id,)
                ).fetchone()

                ingredient_name = ingredient["ingredient_name"]

                try:
                    qty = float(quantity)

                    if qty <= 0:
                        raise ValueError()

                    ingredient_calories = (
                        qty / ingredient["base_quantity"]
                    ) * ingredient["calorific_value"]

                    total_calories += ingredient_calories

                    ingredient_lines.append(
                        f"{ingredient_name} - {qty}g"
                    )

                except:
                    field_errors[f"quantity{i}"] = f"Quantity for {ingredient_name} must be a number greater than 0."

        if selected_count < 2:
            field_errors["ingredients"] = "Please select at least 2 ingredients."

        if not field_errors:

            ingredient_text = "\n".join(ingredient_lines)
            calorie_per_person = total_calories / int(serves)

            conn.execute(
                """
                INSERT INTO recipes
                (
                    recipe_name,
                    ingredient_list,
                    preparation_steps,
                    serves,
                    total_calories,
                    calorie_per_person
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    recipe_name,
                    ingredient_text,
                    preparation_steps,
                    int(serves),
                    round(total_calories, 2),
                    round(calorie_per_person, 2)
                )
            )

            conn.commit()

            flash(
                f"Recipe '{recipe_name}' saved successfully! "
                f"Total Calories: {total_calories:.2f} kcal | "
                f"Calorie Per Person: {calorie_per_person:.2f} kcal"
            )

            conn.close()
            return redirect(url_for("recipe_form"))

    conn.close()

    return render_template(
        "recipe_form.html",
        ingredients=ingredients,
        field_errors=field_errors
    )
@app.route("/recipes")
def recipe_list():

    if not session.get("logged_in"):
        return redirect(url_for("login"))

    conn = get_connection()

    recipes = conn.execute(
        "SELECT * FROM recipes ORDER BY created_at DESC"
    ).fetchall()

    conn.close()

    return render_template(
        "recipe_list.html",
        recipes=recipes
    )


@app.route("/ingredients")
def ingredient_list():

    if not session.get("logged_in"):
        return redirect(url_for("login"))

    conn = get_connection()

    ingredients = conn.execute(
        "SELECT * FROM ingredients ORDER BY ingredient_name"
    ).fetchall()

    conn.close()

    return render_template(
        "ingredient_list.html",
        ingredients=ingredients
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)