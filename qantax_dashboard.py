import matplotlib.pyplot as plt

# Create a figure
fig = plt.figure(figsize=(12, 10))
fig.suptitle('Dashboard for Impacted Customer Record Data\n', fontsize=16)

# First row: two subplots
# Data for Pie Chart 1
sizes_pie1 = [4_000_000, 1_700_000]
labels_pie1 = [f'({sizes_pie1[0]/1_000_000}M) Name, Email,\nFrequent Flyer Details', f'({sizes_pie1[1]/1_000_000}M) Other Records']
ax1 = plt.subplot(2, 2, 1)  # row 1, col 1
ax1.set_title("Breakdown of 5.7M Total Impacted Customer Records")
ax1.pie(sizes_pie1, labels=labels_pie1, autopct='%1.1f%%', startangle=0)

# Data for Pie Chart 2
sizes_pie2 = [1_200_000, 2_800_000]
labels_pie2 = [f'({sizes_pie2[0]/1_000_000}M) Name & Email', f'({sizes_pie2[1]/1_000_000}M) Name, Email,\nFrequent Flyer Details*']
ax2 = plt.subplot(2, 2, 2)  # row 1, col 2
ax2.set_title("Breakdown of 4M Customer Records\ninvolving Name, Email,Frequent Flyer Details")
ax2.pie(sizes_pie2, labels=labels_pie2, autopct='%1.1f%%', startangle=0)

# Second row: one subplot spanning both columns
bar_values = [1_300_000, 1_100_000, 900_000, 400_000, 10_000]
bar_labels = [f'Address ({bar_values[0]/1_000}K)', f'Date of Birth ({bar_values[1]/1_000}K)', f'Phone Number ({bar_values[2]/1_000}K)', f'Gender ({bar_values[3]/1_000}K)', f'Meal Preferences ({bar_values[4]/1_000}K)']
ax3 = plt.subplot(2, 1, 2)  # row 2, spans both cols
ax3.set_title("Data Types in 1.7M Other Records")
ax3.bar(bar_labels, bar_values, color='skyblue')
ax3.set_ylabel('Number of Records')

plt.tight_layout()
plt.show()
