import numpy as np
import matplotlib.pyplot as plt

# Промислове виробництво: додана вартість, в цінах нац. валют на 2000 р., млрд. долл.
# 	                1900	1913	1929	1938	1950	1960	1970	1980	1990	2000
# Германія	        29	51	59	478	93	244	420	510	575	625
# Франція	        28	46	57	52	63	93	190	275	310	355
# Великобританія	53	73	84	105	130	180	245	265	300	335
# СРСР	            40	70	80	105	205	480	725	935	1000 545


# n_groups = 5
# means_men = (20, 35, 30, 35, 27)
# std_men = (2, 3, 4, 1, 2)
# means_women = (25, 32, 34, 20, 25)
# std_women = (3, 5, 2, 3, 3)

n_groups = 10
de = (29, 51, 59, 478, 93, 244, 420, 510, 575, 625)
fr = (28, 46, 57, 52, 63, 93, 190, 275, 310, 355)
uk = (53, 73, 84, 105, 130, 180, 245, 265, 300, 335)
ua = (40, 70, 80, 105, 205, 480, 725, 935, 1000, 545)


fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 1

#Задаємо зміщення кожного бара що б не накладались один на один
br1 = np.arange(len(de))
br2 = [x + bar_width for x in br1]
br3 = [x + bar_width for x in br2]
br4 = [x + bar_width for x in br3]


colors = ['red', 'gray', '#00008b', '#CCCC00']
rects1 = ax.bar(br1, de, bar_width,
                alpha=opacity, color=colors[0],
                label='Німеччина')

rects2 = ax.bar(br2, fr, bar_width,
                alpha=opacity, color=colors[1],
                label='Франція')

rects3 = ax.bar(br3, uk, bar_width,
                alpha=opacity, color=colors[2],
                label='Великобританія')

rects4 = ax.bar(br4, ua, bar_width,
                alpha=opacity, color=colors[3],
                label='Україна')


ax.grid(True, linestyle ='-.')
ax.set_xlabel('Роки')
ax.set_ylabel('Млрд. долл.')
ax.set_title('Промислове виробництво: додана вартість, в цінах нац. валют')
ax.set_xticks(index + 1.5*bar_width)
ax.set_xticklabels(('1900', '1913', '1929', '1938', '1950', '1960', '1970', '1980', '1990', '2000'))
ax.legend(loc='upper left')
fig.tight_layout()
plt.show()
