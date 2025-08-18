def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = (discount_percentage / 100) * int(price)
        new_price = int(price) - discount_amount
        print(f"After applying a discount of {discount_percentage}%, the new price is ${new_price}") 
    else:
        print(f"Sorry no discount was applied, here is the final price: {price}") 


price = input("Input price: ")
discount_percentage =input("Input percentage discount applied: ")
discount_percentage = int(discount_percentage)

calculate_discount(price, discount_percentage)