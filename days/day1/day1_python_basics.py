"""
╔══════════════════════════════════════════════════════════════════╗
║  AI-Engineer-OS — Day 1: Python Fundamentals                     ║
║  Run: python scripts/day1_python_basics.py                       ║
║  No external packages needed — pure Python!                      ║
╚══════════════════════════════════════════════════════════════════╝

7 exercises. Read each one, understand it, then try modifying it.
"""


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCISE 1: Variables & Data Types
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def exercise_1():
    print("\n" + "=" * 50)
    print("  EXERCISE 1: Variables & Data Types")
    print("=" * 50)

    # Python figures out the type automatically — no need to declare it
    name = "Lucky"
    age = 21
    height = 5.9
    is_student = True
    favorite_tool = None  # None = "nothing yet"

    # type() tells you what something is
    print(f"  name        = {name}         → type: {type(name).__name__}")
    print(f"  age         = {age}           → type: {type(age).__name__}")
    print(f"  height      = {height}          → type: {type(height).__name__}")
    print(f"  is_student  = {is_student}       → type: {type(is_student).__name__}")
    print(f"  fav_tool    = {favorite_tool}       → type: {type(favorite_tool).__name__}")

    # Type conversion
    age_as_string = str(age)      # int → str
    height_as_int = int(height)   # float → int (drops decimal)
    print(f"\n  str(21)     = '{age_as_string}'  (now a string, not a number)")
    print(f"  int(5.9)    = {height_as_int}    (decimal gets chopped off)")

    print("\n  ✅ Python has 4 main types: str, int, float, bool")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCISE 2: Strings & f-strings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def exercise_2():
    print("\n" + "=" * 50)
    print("  EXERCISE 2: Strings & f-strings")
    print("=" * 50)

    first = "Lucky"
    last = "Yadav"

    # Concatenation (old way)
    full_name_old = first + " " + last

    # f-string (modern way — use this!)
    full_name = f"{first} {last}"

    print(f"  Full name   : {full_name}")
    print(f"  Uppercase   : {full_name.upper()}")
    print(f"  Lowercase   : {full_name.lower()}")
    print(f"  Length       : {len(full_name)} characters")
    print(f"  First char  : {full_name[0]}")
    print(f"  Last char   : {full_name[-1]}")
    print(f"  Slice [0:5] : {full_name[0:5]}")

    # Useful string methods
    email = "  lucky@example.com  "
    print(f"\n  Raw email   : '{email}'")
    print(f"  Stripped    : '{email.strip()}'")
    print(f"  Has '@'?    : {('@' in email)}")
    print(f"  Replace     : {email.strip().replace('example', 'gmail')}")

    print("\n  ✅ f-strings are your best friend for formatting output.")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCISE 3: Control Flow (if / elif / else)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def exercise_3():
    print("\n" + "=" * 50)
    print("  EXERCISE 3: Control Flow")
    print("=" * 50)

    score = 78

    # Basic if/elif/else
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"  Score: {score} → Grade: {grade}")

    # Combining conditions with and / or / not
    age = 21
    has_id = True

    if age >= 18 and has_id:
        print(f"  Age {age}, has ID → Access granted ✅")
    else:
        print(f"  Access denied ❌")

    # Ternary (one-liner if/else)
    status = "adult" if age >= 18 else "minor"
    print(f"  Status: {status}")

    # TRY IT: Change the score to 95, 45, 60 and re-run to see different outputs!

    print("\n  ✅ if/elif/else is how your code makes decisions.")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCISE 4: Loops
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def exercise_4():
    print("\n" + "=" * 50)
    print("  EXERCISE 4: Loops")
    print("=" * 50)

    # for loop — when you know how many times to repeat
    print("  for loop (counting 1 to 5):")
    for i in range(1, 6):
        print(f"    {i}", end=" ")
    print()

    # Looping through a list
    fruits = ["apple", "banana", "cherry", "date"]
    print("\n  Looping through fruits:")
    for fruit in fruits:
        print(f"    🍎 {fruit}")

    # enumerate — get both index AND value
    print("\n  enumerate (index + value):")
    for index, fruit in enumerate(fruits):
        print(f"    [{index}] {fruit}")

    # while loop — when you don't know how many times
    print("\n  while loop (doubling until > 100):")
    num = 1
    while num <= 100:
        print(f"    {num}", end=" ")
        num *= 2  # double it
    print()

    # break and continue
    print("\n  break & continue:")
    for i in range(1, 11):
        if i == 3:
            print(f"    {i} → skipped (continue)")
            continue  # skip this iteration
        if i == 7:
            print(f"    {i} → stopped (break)")
            break  # exit the loop entirely
        print(f"    {i}")

    print("\n  ✅ for = known iterations, while = unknown iterations.")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCISE 5: Functions
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def exercise_5():
    print("\n" + "=" * 50)
    print("  EXERCISE 5: Functions")
    print("=" * 50)

    # Basic function
    def greet(name):
        return f"Hello, {name}!"

    print(f"  {greet('Lucky')}")

    # Function with default parameter
    def power(base, exponent=2):
        return base ** exponent

    print(f"  power(3)    = {power(3)}")       # 3² = 9
    print(f"  power(3, 3) = {power(3, 3)}")    # 3³ = 27

    # Function that returns multiple values
    def get_stats(numbers):
        return min(numbers), max(numbers), sum(numbers) / len(numbers)

    data = [10, 20, 30, 40, 50]
    low, high, avg = get_stats(data)
    print(f"\n  Data: {data}")
    print(f"  Min: {low}, Max: {high}, Avg: {avg}")

    # Function with *args (variable number of arguments)
    def add_all(*numbers):
        return sum(numbers)

    print(f"\n  add_all(1, 2, 3)       = {add_all(1, 2, 3)}")
    print(f"  add_all(10, 20, 30, 40) = {add_all(10, 20, 30, 40)}")

    print("\n  ✅ Functions = reusable blocks of logic. Use them everywhere.")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCISE 6: Data Structures (List, Dict, Tuple, Set)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def exercise_6():
    print("\n" + "=" * 50)
    print("  EXERCISE 6: Data Structures")
    print("=" * 50)

    # ── LIST: ordered, mutable, allows duplicates ──
    print("\n  📋 LIST:")
    tools = ["Python", "Git", "Docker"]
    tools.append("FastAPI")          # add to end
    tools.insert(0, "VS Code")      # add at position 0
    print(f"    Tools: {tools}")
    print(f"    First: {tools[0]}, Last: {tools[-1]}")
    print(f"    Count: {len(tools)}")
    tools.remove("Git")
    print(f"    After removing Git: {tools}")

    # ── DICTIONARY: key-value pairs ──
    print("\n  📖 DICTIONARY:")
    student = {
        "name": "Lucky",
        "age": 21,
        "skills": ["Python", "AI"],
        "gpa": 9.2
    }
    print(f"    Name  : {student['name']}")
    print(f"    Skills: {student['skills']}")

    # Add / update
    student["university"] = "KIET"
    student["age"] = 22
    print(f"    Updated: {student}")

    # Safe access with .get()
    print(f"    Phone: {student.get('phone', 'Not provided')}")

    # Loop through dict
    print("    All keys:")
    for key, value in student.items():
        print(f"      {key}: {value}")

    # ── TUPLE: ordered, immutable ──
    print("\n  📌 TUPLE (can't be changed after creation):")
    coordinates = (28.6139, 77.2090)  # Delhi coordinates
    print(f"    Delhi: lat={coordinates[0]}, lon={coordinates[1]}")

    # ── SET: unordered, unique values only ──
    print("\n  🔗 SET (auto-removes duplicates):")
    languages = {"Python", "JavaScript", "Python", "Go", "Python"}
    print(f"    Unique languages: {languages}")
    print(f"    Has Python? {'Python' in languages}")

    print("\n  ✅ List = ordered collection, Dict = key-value, "
          "Tuple = fixed, Set = unique.")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCISE 7: Mini Project — Contact Book
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Combines EVERYTHING from today into one small program.

