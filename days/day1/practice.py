def exercise_7():
    print("\n" + "=" * 50)
    print("  EXERCISE 7: Mini Project — Contact Book")
    print("=" * 50)

    # Our "database" — a list of dictionaries
    contacts = []

    def add_contact(name, phone, city="Unknown", email="Unknown"):
        contact = {"name": name, "phone": phone, "city": city, "email": email}
        contacts.append(contact)
        return contact

    def find_contact(name):
        for contact in contacts:
            if contact["name"].lower() == name.lower():
                return contact
        return None

    def delete_contact(name):
        for i in contacts:
            if i["name"].lower() == name.lower():
                contacts.remove(i)
                return True
        return False

    def display_all():
        if not contacts:
            print("    No contacts yet!")
            return
        print(f"    {'Name':<15} {'Phone':<15} {'City':<10} {'Email':<25}")
        print(f"    {'─'*15} {'─'*15} {'─'*10} {'─'*10}")
        for c in contacts:
            print(f"    {c['name']:<15} {c['phone']:<15} {c['city']:<10} {c['email']:<25}")

    # Add some contacts
    add_contact("Lucky", "9876543210", "Delhi","luckyyadav2344@gmail.com")
    add_contact("Rahul", "9123456789", "Mumbai")
    add_contact("Priya", "9988776655", "Bangalore")
    add_contact("Amit", "9112233445")  # city defaults to "Unknown"

    # Display all
    print("\n  All contacts:")
    display_all()
    print(f"contact deleted:{delete_contact('amit')}")
    print("\n  All contacts:")
    display_all()
    # Search
    search_name = "Rahul"
    result = find_contact(search_name)
    if result:
        print(f"\n  🔍 Found: {result['name']} — {result['phone']} ({result['city']}) ({result['email']})")
    else:
        print(f"\n  🔍 '{search_name}' not found.")

    # Count contacts per city
    city_count = {}
    for c in contacts:
        city = c["city"]
        city_count[city] = city_count.get(city, 0) + 1

    print(f"\n  📊 Contacts per city:")
    for city, count in city_count.items():
        print(f"    {city}: {count}")

    def save_contacts():
        with open("contacts.txt", "w") as f:
            for c in contacts:
                f.write(f"{c['name']}, {c['phone']}, {c['city']}, {c['email']}\n")
     
    print(f"contact saved:{save_contacts()}")

    print("\n  ✅ You just built a mini app using lists, dicts, "
          "functions, loops, and f-strings!")
          

exercise_7()