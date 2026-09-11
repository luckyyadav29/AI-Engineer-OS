"""
╔══════════════════════════════════════════════════════════════════╗
║  AI-Engineer-OS — Day 2: Python Intermediate                     ║
║  Topics: OOP, Error Handling, Modules                            ║
║  Run: python day2_python_intermediate.py                         ║
║  No external packages needed — pure Python!                      ║
╚══════════════════════════════════════════════════════════════════╝

8 exercises. Read each one, understand it, then try modifying it.
Builds on Day 1 — uses lists, dicts, functions, f-strings, and file I/O.
"""


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCISE 1: Your First Class
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A class is a BLUEPRINT(like a template). An object is a THING built from that blueprint.
# Think of it like:
#   class = cookie cutter (the shape)
#   object = actual cookie (the real thing)
#
# WHY does this matter for AI engineering?
#   → You'll build classes for: API clients, model configs, data loaders,
#     chatbot sessions, agent tools — everything in production AI uses OOP.

def exercise_1():
    print("\n" + "=" * 50)
    print("  EXERCISE 1: Your First Class")
    print("=" * 50)

    # Define a class with __init__ (the constructor)
    # __init__ runs automatically when you create an object
    # 'self' = "this specific object" — it's how the object refers to itself
    class Dog:
        def __init__(self, name, breed):
            self.name = name      # self.name = this dog's name
            self.breed = breed    # self.breed = this dog's breed

        def bark(self):
            return f"{self.name} says: Woof! 🐕"

        def info(self):
            return f"{self.name} is a {self.breed}"

    # Create objects (instances) from the class
    dog1 = Dog("Buddy", "Golden Retriever")
    dog2 = Dog("Max", "German Shepherd")

    print(f"  {dog1.info()}")
    print(f"  {dog1.bark()}")
    print(f"  {dog2.info()}")
    print(f"  {dog2.bark()}")

    # Access attributes directly
    print(f"\n  dog1.name = {dog1.name}")
    print(f"  dog1.breed = {dog1.breed}")

    # Each object is independent
    dog1.name = "Charlie"  # Change just dog1's name
    print(f"\n  After rename: {dog1.info()}")
    print(f"  dog2 unchanged: {dog2.info()}")

    print("\n  ✅ Classes = blueprints, Objects = real things built from them")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCISE 2: A Real-World Class — AI Model Config
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Let's build something you'll ACTUALLY use in AI engineering:
# a class to store model configuration.

def exercise_2():
    print("\n" + "=" * 50)
    print("  EXERCISE 2: AI Model Config Class")
    print("=" * 50)

    class ModelConfig:
        def __init__(self, name, provider, temperature=0.7, max_tokens=1000):
            self.name = name
            self.provider = provider
            self.temperature = temperature
            self.max_tokens = max_tokens

        def summary(self):
            return (f"Model: {self.name} | Provider: {self.provider} | "
                    f"Temp: {self.temperature} | Max Tokens: {self.max_tokens}")

        def to_dict(self):
            """Convert to dictionary — useful for sending to APIs"""
            return {
                "model": self.name,
                "provider": self.provider,
                "temperature": self.temperature,
                "max_tokens": self.max_tokens,
            }

    # Create different model configs
    gpt = ModelConfig("gpt-4", "OpenAI", temperature=0.3)
    gemini = ModelConfig("gemini-pro", "Google", temperature=0.5, max_tokens=2000)
    claude = ModelConfig("claude-3", "Anthropic")

    print(f"  {gpt.summary()}")
    print(f"  {gemini.summary()}")
    print(f"  {claude.summary()}")

    # to_dict() — you'll use this pattern ALL the time with APIs
    print(f"\n  GPT as dict: {gpt.to_dict()}")

    # Modify config
    gpt.temperature = 0.9
    print(f"\n  After raising temperature: {gpt.summary()}")

    print("\n  ✅ Classes keep related data + behavior together — clean & organized")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCISE 3: __str__, __repr__, and __len__  (Dunder Methods)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# "Dunder" = Double UNDERscore → __init__, __str__, __repr__, etc.
