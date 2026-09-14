# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# DAY 3: Python Advanced
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Topics:
#   1. List Comprehensions — build lists in one line
#   2. Dict Comprehensions — build dicts in one line
#   3. *args and **kwargs — flexible function arguments
#   4. Decorators — wrap functions with extra behavior
#   5. Generators — produce values one at a time (memory efficient)
#
# These are the tools that make Python code clean, fast, and professional.
# You'll see ALL of these in real AI codebases.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# ╔══════════════════════════════════════════════════════════════╗
# ║  EXERCISE 1: List Comprehensions                            ║
# ╚══════════════════════════════════════════════════════════════╝
# List comprehension = a shortcut to build a list in ONE line.
# Instead of writing a for-loop with .append(), you write it all inline.
#
# Syntax: [expression for item in iterable]
# With filter: [expression for item in iterable if condition]

def exercise_1():
    print("\n" + "=" * 50)
    print("  EXERCISE 1: List Comprehensions")
    print("=" * 50)

    # --- Traditional way (what you already know) ---
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Get squares using a for-loop
    squares_loop = []
    for n in numbers:
        squares_loop.append(n ** 2)
    print(f"  Loop way:          {squares_loop}")

    # --- List comprehension way (same result, one line!) ---
    squares_comp = [n ** 2 for n in numbers]
    print(f"  Comprehension way: {squares_comp}")

    # --- With a filter (if condition) ---
    # Only even numbers
    evens = [n for n in numbers if n % 2 == 0]
    print(f"\n  Even numbers: {evens}")

    # Only squares of odd numbers
    odd_squares = [n ** 2 for n in numbers if n % 2 != 0]
    print(f"  Odd squares:  {odd_squares}")

    # --- AI Use Case: Processing model responses ---
    responses = [
        {"model": "gpt-4", "score": 0.95, "tokens": 150},
        {"model": "gemini", "score": 0.88, "tokens": 200},
        {"model": "claude", "score": 0.92, "tokens": 180},
        {"model": "llama", "score": 0.75, "tokens": 300},
    ]

    # Get only model names
    model_names = [r["model"] for r in responses]
    print(f"\n  All models: {model_names}")

    # Get models with score > 0.90
    good_models = [r["model"] for r in responses if r["score"] > 0.90]
    print(f"  Good models (>0.90): {good_models}")

    # Get total tokens used
    total_tokens = sum([r["tokens"] for r in responses])
    print(f"  Total tokens: {total_tokens}")

    # --- String operations with comprehensions ---
    words = ["hello", "WORLD", "Python", "AI"]
    lower_words = [w.lower() for w in words]
    print(f"\n  Lowercased: {lower_words}")

    # Lengths of each word
    lengths = [len(w) for w in words]
    print(f"  Word lengths: {lengths}")

    print("\n  Key: [expression for item in list if condition]")


# ╔══════════════════════════════════════════════════════════════╗
# ║  EXERCISE 2: Dict Comprehensions                            ║
# ╚══════════════════════════════════════════════════════════════╝
# Same idea as list comprehensions, but builds a dictionary.
# Syntax: {key: value for item in iterable}
# With filter: {key: value for item in iterable if condition}

