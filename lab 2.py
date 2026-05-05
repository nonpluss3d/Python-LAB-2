import wave
import struct
import math
import matplotlib.pyplot as plt

# ввод файла
filename = input("Введите имя wav файла: ")

# проверка только на .wav
if not filename.lower().endswith(".wav"):
    print("Файл должен быть .wav")
    exit()

try:
    wav = wave.open(filename, 'r')
except:
    print("Ошибка открытия файла")
    exit()

# параметры файла
sample_rate = wav.getframerate()
n_frames = wav.getnframes()

# ввод количества отсчетов
try:
    n = int(input("Введите количество отсчетов: "))
except:
    print("Ошибка ввода")
    exit()

n = min(n, n_frames)

# чтение данных
frames = wav.readframes(n)
wav.close()

# преобразование в числа
data = []
for i in range(0, len(frames), 2):
    value = struct.unpack('<h', frames[i:i+2])[0]
    data.append(value)

# обрезаем до нужного количества
data_cut = data[:n]


# 1.1 Точечный график
plt.figure()
plt.scatter(range(n), data_cut)
plt.title("Отсчеты сигнала")
plt.xlabel("Номер отсчета")
plt.ylabel("Амплитуда")
plt.grid()


# 1.2 Осциллограмма
time_axis = []
for i in range(n):
    time_axis.append(i / sample_rate)

plt.figure()
plt.plot(time_axis, data_cut)
plt.title("Осциллограмма")
plt.xlabel("Время (сек)")
plt.ylabel("Амплитуда")
plt.grid()


# 1.3 Реальная часть ДПФ
real_part = []
freq = []

for k in range(n):
    re = 0
    for t in range(n):
        angle = 2 * math.pi * k * t / n
        re += data[t] * math.cos(angle)
    real_part.append(re)
    freq.append(k * sample_rate / n)

plt.figure()
plt.scatter(freq, real_part)
plt.title("Реальная часть ДПФ")
plt.xlabel("Частота (Гц)")
plt.ylabel("Re")
plt.grid()


# 1.4 Гистограмма
plt.figure()
plt.hist(data, bins=30)
plt.title("Гистограмма")
plt.xlabel("Амплитуда")
plt.ylabel("Количество")
plt.grid()

plt.show()
