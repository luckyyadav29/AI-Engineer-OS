# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# DAY 3 CHALLENGES — Write It Yourself!
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Rules:
# 1. Read each challenge carefully
# 2. Write the code yourself
# 3. Run this file to test: python day3_challenge.py
# 4. Stuck for 10+ min? Ask for a HINT, not the answer!


# ╔══════════════════════════════════════════════════════════════╗
# ║  CHALLENGE 1: List Comprehensions (Easy)                     ║
# ╚══════════════════════════════════════════════════════════════╝
# Given this list of AI model data:

models = [
    {"name": "gpt-4", "score": 95, "cost": 0.03},
    {"name": "gemini", "score": 88, "cost": 0.01},
    {"name": "claude", "score": 92, "cost": 0.015},
    {"name": "llama", "score": 75, "cost": 0.00},
    {"name": "mistral", "score": 82, "cost": 0.005},
]

# TODO 1: Get a list of just the model names → ["gpt-4", "gemini", ...]
model_names = [i["name"] for i in models]
print(f"Names: {model_names}")

# TODO 2: Get names of models with score > 85 → ["gpt-4", "claude", "gemini"]
good_models = [i["name"] for i in models if i["score"]>85]
print(f"Good models: {good_models}")

# TODO 3: Get a list of costs, doubled → [0.06, 0.02, 0.03, 0.0, 0.01]
doubled_costs = [i["cost"]*2 for i in models]
print(f"Doubled costs: {doubled_costs}")

# TODO 4: Get names of FREE models (cost == 0) → ["llama"]
free_models = [i["name"] for i in models if i["cost"]==0]
print(f"Free models: {free_models}")


# ╔══════════════════════════════════════════════════════════════╗
# ║  CHALLENGE 2: Dict Comprehensions (Easy-Medium)              ║
# ╚══════════════════════════════════════════════════════════════╝
# TODO 1: Create a dict of {model_name: score} from the models list above
# Example: {"gpt-4": 95, "gemini": 88, ...}
score_dict = {i["name"]:i["score"] for i in models}
print(f"Scores: {score_dict}")

# TODO 2: Create a dict of only models with score > 85
# Example: {"gpt-4": 95, "claude": 92, "gemini": 88}
top_scores = {i["name"]:i["score"] for i in models if i["score"]>85}
print(f"Top scores: {top_scores}")

# TODO 3: Given this list, create a dict where key=word, value=length
words = ["python", "ai", "machine", "learning", "deep"]
# Example: {"python": 6, "ai": 2, ...}
word_lengths = {i:len(i) for i in words}
print(f"Word lengths: {word_lengths}")

# TODO 4: Swap keys and values of this dict:
original = {"a": 1, "b": 2, "c": 3, "d": 4}
swapped = {j:i for i,j in original.items()}
print(f"Swapped: {swapped}")  # Should be {1: "a", 2: "b", ...}


# ╔══════════════════════════════════════════════════════════════╗
# ║  CHALLENGE 3: *args and **kwargs (Medium)                    ║
# ╚══════════════════════════════════════════════════════════════╝
# TODO 1: Write a function called "multiply_all" that takes ANY number
# of arguments and multiplies them all together.
# Example: multiply_all(2, 3, 4) → 24
# Example: multiply_all(5, 10) → 50

def multiply_all(*nos):
    product = 1
    for i in nos:
        product *= i
    return product

print(f"multiply_all(2, 3, 4) = {multiply_all(2, 3, 4)}")
print(f"multiply_all(5, 10)   = {multiply_all(5, 10)}")


# TODO 2: Write a function called "build_prompt" that takes:
#   - system_message (required)
#   - *messages (any number of user messages)
#   - **settings (any key=value settings like model, temperature)
# It should return a dictionary with all the info.
#
# Example:
# build_prompt("You are helpful", "Hello", "How are you?",
#              model="gpt-4", temperature=0.7)
# Should return:
# {
#     "system": "You are helpful",
#     "messages": ("Hello", "How are you?"),
#     "settings": {"model": "gpt-4", "temperature": 0.7}
# }

def build_prompt(system_message,*messages, **settings):
    return {"system":system_message,
            "messages":messages,
            "settings":settings}

result = build_prompt("You are helpful", "Hello", "How are you?",
                       model="gpt-4", temperature=0.7)
print(f"Prompt config: {result}")


# ╔══════════════════════════════════════════════════════════════╗
# ║  CHALLENGE 4: Decorators (Medium-Hard)                       ║
# ╚══════════════════════════════════════════════════════════════╝
# TODO 1: Write a decorator called "shout" that:
#   - Takes the result of any function
#   - Converts it to UPPERCASE
#   - Returns the uppercased result
#
# Example:
@shout
def greet(name):
    return f"hello, {name}"


def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)   # Call greet("Lucky") → "hello, Lucky"
        return result.upper()            # "hello, Lucky" → "HELLO, LUCKY"
    return wrapper


@shout
def whisper(text):
    return f"psst... {text}"

print(f"greet('Lucky')     = {greet('Lucky')}")
print(f"whisper('secret')  = {whisper('secret')}")


# TODO 2 (BONUS): Write a decorator called "call_counter" that:
#   - Counts how many times a function has been called
#   - Prints the count each time
#
# Example:
# @call_counter
# def say_hi():
#     return "hi"
# say_hi()  → "Call #1 to say_hi"
# say_hi()  → "Call #2 to say_hi"
# say_hi()  → "Call #3 to say_hi"

# def call_counter(func):
#     ???


# ╔══════════════════════════════════════════════════════════════╗
# ║  CHALLENGE 5: Generators (Medium)                            ║
# ╚══════════════════════════════════════════════════════════════╝
# TODO 1: Write a generator called "fibonacci" that yields
# Fibonacci numbers one at a time (each number = sum of previous two)
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
#
def fibonacci(n):
    """Yield first n Fibonacci numbers"""
    a,b=0,1
    for _ in range(n):
        yield a
        a,b=b,a+b


print("First 10 Fibonacci numbers:")
for num in fibonacci(10):
    print(num, end=" ")
print()


# TODO 2: Write a generator called "chunk_text" that takes a string
# and a chunk_size, and yields chunks of the text.
# Example: chunk_text("Hello World AI", 5) yields "Hello", " Worl", "d AI"
#
def chunk_text(text, chunk_size):
    for i in range(0,len(text),chunk_size):
        yield text[i:i+chunk_size]
    

print("\nChunked text:")
for chunk in chunk_text("Generators are amazing for processing large texts", 10):
    print(f"  [{chunk}]")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HOW TO USE:
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1. Write your code below each TODO
# 2. Uncomment the test/print lines
# 3. Run: python day3_challenge.py
# 4. Stuck? Ask for a HINT!
# Goal: Complete Challenges 1-4 before moving to Day 4
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