# The dunder methods are what connect your custom class to Python's built-in functions.
# These are special methods that Python calls automatically.
# __str__  → what print() shows
# __repr__ → what the developer sees (for debugging)
# __len__  → what len() returns

def exercise_3():
    print("\n" + "=" * 50)
    print("  EXERCISE 3: Dunder Methods (__str__, __repr__, __len__)")
    print("=" * 50)

    class ChatHistory:
        def __init__(self, user_name):
            self.user_name = user_name
            self.messages = []  # list of dicts

        def add_message(self, role, content):
            """Add a message to the chat history"""
            self.messages.append({"role": role, "content": content})

        def __str__(self):
            """What print() shows — human-friendly"""
            return f"Chat with {self.user_name} ({len(self.messages)} messages)"

        def __repr__(self):
            """What developers see — detailed"""
            return f"ChatHistory(user='{self.user_name}', messages={len(self.messages)})"

        def __len__(self):
            """What len() returns"""
            return len(self.messages)

    chat = ChatHistory("Lucky")
    chat.add_message("user", "Hello!")
    chat.add_message("assistant", "Hi Lucky! How can I help?")
    chat.add_message("user", "Explain OOP")

    # __str__ is called by print()
    print(f"  print(chat)  → {chat}")

    # __repr__ is called in the console / debugger
    print(f"  repr(chat)   → {repr(chat)}")

    # __len__ is called by len()
    print(f"  len(chat)    → {len(chat)}")

    # Access the actual messages
    print(f"\n  Messages:")
    for msg in chat.messages:
        print(f"    [{msg['role']}]: {msg['content']}")

    print("\n  ✅ Dunder methods let your classes work with Python's built-in functions")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCISE 4: Inheritance — Building on Existing Classes
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Inheritance = "this class gets everything from that class, PLUS more"
# Parent class (base)  → general behavior
# Child class (derived) → specialized behavior
#
# Real AI example: You have a base "LLMClient" class, then
# "OpenAIClient" and "GeminiClient" inherit from it.

def exercise_4():
    print("\n" + "=" * 50)
    print("  EXERCISE 4: Inheritance")
    print("=" * 50)

    # Parent class — the general blueprint
    class LLMClient:
        def __init__(self, model_name, api_key="demo-key"):
            self.model_name = model_name
            self.api_key = api_key
            self.history = []

        def send_message(self, message):
            """Base method — child classes will override this"""
            self.history.append({"role": "user", "content": message})
            response = f"[{self.model_name}] Echo: {message}"
            self.history.append({"role": "assistant", "content": response})
            return response

        def get_history(self):
            return self.history

        def __str__(self):
            return f"LLMClient(model={self.model_name})"

    # Child class — inherits everything, adds/overrides specific behavior
    class OpenAIClient(LLMClient):
        def __init__(self, model_name="gpt-4", api_key="demo-key"):
            # super() calls the parent's __init__
            super().__init__(model_name, api_key)
            self.provider = "OpenAI"

        def send_message(self, message):
            """Override — specialized behavior for OpenAI"""
            self.history.append({"role": "user", "content": message})
            # In real life, this would call the OpenAI API
            response = f"[OpenAI/{self.model_name}] I'd process: '{message}'"
            self.history.append({"role": "assistant", "content": response})
            return response

        def count_tokens(self, text):
            """Extra method only OpenAI client has"""
            # Rough estimate: 1 token ≈ 4 characters
            return len(text) // 4

    class GeminiClient(LLMClient):
        def __init__(self, model_name="gemini-pro", api_key="demo-key"):
            super().__init__(model_name, api_key)
            self.provider = "Google"

        def send_message(self, message):
            """Override — specialized behavior for Gemini"""
            self.history.append({"role": "user", "content": message})
            response = f"[Google/{self.model_name}] I'd process: '{message}'"
            self.history.append({"role": "assistant", "content": response})
            return response

    # Use the classes
    openai = OpenAIClient()
    gemini = GeminiClient()

    print(f"  {openai.send_message('What is AI?')}")
    print(f"  {gemini.send_message('What is AI?')}")

    # count_tokens only exists on OpenAIClient
    text = "What is artificial intelligence?"
    print(f"\n  Token estimate for '{text}': ~{openai.count_tokens(text)} tokens")

    # isinstance() — check if an object is a certain type
    print(f"\n  Is openai an LLMClient? {isinstance(openai, LLMClient)}")
    print(f"  Is openai an OpenAIClient? {isinstance(openai, OpenAIClient)}")
    print(f"  Is gemini an OpenAIClient? {isinstance(gemini, OpenAIClient)}")

    print("\n  ✅ Inheritance = reuse code + specialize behavior")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCISE 5: Error Handling — try / except / finally / raise
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Errors WILL happen — API calls fail, files are missing, users send bad input.
# A good AI engineer handles errors gracefully instead of crashing.

