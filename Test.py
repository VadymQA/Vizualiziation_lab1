# Відкриваємо файл для читання
with open('output.txt', 'r') as file:
    lines = file.readlines()

# Створюємо новий список для зберігання відфільтрованих рядків
filtered_lines = []
min = 0
max = 10
# Проходимося по кожному рядку
for line in lines:
    # Розбиваємо рядок на стовпці
    columns = line.split()

    # Перевіряємо, чи задовольняють значення другого та третього стовпців умові
    if len(columns) >= 3 and (float(columns[1]) < min or float(columns[2]) < min or float(columns[1]) > max or float(columns[2]) > max):
        continue  # Пропускаємо рядок, якщо умова виконується

    # Додаємо рядок до відфільтрованого списку
    filtered_lines.append(line)

# Відкриваємо файл для запису та записуємо відфільтровані рядки
with open('output2.txt', 'w') as file:
    file.writelines(filtered_lines)
