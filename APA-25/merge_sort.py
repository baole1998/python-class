
def merge_sort(arr):
    # Nếu arr chỉ chứa một phần tử hoặc không có phần tử nào, trả về arr.
        if len(arr) <= 1:
            return arr

        # Chia arr thành hai phần bằng cách tìm chỉ số trung bình.
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Đệ quy gọi merge_sort() trên hai nửa của arr.
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        # Gộp hai nửa đã sắp xếp để tạo ra một dãy hoàn chỉnh đã sắp xếp.
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        return arr


arr=[1,32,46,75,34,243,2423,656,545,34,2,43344,45,24,324]
print(merge_sort(arr))

    