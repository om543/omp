# Simple Customer Interaction Chatbot in Python

print("===== Welcome to Customer Support Chatbot =====")

while True:

    print("\n1. Product Information")
    print("2. Order Status")
    print("3. Return Policy")
    print("4. Contact Support")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nWe provide laptops, mobiles, and accessories.")

    elif choice == '2':
        order_id = input("Enter your Order ID: ")
        print("Order", order_id, "is currently being processed.")

    elif choice == '3':
        print("\nProducts can be returned within 7 days of delivery.")

    elif choice == '4':
        print("\nContact us at support@email.com")
        print("Phone: 9876543210")

    elif choice == '5':
        print("\nThank you for using the chatbot!")
        break

    else:
        print("\nInvalid choice! Please try again.")