def exercise_2():
    print("\n" + "=" * 50)
    print("  EXERCISE 2: Dict Comprehensions")
    print("=" * 50)

    # --- Basic: Create a dict from a list ---
    models = ["gpt-4", "gemini", "claude", "llama"]

    # Traditional way
    model_lengths_loop = {}
    for m in models:
        model_lengths_loop[m] = len(m)
    print(f"  Loop way: {model_lengths_loop}")

    # Dict comprehension way (one line!)
    model_lengths = {m: len(m) for m in models}
    print(f"  Comp way: {model_lengths}")

    # --- From two lists using zip() ---
    # zip() pairs up items from two lists, like a zipper
    names = ["gpt-4", "gemini-pro", "claude-3"]
    prices = [0.03, 0.01, 0.015]

    pricing = {name: price for name, price in zip(names, prices)}
    print(f"\n  Pricing: {pricing}")

    # --- With a filter ---
    scores = {"gpt-4": 95, "gemini": 88, "claude": 92, "llama": 75, "mistral": 82}

    # Only models scoring above 85
    top_models = {name: score for name, score in scores.items() if score > 85}
    print(f"  Top models (>85): {top_models}")

    # --- AI Use Case: Transform API response data ---
    api_responses = [
        {"id": 1, "model": "gpt-4", "response": "Hello!"},
        {"id": 2, "model": "gemini", "response": "Hi there!"},
        {"id": 3, "model": "claude", "response": "Greetings!"},
    ]

    # Create a lookup dict: id → response
    lookup = {r["id"]: r["response"] for r in api_responses}
    print(f"\n  Lookup dict: {lookup}")
    print(f"  Response #2: {lookup[2]}")

    # --- Swapping keys and values ---
    original = {"a": 1, "b": 2, "c": 3}
    swapped = {v: k for k, v in original.items()}
    print(f"\n  Original: {original}")
    print(f"  Swapped:  {swapped}")

    print("\n  Key: {key: value for item in iterable if condition}")


# ╔══════════════════════════════════════════════════════════════╗
# ║  EXERCISE 3: *args and **kwargs                              ║
# ╚══════════════════════════════════════════════════════════════╝
# *args   = accept ANY NUMBER of positional arguments (as a tuple)
# **kwargs = accept ANY NUMBER of keyword arguments (as a dict)
#
# Why? When you don't know in advance how many arguments
# someone will pass to your function.

def exercise_3():
    print("\n" + "=" * 50)
    print("  EXERCISE 3: *args and **kwargs")
    print("=" * 50)

    # --- *args: Variable number of positional arguments ---
    def add_all(*args):
        """Takes any number of numbers and adds them"""
        # args is a TUPLE containing all the arguments
        print(f"    args received: {args} (type: {type(args).__name__})")
        return sum(args)

    print("  *args examples:")
    print(f"    add_all(1, 2)       = {add_all(1, 2)}")
    print(f"    add_all(1, 2, 3, 4) = {add_all(1, 2, 3, 4)}")
    print(f"    add_all(10)         = {add_all(10)}")

    # --- **kwargs: Variable number of keyword arguments ---
    def create_config(**kwargs):
        """Takes any number of key=value pairs"""
        # kwargs is a DICT containing all the keyword arguments
        print(f"\n    kwargs received: {kwargs} (type: {type(kwargs).__name__})")
        return kwargs

    print("\n  **kwargs examples:")
    config1 = create_config(model="gpt-4", temperature=0.7)
    print(f"    config1 = {config1}")

    config2 = create_config(model="gemini", temperature=0.9, max_tokens=1000, stream=True)
    print(f"    config2 = {config2}")

    # --- Combining regular args, *args, and **kwargs ---
    def ai_log(action, *models, **settings):
        """
        action  = required (normal arg)
        *models = any number of model names (tuple)
        **settings = any key=value pairs (dict)
        """
        print(f"\n    Action: {action}")
        print(f"    Models: {models}")
        print(f"    Settings: {settings}")

    print("\n  Combined example:")
    ai_log("compare", "gpt-4", "gemini", "claude",
           temperature=0.7, max_tokens=500)

    # --- Real AI Use Case: Flexible API wrapper ---
    def call_llm(prompt, model="gpt-4", **options):
        """A flexible function that accepts any extra options"""
        config = {"model": model, "prompt": prompt}
        config.update(options)  # Merge all extra options into config
        return config

    result = call_llm(
        "Explain Python",
        model="gemini",
        temperature=0.8,
        max_tokens=1000,
        stream=True
    )
    print(f"\n  Flexible API call config:")
    for key, value in result.items():
        print(f"    {key}: {value}")

    # --- Unpacking: The reverse of *args ---
    numbers = [1, 2, 3, 4, 5]
    print(f"\n  Unpacking a list with *:")
    print(f"    print(*numbers) =", *numbers)  # Same as print(1, 2, 3, 4, 5)

    settings = {"model": "gpt-4", "temp": 0.7}
    print(f"    Unpacking a dict with **: {*settings}")
    # **settings would unpack to: model="gpt-4", temp=0.7

    print("\n  Key: *args = tuple of extras, **kwargs = dict of extras")


