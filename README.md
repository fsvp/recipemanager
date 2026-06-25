# Recipe Management & Calorie Calculation Web Application

## Project Description

This is a Flask-based web application for managing recipes and calculating calorie values based on selected ingredients and their quantities.

The application includes login authentication, session protection, recipe entry, calorie calculation, recipe listing, and ingredient listing.

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- Bootstrap 5

## Default Login Credentials

Username: admin  
Password: recipe123

## Database Name

recipes.db

## Features

- Login page with hard-coded credentials
- Session-based authentication
- Logout functionality
- Protected pages
- Recipe entry form
- 10 ingredient selection rows
- Dynamic ingredient dropdowns from database
- Server-side validations
- Automatic calorie calculation
- Calorie per person calculation
- Recipe list page
- Ingredient list page
- Bootstrap styled user interface

## Validations Implemented

- Recipe name is required
- Recipe name must contain at least 3 characters
- Recipe name must be unique
- At least 2 ingredients must be selected
- Duplicate ingredients are not allowed
- Quantity must be a number greater than 0
- Preparation steps cannot be empty
- Preparation steps cannot contain only numbers
- Serves must be a whole number greater than 0

## Calorie Calculation Formula

For each ingredient:

```text
ingredient_calories = (quantity_used / base_quantity) * calorific_value