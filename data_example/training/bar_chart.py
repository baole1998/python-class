''' Biểu đồ cột '''

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

labels = ('Huế', 'Sài Gòn', 'Hà Nội', 'Đà Nẵng')
sizes = [17, 33, 42, 7]
bar_labels = ['red', 'blue', 'green', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

ax.bar(labels, sizes, label=bar_labels, color=bar_colors)

ax.set_ylabel('Số lượng học viên')
ax.set_title('Số lượng học viên tham gia lớp đào tạo Python theo tỉnh thành')
ax.legend(title='Tỉnh thành')

plt.show()