''' Biểu đồ tròn '''

import matplotlib.pyplot as pyplot
labels = ('Huế', 'Sài Gòn', 'Hà Nội', 'Đà Nẵng')
sizes = [17, 33, 42, 7]
explode = (0, 0, 0.1, 0)
pyplot.pie(
    sizes,
    labels=labels,
    autopct='%1.f%%',
    explode=explode,
    counterclock=False,
    startangle=105,
    shadow=True
)
pyplot.axis('equal')