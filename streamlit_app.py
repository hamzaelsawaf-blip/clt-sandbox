import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="CLT Sandbox", layout="wide")

st.title("Central Limit Theorem Sandbox")
st.write("""
This app shows how the distribution of sample means becomes approximately normal 
as the sample size increases, even when the original population is not normal.
""")

# Sidebar controls
st.sidebar.header("Simulation Settings")

distribution = st.sidebar.selectbox(
    "Choose population distribution:",
    ["Uniform", "Exponential", "Normal"]
)

sample_size = st.sidebar.slider(
    "Sample size (n):",
    min_value=2,
    max_value=100,
    value=10
)

num_samples = st.sidebar.slider(
    "Number of samples:",
    min_value=100,
    max_value=10000,
    value=1000,
    step=100
)

# Generate population
population_size = 100000

if distribution == "Uniform":
    population = np.random.uniform(0, 100, population_size)

elif distribution == "Exponential":
    population = np.random.exponential(scale=10, size=population_size)

else:
    population = np.random.normal(loc=50, scale=10, size=population_size)

# Generate sample means
sample_means = []

for i in range(num_samples):
    sample = np.random.choice(population, size=sample_size)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Original Population Distribution")
    fig1, ax1 = plt.subplots()
    ax1.hist(population, bins=50, edgecolor="black")
    ax1.set_xlabel("Value")
    ax1.set_ylabel("Frequency")
    st.pyplot(fig1)

with col2:
    st.subheader("Distribution of Sample Means")
    fig2, ax2 = plt.subplots()
    ax2.hist(sample_means, bins=50, edgecolor="black")
    ax2.set_xlabel("Sample Mean")
    ax2.set_ylabel("Frequency")
    st.pyplot(fig2)

# Statistics
st.subheader("Simulation Results")

col3, col4, col5 = st.columns(3)

with col3:
    st.metric("Mean of Population", round(np.mean(population), 2))

with col4:
    st.metric("Mean of Sample Means", round(np.mean(sample_means), 2))

with col5:
    st.metric("Standard Deviation of Sample Means", round(np.std(sample_means), 2))

st.write("""
### Explanation
As the sample size increases, the sample means become more normally distributed.
This supports the Central Limit Theorem, which is an important concept in Quality Engineering.
""")
