voters = set()
voters.add("Esther")
voters.add("Susan")
voters.add("Oba")
while True:
    voter = input("Enter your name: ").strip()
    try:
        if voter.title() == "Finalized":
            break
        if voter in voters:
                print(f"Beware, '{voter}' name already exists")
        else:
                voters.add(voter)
                print(f"Congrats, '{voter}' you have registered")
        print("\nSuccessfully registered")
        print(f"All unique voters: {len(voters)}")
    except:
        print("Unexpected error")