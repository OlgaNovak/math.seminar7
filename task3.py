# Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.

import numpy as np
from scipy import stats

x=np.array([150, 160, 165, 145, 155])
y=np.array([140, 155, 150, 130, 135])


print(stats.wilcoxon(x,y))                         # используем критерий Уилкоксона (сравнение двух зависимых выборок)
# WilcoxonResult(statistic=0.0, pvalue=0.0625)
# pvalue>alfa -> H0, т.е. статистические различия не обнаружены на уровне значимости alfa=0.05