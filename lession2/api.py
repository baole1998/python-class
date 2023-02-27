from flask import Flask, render_template  # chúng ta nhập (import) vào lớp (class) Flask.

app = Flask(__name__)  # Khởi tạo instance của class, nó chính là một ứng dụng WSGI. Hay nói cách khác, dòng code này tạo một web server để chuyển các yêu cầu từ client tới ứng dụng web. Tham số đầu được truyền vào ở đây là '__name__', bạn nên giữ nguyên như vậy nếu ứng dụng của bạn chỉ có một module duy nhất như trong ví dụ này, nếu bạn xây dựng ứng dụng web lớn hơn và có nhiều module thì bạn có thể thay đổi tham số đầu tiên này như theo hướng dẫn trong tài liệu Flask api.


@app.route('/hello')  # python ký tự @ là thể hiện cho Decorators, route decorator cho FLask biết được url nào ứng với hàm nào. Trong ví dụ trên url '/hello' ứng với hàm hello_world(), do vậy khi client gửi yêu cầu theo đường dẫn http://<ip_or_domain>:<port>/hello (ví dụ: http://127.0.0.1:5000/hello), web server dựa vào đường dẫn và route decorator để chuyển yêu cầu tới hàm xử lý tương ứng hello_world(), hàm này đóng vai trò làm ứng dụng web (web application).
def hello_world():      # Hàm hello_world() là một hàm python thông thường, nó xử lý yêu cầu được gửi lên từ client và trả về kết quả mà client mong muốn.
    return 'Hello, World!'

@app.route('/')      # python ký tự @ là thể hiện cho Decorators, route decorator cho FLask biết được url nào ứng với hàm nào. Trong ví dụ trên url '/hello' ứng với hàm hello_world(), do vậy khi client gửi yêu cầu theo đường dẫn http://<ip_or_domain>:<port>/hello (ví dụ: http://127.0.0.1:5000/hello), web server dựa vào đường dẫn và route decorator để chuyển yêu cầu tới hàm xử lý tương ứng hello_world(), hàm này đóng vai trò làm ứng dụng web (web application).
def template():      # Hàm hello_world() là một hàm python thông thường, nó xử lý yêu cầu được gửi lên từ client và trả về kết quả mà client mong muốn.
    return render_template('index.html'),500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


# Flask app được chạy với lệnh app.run(). Chúng ta có thể điều chỉnh một số tham số trong hàm run.

# host='0.0.0.0': Địa chỉ IP để ứng dụng Flask lắng nghe các kết nối, mặc định giá trị của tham số này là '127.0.0.1' và ứng dụng flask chỉ chấp nhận các kết nối từ máy local. chuyển giá trị này thành '0.0.0.0' để ứng dụng chấp nhận các kết nối từ bên ngoài.

# port=5001: Giá trị của port là một số nguyên, giá trị mặc định bằng 5000. Là cổng được mở trên máy mà ứng dụng Flask chạy, cần chọn cổng mà chưa được mở trên máy để tránh gặp lỗi khi chạy.
