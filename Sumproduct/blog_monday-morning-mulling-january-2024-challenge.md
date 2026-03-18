# Monday Morning Mulling: January 2024 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-january-2024-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: January 2024 Challenge

*   January 28, 2024

Monday Morning Mulling: January 2024 Challenge
==============================================

Monday Morning Mulling: January 2024 Challenge
==============================================

29 January 2024

_On the final [Friday](https://www.sumproduct.com/blog/article/fff-mmm/final-friday-fix-january-2024-challenge)
 of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

**_This month was a little bit different…_**

Here at SumProduct we’ve been learning a lot about ChatGPT recently in order to stay up to date with the latest technology. With last Friday falling on Australia day, we figured we would get ChatGPT to pick up the slack for all the staff on holiday and write this month’s FFF. Did any of you notice a difference? We used the new GPTs feature to create a custom AI whose purpose is to make Final Friday Fixes and Monday Morning Mullings and it wrote almost all of the Friday’s blog along with today’s blog, while even generating the Excel sample file for you to download.

For those who are interested to learn more about how we did it, there will be an article on the website and in the March newsletter going through the steps. You may even enquire about our upcoming ‘Introduction to ChatGPT’ training course to master the tool – if that’s indeed possible! For everyone else, enjoy this months AI generated Monday Morning Mulling and see if you outsmarted the AI…

**_The Challenge_**

As another week begins, we’re back with the solution to our sun-soaked Excel challenge. This challenge was all about managing a summer camp’s activities, ensuring none were overbooked. Let’s unravel the solution, which ensures that each camper gets their fair share of fun under the sun!

We had two Excel tables – **Activities\_Table** and **SignUps\_Table**. Our task was to create a dynamic formula to check if the number of sign-ups for each activity per day exceeded its maximum capacity. You could download the question file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/Jan/FFF/extendedsummercampactivities.xlsx)
 which contains the following Tables:

![](<Base64-Image-Removed>)

The requirements were for the solution to:

· be dynamic and update immediately as new sign-ups are added

· use only Excel formulas – no Power Query, Get & Transform, or VBA allowed

· be case-insensitive.

**_Suggested Solution_**

**SETTING UP DAY COLUMNS IN THE ACTIVITIES TABLE**

We need to prepare the **Activities\_Table** for our calculations. In addition to the ‘Activity’ and ‘Max Capacity’ columns, we added columns for each day of the week (Monday to Friday). These columns will hold the count of sign-ups for each activity per day.

![](<Base64-Image-Removed>)

**THE FORMULA**

We used the **[COUNTIFS](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-countifs-function)
**function in Excel, which counts the number of times multiple conditions are met. The formula structure in each day column of the **Activities** table is as follows:

**\=COUNTIFS(SignUps\_Table\[Activity\], Activities\_Table\[@Activity\], SignUps\_Table\[Day\], “Specific Day”)**

Here, **SignUps\_Table\[Activity\]** and **SignUps\_Table\[Day\]** refer to the respective columns in the **SignUps\_Table**, and **Activities\_Table\[@Activity\]** refers to the current activity in the **Activities\_Table**. **“Specific Day”** is replaced with the cell reference for actual day we’re checking (_e.g_. **C$1**).

**COMPARING WITH MAXIMUM CAPACITY**

**\=IF(COUNTIFS(SignUps\_Table\[Activity\], Activities\_Table\[@Activity\], SignUps\_Table\[Day\], C$1) > Activities\_Table\[@\[Max Capacity\]\], “Overbooked”, “Available”)**

This formula is replicated for each day column, changing the **C$1** parameter to the respective column reference. The formula returns “Overbooked” for activities that exceed their capacity on a given day and “Available” for those within capacity.

![](<Base64-Image-Removed>)

**DETAILED EXPLANATION**

The **[COUNTIFS](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-countifs-function)
**function works by counting the number of times sign-ups for an activity occur on a specified day. It cross-references the activity name and the day between the **Activities\_Table** and the **SignUps\_Table**.

By placing this formula in each day column next to every activity, we can dynamically track the number of sign-ups as they happen. The **[IF](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-if-function)
**statement then checks if this count exceeds the maximum capacity. If it does, it flags the activity as “Overbooked.”

**_Word to the Wise_**

While our formula works great for small to medium datasets, larger datasets with thousands of entries might require more efficient data management solutions like Power Query or even PivotTables for better performance and ease of use.

With this solution, managing the summer camp activities should be a breeze, ensuring every camper has their day in the sun! Stay tuned for our next Excel adventure in the upcoming Final Friday Fix!

_The Final Friday Fix will return on Friday 23 February 2024 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-january-2024-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-january-2024-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-january-2024-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-january-2024-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-january-2024-challenge/#0 "close")

top