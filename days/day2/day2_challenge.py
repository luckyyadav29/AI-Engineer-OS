# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# DAY 2 CHALLENGES — Write It Yourself! 💪
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Rules:
# 1. Read the challenge description carefully
# 2. Write the code yourself inside each function/class
# 3. Run this file after each challenge to test your code
# 4. If you're stuck for 10+ minutes, ask me for a hint (not the answer!)
# 5. DO NOT look at practice.py — that's the answer key!


# ╔══════════════════════════════════════════════════════════════╗
# ║  CHALLENGE 1: Create Your First Class (Easy)                ║
# ╚══════════════════════════════════════════════════════════════╝
# Create a class called "Song" that represents a music track.
#
# Requirements:
#   - __init__ should take: title, artist, duration_seconds
#   - Create a method "play()" that returns: "🎵 Now playing: <title> by <artist>"
#   - Create a method "duration_formatted()" that returns duration as "M:SS"
#     Example: 185 seconds → "3:05", 60 seconds → "1:00"
#
# Test your class by creating 2 songs and printing their info.

# 👇 Write your code below this line:
# class Song:

#     def __init__(self,title,artist,duration_seconds):
#         self.title=title
#         self.artist=artist
#         self.duration_seconds=duration_seconds
    
#     def play(self):
#         return f"🎵 Now playing : {self.title} by {self.artist}"

#     def duration_formatted(self):
#         return f"{self.duration_seconds//60}:{self.duration_seconds%60:0>2d}"   


# ── Test it (uncomment these after writing your class) ──
# song1 = Song("Shape of You", "Ed Sheeran", 233)
# song2 = Song("Blinding Lights", "The Weeknd", 200)
# print(song1.play())
# print(f"Duration: {song1.duration_formatted()}")
# print(song2.play())
# print(f"Duration: {song2.duration_formatted()}")


# ╔══════════════════════════════════════════════════════════════╗
# ║  CHALLENGE 2: Dunder Methods (Easy-Medium)                  ║
# ╚══════════════════════════════════════════════════════════════╝
# Add these dunder methods to your Song class (or create a new version):
#
# Requirements:
#   - __str__  → should return: "Shape of You - Ed Sheeran (3:53)"
#   - __repr__ → should return: "Song(title='Shape of You', artist='Ed Sheeran')"
#   - __len__  → should return the duration in seconds
#
# After adding these, the following should work:
#   print(song1)         →  "Shape of You - Ed Sheeran (3:53)"
#   repr(song1)          →  "Song(title='Shape of You', artist='Ed Sheeran')"
#   len(song1)           →  233

# 👇 Write your updated Song class below:
class Song:

    def __init__(self,title,artist,duration_seconds):
        self.title=title
        self.artist=artist
        self.duration_seconds=duration_seconds
    
    def __str__(self):
        return f"{self.title}-{self.artist} {self.duration_formatted()}"

    def __repr__(self):
        return f"Song(title='{self.title}',artist='{self.artist}')"

    def __len__(self):
        return self.duration_seconds

    def play(self):
        return f"🎵 Now playing : {self.title} by {self.artist}"

    def duration_formatted(self):
        return f"{self.duration_seconds//60}:{self.duration_seconds%60:0>2d}"      
    


# ── Test it (uncomment after writing) ──
# song = Song("Bohemian Rhapsody", "Queen", 354)
# print(song)              # Should use __str__
# print(repr(song))        # Should use __repr__
# print(f"Length: {len(song)} seconds")  # Should use __len__


# ╔══════════════════════════════════════════════════════════════╗
# ║  CHALLENGE 3: Inheritance (Medium)                           ║
# ╚══════════════════════════════════════════════════════════════╝
# Create a parent class "Vehicle" and two child classes.
#
# Parent: Vehicle
#   - __init__ takes: brand, model, year
#   - Method "info()" returns: "2024 Toyota Camry"
#   - Method "start()" returns: "🚗 Starting engine..."
#
# Child 1: ElectricVehicle(Vehicle)
#   - Extra attribute: battery_percent (default 100)
#   - Override "start()" to return: "⚡ Starting electric motor... (Battery: 85%)"
#   - New method "charge()" that sets battery_percent to 100 and returns "🔋 Fully charged!"
#
# Child 2: Truck(Vehicle)
#   - Extra attribute: cargo_capacity_kg
#   - Override "start()" to return: "🚛 Starting diesel engine..."
#   - New method "load(weight)" that:
#       - If weight > cargo_capacity_kg → raise ValueError("Too heavy!")
#       - Otherwise returns "📦 Loaded {weight}kg"