# ╔══════════════════════════════════════════════════════════════╗
# ║  EXERCISE 4: Decorators                                      ║
# ╚══════════════════════════════════════════════════════════════╝
# A decorator WRAPS a function with extra behavior.
# Think of it like adding a layer around a function:
#   - Do something BEFORE the function runs
#   - Run the original function
#   - Do something AFTER the function runs
#
# Syntax: @decorator_name (placed above the function)
#
# Real uses: logging, timing, authentication, retrying failed API calls

def exercise_4():
    print("\n" + "=" * 50)
    print("  EXERCISE 4: Decorators")
    print("=" * 50)

    import time

    # --- Step 1: Understanding what a decorator IS ---
    # A decorator is just a function that takes a function and returns a new function.

    # Let's build one step by step:
    def my_logger(func):
        """This is a decorator — it wraps another function"""
        def wrapper(*args, **kwargs):
            print(f"    >> Calling {func.__name__}()")
            result = func(*args, **kwargs)  # Call the original function
            print(f"    << {func.__name__}() returned: {result}")
            return result
        return wrapper

    # Apply the decorator using @
    @my_logger
    def add(a, b):
        return a + b

    @my_logger
    def greet(name):
        return f"Hello, {name}!"

    print("  Logger decorator:")
    add(3, 5)
    greet("Lucky")

    # --- Step 2: A timing decorator (VERY useful in AI!) ---
    def timer(func):
        """Measures how long a function takes to run"""
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            elapsed = round(end - start, 4)
            print(f"    [{func.__name__}] took {elapsed}s")
            return result
        return wrapper

    @timer
    def slow_function():
        """Simulates a slow API call"""
        time.sleep(0.5)  # Wait 0.5 seconds
        return "Done!"

    @timer
    def fast_function():
        return sum(range(1000000))

    print("\n  Timer decorator:")
    slow_function()
    fast_function()

    # --- Step 3: A retry decorator (CRITICAL for API calls!) ---
    def retry(max_attempts=3):
        """Decorator that retries a function if it fails"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                for attempt in range(1, max_attempts + 1):
                    try:
                        result = func(*args, **kwargs)
                        print(f"    Attempt {attempt}: Success!")
                        return result
                    except Exception as e:
                        print(f"    Attempt {attempt}: Failed ({e})")
                        if attempt == max_attempts:
                            print(f"    All {max_attempts} attempts failed!")
                            raise
            return wrapper
        return decorator

    import random

    @retry(max_attempts=3)
    def unreliable_api_call():
        """Simulates an API that fails randomly"""
        if random.random() < 0.6:  # 60% chance of failure
            raise ConnectionError("Server timeout")
        return {"status": "success"}

    print("\n  Retry decorator:")
    try:
        unreliable_api_call()
    except ConnectionError:
        print("    (All retries exhausted in this run)")

    print("\n  Key: @decorator adds behavior AROUND your function")


# ╔══════════════════════════════════════════════════════════════╗
# ║  EXERCISE 5: Generators                                      ║
# ╚══════════════════════════════════════════════════════════════╝
# A generator is a function that produces values ONE AT A TIME
# instead of building an entire list in memory.
#
# Key difference:
#   - List: [1, 2, 3, 4, 5] — ALL values stored in memory at once
#   - Generator: produces 1, then 2, then 3... one by one
#
# Uses 'yield' instead of 'return'
# 'yield' = "give this value and PAUSE, continue when asked for more"
#
# Why? When dealing with millions of items (like training data),
# you can't load everything into memory at once!

def exercise_5():
    print("\n" + "=" * 50)
    print("  EXERCISE 5: Generators")
    print("=" * 50)

    # --- Basic generator ---
    def count_up_to(n):
        """Generates numbers from 1 to n, one at a time"""
        i = 1
        while i <= n:
            yield i    # Pause here, give this value, resume when asked
            i += 1

    print("  Basic generator:")
    counter = count_up_to(5)  # This does NOT run the function yet!
    print(f"    Type: {type(counter)}")  # It's a generator object
    print(f"    next(): {next(counter)}")  # 1 — runs until first yield
    print(f"    next(): {next(counter)}")  # 2 — resumes, runs until next yield
    print(f"    next(): {next(counter)}")  # 3

    # Using in a for loop (the normal way)
    print("    Full loop:", end=" ")
    for num in count_up_to(5):
        print(num, end=" ")
    print()

    # --- Generator vs List: Memory comparison ---
    import sys

    # List: stores ALL 1 million numbers in memory
    big_list = [i for i in range(1_000_000)]
    list_size = sys.getsizeof(big_list)

    # Generator: stores only the FORMULA, not the numbers
    big_gen = (i for i in range(1_000_000))  # Note: () not []
    gen_size = sys.getsizeof(big_gen)

    print(f"\n  Memory comparison (1 million numbers):")
    print(f"    List size:      {list_size:,} bytes ({list_size // 1024} KB)")
    print(f"    Generator size: {gen_size:,} bytes")
    print(f"    Generator is {list_size // gen_size}x smaller!")

    # --- AI Use Case: Processing training data in batches ---
    def batch_loader(data, batch_size=3):
        """Yields data in batches — like loading training data"""
        for i in range(0, len(data), batch_size):
            yield data[i:i + batch_size]

    training_data = [
        "What is AI?",
        "Explain Python",
        "Define ML",
        "What is NLP?",
        "Explain RAG",
        "Define LLM",
        "What is fine-tuning?",
        "Explain embeddings",
    ]

    print(f"\n  Batch loading (batch_size=3):")
    for batch_num, batch in enumerate(batch_loader(training_data, batch_size=3), 1):
        print(f"    Batch {batch_num}: {batch}")

    # --- Generator Expression (one-liner generator) ---
    # Same as list comprehension but with () instead of []
    squares_list = [x**2 for x in range(5)]     # List — stored in memory
    squares_gen = (x**2 for x in range(5))       # Generator — lazy

    print(f"\n  List:      {squares_list}")
    print(f"  Generator: {squares_gen}")  # Shows object, not values
    print(f"  Gen values: {list(squares_gen)}")  # Convert to list to see values

    # --- AI Use Case: Streaming API responses ---
    def stream_response(text):
        """Simulates streaming an AI response word by word"""
        words = text.split()
        for word in words:
            yield word

    print(f"\n  Streaming AI response:")
    print("    ", end="")
    for word in stream_response("Generators are perfect for streaming AI responses token by token"):
        print(word, end=" ")
    print()

    print("\n  Key: yield = pause & produce | generators = memory efficient")


# ╔══════════════════════════════════════════════════════════════╗
# ║  EXERCISE 6: Putting It All Together                         ║
# ╚══════════════════════════════════════════════════════════════╝
# Combine comprehensions, *args/**kwargs, decorators, and generators
# into one practical AI-themed example.

def exercise_6():
    print("\n" + "=" * 50)
    print("  EXERCISE 6: Putting It All Together")
    print("=" * 50)

    import time
    import random

    # Timer decorator
    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = round(time.time() - start, 4)
            print(f"    [{func.__name__}] completed in {elapsed}s")
            return result
        return wrapper

    # A class that uses everything from Day 3
    class DataPipeline:
        """Processes AI training data using advanced Python features"""

        def __init__(self, name, *data_sources, **config):
            """Uses *args for data sources, **kwargs for config"""
            self.name = name
            self.data_sources = list(data_sources)
            self.config = {
                "batch_size": config.get("batch_size", 4),
                "filter_empty": config.get("filter_empty", True),
                "lowercase": config.get("lowercase", True),
            }
            self.processed = []

        @timer
        def process(self, raw_data):
            """Process raw data using comprehensions"""
            # Step 1: Filter empty strings (list comprehension + condition)
            if self.config["filter_empty"]:
                cleaned = [item.strip() for item in raw_data if item.strip()]
            else:
                cleaned = [item.strip() for item in raw_data]

            # Step 2: Lowercase if configured (list comprehension)
            if self.config["lowercase"]:
                cleaned = [item.lower() for item in cleaned]

            # Step 3: Create metadata (dict comprehension)
            self.processed = [
                {"text": item, "length": len(item), "word_count": len(item.split())}
                for item in cleaned
            ]

            return self.processed

        def get_batches(self, batch_size=None):
            """Generator that yields data in batches"""
            bs = batch_size or self.config["batch_size"]
            for i in range(0, len(self.processed), bs):
                yield self.processed[i:i + bs]

        def get_stats(self):
            """Uses comprehensions to calculate stats"""
            if not self.processed:
                return "No data processed yet"

            lengths = [item["length"] for item in self.processed]
            word_counts = [item["word_count"] for item in self.processed]

            return {
                "total_items": len(self.processed),
                "avg_length": round(sum(lengths) / len(lengths), 1),
                "avg_words": round(sum(word_counts) / len(word_counts), 1),
                "longest": max(lengths),
                "shortest": min(lengths),
            }

        def __str__(self):
            return f"DataPipeline('{self.name}', {len(self.processed)} items)"

    # --- Use the pipeline ---
    raw_data = [
        "What is Artificial Intelligence?",
        "  Explain machine learning  ",
        "",
        "How do neural networks work?",
        "  ",
        "What is Natural Language Processing?",
        "Define deep learning",
        "Explain transformers and attention",
        "What are embeddings?",
        "",
        "How does RAG work?",
        "Explain fine-tuning vs prompting",
    ]

    # Create pipeline with *args and **kwargs
    pipeline = DataPipeline(
        "AI Questions",                   # name (regular arg)
        "web_scrape", "user_uploads",     # *args (data sources)
        batch_size=3,                     # **kwargs (config)
        lowercase=True
    )

    print(f"\n  Pipeline: {pipeline}")
    print(f"  Config: {pipeline.config}")
    print(f"  Sources: {pipeline.data_sources}")

    # Process data (uses decorator + comprehensions)
    result = pipeline.process(raw_data)

    print(f"\n  Processed {len(result)} items (filtered empty lines)")

    # Get stats (uses comprehensions)
    stats = pipeline.get_stats()
    print(f"\n  Stats:")
    for key, value in stats.items():
        print(f"    {key}: {value}")

    # Batch loading (uses generator)
    print(f"\n  Batches (size=3):")
    for i, batch in enumerate(pipeline.get_batches(), 1):
        texts = [item["text"][:30] for item in batch]  # Comprehension!
        print(f"    Batch {i}: {texts}")

    print(f"\n  {pipeline}")
    print("\n  Comprehensions + *args/**kwargs + Decorators + Generators = Pro Python!")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# RUN ALL EXERCISES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if __name__ == "__main__":
    print("Day 3: Python Advanced")
    print("=" * 55)

    exercise_1()   # List Comprehensions
    exercise_2()   # Dict Comprehensions
    exercise_3()   # *args and **kwargs
    exercise_4()   # Decorators
    exercise_5()   # Generators
    exercise_6()   # Putting It All Together

    print("\n" + "=" * 55)
    print("Day 3 Complete!")
    print("=" * 55)
    print("""
    What you learned:
    1. List Comprehensions  - [x for x in list if condition]
    2. Dict Comprehensions  - {k: v for k, v in items}
    3. *args/**kwargs       - flexible function arguments
    4. Decorators           - @wrapper adds behavior around functions
    5. Generators           - yield values one at a time (memory efficient)
    6. Combined everything into a DataPipeline

    Now open day3_challenge.py and practice!
    """)
