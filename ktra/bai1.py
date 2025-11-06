chuoi = "TV, Laptop, Phone, TV, Tablet, Laptop, Camera"
list1 = chuoi.split(", ")
list2 = set(list1)
list3 = tuple(list2)
print(f"Kho hàng (tuple): {list3}")
print(f"Tổng số loại hàng: {len(list3)}")
banchay = {"Phone", "Laptop", "Smartwatch"}
print(f"Sản phẩm bán chạy trong kho: {set(list3).intersection(banchay)}")
print(f"Sản phẩm không nằm trong danh sách bán chạy: {set(list3).difference(banchay)}")