def exercise_5():
    print("\n" + "=" * 50)
    print("  EXERCISE 5: Error Handling")
    print("=" * 50)

    # --- Basic try/except ---
    print("  1. Basic try/except:")
    try:
        result = 10 / 0  # This will crash!
    except ZeroDivisionError:
        print("    ⚠️  Can't divide by zero! Handled gracefully.")

    # --- Catching the error message ---
    print("\n  2. Catching error details:")
    try:
        numbers = [1, 2, 3]
        print(numbers[10])  # Index doesn't exist
    except IndexError as e:
        print(f"    ⚠️  Error: {e}")

    # --- Multiple except blocks ---
    print("\n  3. Multiple error types:")
    test_values = ["hello", 0, 5]
    for val in test_values:
        try:
            result = 100 / int(val)
            print(f"    100 / {val} = {result}")
        except ValueError:
            print(f"    ⚠️  '{val}' is not a number!")
        except ZeroDivisionError:
            print(f"    ⚠️  Can't divide by {val}!")

    # --- finally — ALWAYS runs ---
    print("\n  4. finally block (always runs):")
    try:
        f = open("temp_test.txt", "w")
        f.write("testing")
        # Even if an error happened above, finally still runs
    finally:
        f.close()
        print("    File closed in 'finally' — cleanup guaranteed ✅")

    # --- raise — throw your own errors ---
    print("\n  5. Raising custom errors:")

    def set_temperature(temp):
        """Temperature for LLMs must be between 0.0 and 2.0"""
        if not isinstance(temp, (int, float)):
            raise TypeError(f"Temperature must be a number, got {type(temp).__name__}")
        if temp < 0 or temp > 2.0:
            raise ValueError(f"Temperature must be 0.0-2.0, got {temp}")
        return temp

    # Valid
    print(f"    set_temperature(0.7) → {set_temperature(0.7)}")

    # Invalid — too high
    try:
        set_temperature(5.0)
    except ValueError as e:
        print(f"    set_temperature(5.0) → ⚠️ {e}")

    # Invalid — wrong type
    try:
        set_temperature("hot")
    except TypeError as e:
        print(f"    set_temperature('hot') → ⚠️ {e}")

    # Clean up temp file
    import os
    os.remove("temp_test.txt")

    print("\n  ✅ try/except = catch errors | finally = cleanup | raise = throw errors")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCISE 6: Custom Exceptions
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# You can create your OWN error types by inheriting from Exception.
# This is common in production code — "APIError", "AuthenticationError", etc.

