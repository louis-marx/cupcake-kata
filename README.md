# 🧁 Cupcake Kata

A coding kata for practicing **Decorator** and **Composite** design patterns.

## Problem Description

Write a program that can build cakes with toppings like:
- "🧁 with 🍫 and 🥜"
- "🍪 with 🍫"

**Important:** The order of toppings matters!

Your solution should:
1. Show the name of any cake combination
2. Calculate the price (base cake + toppings)
3. Support bundles with 10% discount

## Getting Started

```bash
uv run pytest
```

## Design Patterns

### Decorator Pattern
```python
cake = Sugar(Nuts(Chocolate(Cupcake())))
print(cake.name())   # "🧁 with 🍫 and 🥜 and 🍬"
print(cake.price())  # 1.3 (1.0 + 0.1 + 0.1 + 0.1)
```

### Composite Pattern
```python
bundle = Bundle([Chocolate(Cupcake()), Nuts(Cookie())])
print(bundle.price())  # 2.88 ((1.1 + 2.1) * 0.9)
```

## Specifications

### Names
- "🧁" for Cupcake
- "🍪" for Cookie
- "🧁 with 🍫" for Cupcake with Chocolate
- "🍪 with 🍫 and 🥜" for Cookie with Chocolate and Nuts
- ...

### Prices
- Cupcake: $1.00, 
- Cookie: $2.00
- Toppings: $0.10 each
- Bundle: 10% discount