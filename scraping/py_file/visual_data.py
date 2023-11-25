from matplotlib import pyplot as plt

# klass = [i for i in range(1, 12)]
# ball = [10, 10, 10, 8.8, 9.6, 7, 7.4, 7.8, 8.2, 8.5, 8.7]
#
# plt.plot(klass,
#          ball,
#          color='blue',
#          marker='o',
#          linestyle='solid')
#
# #  параметры диаграмы
# plt.title('Средний балл за 11 классов')
#
# # Добавление названия оси y
# plt.ylabel('балл')
#
# #  Добавление названия оси x
# plt.xlabel('классы')
#
# # Вывод диаграмы
# plt.show()


movie = ['2019', '2020']
num = [55.680, 49.973]

plt.bar(range(len(movie)), num)
plt.title('Бабки Ауди в моем кармане')
plt.ylabel('Бабки, триллионы')
plt.xticks(range(len(movie)), movie)
plt.show()

