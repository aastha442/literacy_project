# 📊 Literacy Project

An interactive **Streamlit** dashboard for analyzing **digital literacy** across Indian districts.  
Users can **select an area** to view insights like **total vs. literate population, male vs. female literacy rates**, and compare literacy rates **state-wise vs. national** benchmarks.

---

## 🚀 Features

- 📌 **Area Selection**: Choose a district/state to analyze.
- 📊 **Visualizations**:
  - **Total Population vs. Literate Population**
  - **Male vs. Female Literacy Rate**
  - **State Literacy Rate vs. India (Gauge Chart)**
  - **Compare Two Areas for Literacy Metrics**
- 📁 **Data Source**: Processed using **SQL** for cleaning & transformation.

---

## 📂 Data Sources

- **Raw Data**:https://censusindia.gov.in/census.website/data/census-tables
- **Cleaned Data (Used in this project)**: Available in `/data/final_data.csv`

> *The raw dataset was cleaned using SQL queries (see `database/sql_queries.sql`). The cleaned data is used for visualization in Streamlit.*

---

## 🖥️ How to Run the Project

### 🔹 1️⃣ Clone the Repository
```bash
git clone https://github.com/aastha442/literacy_project.git
cd literacy_project
```
-INSTALL THE DEPENDENCIES 
-RUN THE STREAMLIT DASHBOARD
## 📸 Dashboard Preview

 

<p align="center">
  <img src="Screenshot1.png" width="45%">
  <img src="Screenshot2.png" width="45%">
  <img src="Screenshot3.png" width="45%">
</p>



---
## 🛠️ Technologies Used

| Technology  | Purpose |
|-------------|---------|
| **Python** 🐍 | Core programming language for data processing and visualization |
| **Pandas** 📊 | Data manipulation and analysis |
| **Streamlit** 🎨 | Interactive dashboard for visualization |
| **SQL (MySQL)** 🛢️ | Data cleaning and transformation |
| **Matplotlib & Seaborn** 📈 | Data visualization and plotting |



