**sandwich_generator.py**
```python
import random

ingredients = ['bread', 'lettuce', 'tomato', 'cheese', 'ham', 'turkey', 'pickles', 'mustard']

def generate_sandwich():
    selected = random.sample(ingredients, 4)
    print("Your sandwich includes:", ", ".join(selected))

if __name__ == "__main__":
    generate_sandwich()
