import os
from jinja2 import Environment, FileSystemLoader
from datetime import date

def generate_quotation(heading, items, note, shipping_date, contact):
    template_dir = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("quotation_template.html")

    output = template.render(
        heading=heading,
        items=items,
        note=note,
        shipping_date=shipping_date,
        contact=contact,
        date=date.today().strftime("%Y-%m-%d")
    )

    with open("quotation_sheet.html", "w") as f:
        f.write(output)

if __name__ == "__main__":
    heading = {
        "buyer": "John Doe",
        "inquiry_code": "INQ123",
        "application": "Home Appliances",
        "receiver_address": "123 Main St, Springfield, MA 01101",
        "receiver": "Jane Smith",
        "telephone": "555-123-4567"
    }

items = [    {        "no": 1,        "product_name": "Washing Machine",        "code": "WM123",        "size": "600x600x900",        "material": "Stainless Steel",        "quantity": 10,        "unit_price": 500,        "total_price": 5000,        "remark": "Standard model"    },    {        "no": 2,        "product_name": "Refrigerator",        "code": "RF456",        "size": "700x700x1800",        "material": "Stainless Steel",        "quantity": 5,        "unit_price": 1200,        "total_price": 6000,        "remark": "Double door model"    }]

note = "All prices are in USD. Taxes and shipping costs are not included."
shipping_date = "2023-04-15"
contact = "John Doe (john.doe@example.com)"

generate_quotation(heading, items, note, shipping_date, contact)
