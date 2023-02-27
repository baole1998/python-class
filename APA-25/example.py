# Cấu trúc dữ liệu:
# - Array
# - Linked list
# - Stack
# - Queues
# - Binary tree
# - Graphs
# - Hash table
# Mảng (Array): Một mảng là một tập hợp các phần tử có cùng kiểu dữ liệu và được lưu trữ liên tiếp trong bộ nhớ. Các phần tử trong mảng được truy cập thông qua chỉ mục của chúng.

# Danh sách liên kết (Linked List): Một danh sách liên kết là một danh sách các nút, trong đó mỗi nút chứa một giá trị dữ liệu và một liên kết đến nút tiếp theo trong danh sách. Các nút trong danh sách liên kết không được lưu trữ liên tiếp trong bộ nhớ.

# Cây (Tree): Một cây là một cấu trúc dữ liệu phân cấp, trong đó mỗi nút chứa một giá trị dữ liệu và có thể có một hoặc nhiều nút con.

# Đồ thị (Graph): Một đồ thị là một tập hợp các đỉnh và các cạnh giữa các đỉnh đó. Mỗi đỉnh có thể có một hoặc nhiều cạnh nối với các đỉnh khác.

# Hàng đợi (Queue): Một hàng đợi là một cấu trúc dữ liệu trừu tượng, trong đó các phần tử được chèn vào cuối hàng đợi và được loại bỏ từ đầu hàng đợi.

# Ngăn xếp (Stack): Một ngăn xếp là một cấu trúc dữ liệu trừu tượng, trong đó các phần tử được chèn vào và loại bỏ từ cùng một đầu của ngăn xếp.

if __name__ == "__main__":
    # Hàm tìm kiếm theo chiều sâu
    # Định nghĩa một đồ thị bằng danh sách kề
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    def dfs(graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for next in graph[start]:
            if next not in visited:
                dfs(graph, next, visited)

    # Sử dụng hàm tìm kiếm theo chiều sâu để tìm đường đi từ đỉnh A đến các đỉnh khác
    dfs(graph, 'A')
