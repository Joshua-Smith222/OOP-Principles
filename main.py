# main.py
from budget_category import BudgetCategory  # Importing the BudgetCategory class

def main():
    # Create a BudgetCategory object
    food_category = BudgetCategory("Food", 500)

    # Adding some expenses
    food_category.add_expense(100)
    food_category.add_expense(50)

    # Display the category summary
    food_category.display_category_summary()

    # Modify the allocated budget
    food_category.set_allocated_budget(600)
    food_category.display_category_summary()

    # Try adding an invalid expense
    food_category.add_expense(-30)  # This should trigger validation

if __name__ == "__main__":
    main()
