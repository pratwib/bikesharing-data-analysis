# 🚲 Bikesharing Data Analysis and Dashboard
Dataset by: Capital Bikeshare

## 📓 Data Analysis with Jupyter Notebook
⚠️ See the detail of analysis and visualization on the [notebook](https://github.com/pratwib/bikesharing-data-analysis/blob/main/notebook.ipynb) 

### Defining Business Question
1. How is the number comparison between casual and registered user types?
2. During which season do users of bike-sharing services reach their peak?
3. How has the bike-sharing user trend been in the last 2 years?
4. What is the usage pattern of bike-sharing services based on day of the week?
5. Does weather affect the usage of bike-sharing services?
6. Is there a correlation between temperature conditions and the number of users of bike-sharing services?

### Insights and Conclusions
1. The number of `registered` bike-sharing users, totaling 2.6 million, is **notably higher** compared to `casual` users, which amount to 600,000. This indicates a substantial difference, with `registered` users being approximately 4x more numerous than `casual` users.

2. The bike-sharing service **reaches its peak during fall** `season`, with 1 million users. Summer and winter closely follow, while the usage is comparatively lower in spring `season`, with around 470,000 users. Interestingly, when examining user types, there is no notable difference in the seasonal patterns, as all seasons demonstrate a similar total user count trend.

3. In the last 2 years (2011-2012), there was an **overall growth** in the number of bike-sharing users. This increase was particularly pronounced among `registered` users. The annual trend for both user types consistently involves a low point in Q1, a peak in Q3, and a decrease in Q4. Significantly, `registered` users outperformed casual users in terms of quantity, showcasing a substantial increase for both user categories.

4. The usage pattern of bike-sharing services based on the day of the week reveals a **consistent overall value around 400,000** users daily. However, a closer look by user types shows that `registered` users tend to be **higher on weekdays**, while `casual` users show **higher usage on weekends**. The trend aligns with the distinction observed in the visualization of bike-sharing users on working days, where the **number in total significantly increases** to 2.3 million. On the contrary, during holidays, there is a **drastic decrease** in bike-sharing users, reaching only 78,000.

5. The barplot analysis indicates that weather has a **significant impact** on the usage og bike-sharing services. Approximately 3/4 of users, totalling 2.3 million, prefer biking in clear `weather`. Interestingly, during heavy rain, there are no bike-sharing users at all, suggesting a notable influence of `weather` conditions on the choice to use bike-sharing services.

6. The observations from the heatmap and scatterplot suggest a correlation between temperature conditions and `count` of bike-sharing users. There is a **positive moderate correlation**, around 0.6 points, with both `temp` and `atemp`, indicating that `count` of bike-sharing users **tends to increase** as temperature rises. Additionally, there is a **slight negative correlation**, about -0.1 point for `hum` and -0.23 points for `windspeed`, implying that as humidity and wind speed increase, there is a **small decrease** in `count` of bike-sharing users.

##  📟 Dashboard with Streamlit Cloud

### Streamlit Cloud
⚠️ View the dashboard directly on this link: https://capital-bikeshare-alfikri.streamlit.app/

The dashboard shows the count of total rides across the year and season. It also shows the difference casual riders and registered riders use of the bikesharing service, based on hour and day of the week.

<p align="center">
  <img src="/image/streamlit_dashboard.png" />

### Run Streamlit on Local

#### Install Dependencies

To install all the required libraries, open your terminal/command prompt/conda prompt, navigate to this project folder, and run the following command:

```bash
pip install -r requirements.txt
```

#### Run Dashboard
```bash
cd dashboard
streamlit run dashboard.py
```

Thanks for visiting my project! 🔥
