import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Načtení dat
path = "datasets/crack_meter/CalibData-30kHz-0-12--.csv"
dataset = pd.read_csv(path, sep=";")

# Sloupce
x_axis = "Current"
y_axis = "VoltageDrop"
hue = "CrackSize"

# Výchozí limity
vmin = dataset[y_axis].min()
vmax = dataset[y_axis].max()

# Figure a prostor pro slidery
fig, ax = plt.subplots(figsize=(9, 6))
plt.subplots_adjust(bottom=0.25)

# Počáteční filtrovaná data
filtered_data = dataset[dataset[y_axis].between(vmin, vmax)]

# První vykreslení
scatter = sns.scatterplot(
    data=filtered_data,
    x=x_axis,
    y=y_axis,
    hue=hue,
    palette="Spectral",
    ax=ax
)
ax.set_title("Interaktivní filtr podle VoltageDrop")

# Osy pro slidery
ax_min = plt.axes([0.15, 0.10, 0.65, 0.03])
ax_max = plt.axes([0.15, 0.05, 0.65, 0.03])

slider_min = Slider(ax_min, "Min VoltageDrop", vmin, vmax, valinit=vmin)
slider_max = Slider(ax_max, "Max VoltageDrop", vmin, vmax, valinit=vmax)

def update(val):
    min_val = slider_min.val
    max_val = slider_max.val

    # Oprava, kdyby min bylo větší než max
    if min_val > max_val:
        return

    ax.clear()

    filtered = dataset[dataset[y_axis].between(min_val, max_val)]

    sns.scatterplot(
        data=filtered,
        x=x_axis,
        y=y_axis,
        hue=hue,
        palette="Spectral",
        ax=ax
    )

    ax.set_title(f"VoltageDrop mezi {min_val:.0f} a {max_val:.0f}")
    fig.canvas.draw_idle()

slider_min.on_changed(update)
slider_max.on_changed(update)

plt.show()