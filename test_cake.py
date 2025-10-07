"""
Start with the first test and make it pass, then move to the next one.
Run: uv run pytest
"""

from cake import Cupcake


# Basic cake functionality
def test_cupcake_name():
    cupcake = Cupcake()
    assert cupcake.name() == "🧁"

# def test_cookie_name():
#     cookie = Cookie()
#     assert cookie.name() == "🍪"

# def test_cupcake_price():
#     cupcake = Cupcake()
#     assert cupcake.price() == 1.0

# def test_cookie_price():
#     cookie = Cookie()
#     assert cookie.price() == 2.0


# # Single toppings
# def test_cupcake_with_chocolate_name():
#     cake = Chocolate(Cupcake())
#     assert cake.name() == "🧁 with 🍫"

# def test_cookie_with_chocolate_name():
#     cake = Chocolate(Cookie())
#     assert cake.name() == "🍪 with 🍫"

# def test_cupcake_with_chocolate_price():
#     cake = Chocolate(Cupcake())
#     assert cake.price() == 1.1

# def test_cookie_with_chocolate_price():
#     cake = Chocolate(Cookie())
#     assert cake.price() == 2.1


# # Multiple toppings
# def test_cookie_with_chocolate_and_nuts_name():
#     cake = Nuts(Chocolate(Cookie()))
#     assert cake.name() == "🍪 with 🍫 and 🥜"

# def test_cookie_with_nuts_and_chocolate_name():
#     cake = Chocolate(Nuts(Cookie()))
#     assert cake.name() == "🍪 with 🥜 and 🍫"

# def test_cookie_with_chocolate_and_nuts_price():
#     cake = Nuts(Chocolate(Cookie()))
#     assert cake.price() == 2.2

# def test_complex_cake_with_all_toppings():
#     cake = Sugar(Nuts(Chocolate(Cupcake())))
#     assert cake.name() == "🧁 with 🍫 and 🥜 and 🍬"
#     assert cake.price() == 1.3


# # Bundles
# def test_bundle_with_single_cupcake():
#     cupcake = Cupcake()
#     bundle = Bundle([cupcake])
#     assert bundle.price() == 0.9  # 1.0 * 0.9

# def test_bundle_with_cupcake_and_cookie():
#     cupcake = Cupcake()
#     cookie = Cookie()
#     bundle = Bundle([cupcake, cookie])
#     assert bundle.price() == 2.7  # (1.0 + 2.0) * 0.9

# def test_bundle_with_decorated_cakes():
#     decorated_cupcake = Chocolate(Cupcake())
#     decorated_cookie = Nuts(Cookie())
#     bundle = Bundle([decorated_cupcake, decorated_cookie])
#     assert bundle.price() == 2.88  # (1.1 + 2.1) * 0.9

# def test_nested_bundles():
#     cupcake1 = Cupcake()
#     cupcake2 = Cupcake()
#     inner_bundle = Bundle([cupcake1, cupcake2])

#     cookie = Cookie()
#     outer_bundle = Bundle([inner_bundle, cookie])
#     assert outer_bundle.price() == 3.42  # ((1 + 1) * 0.9 + 2.0) * 0.9


# # Integration test
# def test_complex_scenario():
#     fancy_cupcake = Sugar(Nuts(Chocolate(Cupcake())))
#     simple_cookie = Chocolate(Cookie())
#     plain_cupcake = Cupcake()

#     cake_bundle = Bundle([fancy_cupcake, simple_cookie])
#     mega_bundle = Bundle([cake_bundle, plain_cupcake])

#     assert abs(mega_bundle.price() - 3.654) < 0.001  # ((1.3 + 2.1) * 0.9 + 1.0) * 0.9