from django import template

register = template.Library()

@register.filter
def format_price(price):
    # Convert the price to a string
    price_str = str(price)
    
    # Split the price into integer and decimal parts
    if '.' in price_str:
        integer_part, decimal_part = price_str.split('.')
    else:
        integer_part = price_str
        decimal_part = ''
    
    # Reverse the integer part for easier processing
    reversed_integer = integer_part[::-1]
    
    # Add commas every three digits
    grouped_integer = ','.join(reversed_integer[i:i+3] for i in range(0, len(reversed_integer), 3))
    
    # Reverse the integer part back to normal
    formatted_integer = grouped_integer[::-1]
    
    # Combine the formatted integer part with the decimal part if it exists
    if decimal_part:
        return f'{formatted_integer}.{decimal_part}'
    else:
        return formatted_integer
