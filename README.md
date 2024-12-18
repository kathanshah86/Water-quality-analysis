# Water-quality-analysis
#Group Memebers
* Prisha [KU2407U358]
* Kathan [KU2407U311]
* Yesha  [KU2407U391]
* Akshit [KU2407U252]
* Dev    [Ku2407U297]
#Objective of the Project
The objective of this project is to analyze water quality using key parameters like pH, Turbidity, and Dissolved Oxygen (DO). The project aims to classify water quality into categories such as "Good," "Moderate," or "Polluted" using rule-based logic and visualize the distributions and relationships between features.

#Tools and Libraries Used

The project is implemented in Python with the following libraries:

Pandas: For data manipulation and analysis.
NumPy: For numerical computations.
Matplotlib: For data visualization (histograms, scatter plots, and bar charts).

#Data Source(s)

The dataset used in this project is stored as a CSV file: water_quality_data.csv.
Ensure this file is present in the same folder as the code.

#Summary of Results

Key Steps Performed:
Data Loading and Preprocessing:
Loaded the dataset using Pandas.
Checked for and displayed missing values.
Generated descriptive statistics to summarize features.
Visualizations:
Histograms: Displayed the distribution of each feature (e.g., pH, DO).
Boxplots: Identified potential outliers across features.
Scatterplot: Analyzed the relationship between pH and DO.
Water Quality Classification:
A rule-based function classified water quality based on:
pH: Between 6.5 and 8.5 (Good range).
Turbidity: Below or equal to 5 NTU.
DO: Above or equal to 6 mg/L.
Categories include:

Good: Satisfies all thresholds.
Moderate: Falls between "Good" and "Polluted."
Polluted: High turbidity (>8 NTU) or very low DO (<4 mg/L).
Results:
Displayed the count of water samples in each quality category.
Visualized the distribution of water quality using a bar chart.

#Sample Outputs

Updated Dataset with Classification:
pH	Turbidity (NTU)	DO (mg/L)	Quality
7.2	3.5	6.5	Good
5.5	9.0	3.0	Polluted
Water Quality Distribution:
A bar chart displaying the counts of Good, Moderate, and Polluted samples.

#Challenges Faced

Ensuring proper thresholds for classification based on water quality standards.
Visualizing relationships between multiple features effectively.
Handling missing or inconsistent data values.

#Future Improvements

Use machine learning techniques to classify water quality more accurately.
Integrate real-time water quality monitoring data.
Create an interactive dashboard for better analysis and visualization.