# 👇 Write your classes below:
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def info(self):
        return f"{self.year} {self.brand} {self.model}"

    def start(self):
        return "🚗 Starting engine..."

class ElectricVehicle(Vehicle):
    def __init__(self,brand,model,year,battery_percent=100):
        super().__init__(brand,model,year)
        self.battery_percent=battery_percent
    def start(self):
        return f"⚡ Starting electric motor... (Battery: {self.battery_percent}%)"
    def charge(self):
        self.battery_percent=100
        return "🔋 Fully charged!"

class Truck(Vehicle):
    def __init__(self,brand,model,year,cargo_capacity_kg):
        super().__init__(brand,model,year)
        self.cargo_capacity_kg=cargo_capacity_kg

    def start(self):
        return "🚛 Starting diesel engine..."

    def load(self,weight):
        if weight>self.cargo_capacity_kg:
            raise ValueError("Too heavy!")
        else:
            return f"📦 Loaded {weight}kg"    



    

# # ── Test it (uncomment after writing) ──
# tesla = ElectricVehicle("Tesla", "Model 3", 2024, battery_percent=85)
# truck = Truck("Ford", "F-150", 2023, cargo_capacity_kg=1000)

# print(tesla.info())
# print(tesla.start())
# print(tesla.charge())

# print(truck.info())
# print(truck.start())
# print(truck.load(500))

# try:
#     truck.load(2000)
# except ValueError as e:
#     print(f"⚠️ {e}")

# # These should work because of inheritance:
# print(f"Is tesla a Vehicle? {isinstance(tesla, Vehicle)}")
# print(f"Is truck an ElectricVehicle? {isinstance(truck, ElectricVehicle)}")


# ╔══════════════════════════════════════════════════════════════╗
# ║  CHALLENGE 4: Error Handling + Custom Exceptions (Medium)    ║
# ╚══════════════════════════════════════════════════════════════╝
# Create a simple BankAccount class with custom exceptions.
#
# Custom Exceptions (create these first):
#   - BankError(Exception)           → base error for all bank issues
#   - InsufficientFundsError(BankError) → when trying to withdraw too much
#   - InvalidAmountError(BankError)     → when amount is negative or not a number
#
# BankAccount class:
#   - __init__ takes: owner_name, balance (default 0)
#   - deposit(amount):
#       - If amount is not a number → raise InvalidAmountError
#       - If amount <= 0 → raise InvalidAmountError("Amount must be positive")
#       - Otherwise, add to balance and return new balance
#   - withdraw(amount):
#       - Same validation as deposit
#       - If amount > balance → raise InsufficientFundsError
#       - Otherwise, subtract from balance and return new balance
#   - __str__ → "BankAccount(Lucky: ₹5000)"

# 👇 Write your exceptions and class below:
class BankError(Exception):
    pass

class InsufficientFundsError(BankError):
    pass

class InvalidAmountError(BankError):
    pass

class BankAccount:
    def __init__(self,owner_name,balance=0):
        self.owner_name=owner_name
        self.balance=balance

    def deposit(self,amount):
        if not isinstance(amount,(int,float)):
            raise InvalidAmountError("Amount must be a number")
        if amount <=0:
            raise InvalidAmountError("Amount must be positive")

        self.balance+=amount
        return self.balance

    def withdraw(self,amount):
        if not isinstance(amount,(int,float)):
            raise InvalidAmountError("Amount must be a number")
        if amount <=0:
            raise InvalidAmountError("Amount must be positive")
        if amount >self.balance:
            raise InsufficientFundsError("Insufficient Funds")
        self.balance-=amount
        return self.balance

    def __str__(self):
        return f"BankAccount({self.owner_name}: ₹{self.balance})"

# # ── Test it (uncomment after writing) ──
# account = BankAccount("Lucky", 1000)
# print(account)

# print(f"Deposited. New balance: ₹{account.deposit(500)}")
# print(f"Withdrew. New balance: ₹{account.withdraw(200)}")

# # These should raise errors:
# try:
#     account.withdraw(50000)
# except InsufficientFundsError as e:
#     print(f"⚠️ {e}")

