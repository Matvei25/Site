import matplotlib.pyplot as plt

# Данные для построения графика
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание графика
plt.plot(x, y)

# Настройка осей и заголовка
plt.xlabel('X-ось')
plt.ylabel('Y-ось')
plt.title('Пример графика')

# Отображение графика
plt.show()
