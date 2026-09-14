# Day 3: Python Advanced

## Topics Covered
1. **List Comprehensions** — build lists in one powerful line
2. **Dict Comprehensions** — build dictionaries in one line
3. **\*args and \*\*kwargs** — accept any number of arguments
4. **Decorators** — wrap functions with extra behavior (@timer, @retry)
5. **Generators** — produce values one at a time (memory efficient with `yield`)

## Files
| File | Purpose |
|------|---------|
| `day3_python_advanced.py` | Lesson with 6 guided exercises |
| `day3_challenge.py` | Practice problems to solve yourself |

## Key Concepts

### List Comprehension
```python
[expression for item in list if condition]
```

### Dict Comprehension
```python
{key: value for item in list if condition}
```

### *args and **kwargs
```python
def func(*args, **kwargs):
    # args = tuple of positional args
    # kwargs = dict of keyword args
```

### Decorators
```python
@my_decorator
def my_function():
    pass
# Same as: my_function = my_decorator(my_function)
```

### Generators
```python
def my_gen():
    yield 1  # pause, give 1
    yield 2  # pause, give 2
    yield 3  # pause, give 3
```

## AI Engineering Connection
- **Comprehensions**: Processing API responses, filtering model results
- **\*args/\*\*kwargs**: Building flexible API wrappers (Day 5-6)
- **Decorators**: Logging, timing, retry logic for API calls (Day 10+)
- **Generators**: Streaming responses, batch loading training data (Day 14+)
