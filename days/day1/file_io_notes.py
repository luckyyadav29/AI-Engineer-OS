# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FILE I/O — Step by Step from Zero
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Run this file from the scripts folder:
#   cd scripts
#   python pd1.py


# ══════════════════════════════════════════
# STEP 1: WRITING to a file
# ══════════════════════════════════════════
# open("filename", "w") → "w" means WRITE mode
# If the file doesn't exist, Python CREATES it
# If it already exists, it OVERWRITES it

f = open("hello.txt", "w")
f.write("Hello World!")
f.close()

print("Step 1: Created hello.txt ✅")
# Go check your scripts folder — hello.txt is now there!


# ══════════════════════════════════════════
# STEP 2: READING from a file
# ══════════════════════════════════════════
# open("filename", "r") → "r" means READ mode

f = open("hello.txt", "r")
content = f.read()
f.close()

print(f"Step 2: Read from hello.txt → '{content}' ✅")


# ══════════════════════════════════════════
# STEP 3: Why do we need f.close()?
# ══════════════════════════════════════════
# When you open() a file, your computer "locks" it.
# If you forget f.close(), the file stays locked.
# That can cause bugs, data loss, or crashes.
#
# SOLUTION → use "with" so Python closes it FOR you:

with open("hello.txt", "r") as f:
    content = f.read()

# f is automatically closed here — no need to call f.close()
print(f"Step 3: Using 'with' → '{content}' ✅")


# ══════════════════════════════════════════
# STEP 4: Writing MULTIPLE lines
# ══════════════════════════════════════════
# \n = new line (like pressing Enter)

with open("names.txt", "w") as f:
    f.write("Lucky\n")
    f.write("Rahul\n")
    f.write("Priya\n")

print("Step 4: Created names.txt with 3 names ✅")


# ══════════════════════════════════════════
# STEP 5: Reading ALL lines at once
# ══════════════════════════════════════════

with open("names.txt", "r") as f:
    everything = f.read()  # one big string

print(f"Step 5: Read all at once →")
print(everything)


# ══════════════════════════════════════════
# STEP 6: Reading LINE BY LINE
# ══════════════════════════════════════════
# f.readlines() gives you a LIST of lines

with open("names.txt", "r") as f:
    lines = f.readlines()

print(f"Step 6: readlines() → {lines}")
# Output: ['Lucky\n', 'Rahul\n', 'Priya\n']

# Clean way — loop through each line:
with open("names.txt", "r") as f:
    for line in f:
        name = line.strip()  # .strip() removes the \n
        print(f"  Hello, {name}!")


# ══════════════════════════════════════════
# STEP 7: APPEND mode — add WITHOUT erasing
# ══════════════════════════════════════════
# "w" = write (erases old content)
# "a" = append (adds to the end)

with open("names.txt", "a") as f:
    f.write("Amit\n")
    f.write("Sneha\n")

print("\nStep 7: Appended 2 more names ✅")

with open("names.txt", "r") as f:
    print(f.read())


# ══════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════
print("━" * 40)
print("  FILE I/O CHEAT SHEET")
print("━" * 40)
print("""
  MODES:
    "r"  → Read     (file must exist)
    "w"  → Write    (creates new / erases old)
    "a"  → Append   (adds to end)

  METHODS:
    f.read()       → entire file as one string
    f.readlines()  → list of lines
    f.write("...")  → write text to file
    f.close()      → close the file

  BEST PRACTICE:
    with open("file.txt", "r") as f:
        content = f.read()
    # auto-closes when done!
""")