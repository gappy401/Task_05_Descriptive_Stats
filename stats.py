import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from CSV or manually define it
# For simplicity, here's a sample structure using key players
data = {
    'Player': [
        'Ward, Emma', 'Trinkaus, Caroline', 'Muchnick, Emma', 'Britton, Gracie',
        'Vogelman, Alexa', 'Cotter, Mileena', 'Caramelli, Joely', 'Guzik, Molly',
        'Adamson, Olivia', 'Volpe, Ashlee', 'DeVito, Sam', 'Vandiver, Coco'
    ],
    'GP': [19, 19, 19, 19, 19, 19, 19, 19, 3, 8, 19, 19],
    'G': [30, 32, 34, 20, 21, 21, 16, 14, 10, 14, 8, 0],
    'A': [46, 11, 7, 10, 6, 2, 4, 5, 6, 2, 2, 0],
    'PTS': [76, 43, 41, 30, 27, 23, 20, 19, 16, 16, 10, 0],
    'SH': [77, 72, 71, 41, 46, 50, 46, 34, 18, 31, 12, 0],
    'SH_pct': [0.39, 0.444, 0.479, 0.488, 0.457, 0.42, 0.348, 0.412, 0.556, 0.452, 0.667, 0],
    'GB': [6, 6, 27, 8, 25, 11, 23, 15, 2, 5, 22, 34],
    'TO': [41, 16, 31, 16, 27, 26, 8, 14, 7, 10, 11, 3],
    'DC': [0, 8, 13, 1, 31, 24, 39, 13, 5, 0, 11, 51]
}

df = pd.DataFrame(data)

# Calculate derived metrics
df['PPG'] = df['PTS'] / df['GP']
df['Efficiency'] = df['PTS'] / df['SH']

# Set plot style
sns.set(style="whitegrid")

# 1. Goals vs Assists
plt.figure(figsize=(12, 6))
sns.barplot(x='Player', y='G', data=df, color='skyblue', label='Goals')
sns.barplot(x='Player', y='A', data=df, color='orange', label='Assists')
plt.title('Goals vs Assists per Player')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# 2. Shot Percentage
plt.figure(figsize=(12, 6))
sns.barplot(x='Player', y='SH_pct', data=df, palette='viridis')
plt.title('Shot Percentage per Player')
plt.xticks(rotation=45)
plt.ylabel('Shot %')
plt.tight_layout()
plt.show()

# 3. Points per Game
plt.figure(figsize=(12, 6))
sns.barplot(x='Player', y='PPG', data=df, palette='magma')
plt.title('Points per Game')
plt.xticks(rotation=45)
plt.ylabel('PPG')
plt.tight_layout()
plt.show()

# 4. Ground Balls vs Turnovers
plt.figure(figsize=(12, 6))
sns.barplot(x='Player', y='GB', data=df, color='green', label='Ground Balls')
sns.barplot(x='Player', y='TO', data=df, color='red', label='Turnovers')
plt.title('Ground Balls vs Turnovers')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# 5. Draw Controls
plt.figure(figsize=(12, 6))
sns.barplot(x='Player', y='DC', data=df, palette='coolwarm')
plt.title('Draw Controls per Player')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Shooting Efficiency (Points per Shot)
plt.figure(figsize=(12, 6))
sns.barplot(x='Player', y='Efficiency', data=df, palette='cividis')
plt.title('Shooting Efficiency (Points per Shot)')
plt.xticks(rotation=45)
plt.ylabel('Efficiency')
plt.tight_layout()
plt.show()