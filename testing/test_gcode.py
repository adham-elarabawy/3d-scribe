import sys
sys.path.append("../lib")
from TextToGcode import ttg
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

out = ttg("test", 30, 0, "file", 10).toGcode("ON COMMAND", "OFF COMMAND", "FAST COMMAND", "SLOW COMMAND")
print(out)

# filtered_out = np.array(list(filter(lambda i:(type(i) is tuple) or (i == "char_completed"), out)))
# character_indices = np.append(np.array([-1]), np.where(filtered_out=="char_completed"))
# characters_points = list()
# for i, _ in enumerate(character_indices[:-1]):
#     characters_points += [filtered_out[character_indices[i] + 1:character_indices[i+1]]]

# for character_points in characters_points:
#     x, y = zip(*character_points)
#     print(x, y)
#     plt.scatter(x, y)
# plt.show()