def exercise_6():
    print("\n" + "=" * 50)
    print("  EXERCISE 6: Custom Exceptions")
    print("=" * 50)

    # Define custom exceptions — they inherit from Exception
    class APIError(Exception):
        """Raised when an API call fails"""
        pass

    class AuthenticationError(APIError):
        """Raised when API key is invalid"""
        pass

    class RateLimitError(APIError):
        """Raised when you've sent too many requests"""
        def __init__(self, retry_after=60):
            self.retry_after = retry_after
            super().__init__(f"Rate limited! Retry after {retry_after} seconds.")

    # Simulate API calls with different errors
    def fake_api_call(api_key, request_count):
        if api_key == "":
            raise AuthenticationError("API key is empty!")
        if api_key == "invalid":
            raise AuthenticationError("Invalid API key: 'invalid'")
        if request_count > 100:
            raise RateLimitError(retry_after=30)
        return {"status": "success", "data": "Hello from the API!"}

    # Test different scenarios
    test_cases = [
        ("valid-key-123", 1),
        ("", 1),
        ("invalid", 1),
        ("valid-key-123", 150),
    ]

    for api_key, count in test_cases:
        try:
            result = fake_api_call(api_key, count)
            print(f"    ✅ key='{api_key}', requests={count} → {result['status']}")
        except AuthenticationError as e:
            print(f"    🔑 Auth Error: {e}")
        except RateLimitError as e:
            print(f"    ⏳ Rate Limit: {e} (retry in {e.retry_after}s)")
        except APIError as e:
            print(f"    ❌ API Error: {e}")

    print("\n  ✅ Custom exceptions make your error handling specific & professional")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCISE 7: Modules & Imports
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Modules = Python files you can import and reuse.
# Python has tons of built-in modules. You'll also create your own.

