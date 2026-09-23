# Week 3 Lab: Modular Inventory Auditor

def get_valid_input():
    user_input = input("Enter stock quantity: ").strip()
    
    if user_input.lower() == "quit":
        return "quit"
    
    if user_input.isdigit():
        quantity = int(user_input)
        return quantity
    else:
        print("Error: '" + user_input + "' is not a valid number.")
        return -1

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print("\n=== FINAL REPORT ===")
    print("Total Units Processed : " + str(total_units))
    print("Rejected Entries      : " + str(failed_attempts))

# Main program
total_inventory = 0
rejected_entries = 0
total_tax = 0.0

print("=== Inventory Auditor ===")
print("Enter stock quantities (or type 'quit' to exit).")
print("Max capacity: 500 units\n")

while True:
    result = get_valid_input()
    
    if result == "quit":
        break
    
    if result == -1:
        rejected_entries = rejected_entries + 1
        continue
    
    if result < 0:
        print("Error: Negative values are not allowed.")
        rejected_entries = rejected_entries + 1
        continue
    
    total_inventory = process_delivery(total_inventory, result)
    tax = calculate_tax(result)
    total_tax = total_tax + tax
    print("Added " + str(result) + ". Current total: " + str(total_inventory))
    print("Tax for this delivery: " + str(tax))
    
    if total_inventory > 500:
        print("ALERT: Inventory exceeded 500 units! Total = " + str(total_inventory))
        break

generate_report(total_inventory, rejected_entries)