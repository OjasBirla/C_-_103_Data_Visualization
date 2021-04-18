import pandas as pd
import plotly.express as px

df = pd.read_csv("Data.csv")
graph = px.scatter(df, x="date", y="cases", color="country")
graph.show()