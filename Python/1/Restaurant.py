"""Restaurant"""
def restaurant():
    """Restaurant"""
    food_price = float(input())
    promo_price = float(input())
    discount = (100-float(input()))/100
    new_menu = float(input())
    all_price = food_price+new_menu
    if all_price >= promo_price:
        all_price = all_price*discount
    if food_price >= promo_price:
        food_price = food_price*discount
    if all_price < food_price:
        print("Yes %.3f"%(food_price-all_price))
    elif food_price < all_price:
        print("No %.3f"%(all_price-food_price))
    else:
        print("Yes")
restaurant()