def exercise_7():
    print("\n" + "=" * 50)
    print("  EXERCISE 7: Modules & Imports")
    print("=" * 50)

    # --- Built-in modules ---
    import os
    import json
    import random
    import datetime

    # os — interact with the operating system
    print(f"  📁 Current directory: {os.path.basename(os.getcwd())}")
    print(f"  📁 This file exists: {os.path.exists('day2_python_intermediate.py')}")

    # json — work with JSON data (you'll use this CONSTANTLY with APIs)
    data = {
        "model": "gpt-4",
        "messages": [
            {"role": "user", "content": "Hello!"}
        ],
        "temperature": 0.7,
    }
    json_string = json.dumps(data, indent=2)
    print(f"\n  📦 Python dict → JSON string:")
    for line in json_string.split("\n"):
        print(f"    {line}")

    # Parse JSON back to Python dict
    parsed = json.loads(json_string)
    print(f"\n  📦 JSON string → Python dict:")
    print(f"    Model: {parsed['model']}")
    print(f"    Message: {parsed['messages'][0]['content']}")

    # random — useful for sampling, testing, shuffling
    choices = ["gpt-4", "gemini-pro", "claude-3", "llama-3"]
    print(f"\n  🎲 Random model: {random.choice(choices)}")
    print(f"  🎲 Random temperature: {round(random.uniform(0, 1), 2)}")

    # datetime — timestamps, logging, scheduling
    now = datetime.datetime.now()
    print(f"\n  🕐 Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

    print("\n  ✅ os, json, random, datetime — your most-used built-in modules")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCISE 8: Putting It All Together — AI Prompt Logger
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Build a class that:
# - Stores prompts and responses
# - Handles errors gracefully
# - Saves/loads from JSON files
# - Uses everything from Day 1 + Day 2

def exercise_8():
    print("\n" + "=" * 50)
    print("  EXERCISE 8: AI Prompt Logger (Full Project)")
    print("=" * 50)

    import json
    import datetime
    import os

    class PromptLogger:
        """Logs AI prompts and responses to a JSON file"""

        def __init__(self, filename="prompt_log.json"):
            self.filename = filename
            self.logs = []
            # Try to load existing logs
            self._load()

        def _load(self):
            """Load existing logs from file (private method with _)"""
            try:
                with open(self.filename, "r") as f:
                    self.logs = json.load(f)
                print(f"    📂 Loaded {len(self.logs)} existing logs")
            except FileNotFoundError:
                print(f"    📂 No existing log file — starting fresh")
                self.logs = []
            except json.JSONDecodeError:
                print(f"    ⚠️  Log file corrupted — starting fresh")
                self.logs = []

        def log(self, prompt, response, model="gpt-4"):
            """Log a prompt-response pair"""
            if not prompt.strip():
                raise ValueError("Prompt cannot be empty!")

            entry = {
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "model": model,
                "prompt": prompt,
                "response": response,
                "prompt_length": len(prompt),
                "response_length": len(response),
            }
            self.logs.append(entry)
            return entry

        def save(self):
            """Save all logs to JSON file"""
            with open(self.filename, "w") as f:
                json.dump(self.logs, f, indent=2)
            print(f"    💾 Saved {len(self.logs)} logs to {self.filename}")

        def get_stats(self):
            """Get statistics about logged prompts"""
            if not self.logs:
                return "No logs yet!"

            total = len(self.logs)
            models_used = {}
            total_prompt_chars = 0

            for entry in self.logs:
                model = entry["model"]
                models_used[model] = models_used.get(model, 0) + 1
                total_prompt_chars += entry["prompt_length"]

            return {
                "total_prompts": total,
                "models_used": models_used,
                "avg_prompt_length": round(total_prompt_chars / total),
            }

        def __str__(self):
            return f"PromptLogger({len(self.logs)} logs → {self.filename})"

        def __len__(self):
            return len(self.logs)

    # --- Use the PromptLogger ---
    logger = PromptLogger("day2_prompt_log.json")

    # Log some prompts
    logger.log("Explain OOP in Python", "OOP is a programming paradigm...", model="gpt-4")
    logger.log("What is RAG?", "RAG stands for Retrieval Augmented...", model="gemini-pro")
    logger.log("Write a haiku about code", "Lines of logic flow...", model="claude-3")

    # Try logging an empty prompt
    try:
        logger.log("", "This should fail")
    except ValueError as e:
        print(f"    ⚠️  Caught: {e}")

    # Print info
    print(f"\n    {logger}")
    print(f"    Total logs: {len(logger)}")

    # Get stats
    stats = logger.get_stats()
    print(f"\n    📊 Stats:")
    print(f"      Total prompts: {stats['total_prompts']}")
    print(f"      Avg prompt length: {stats['avg_prompt_length']} chars")
    print(f"      Models used: {stats['models_used']}")

    # Save to file
    logger.save()

    # Show what the JSON file looks like
    print(f"\n    📄 File contents:")
    with open("day2_prompt_log.json", "r") as f:
        content = f.read()
    for line in content.split("\n")[:12]:
        print(f"      {line}")
    print(f"      ...")

    # Clean up
    os.remove("day2_prompt_log.json")

    print("\n  ✅ OOP + Error Handling + Modules + File I/O = production-ready patterns!")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# RUN ALL EXERCISES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if __name__ == "__main__":
    print("🚀 Day 2: Python Intermediate — OOP, Error Handling, Modules")
    print("━" * 55)

    exercise_1()   # Classes & Objects
    exercise_2()   # AI Model Config class
    exercise_3()   # Dunder methods
    exercise_4()   # Inheritance
    exercise_5()   # Error handling
    exercise_6()   # Custom exceptions
    exercise_7()   # Modules & imports
    exercise_8()   # Full project — Prompt Logger

    print("\n" + "━" * 55)
    print("🎉 Day 2 Complete!")
    print("━" * 55)
    print("""
    📝 What you learned:
    1. Classes & Objects — blueprints for organizing code
    2. __init__, self — constructor and instance reference
    3. __str__, __repr__, __len__ — dunder methods
    4. Inheritance — reuse + specialize (parent → child)
    5. try/except/finally/raise — graceful error handling
    6. Custom Exceptions — professional error types
    7. Modules — os, json, random, datetime
    8. Combined everything into a Prompt Logger

    🏋️ Now open practice.py and build the homework project!
    """)
