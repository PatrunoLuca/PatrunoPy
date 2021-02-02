import matplotlib.pyplot as plt

data = {'8': 12.6, '10': 12.6,'12': 12.7,'14': 13,'16': 12.7,'18': 12.4,'20': 12.2, '22': 11.9, '24': 11.8,}
names = data.keys()
values = list(data.values())
plt.plot(names,values)
plt.axis([0, len(names), min(values), max(values)])
plt.title('Meteo del 9 dicembre a napoli')
plt.xlabel('Data')
plt.ylabel('Temperatura')

plt.show()
# per tutti i parametri consulta https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
