import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px

# Set style

sns.set(style="dark")

st.set_page_config(
    page_title="Bike-sharing Dashboard",
    page_icon=":pager:",
    layout="wide",
)

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Load dataset

df = pd.read_csv(
    "https://raw.githubusercontent.com/pratwib/bikesharing-data-analysis/main/dashboard/cleaned_day.csv"
)
df["dateday"] = pd.to_datetime(df["dateday"])

# Create functions


def create_monthly_users_df(df):
    monthly_users_df = df.resample(rule="M", on="dateday").agg(
        {
            "casual": "sum",
            "registered": "sum",
            "count": "sum",
        }
    )
    monthly_users_df.index = monthly_users_df.index.strftime("%b-%y")
    monthly_users_df = monthly_users_df.reset_index()
    monthly_users_df = monthly_users_df.rename(
        columns={
            "dateday": "month-year",
            "count": "total",
        }
    )
    return monthly_users_df


def create_seasonly_users_df(df):
    seasonly_users_df = df.groupby("season").agg(
        {
            "casual": "sum",
            "registered": "sum",
            "count": "sum",
        }
    )
    seasonly_users_df = seasonly_users_df.reset_index()
    seasonly_users_df.rename(
        columns={
            "count": "total",
        },
        inplace=True,
    )
    seasonly_users_df = pd.melt(
        seasonly_users_df,
        id_vars=["season"],
        value_vars=["casual", "registered"],
        var_name="type of users",
        value_name="count",
    )
    seasonly_users_df = seasonly_users_df.sort_values(by="count", ascending=True)
    return seasonly_users_df


def create_weekday_users_df(df):
    weekday_users_df = df.groupby("weekday").agg(
        {"casual": "sum", "registered": "sum", "count": "sum"}
    )
    weekday_users_df = weekday_users_df.reset_index()
    weekday_users_df = pd.melt(
        weekday_users_df,
        id_vars=["weekday"],
        value_vars=["casual", "registered"],
        var_name="type of users",
        value_name="total",
    )
    weekday_users_df["weekday"] = pd.Categorical(
        weekday_users_df["weekday"],
        categories=[
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ],
    )
    weekday_users_df = weekday_users_df.sort_values("weekday")
    return weekday_users_df


def create_wordkingday_users_df(df):
    weekday_users_df = df.groupby("workingday").agg(
        {
            "casual": "sum",
            "registered": "sum",
            "count": "sum",
        }
    )
    weekday_users_df = weekday_users_df.reset_index()
    weekday_users_df = weekday_users_df.rename(
        columns={
            "count": "total",
        }
    )
    return weekday_users_df


def create_holiday_users_df(df):
    holiday_users_df = df.groupby("holiday").agg(
        {
            "casual": "sum",
            "registered": "sum",
            "count": "sum",
        }
    )
    holiday_users_df = holiday_users_df.reset_index()
    holiday_users_df = holiday_users_df.rename(
        columns={
            "count": "total",
        }
    )
    return holiday_users_df


# Create dashboard

# Sidebar display

min_date = df["dateday"].min()
max_date = df["dateday"].max()

with st.sidebar:
    st.image(
        "https://github.com/pratwib/bikesharing-data-analysis/blob/main/dashboard/logo_cb.png?raw=true"
    )

    start_date, end_date = st.date_input(
        label="Select Date:",
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date],
    )

    st.sidebar.markdown("Pratama Wibi's Profile:")

    col1, col2 = st.sidebar.columns(2)

    with col1:
        st.markdown(
            "[![LinkedIn](https://img.icons8.com/glyph-neue/FFFFFF/linkedin)](https://www.linkedin.com/in/pratwib/)"
        )
    with col2:
        st.markdown(
            "[![Github](https://img.icons8.com/glyph-neue/FFFFFF/github)](https://github.com/pratwib)"
        )

main_df = df[(df["dateday"] >= str(start_date)) & (df["dateday"] <= str(end_date))]

# Connect functions with main_df

monthly_users_df = create_monthly_users_df(main_df)
seasonly_users_df = create_seasonly_users_df(main_df)
weekday_users_df = create_weekday_users_df(main_df)
workingday_users_df = create_wordkingday_users_df(main_df)
holiday_users_df = create_holiday_users_df(main_df)


# Mainpage display


st.title(":pager: Bike-Sharing Dashboard for Capital Bikeshare")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    total_users = main_df["count"].sum()
    st.metric("Total Users", value=total_users)
with col2:
    casual_users = main_df["casual"].sum()
    st.metric("Casual Users", value=casual_users)
with col3:
    registered_users = main_df["registered"].sum()
    st.metric("Registered Users", value=registered_users)

st.markdown("---")

fig = px.line(
    monthly_users_df,
    x="month-year",
    y=["total"],
    color_discrete_sequence=["green"],
    markers=True,
    title="Monthly Bike-sharing Users",
).update_layout(xaxis_title="", yaxis_title="Total Users")

st.plotly_chart(fig, use_container_width=True)

fig = px.line(
    monthly_users_df,
    x="month-year",
    y=["casual", "registered"],
    color_discrete_sequence=["blue", "orange"],
    markers=True,
    title="",
).update_layout(xaxis_title="", yaxis_title="Total Users", showlegend=False)

st.plotly_chart(fig, use_container_width=True)

fig = px.bar(
    seasonly_users_df,
    x=["count"],
    y="season",
    color="type of users",
    barmode="group",
    color_discrete_sequence=["blue", "orange"],
    title="Seasonly Bike-sharing Users",
).update_layout(xaxis_title="Total Users", yaxis_title="")

st.plotly_chart(fig, use_container_width=True)

fig1 = px.bar(
    weekday_users_df,
    x="weekday",
    y=["total"],
    color_discrete_sequence=["green"],
    title="Daily Bike-sharing Users",
).update_layout(xaxis_title="", yaxis_title="Total Users")

fig2 = px.bar(
    weekday_users_df,
    x="weekday",
    y=["total"],
    color="type of users",
    barmode="group",
    color_discrete_sequence=["blue", "orange"],
).update_layout(xaxis_title="", yaxis_title="Total Users")

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig1, use_container_width=True)
right_column.plotly_chart(fig2, use_container_width=True)

fig1 = px.bar(
    workingday_users_df,
    x="workingday",
    y=["total"],
    color="workingday",
    title="Bike-sharing Users by Workingday",
)

fig1.update_layout(xaxis_title="", yaxis_title="Total Users", showlegend=False)
fig1.update_xaxes(tickvals=[0, 1], ticktext=["No", "Yes"])

fig2 = px.bar(
    holiday_users_df,
    x="holiday",
    y=["total"],
    color="holiday",
    title="Bike-sharing Users by Holiday",
)

fig2.update_layout(xaxis_title="", yaxis_title="Total Users")
fig2.update_xaxes(tickvals=[0, 1], ticktext=["No", "Yes"])

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig1, use_container_width=True)
right_column.plotly_chart(fig2, use_container_width=True)

st.caption("Copyright (c) 2023, made by Pratama Wibi")
