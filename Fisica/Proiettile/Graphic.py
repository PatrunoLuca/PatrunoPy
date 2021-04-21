from matplotlib import pyplot as plt
from pandas import DataFrame, read_csv

with open("0.csv", "r") as csvfile:
    Angle0 = read_csv(csvfile)
with open("32.csv", "r") as csvfile:
    Angle32 = read_csv(csvfile)

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(Angle0["Time (s)"].tolist(), Angle0["Linear Acceleration x (m/s^2)"].tolist())
ax1.plot(Angle0["Time (s)"].tolist(), Angle0["Linear Acceleration y (m/s^2)"].tolist())
ax1.plot(Angle0["Time (s)"].tolist(), Angle0["Linear Acceleration z (m/s^2)"].tolist())
ax1.legend(["X", "Y", "Z"])
ax1.set_xlabel('Time (s)')
ax1.set_ylabel("Linear Acceleration (m/s^2)")
ax1.set_title("0 degree")

ax2.plot(Angle32["Time (s)"].tolist(), Angle32["Linear Acceleration x (m/s^2)"].tolist())
ax2.plot(Angle32["Time (s)"].tolist(), Angle32["Linear Acceleration y (m/s^2)"].tolist())
ax2.plot(Angle32["Time (s)"].tolist(), Angle32["Linear Acceleration z (m/s^2)"].tolist())
ax2.legend(["X", "Y", "Z"])
ax2.set_xlabel('Time (s)')
ax2.set_ylabel("Linear Acceleration (m/s^2)")
ax2.set_title("32 degree")

plt.tight_layout()
plt.get_current_fig_manager().window.state('zoomed')
plt.show()