# try:
#     account.deposit(-100)
# except InvalidAmountError as e:
#     print(f"⚠️ {e}")

# try:
#     account.deposit("hundred")
# except InvalidAmountError as e:
#     print(f"⚠️ {e}")


# ╔══════════════════════════════════════════════════════════════╗
# ║  CHALLENGE 5: Modules + File I/O (Medium-Hard)              ║
# ╚══════════════════════════════════════════════════════════════╝
# Create a "TodoList" class that saves/loads tasks from a JSON file.
#
# You'll need: import json, import datetime
#
# TodoList class:
#   - __init__ takes: filename (default "todos.json")
#       - Initialize an empty list of tasks
#       - Try to load existing tasks from the file (handle FileNotFoundError!)
#
#   - add_task(task_text):
#       - Add a dict with: {"task": task_text, "done": False, "created": <current datetime as string>}
#       - Return the dict you just added
#
#   - complete_task(index):
#       - Mark the task at that index as done (set "done" to True)
#       - If index is out of range, raise IndexError("Task not found!")
#
#   - get_pending():
#       - Return a list of only tasks where "done" is False
#
#   - save():
#       - Save all tasks to the JSON file
#
#   - __str__ → "TodoList: 3 tasks (1 pending)"
#   - __len__ → total number of tasks

# 👇 Write your class below:

import json
from datetime import datetime 

class TodoList:
    def __init__(self,filename="todos.json"):
        self.filename=filename
        self.tasks=[]
        
        try:
            with open(self.filename,"r") as f:
                self.tasks=json.load(f)
        except FileNotFoundError:
            self.tasks=[]
    def add_task(self,task_text):
        task={
            "task":task_text,
            "done":False,
            "created":datetime.now().isoformat()
        }
        self.tasks.append(task)
        return self.tasks
    
    def complete_task(self,index):
        if not isinstance(index,int) or index<0 or index >=len(self.tasks):
            raise IndexError("Task not found!")
        self.tasks[index]["done"]=True

    def get_pending(self):
        pending=[]
        for task in self.tasks:
            if task["done"]==False:
                pending.append(task) 
        return pending        
        
    def save(self):
        with open(self.filename,"w") as f:
            json.dump(self.tasks,f,indent=4)
    def __str__(self):
        return f"TodoList: {len(self.tasks)} tasks ({len(self.get_pending())} pending)"

    def __len__(self):
        return len(self.tasks)    
        

# ── Test it (uncomment after writing) ──
todos = TodoList("test_todos.json")
todos.add_task("Learn Python OOP")
todos.add_task("Build an AI chatbot")
todos.add_task("Deploy to production")

print(todos)
print(f"Total tasks: {len(todos)}")

todos.complete_task(0)  # Mark first task as done
print(f"Pending tasks: {len(todos.get_pending())}")

todos.save()
print("Saved! ✅")

# Clean up test file
import os
os.remove("test_todos.json")


# ╔══════════════════════════════════════════════════════════════╗
# ║  🏆 BOSS CHALLENGE: Combine Everything (Hard)               ║
# ╚══════════════════════════════════════════════════════════════╝
# Build a "ContactBook" app that uses ALL Day 2 concepts:
#   - Classes & __init__
#   - Dunder methods (__str__, __len__)
#   - Inheritance (create a VIPContact that inherits from Contact)
#   - Custom exceptions (DuplicateContactError, ContactNotFoundError)
#   - Modules (json for saving, datetime for timestamps)
#   - Error handling (try/except)
#
# This is open-ended — design it yourself! Here's the minimum:
#   - Contact class with: name, phone, email
#   - VIPContact(Contact) with extra: company, priority_level
#   - ContactBook class that can: add, search, delete, save to JSON
#   - Custom exceptions for duplicate names and missing contacts
#
# NO SKELETON PROVIDED — design it from scratch! 🚀

# 👇 Write your entire solution below:




# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HOW TO USE THIS FILE:
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1. Start with Challenge 1 (easiest)
# 2. Write your code below each challenge
# 3. Uncomment the test lines to check if your code works
# 4. Run: python day2_challenge.py
# 5. Move to the next challenge
#
# 💡 If stuck: Ask me for a HINT (not the full answer!)
# 🎯 Goal: Complete at least Challenges 1-4 before moving to Day 3
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
