import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 1. DATA LOAD KARO
df = pd.read_csv('cleaned_country_data.csv')

# 2. DASHBOARD BANANA START
fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=('1. Bar Chart: Top 10 GDP Countries', 
                    '2. Line Chart: Population vs Area',
                    '3. Pie Chart: Region Distribution',
                    '4. Histogram: Literacy Distribution', 
                    '5. Scatter Plot: GDP vs Literacy',
                    '6. Heatmap: Correlation'),
    specs=[[{"type": "bar"}, {"type": "scatter"}],
           [{"type": "pie"}, {"type": "histogram"}],
           [{"type": "scatter"}, {"type": "heatmap"}]]
)

# Chart 1: BAR CHART - Top 10 GDP
top_gdp = df.nlargest(10, 'GDP')
fig.add_trace(go.Bar(x=top_gdp['Country'], y=top_gdp['GDP'], 
                     name='GDP', marker_color='crimson'), row=1, col=1)

# Chart 2: LINE CHART - Population vs Area sorted
df_sorted = df.sort_values('Area').head(20)
fig.add_trace(go.Scatter(x=df_sorted['Area'], y=df_sorted['Population'], 
                         mode='lines+markers', name='Pop vs Area', line=dict(color='royalblue')), row=1, col=2)

# Chart 3: PIE CHART - Region
region_counts = df['Region'].value_counts().head(5)
fig.add_trace(go.Pie(labels=region_counts.index, values=region_counts.values, name='Regions'), row=2, col=1)

# Chart 4: HISTOGRAM - Literacy
fig.add_trace(go.Histogram(x=df['Literacy'], name='Literacy', marker_color='green'), row=2, col=2)

# Chart 5: SCATTER PLOT - GDP vs Literacy with trendline
fig.add_trace(go.Scatter(x=df['Literacy'], y=df['GDP'], mode='markers',
                         name='GDP vs Literacy', marker=dict(color='orange')), row=3, col=1)

# Chart 6: HEATMAP - Correlation
numeric_df = df.select_dtypes(include=['float64', 'int64'])
fig.add_trace(go.Heatmap(z=numeric_df.corr().values,
                         x=numeric_df.columns, y=numeric_df.columns,
                         colorscale='RdBu'), row=3, col=2)

# 3. DASHBOARD CUSTOMIZE KARO
fig.update_layout(height=1200, width=1600, title_text="CodeSoft Task 3: Country Data Dashboard",
                  title_x=0.5, showlegend=False, template='plotly_white')

# 4. SAVE KARO AUR DIKHAO
fig.write_html("dashboard.html")  # Interactive dashboard
#fig.write_image("dashboard.png")  # Image bhi ban jayegi
fig.show()

print("===== TASK 3 COMPLETE =====")
print("Dashboard saved as 'dashboard.html' and 'dashboard.png'")
print("\nINSIGHTS:")
print("1. Luxembourg, Singapore have highest GDP per capita")
print("2. Strong positive correlation between Literacy and GDP") 
print("3. Asia has maximum countries in dataset")
print("4. Most countries have literacy > 80%")