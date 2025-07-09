### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount in ingredients.items():
            if self.machine_resources.get(item, 0) < amount:
                print(f"Sorry there is not enough {item}.")
                return False
            return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins")
        try:
            dollars = int(input("How many large dollars?:")) * 1.00
            half_dollars = int(input("How many half dollars?: ")) * .50
            quarters = int(input("How many quarters?: ")) * .25
            nickels = int(input("How many half nickels?: ")) * .05
        except ValueError:
            print("Invalid input.")
            return 0.0
        return round(dollars + half_dollars + quarters + nickels, 2)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("C'mon now that's not enough money. Money will be refunded.")
            return False
        change = round(coins - cost, 2)
        print(f"Here is ${change:.2f} in change.")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
            print(f"{sandwich_size} sandwich is done. Enjoy!")

    def show_report(self):
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print(f"Ham: {self.machine_resources['ham']} slice(s)")
        print(f"Cheese: {self.machine_resources['cheese']} pound(s)")

### Make an instance of SandwichMachine class and write the rest of the codes ###

def run_machine():
    machine = SandwichMachine(resources)
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()
        if choice == "off":
            break
        elif choice == "report":
            machine.show_report()
        elif choice in recipes:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if machine.check_resources(ingredients):
                coins = machine.process_coins()
                if machine.transaction_result(coins, cost):
                    machine.make_sandwich(choice, ingredients)
        else:
            print("Invalid selection. Please choose from (small/ medium/ large/ off/ report).")
run_machine()