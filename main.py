def show_tips():
    print("\nSafety Tips:")
    print("- Never share OTP or PIN with anyone")
    print("- Do not scan QR codes to receive money")
    print("- Always verify UPI IDs before sending money")
    print("- Avoid clicking unknown links")
    print("- Do not approve unknown collect requests\n")


def check_fraud():
    print("\nEnter Transaction Details")

    sender_known = input("Is the sender known? (yes/no): ").lower()
    transaction_type = input("Transaction type (send/request/scan): ").lower()
    urgency = input("Is there urgency or pressure? (yes/no): ").lower()

    print("\nAnalyzing transaction...\n")

    if sender_known == "no" and transaction_type == "request":
        print("Warning: Unknown sender requesting money. Possible fraud")
    
    elif transaction_type == "scan":
        print("Warning: Scanning QR codes usually means you are paying money")
    
    elif urgency == "yes":
        print("Warning: Fraudsters often create urgency to trick users")
    
    else:
        print("Transaction appears safe. Proceed carefully")

    show_tips()


def main():
    print("UPI Fraud Detection and Awareness System")

    while True:
        print("\nMenu:")
        print("1. Check a transaction")
        print("2. View safety tips")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            check_fraud()
        elif choice == "2":
            show_tips()
        elif choice == "3":
            print("Exiting")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
