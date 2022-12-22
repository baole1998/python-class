a_list = ["APF", 100, "API", 200]
# for index, value in enumerate(a_list, start=1):
#     print(f"Đây là giá trị thứ {index} trong list:", value)
    
a_tuple: tuple = tuple(("APF", 100, "API", 200))
for index, value in enumerate(a_tuple):
    print("Index now")
    assert index == 10, "Index phải bằng 10 luôn, nếu không bằng 10 luôn thì dừng"
    print(f"Đây là giá trị thứ {index} trong tuples:", value)