import matplotlib.pyplot as plt

data = {'1E': 31, '2E': 30, '3E': 25, '4E': 20}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Numero di alunni presenti nelle classi')


plt.show()