import matplotlib.pyplot as plt
from persian_fix import fix_persian

days = [1, 2, 3, 4, 5, 6, 7]
temperature = [20, 22, 19, 25, 27, 24, 21]

plt.plot(days, temperature, marker='o', color='blue')
plt.title(fix_persian("دمای هوا در یک هفته"))
plt.xlabel(fix_persian("روز"))
plt.ylabel(fix_persian("دما (درجه)"))
plt.grid(True)
plt.savefig("line_chart.png")
plt.show()