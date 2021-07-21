import sys
sys.path.append("../lib")
from TextToGcode import ttg
import matplotlib.pyplot as plt
import numpy as np
from scribelib import Path

plt.style.use('ggplot')

out = ttg("test", 30, 0, "visualize", 10).toGcode("ON COMMAND", "OFF COMMAND", "FAST COMMAND", "SLOW COMMAND")

path = Path(out)