# print("")
# print("-"*50)
# print("testing `uv`")
# print("-" * 50)
# print("")


import seaborn as sns
import matplotlib.pyplot as plt
# Sample data
data = sns.load_dataset("penguins").dropna()
# Plot using seaborn only
sns.scatterplot(
data=data, x="flipper_length_mm", y="body_mass_g"
)
plt.title("Flipper Length vs Body Mass by Species")
plt.show()