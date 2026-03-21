import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = "datasets/crack_meter/CalibData-30kHz-0-12--.csv"
dataset = pd.read_csv(path, sep=";")

dataset.rename(
    columns={
        "VoltageDrop": "Voltage drop",
        "CrackSize": "Crack size",
    },
    inplace=True,
)

plt.figure(figsize= (12, 6))
plt.title("Voltage Drop vs Crack Size")

sns.lineplot(
    data=dataset, 
    x="Crack size", 
    y="Voltage drop"
)

plt.show()