import cashier
import data
import sandwich_maker

recipes = data.recipes
resources = data.resources

maker = sandwich_maker.SandwichMaker(resources)
cashier_obj = cashier.Cashier()

def main():
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

        if choice == "off":
            break
        elif choice == "report":
            maker.print_report()
        elif choice in recipes:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if maker.check_resources(ingredients):
                coins = cashier_obj.process_coins()
                if cashier_obj.transaction_result(coins, cost):
                    maker.make_sandwich(choice, ingredients)
        else:
            print("Invalid selection. Please choose from (small/ medium/ large/ off/ report).")

# Start the program
if __name__ == "__main__":
    main()