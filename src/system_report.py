import subprocess
from collections import defaultdict
from datetime import datetime

# Вызываем 'ps aux' и получаем его вывод
output = subprocess.check_output(['ps', 'aux']).decode('utf-8')

# Разбиваем вывод построчно
lines = output.split('\n')

# Словарь для подсчета пользовательских процессов
user_processes = defaultdict(int)

# Переменные для подсчета общей памяти и CPU
total_memory = 0
total_cpu = 0.0

# Словари для определения процессов, использующих больше всего памяти и CPU
most_memory_process = {'name': '', 'memory': 0}
most_cpu_process = {'name': '', 'cpu': 0.0}

# Проходим по каждой строке вывода 'ps aux'
for line in lines[1:]:
    parts = line.split()

    # Пропускаем пустые строки
    if not parts:
        continue

    # Получаем информацию о процессе
    user = parts[0]
    memory = float(parts[5]) / 1024  # Переводим килобайты в мегабайты
    cpu = float(parts[2])

    # Добавляем процесс к подсчету пользовательских процессов
    user_processes[user] += 1

    # Обновляем общую память и CPU
    total_memory += memory
    total_cpu += cpu

    # Проверяем, использует ли этот процесс больше памяти или CPU, чем предыдущие
    if memory > most_memory_process['memory']:
        most_memory_process['name'] = parts[10][:20]  # Первые 20 символов имени процесса
        most_memory_process['memory'] = memory
    if cpu > most_cpu_process['cpu']:
        most_cpu_process['name'] = parts[10][:20]  # Первые 20 символов имени процесса
        most_cpu_process['cpu'] = cpu

# Формируем текст отчета.
report = f"Отчёт о состоянии системы:\n"
report += f"Пользователи системы: {list(user_processes.keys())}\n"
report += f"Процессов запущено: {len(lines) - 2}\n"  # Исключаем первую строку заголовков и последнюю пустую строку
report += f"Пользовательских процессов:\n"
for user, count in user_processes.items():
    report += f"{user}: {count}\n"
report += f"Всего памяти используется: {total_memory:.1f} mb\n"
report += f"Всего CPU используется: {total_cpu:.1f}%\n"
report += f"Больше всего памяти использует: ({most_memory_process['name']}, {most_memory_process['memory']:.1f} mb)\n"
report += f"Больше всего CPU использует: ({most_cpu_process['name']}, {most_cpu_process['cpu']:.1f}%)\n"

# Получаем текущую дату и время
current_datetime = datetime.now()

# Формируем название файла
file_name = f"report_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

# Записываем отчет в файл
with open(file_name, 'w') as file:
    file.write(report)

print("Отчет сохранен в файл:", file_name)
