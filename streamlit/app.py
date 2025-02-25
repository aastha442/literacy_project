import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

# Load data (Replace with your actual file or database)
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\pc\Desktop\Literacy_project\data\final data.csv")  # Change this to your actual data source
    return df

df = load_data()

# Dropdown for selecting an area
selected_area = st.selectbox("Select an Area", df["Area Name"].unique())

# Display the selected area
st.write(f"## Data for: **{selected_area}**")

# Filter data for the selected area
area_data = df[df["Area Name"] == selected_area]
india_data = df[df["Area Name"] == "INDIA"]

# Check if data exists for the selected area
if not area_data.empty:
    # Extract values for the graph
    total_population = area_data["Total Population"].values[0]
    total_literates = area_data["Total literates"].values[0]
    attending_education = area_data["Total population attending educational institution"].values[0]
    
    # New Literate Population calculation
    literate_population = total_literates + attending_education
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Plot Total Population vs. Literate Population
        fig, ax = plt.subplots(figsize=(5, 5))
        bars = ax.bar(["Total Population", "Literate Population"], 
                      [total_population, literate_population], 
                      color=["blue", "green"])
        
        # Add text labels inside bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height - height*0.1, f'{int(height)}', 
                    ha='center', va='center', fontsize=10, color='white', fontweight='bold')
        
        ax.set_ylabel("Population Count")
        ax.set_title("Total Population vs. Literate Population")
        st.pyplot(fig)
    
    with col2:
        # Extract Male & Female Literacy Data
        male_literates = area_data["Male literates"].values[0]
        male_attending_education = area_data["Male population attending educational institution"].values[0]
        female_literates = area_data["Female literates"].values[0]
        female_attending_education = area_data["Female population attending educational institution"].values[0]

        male_literate_population = male_literates + male_attending_education
        female_literate_population = female_literates + female_attending_education

        # Plot Male vs Female Literate Population
        fig2, ax2 = plt.subplots(figsize=(5, 5))
        bars2 = ax2.bar(["Male Literates", "Female Literates"], 
                         [male_literate_population, female_literate_population], 
                         color=["#1f77b4", "#ff7f0e"])
        
        # Add text labels inside bars
        for bar in bars2:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2, height - height*0.1, f'{int(height)}', 
                     ha='center', va='center', fontsize=10, color='white', fontweight='bold')
        
        ax2.set_ylabel("Population Count")
        ax2.set_title("Male vs. Female Literate Population")
        st.pyplot(fig2)
    
    # Gauge Chart for Literacy Rate Comparison
    literacy_rate = (literate_population / total_population) * 100
    india_literacy_rate = (india_data["Total literates"].values[0] + india_data["Total population attending educational institution"].values[0]) / india_data["Total Population"].values[0] * 100
    
    gauge_fig = go.Figure()
    gauge_fig.add_trace(go.Indicator(
        mode="gauge+number+delta",
        value=literacy_rate,
        title={"text": "Literacy Rate vs India"},
        delta={"reference": india_literacy_rate, "increasing": {"color": "green"}, "decreasing": {"color": "red"}},
        gauge={"axis": {"range": [0, 100]}, "bar": {"color": "blue"}}
    ))
    if st.button("Show Literacy Rate Gauge"):
        st.plotly_chart(gauge_fig)
    
    # Comparison for Two Areas
    area_1 = st.selectbox("Select First Area", df["Area Name"].unique(), key="area1")
    area_2 = st.selectbox("Select Second Area", df["Area Name"].unique(), key="area2")
    area1_data, area2_data = df[df["Area Name"] == area_1], df[df["Area Name"] == area_2]
    
    if not area1_data.empty and not area2_data.empty:
        literacy_rate_1 = (area1_data["Total literates"].values[0] + area1_data["Total population attending educational institution"].values[0]) / area1_data["Total Population"].values[0] * 100
        literacy_rate_2 = (area2_data["Total literates"].values[0] + area2_data["Total population attending educational institution"].values[0]) / area2_data["Total Population"].values[0] * 100
        
        comparison_fig = px.bar(x=[area_1, area_2], y=[literacy_rate_1, literacy_rate_2], 
                                title="Comparison of Literacy Rates", labels={"x": "Area", "y": "Literacy Rate (%)"}, 
                                text_auto=True, color_discrete_sequence=["#636EFA", "#EF553B"])
        st.plotly_chart(comparison_fig)
    
  
   

