def create_item(name, qty, price):
    item = {"name" : name, "soluong" : qty, "price" : price}
    return item
def calc_total(items):
    total = 0
    for item in items:
        total += item["soluong"] * item["price"]
    return total
def format_invoice(customer, items):
    hoadon = f"customer : {customer}"
    hoadon += "\n---------------------"
    hoadon += f"\nProduct   Qty    Price    Subtotal "
    total = 0
    for item in items:
        name = item["name"]
        qty = item["soluong"]
        price = item["price"]
        subtotal = qty * price
        total += subtotal
        hoadon += f"\n{name}    {qty}   {price}    {subtotal}"
    hoadon += f"\nTOTAL : {total}"
    return hoadon
def export_text(invoice_string):
    dong = invoice_string.split("\n")
    return dong
items = []
items.append(create_item("pen",2,7))
items.append(create_item("book",3,10))
items.append(create_item("thuoc ke",5,4))
hoadon = format_invoice("Tran Van Son",items)
print(hoadon)
dong = export_text(hoadon)
print(dong)    