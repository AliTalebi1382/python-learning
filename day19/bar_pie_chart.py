import matplotlib.pyplot as plt
from persian_fix import fix_persian

# نمودار میله‌ای
subjects = [fix_persian("ریاضی"), fix_persian("فیزیک"), fix_persian("شیمی"), fix_persian("ادبیات")]
scores = [18, 15, 17, 19]

plt.figure()
plt.bar(subjects, scores, color=['red', 'blue', 'green', 'orange'])
plt.title(fix_persian("نمرات دروس"))
plt.xlabel(fix_persian("درس"))
plt.ylabel(fix_persian("نمره"))
plt.savefig("bar_chart.png")
plt.show()

# نمودار دایره‌ای
cities = [fix_persian("تهران"), fix_persian("اصفهان"), fix_persian("شیراز"), fix_persian("مشهد")]
population_percent = [40, 25, 20, 15]

plt.figure()
plt.pie(population_percent, labels=cities, autopct='%1.1f%%')
plt.title(fix_persian("درصد دانش‌آموزان بر اساس شهر"))
plt.savefig("pie_chart.png")
plt.show()