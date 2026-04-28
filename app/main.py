import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="African Climate Dashboard",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------------
# Load Data
# -----------------------------------
@st.cache_data
def load_data():
    files = {
        "Ethiopia": "data/ethiopia_clean.csv",
        "Kenya": "data/kenya_clean.csv",
        "Sudan": "data/sudan_clean.csv",
        "Tanzania": "data/tanzania_clean.csv",
        "Nigeria": "data/nigeria_clean.csv"
    }

    dfs = []

    for country, path in files.items():
        df = pd.read_csv(path)
        df["Country"] = country
        df["DATE"] = pd.to_datetime(df["YEAR"] * 1000 + df["DOY"], format="%Y%j")
        df["Year"] = df["DATE"].dt.year
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)

df = load_data()

# -----------------------------------
# Sidebar
# -----------------------------------
st.sidebar.title("Filters")

countries = st.sidebar.multiselect(
    "Select Countries",
    df["Country"].unique(),
    default=df["Country"].unique()
)

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (int(df["Year"].min()), int(df["Year"].max()))
)

variable = st.sidebar.selectbox(
    "Select Variable",
    ["T2M", "PRECTOTCORR", "RH2M", "WS2M"]
)

filtered = df[
    (df["Country"].isin(countries)) &
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1])
]

# -----------------------------------
# Header
# -----------------------------------
st.title("🌍 African Climate Trend Dashboard")
st.caption("Climate comparison for Ethiopia, Kenya, Sudan, Tanzania, and Nigeria")

# -----------------------------------
# KPI Cards
# -----------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Countries", len(countries))
col2.metric("Records", f"{len(filtered):,}")
col3.metric("Avg Temp °C", round(filtered["T2M"].mean(), 2))
col4.metric("Avg Rainfall", round(filtered["PRECTOTCORR"].mean(), 2))

# -----------------------------------
# Trend Chart
# -----------------------------------
st.subheader("📈 Climate Trend")

trend = filtered.groupby(["Year", "Country"])[variable].mean().reset_index()

fig = px.line(
    trend,
    x="Year",
    y=variable,
    color="Country",
    markers=True,
    line_shape="linear"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------
# Boxplot
# -----------------------------------
st.subheader("📦 Distribution Comparison")

fig2 = px.box(
    filtered,
    x="Country",
    y=variable,
    color="Country"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------------
# Heatmap Correlation
# -----------------------------------
st.subheader("🔥 Variable Correlation")

corr = filtered[["T2M","PRECTOTCORR","RH2M","WS2M"]].corr()

fig3 = px.imshow(
    corr,
    text_auto=True,
    aspect="auto"
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------------
# Data Preview
# -----------------------------------
st.subheader("📄 Dataset Preview")
st.dataframe(filtered.head(100), use_container_width=True)