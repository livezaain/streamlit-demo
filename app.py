"""Nobel Prize Data Dashboard - Streamlit App"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Page configuration
st.set_page_config(
    page_title="Nobel Prize Data Dashboard",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)


@st.cache_data
def load_data(filepath):
    """Load Nobel Prize data from CSV."""
    df = pd.read_csv(filepath)
    # Convert award_year to int
    df["award_year"] = df["award_year"].astype(int)
    return df


def filter_data(df, year_range, categories, gender, country):
    """Filter dataframe based on user selections."""
    filtered = df.copy()

    # Filter by year range
    filtered = filtered[
        (filtered["award_year"] >= year_range[0])
        & (filtered["award_year"] <= year_range[1])
    ]

    # Filter by categories
    if categories:
        filtered = filtered[filtered["category"].isin(categories)]

    # Filter by gender
    if gender != "All":
        filtered = filtered[filtered["sex"] == gender.lower()]

    # Filter by country
    if country != "All":
        filtered = filtered[filtered["birth_country"] == country]

    return filtered


def calculate_stats(df):
    """Calculate summary statistics."""
    stats = {
        "total_prizes": len(df),
        "total_laureates": int(df["laureate_id"].nunique()),
        "countries_count": int(df["birth_country"].nunique()),
        "gender_split": df["sex"].value_counts().to_dict(),
    }
    return stats


# Main app
def main():
    st.title("🏆 Nobel Prize Data Dashboard")
    st.markdown("Explore Nobel Prize winners from 1901 to 2025")
    st.markdown("---")

    # Load data
    try:
        df = load_data("data/nobel_prizes_1901-2025_cleaned.csv")
    except FileNotFoundError:
        st.error(
            "Data file not found. Please ensure "
            "'data/nobel_prizes_1901-2025_cleaned.csv' exists."
        )
        st.stop()

    # Sidebar filters
    st.sidebar.header("🔍 Filters")

    # Year range slider
    min_year = int(df["award_year"].min())
    max_year = int(df["award_year"].max())
    year_range = st.sidebar.slider(
        "Year Range", min_value=min_year, max_value=max_year, value=(min_year, max_year)
    )

    # Category filter
    all_categories = sorted(df["category"].unique())
    selected_categories = st.sidebar.multiselect(
        "Categories", options=all_categories, default=all_categories
    )

    # Gender filter
    gender_filter = st.sidebar.radio("Gender", options=["All", "Male", "Female"])

    # Country filter
    countries = ["All"] + sorted(df["birth_country"].dropna().unique().tolist())
    country_filter = st.sidebar.selectbox("Birth Country", options=countries)

    # Apply filters
    filtered_df = filter_data(
        df, year_range, selected_categories, gender_filter, country_filter
    )

    # Calculate statistics
    stats = calculate_stats(filtered_df)

    # Display metrics
    st.subheader("📊 Overview")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Prizes", stats["total_prizes"])

    with col2:
        st.metric("Unique Laureates", stats["total_laureates"])

    with col3:
        st.metric("Countries", stats["countries_count"])

    with col4:
        male_count = stats["gender_split"].get("male", 0)
        female_count = stats["gender_split"].get("female", 0)
        total = male_count + female_count
        female_pct = (female_count / total * 100) if total > 0 else 0
        st.metric("Female %", f"{female_pct:.1f}%")

    st.markdown("---")

    # Create tabs for different views
    tab1, tab2, tab3 = st.tabs([
        "📋 Data Table",
        "📈 Statistics",
        "🌍 Geographic Analysis"
    ])

    with tab1:
        st.subheader("Filtered Nobel Prize Data")

        # Display key columns
        display_cols = [
            "award_year",
            "known_name",
            "category",
            "sex",
            "birth_country",
            "motivation",
        ]
        available_cols = [col for col in display_cols if col in filtered_df.columns]

        st.dataframe(filtered_df[available_cols], use_container_width=True, height=400)

        # Download button
        csv = filtered_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Filtered Data (CSV)",
            data=csv,
            file_name="nobel_prizes_filtered.csv",
            mime="text/csv",
        )

    with tab2:
        st.subheader("Statistical Analysis")

        col1, col2 = st.columns(2)

        with col1:
            # Prizes by category
            st.write("**Prizes by Category**")
            category_counts = filtered_df["category"].value_counts().sort_index()
            fig1 = px.bar(
                x=category_counts.index,
                y=category_counts.values,
                labels={"x": "Category", "y": "Count"},
                title="Distribution by Category",
            )
            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            # Top 10 countries
            st.write("**Top 10 Countries by Laureates**")
            country_counts = filtered_df["birth_country"].value_counts().head(10)
            fig2 = px.bar(
                x=country_counts.values,
                y=country_counts.index,
                orientation="h",
                labels={"x": "Count", "y": "Country"},
                title="Top 10 Countries",
            )
            st.plotly_chart(fig2, use_container_width=True)

        # Gender distribution over time
        st.write("**Gender Distribution Over Time**")
        gender_by_year = (
            filtered_df.groupby(["award_year", "sex"]).size().reset_index(name="count")
        )
        fig3 = px.line(
            gender_by_year,
            x="award_year",
            y="count",
            color="sex",
            title="Gender Distribution Over Time",
            labels={"award_year": "Year", "count": "Number of Laureates"},
        )
        st.plotly_chart(fig3, use_container_width=True)

        # Shared vs Solo prizes
        if "is_shared" in filtered_df.columns:
            col1, col2 = st.columns(2)

            with col1:
                st.write("**Shared vs Solo Prizes**")
                shared_counts = filtered_df["is_shared"].value_counts()
                labels = ["Solo", "Shared"]
                values = [shared_counts.get(0, 0), shared_counts.get(1, 0)]

                fig4 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3)])
                fig4.update_layout(title="Prize Sharing Distribution")
                st.plotly_chart(fig4, use_container_width=True)

            with col2:
                st.write("**Prizes by Decade**")
                # Calculate decade
                filtered_df_copy = filtered_df.copy()
                filtered_df_copy["decade"] = (
                    filtered_df_copy["award_year"] // 10
                ) * 10
                decade_counts = (
                    filtered_df_copy.groupby("decade").size().reset_index(name="count")
                )

                fig5 = px.bar(
                    decade_counts,
                    x="decade",
                    y="count",
                    title="Nobel Prizes by Decade",
                    labels={"decade": "Decade", "count": "Number of Prizes"},
                )
                st.plotly_chart(fig5, use_container_width=True)

    with tab3:
        st.subheader("Geographic Distribution")

        # Prizes by country on map (top 20)
        country_data = (
            filtered_df["birth_country"].value_counts().head(20).reset_index()
        )
        country_data.columns = ["country", "count"]

        st.write("**Top 20 Countries by Laureate Count**")
        st.dataframe(country_data, use_container_width=True)

        # Category breakdown by top 5 countries
        top_5_countries = (
            filtered_df["birth_country"].value_counts().head(5).index.tolist()
        )
        top_countries_df = filtered_df[
            filtered_df["birth_country"].isin(top_5_countries)
        ]

        st.write("**Category Distribution in Top 5 Countries**")
        category_country = (
            top_countries_df.groupby(["birth_country", "category"])
            .size()
            .reset_index(name="count")
        )
        fig6 = px.bar(
            category_country,
            x="birth_country",
            y="count",
            color="category",
            title="Prize Categories by Top 5 Countries",
            labels={"birth_country": "Country", "count": "Number of Prizes"},
        )
        st.plotly_chart(fig6, use_container_width=True)

    # Footer
    st.markdown("---")
    st.caption(
        "Data source: Nobel Prize dataset (1901-2025) | Built with Streamlit"
    )


if __name__ == "__main__":
    main()
