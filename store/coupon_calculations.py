"""
Author: Viktoriia Denys
Program: coupon_calculations.py
This program accepts the amount of the purchase,the cash coupon,
the percent coupon and it will calculate and return the total order item
"""
TAX = 0.06

"""
up to $10 dollars, shipping is $5.95
$10 and up to $30 dollars, shipping is $7.95
$30 and up to $50 dollars, shipping is $11.95
Shipping is free for $50 and over
"""

def calculate_price(price, cash_coupon, percent_coupon):
    cash_coupon_price = price - cash_coupon
    percent_coupon_price = cash_coupon_price - (cash_coupon_price*percent_coupon/100)
    subtotal_tax = percent_coupon_price + (percent_coupon_price*TAX)
    shipping = 0

    if percent_coupon_price < 10:
        shipping = 5.95
    elif percent_coupon_price < 30:
        shipping = 7.95
    elif percent_coupon_price < 50:
        shipping = 11.95
    else:
        shipping = 0

    total = subtotal_tax + shipping
    return total


if __name__ == '__main__':
    print(calculate_price(75.00, 5, 10))