def exercise_7():
    print("\n" + "=" * 50)
    print("  EXERCISE 7: Mini Project — Contact Book")
    print("=" * 50)

    # Our "database" — a list of dictionaries
    contacts = []

    def add_contact(name, phone, city="Unknown"):
        contact = {"name": name, "phone": phone, "city": city}
        contacts.append(contact)
        return contact

    def find_contact(name):
        for contact in contacts:
            if contact["name"].lower() == name.lower():
                return contact
        return None

    def display_all():
        if not contacts:
            print("    No contacts yet!")
            return
        print(f"    {'Name':<15} {'Phone':<15} {'City':<10}")
        print(f"    {'─'*15} {'─'*15} {'─'*10}")
        for c in contacts:
            print(f"    {c['name']:<15} {c['phone']:<15} {c['city']:<10}")

    # Add some contacts
    add_contact("Lucky", "9876543210", "Delhi")
    add_contact("Rahul", "9123456789", "Mumbai")
    add_contact("Priya", "9988776655", "Bangalore")
    add_contact("Amit", "9112233445")  # city defaults to "Unknown"

    # Display all
    print("\n  All contacts:")
    display_all()

    # Search
    search_name = "Rahul"
    result = find_contact(search_name)
    if result:
        print(f"\n  🔍 Found: {result['name']} — {result['phone']} ({result['city']})")
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

    print("\n  ✅ You just built a mini app using lists, dicts, "
          "functions, loops, and f-strings!")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MAIN
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def main():
    print("\n" + "━" * 50)
    print("  🐍 AI-Engineer-OS — Day 1: Python Fundamentals")
    print("━" * 50)

    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()

    print("\n" + "━" * 50)
    print("  🎓 Day 1 Complete!")
    print("━" * 50)
    print("""
  WHAT YOU LEARNED TODAY:
  ┌───────────────────────────────────────────────┐
  │ 1. Variables & types (str, int, float, bool)  │
  │ 2. f-strings for clean output                 │
  │ 3. if/elif/else for decisions                 │
  │ 4. for & while loops                          │
  │ 5. Functions with parameters & returns        │
  │ 6. Lists, Dicts, Tuples, Sets                 │
  │ 7. Combined it all in a mini project          │
  └───────────────────────────────────────────────┘

  HOMEWORK:
  • Modify the Contact Book to also store email addresses
  • Add a delete_contact() function
  • Add a function that saves contacts to a .txt file

  NEXT → Day 2: Lists deep-dive, list comprehensions, 
         string methods, and more mini projects.
    """)


if __name__ == "__main__":
    main()
