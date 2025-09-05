import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Downloaded csv
df = pd.read_csv("data/livedata-weekly-job-changes-2025-07-23.csv")

# Convert date columns to datetime
df['previous_job.started_at'] = pd.to_datetime(df['previous_job.started_at'], errors = 'coerce')
df['previous_job.ended_at'] = pd.to_datetime(df['previous_job.ended_at'], errors = 'coerce')

# Create a 'month' column for arrivals vs departures
# Lambda function; Return first/end date based on arrival/departure classification
# axis = 1 - Count by rows instead of columnsf 
df['month'] = df.apply(
    lambda row: row['previous_job.started_at']
    if row['arrival/departure'] == 'arrival' else row['previous_job.ended_at'],
    axis = 1
).dt.tz_localize(None).dt.to_period('M').dt.start_time # No timezone; start of each month

# Filter to a copy with only 2025
df_2025 = df[df['month'].dt.year == 2025].copy() # Create copy

# Sum monthly counts
monthly_counts = (df_2025.groupby(['month', 'arrival/departure'])
                  .size()
                  .reset_index(name='count')
)

# Pivot into month as index
pivot_monthly = monthly_counts.pivot(index = 'month', columns='arrival/departure', values='count').fillna(0)
pivot_monthly.index = pivot_monthly.index.strftime("%b")

# Plot monthly bars
pivot_monthly.plot(kind="bar", stacked=False, color=["gold","blue"])

# Aesthetics
plt.title("Monthly Job Arrivals vs. Departures (2025)")
plt.ylabel("Number of Changes")
plt.xlabel("Month")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()
#plt.clf()

# New chart for 10 companies with most departures
departures = df[df['arrival/departure'] == 'departure']
top_departure_companies = departures['previous_job.company.name'].value_counts().nlargest(10)

sns.barplot(
    x=top_departure_companies.values,
    y=top_departure_companies.index,
    hue=top_departure_companies.index,
    dodge=False,
    legend=False,
    palette='coolwarm'
)
plt.title("Top Companies by Number of Departures")
plt.xlabel("Number of Departures")
plt.ylabel("Company")
plt.grid(axis = 'x', linestyle = '--', alpha = 0.5)

plt.show()
#plt.clf()

# Rank top 10 job functions connected to departures
departures_by_function = (
    departures['previous_job.function']
    .value_counts()
    .nlargest(10)
    .reset_index()
)

# Rename columns
departures_by_function.columns = ['previous_job.function', 'count']

# Barplot
sns.barplot(
    data=departures_by_function,
    x='count',
    y='previous_job.function',
    hue='previous_job.function',
    palette='Reds_r',
    legend=False
)

plt.show()