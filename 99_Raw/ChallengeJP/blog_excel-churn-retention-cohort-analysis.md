# A Guide to Churn, Retention and Cohort Analysis | ChallengeJP

**Source:** https://www.challengejp.com/blog/excel-churn-retention-cohort-analysis

---

How to Use Cohort Analysis to Calculate Retention and Churn Rate in Microsoft Excel
===================================================================================

*   ![Jacek Polewski](https://www.challengejp.com/wp-content/cache/flying-press/gravatar-0c5b42d9d6e4.png) [Jacek Polewski](https://www.challengejp.com/blog/author/adminchallengejp-com/ "Posts by Jacek Polewski")
    
*   June 15, 2020October 12, 2025

Last Updated on October 12, 2025

Your business data contains valuable information about your customers, operations, costs and finances. Using cohort analysis, a type of behavioural data analytics, you can dig deeper into customer behaviour data and calculate your business’s retention and churn rate. 

This article will guide you through conducting a cohort analysis to calculate retention and churn rates in Microsoft Excel. Together, we’ll follow a step-by-step process using a simple user log spreadsheet to demonstrate. 

A user log we’ll refer to throughout this tutorial has three simple columns: 

*   **Event** — This will be either a sign-up, renewal or unsubscribe
*   **User ID** — A number will be assigned to each customer/subscriber so you can see which users the events apply to.
*   **Date** — A date will be listed next to each event to tell when each user subscribed, renewed or unsubscribed.

You can download the user log file to follow along with this tutorial. The final analysis spreadsheets show the calculations, tables and insights you’ll have after following the steps in this article:

[User Log (CSV)](https://www.challengejp.com/wp-content/uploads/2020/06/user_log.csv)

[Final Analysis (Google Sheets)](https://docs.google.com/spreadsheets/d/1B8Ko9he_yQRArF1Oh-kKXfhQFcs5rr1177N_JPb205g/edit?usp=sharing)

[Final Analysis (Excel file)](https://www.challengejp.com/wp-content/uploads/2021/03/cohort_churn_retention_analysis.xlsx)

**Note: If you scroll down to the bottom of this article, you’ll find a video version of this tutorial.**

**What is Cohort Analysis?**
----------------------------

Cohort analysis is a type of behavioural analytics. It involves taking your customer data, but rather than looking at all users simultaneously, it splits them into groups (i.e. cohorts). The grouping is based on certain characteristics such as demographics, interests, lifespan, etc. 

Even if your business is only recently established and you only have a limited amount of data, cohort analysis will give you valuable insights into how customers respond to your products or services. You can clearly understand user engagement and identify any lack of activity by certain user groups.

Cohort analysis will also shed light on your churn rate and retention, and by measuring these factors, you can then take action to reduce churn and improve retention. 

Table of Contents

Toggle

**Step 1: Prepare Data for Cohort Analysis** 
---------------------------------------------

Once you’ve downloaded the user log for this tutorial, you’ll see the three columns with inputted data. ‘Event’ describes a type of action related to a given row (i.e. start of subscription, renewal, or user termination). ‘User\_id’ is a unique identifier of a user. The ‘Date’ is the event’s day, month and year.

While the spreadsheet already has enough data points to analyse the user journey, adding a few extra columns makes the job much easier. To make it possible to analyse user behaviour by the month and year when they joined the service, you need to add two columns for year and month. You can do this using the [MONTH and YEAR function](https://www.excel-easy.com/functions/date-time-functions.html)
 in Microsoft Excel or Google Sheets.

Next, create a ‘month\_no’ column — this will show the month in which an event occurred, counting Month 1 as the month that your first user signed up. For example, if your business’s first user signed up in January, this will be Month 1, and if another user signs up in April, this will be Month 4. 

**Step 2: Create a Monthly Summary of Data**
--------------------------------------------

With these columns set up, you can create a simple pivot table that shows the number of user signups, renewals, and unsubscribes by month and year. To do this, select all the data (use the Control+A shortcut), then click on the drop-down ‘Data’ menu in Google Sheets or Microsoft Excel and select ‘Pivot Table’. 

Then, in the pivot table editor, add ‘Event’ to your rows and ‘Year’ and ‘Month’ to your columns. Select ‘User ID’ for values and choose COUNTA to summarise the numbers. And, to make the presentation a bit clearer, just un-click ‘show total’ on the Month and Year columns.

The resulting table will show you how many events occurred each month. Use this information to create a secondary table beneath this first pivot table to show the closing number of users at the end of each month.

[![Pivot Table - Cohort Analysis](https://www.challengejp.com/wp-content/uploads/2020/07/pivot-table-cohort-analysis.png)](https://www.challengejp.com/wp-content/uploads/2020/07/pivot-table-cohort-analysis.png)

A Google Sheet summary of user signups, renewals and unsubscribes by month and year.

**Step 3: Assign Users to Cohorts** 
------------------------------------

While showing user numbers by month can be very helpful, you ideally want to understand better how users behave. To do this, you can assign users to a specific cohort (a group of users with similar characteristics). 

Cohort analysis often involves grouping users by age range, profession, gender, etc. We don’t have that information in our example dataset, so we will group users based on their signing up. 

To do this, create another column labelled ‘cohort\_month’. This will allow you to see which cohort users belong to easily. You’ll then need to apply a filter to your table so that it only displays sign-ups. Then, copy this table and paste it into a new sheet. Name the sheet ‘cohort\_lookup’ and rename the column ‘month\_no’ to ‘cohort\_month’ for clarity.

**Step 4: Add a Cohort Age Column** 
------------------------------------

With the user cohort table completed you need to head back to our log sheet and finish your data preparation. Remove the filter applied in step 2, and then you’ll need to create a ‘cohort\_month’ column for this sheet. This involves using a [v-lookup](https://www.excel-easy.com/examples/vlookup.html)
 between the user\_id value and the table in the ‘cohort\_lookup’ sheet. Once you’ve done this, every event of each user will be assigned to a specific cohort. 

For the next step, you need to add a ‘cohort\_age’ column. This will let you know how long a user has been signed up for. To calculate cohort age, subtract the ‘cohort\_month’ from the ‘month\_number’. 

[![Cohort Age - Cohort Analysis](https://www.challengejp.com/wp-content/uploads/2020/07/cohort-age-cohort-analysis.png)](https://www.challengejp.com/wp-content/uploads/2020/07/cohort-age-cohort-analysis.png)

A spreadsheet showing calculations for month number, cohort month and cohort age.

**Step 5: Assign Event Value** 
-------------------------------

Next, we want to assign a value to each event. For this analysis, any ‘signup’ or ‘renewal’ will carry a value of 1 and ‘unsubscribe’ will have a value of 0. This is so that you can count the number of active users and discount any unsubscribed users.

**Step 6: Create a User Profile Pivot Table to Display User Behaviour**
-----------------------------------------------------------------------

For the next step, create another pivot table to see how users behave during their subscriptions. The table should show the date users signed up, how long they remained a customer, and when they cancelled or unsubscribed. 

When creating your pivot table, populate the rows with ‘cohort\_month’, the columns with ‘cohort\_age’, and for the value, add ‘event\_value’ and summarise by SUM. 

You should now be able to see how many users signed up each month, how many renewed and how many unsubscribed. 

[![cohort churn analysis](https://www.challengejp.com/wp-content/uploads/2020/07/cohort-churn-analysis.png)](https://www.challengejp.com/wp-content/uploads/2020/07/cohort-churn-analysis.png)

A table listing users by their cohort\_id showing the total number of users per month.

**Step 7: Cohort Retention Analysis** 
--------------------------------------

Using the user profile pivot table that you created in Step 5, you can create a user retention table. The table will show the number of users that subscribed to the service as a percentage of initial signups.

For instance, the screenshot below shows that 26.3% of users in the month 4 cohort renewed their subscription in month 6. 

While the user profile table gives a good overview of absolute numbers, a retention table gives a better insight into the relative behaviour of users. For example, you can see that users from certain cohorts remain paying customers longer than users in other cohorts. 

[![customer data -cohort analysis](https://www.challengejp.com/wp-content/uploads/2020/07/customer-data-cohort-analysis.png)](https://www.challengejp.com/wp-content/uploads/2020/07/customer-data-cohort-analysis.png)

A table showing the monthly user retention rates of each cohort\_id.

**Step 8: Cohort Churn Analysis** 
----------------------------------

In addition to your retention table, a user churn table can help you see how many users you lose each month. The table will also show how ‘old’ users are when unsubscribed or cancelled. 

Looking at the month 8 cohort, we can see that 93.8% (15 out of 16) of users unsubscribed from the service before their first renewal! Another interesting emerging pattern is that, on average, 64.5% of users cancelled before Month 1. One explanation is that the sign-up came with a free trial offer. When the trial ended, users may have cancelled their subscription before the first payment. 

[![cohort churn analysis stage 7](https://www.challengejp.com/wp-content/uploads/2020/07/cohort-churn-analysis-stage-7.png)](https://www.challengejp.com/wp-content/uploads/2020/07/cohort-churn-analysis-stage-7.png)

A monthly user churn analysis table showing incremental churn percentage.

**Step 9: Analysis and Interpretation**
---------------------------------------

The user log we’ve used in this tutorial is a simple dataset. However, even with this snippet of user data, we can draw some interesting conclusions.

We can see that in month 8, there must have been an event or factor that influenced user behaviour. That event caused more users to end their subscriptions than in other months. Factors might also have convinced users who signed up in months 4 or 11 to remain paying customers longer than other users. 

One thing to note is that this data only has 14-20 users per cohort. Random occurrences can cause fluctuations in patterns and trends, so we need to gather more data. With a larger dataset, cohort analysis will help you identify clear retention and churn rate patterns. 

When analysing your business data, you can look at churn rate and retention alongside your sales and marketing campaigns. You can also use the historical data as a benchmark to measure the effectiveness of future campaigns. 

Look for when users sign up and how long they remain customers when they unsubscribe. What do you think may cause them to leave your business? Once you’ve made sense of your data and gained a better understanding, you can use these insights to implement different strategies to improve retention and reduce churn.

**Bonus Insight: Lifetime User Value**
--------------------------------------

As an extra, I’ve also added a lifetime user value table to the final analysis of the user log. You can see how I created this in the video below, or take a look at the final analysis spreadsheet to see how you can use your user retention figures to calculate user lifetime value and how each user contributes to your total revenue. 

**Read More:** Visit my tutorial on [How to Create a Subscription Model with Churn Calculation](https://www.challengejp.com/blog/how-to-create-subscription-model-with-churn-calculation/)
 to learn about applying cohort analysis results to build a cash flow forecast.

**Watch Video Tutorial**
------------------------

▶️ [Watch on YouTube](https://youtu.be/HY-ewBkmVaI)

![How to Use Cohort Analysis to Calculate Retention and Churn Rate in Microsoft Excel](https://www.challengejp.com/wp-content/cache/flying-press/HY-ewBkmVaI-hqdefault.jpg)

Get in Touch
------------

_[![challengejp_data_analyst](https://www.challengejp.com/wp-content/uploads/2020/07/jp_photo-300x200.jpg)](https://www.challengejp.com/about/)
Hi, my name is Jacek and I love spreadsheets! I h__ope you’ve enjoyed reading this tutorial as much as I did writing it! If you have any questions about Microsoft Excel and data analysis, don’t hesitate to **[get in touch](https://www.challengejp.com/contact/)
**._

_[**Explore my other tutorials**](https://www.challengejp.com/blog/)
 to learn more about data and financial analysis. If you need further support, find out about my [**One-to-One Training**](https://www.challengejp.com/services/financial-modelling-data-training/)
 and **[Data Analytics Services](https://www.challengejp.com/services/data-analytics/)
**._

Learn More
----------

[Analyze and Forecast Customer Churn and Revenue](https://www.challengejp.com/blog/power-bi-customer-churn-revenue-forecast-tutorial/)
 – Build a churn/retention model in Power BI using DAX, cohort analysis, and interactive forecasts.

[Subscription Model with Churn Calculation](https://www.challengejp.com/blog/how-to-create-subscription-model-with-churn-calculation/)
 – Learn how to apply churn and retention rate analysis to build a subscription model with a customer’s life cycle and lifetime value calculator.

[Use Python and Pandas for Data Consolidation and Transformation](https://www.challengejp.com/blog/python-excel-data-consolidation-transformation/)
 – This step-by-step tutorial will introduce you to Python and teach you how to write scripts to speed up your work with data.

[Creating a Marketing Investment Plan](https://www.challengejp.com/blog/how-to-create-marketing-investment-plan-excel-tutorial/)
 – Learn more about combining churn and customer lifetime calculations with marketing assumptions in a financial and cash flow model.

[Power BI Marketing Performance & Forecast Dashboard](https://www.challengejp.com/blog/power-bi-marketing-performance-forecast-dashboard/)
 — Create a Power BI dashboard to track campaign performance, model customer growth, and forecast marketing ROI with DAX-driven metrics.

[→ View all tutorials](https://www.challengejp.com/services/tutorials/)

Tags:[Business Insights](https://www.challengejp.com/blog/tag/business-insights/ "Business Insights")
[Data Analytics](https://www.challengejp.com/blog/tag/data-analytics/ "Data Analytics")

6 thoughts on “How to Use Cohort Analysis to Calculate Retention and Churn Rate in Microsoft Excel”
---------------------------------------------------------------------------------------------------

1.  ![](https://www.challengejp.com/wp-content/cache/flying-press/gravatar-61a6bed77493.png)
    
    Francisco [January 11, 2021 at 6:19 pm](https://www.challengejp.com/blog/excel-churn-retention-cohort-analysis/#comment-129)
    
    Hi Jacek, thank you for the article, it’s super complete and helpful!
    
2.  1.  ![](https://www.challengejp.com/wp-content/cache/flying-press/gravatar-2ccff6170f01.png)
        
        Jacek Polewski [January 11, 2021 at 8:43 pm](https://www.challengejp.com/blog/excel-churn-retention-cohort-analysis/#comment-130)
        
        You’re welcome, Francisco. Glad I could help!!
        
3.  ![](https://www.challengejp.com/wp-content/cache/flying-press/gravatar-a59b50936f05.png)
    
    Andre [February 27, 2021 at 10:46 pm](https://www.challengejp.com/blog/excel-churn-retention-cohort-analysis/#comment-482)
    
    Thank you, Jacek, for a precise step-by-step explanation!
    
4.  1.  ![](https://www.challengejp.com/wp-content/cache/flying-press/gravatar-2ccff6170f01.png)
        
        Jacek Polewski [February 28, 2021 at 11:05 pm](https://www.challengejp.com/blog/excel-churn-retention-cohort-analysis/#comment-497)
        
        You’re welcome, Andre!
        
5.  ![](https://www.challengejp.com/wp-content/cache/flying-press/gravatar-3a68be02e295.png)
    
    [Kuliah Terbaik](https://uhamka.ac.id/)
     [December 18, 2023 at 7:14 pm](https://www.challengejp.com/blog/excel-churn-retention-cohort-analysis/#comment-14110)
    
    Would it be alright if I added this content to my dataset? I’d like to highlight that this is for my personal hobby as a data scientist, and I’ll be citing the source conscientiously. Here my campus page at [Kampus Terbaik](https://uhamka.ac.id/)
     Thanks! ID : CMT-CZLOJF159BHUWDHKXB
    
6.  1.  ![](https://www.challengejp.com/wp-content/cache/flying-press/gravatar-2ccff6170f01.png)
        
        Jacek Polewski [December 21, 2023 at 11:08 pm](https://www.challengejp.com/blog/excel-churn-retention-cohort-analysis/#comment-14142)
        
        Hi Kuliah, that’s not a problem – feel free to use it!
        

Comments are closed.

  

**Redirecting to FastSpring for secure payment and local tax handling in your region...**

You’ll see challengejp.onfastspring.com in your address bar.