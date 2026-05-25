import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import time

start_time = time.time()

#чтение файла
filename = "12.wav"
sample_rate, data = wavfile.read(filename)

print(f"Частота дискретизации:", sample_rate, " Гц")

#количество отсчётов
while True:
    try:
        n = int(input(f"Введите количество отсчетов: "))
        if 1 <= n <= len(data):
            break
        else:
            print(f"Число должно быть от 1 до ", len(data))
    except ValueError:
        print("Ошибка ввода")

data_cut = data[:n]

#точечный график
plt.figure(figsize=(10, 4))
plt.plot(range(n), data_cut, 'o', markersize=2)
plt.title("Точечный график")
plt.xlabel("Номер отсчета")
plt.ylabel("Амплитуда")
plt.grid(True)


#осциллограмма
time_axis = np.arange(len(data)) / sample_rate

plt.figure(figsize=(10, 4))
plt.plot(time_axis, data)
plt.title("Осциллограмма")
plt.xlabel("Секунды")
plt.ylabel("Амплитуда")
plt.grid(True)


#дпф
fft_result = np.fft.fft(data)          # комплексное ДПФ
real_part = np.real(fft_result)        # Re(ДПФ)
freq_axis = np.fft.fftfreq(len(data), d=1/sample_rate)

#положительные частоты
half_n = len(data) // 2
freq_axis = freq_axis[:half_n]
real_part = real_part[:half_n]

plt.figure(figsize=(10, 4))
plt.plot(freq_axis, real_part)
plt.title("ДПФ")
plt.xlabel("Частота")
plt.ylabel("Re")
plt.grid(True)

#Гистограмма
plt.figure(figsize=(10, 4))
plt.hist(data, bins=50, edgecolor='black')
plt.title("Гистограмма")
plt.xlabel("Амплитуда")
plt.ylabel("Отсчёт")
plt.grid(True, axis='y')

plt.show()

print(f"Время выполнения: {time.time() - start_time:.4f} секунд")
