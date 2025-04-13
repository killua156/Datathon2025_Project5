# crime_dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("Districtwise_Crime_of_India_2001_to_2014 - Sheet1.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

st.title("Crime Dashboard: India IPC 2013")

# Sidebar filters
year = st.selectbox("Select Year", sorted(df['year'].unique()))
state = st.selectbox("Select State", sorted(df['state/ut'].unique()))
districts = df[df['state/ut'] == state]['district'].unique()
district = st.selectbox("Select District", sorted(districts))

# Filtered data
filtered = df[(df['year'] == year) & 
              (df['state/ut'] == state) & 
              (df['district'] == district)]

# KPIs
st.metric("Total IPC Crimes", int(filtered['total_ipc_crimes'].sum()))
st.metric("Murders", int(filtered['murder'].sum()))
st.metric("Rape", int(filtered['rape'].sum()))
st.metric("Theft", int(filtered['theft'].sum()))

# Plot
fig = px.bar(filtered.melt(id_vars=['year'], 
                           value_vars=['murder', 'rape', 'theft', 'kidnapping_&_abduction']),
             x='variable', y='value', color='variable',
             title="Selected District Crime Breakdown")
st.plotly_chart(fig)
