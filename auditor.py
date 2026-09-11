# Week 2 Lab: Flow Control

# Requirement 1: Initialize inventory to zero
total_inventory = 0
rejected_entries = 0

print("=== Inventory Auditor ===")
print("Enter stock quantities (or type 'quit' to exit).")
print("Max capacity: 500 units\n")

# Requirement 2: Continuous loop until user types 'quit'
while True:
    user_input = input("Enter stock quantity: ").strip()

    # Requirement 8: Handle quit
    if user_input.lower() == "quit":
        break

    # Requirement 4: Reject non-numeric input
    if not user_input.isdigit():
        print(f" Error: '{user_input}' is not a valid number.\n")
        rejected_entries += 1
        continue

    quantity = int(user_input)

    # Requirement 5: Reject negative numbers
    if quantity < 0:
        print(" Error: Negative values are not allowed.\n")
        rejected_entries += 1
        continue

    # Requirement 6: Update running total
    total_inventory += quantity
    print(f" Added {quantity}. Current total: {total_inventory}\n")

    # Requirement 7: Overstock alert
    if total_inventory > 500:
        print(f" ALERT: Inventory exceeded 500 units! Total = {total_inventory}")
        break

# Requirement 8: Final report
print("\n=== FINAL REPORT ===")
print(f"Total Units Processed : {total_inventory}")
print(f"Rejected Entries      : {rejected_entries}")