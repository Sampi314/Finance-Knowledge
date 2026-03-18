# 5 pivot tables you probably haven't seen before | Exceljet

**Source:** https://exceljet.net/articles/5-pivot-tables-you-probably-havent-seen-before

---

[Skip to main content](https://exceljet.net/articles/5-pivot-tables-you-probably-havent-seen-before#main-content)

[](https://exceljet.net/articles/5-pivot-tables-you-probably-havent-seen-before#)

*   [Previous](https://exceljet.net/articles/cool-things-you-can-do-with-conditional-formatting)
    
*   [Next](https://exceljet.net/articles/can-pivot-tables-save-your-job)
    

5 pivot tables you probably haven't seen before
===============================================

by Dave Bruns · Updated 18 Jun 2024

![Pivot tables to delight and amaze!](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/emailsub2.png "Pivot tables to delight and amaze!")

Summary
-------

In this article, we take a short tour of some "unconventional" pivot tables you probably haven't seen before. These are interesting pivot tables created to analyze something _other_ than sales data.

One thing you might have noticed about pivot tables is that almost all the examples you see are based on sales data. This makes sense in a way: sales is where the money is, and companies _always_ have sales data in one form or another. However, pivot tables can handle a lot more than just sales. _Any time_ you need to work with data, you should be thinking about pivot tables.

To illustrate how flexible and useful pivot tables are, here are five interesting examples you probably haven't seen before. I'm not going to explain how to create each pivot table in this article (I'll leave that for another day). I just want to give you some ideas about how you can use pivot tables with your own data.

### Time tracking

Imagine you need to log time for different clients and projects and periodically report your time by client and project. There are of course many applications dedicated to time-tracking, but you can easily create your own flexible system using Pivot Tables.

At a minimum, what you need to record is a date, the time you spent, the client name, and the project. So, after you enter the data consistently, you might end up with source data that looks something like this:

![Simple time tracking data by client and project](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/timesheet0.png?itok=zuUm2zMx "Simple time tracking data by client and project")

Note that there are no blank lines - you just need to enter the data as you go.

Now the summaries. First, you might want an overview of your time by week. Here we are using the week numbers provided by Excel's [WEEKNUM function](https://exceljet.net/functions/weeknum-function)
 (see column C of the source data):

![A summary of time by week number](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/timesheet1.png?itok=KEAYOABu "A summary of time by week number")

You might also want to arrange the pivot table to show a more traditional timesheet layout, with days of the week across the top:

![A summary of time logged for one week](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/timesheet2.png?itok=qJB009Fe "A summary of time logged for one week")

Each time you filter on a different week number, your pivot table will build a new time sheet that displays the dates that belong to the week. Note that by adding a column for Name to the data, you could track and report time for multiple people. You could also add a rate column to the data and use a pivot table to summarize the cost or billing rate of time logged.

> We also have [video training for Pivot Tables](https://exceljet.net/training/core-pivot)

### User activity in a web portal

Imagine you're given a data dump from a large company's website. The website is a portal that provides product information to partners. Partners sign up on an ongoing basis throughout the year, and the portal has been running for a long time. You open up the data and take a look. Yikes. There are more than 30,000 users in there! The data looks something like this:

![Raw server data showing user account details](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/user_activity0.png?itok=X9Mv9fgm "Raw server data showing user account details")  
_Lots of user data. Emails are fictitious, of course!_

Your boss wants to know some basic information: how many users are currently active? How many users are being created each month? What partners have the most user accounts, and so on? Also, she's meeting the CEO at lunch. Can you get that info to her in the next hour? Gulp.

Before you panic and break out heavy-duty functions like COUNTIF, SUMIF, INDEX, and so on, take a deep breath. This kind of data is perfect for pivot tables, which will crunch through it quickly and still leave you time for a cup of coffee. First, active vs. inactive users. This kind of summary is a piece of cake with pivot tables, even with huge data sets:

![A simple summary of all users by status](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/user_activity1.png?itok=KQT6iGLz "A simple summary of all users by status")  
_Interesting. Some users are "suspended". Who knew?_

Next, the top 10 partners by number of active users. This is easily done by using the pivot tables built-in "Top 10" value filter.

![The top 10 partners by number of active users](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/user_activity2.png?itok=bRIHYxUi "The top 10 partners by number of active users")

And finally, by grouping user creation dates by year and month, you can easily show the complete history of user creation:

![The number of users created by year and month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/user_activity3.png?itok=H3xYFxy7 "The number of users created by year and month")  
_There must have been an import back in December 2009_.

### Class list

In this example, you're helping to coordinate sign-ups for a class that's offered on Mondays, Wednesdays, and Fridays. Each day during the sign-up period, you get a set of data that looks like this:

![This data shows which students have registered for which class](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/classlist0.png?itok=-03N4I7B "This data shows which students have registered for which class")  
_Note the data is formatted as a Table; important for updating later_

Your job is to send a simple report to the instructor at the start of each day that shows current registrations. There's not a lot of data here, but if you create the report manually, you'll need to use some combination of filtering, sorting, copying, and pasting, and you'll have to repeat the process each day.

Once again, this is an easy job for a pivot table. Just build a simple pivot table that summarizes by class day:

![A summary of current class registrations](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/classlist1.png?itok=-ep_wu4W "A summary of current class registrations")  
_35 people have registered so far. Only 8 for the Friday class._

By adding names, you can quickly create a full class list.

![Pivot table: Current class registrations with student names](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/classlist2.png?itok=dBFKpjNm "Pivot table: Current class registrations with student names")

By moving the Class field into the column labels area, you can create a report that keeps all students together in alphabetical order.

![Pivot table: Current class registrations all students in alphabetical order](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/classlist3.png?itok=9DCAGK_n "Pivot table: Current class registrations all students in alphabetical order")  
_One Pivot Table quirk is a tendency to want to count everything._

Now that you've got a report layout you like, how do you update the report each day? Simple. Just paste in the latest data, (overwriting the existing data) and refresh the pivot table(s). This should take less than a minute, with no busy work.

See also: [Why should use a table for your Pivot table](https://exceljet.net/videos/why-you-should-use-a-table-for-your-pivot-table)

### Instrument measurements

You've got measurement data from a system that records the temperature, relative humidity, and dew point in a greenhouse every two minutes. The data looks like this:

![Raw data: instrument readings taken every two minutes](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/measurements0.png?itok=usirYi-g "Raw data: instrument readings taken every two minutes")

What you need is a quick breakdown that shows the average reading per hour. Yes, you could create formulas to do this, but it will be a lot of work. By flowing the data through a pivot table, you can simply add each measurement as a value, and change the display to show average instead of sum. This will give you a tidy summary that shows the average of each reading by hour:

![Pivot table: instrument readings averaged by hour](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/measurements1.png?itok=yuac7FqJ "Pivot table: instrument readings averaged by hour")  
_Average readings per hour in less than 5 minutes_

### Email signups

You're working with a client who is tracking email signups on their website. The client is planning a new marketing campaign and wants to know which day of the week is best for signups, based on the data they have so far. The day of the week is a little tricky since it doesn't appear anywhere in the data, but you can easily add it to the data using the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
. Your data now looks like this:

![Raw data: email signups with day of week added with a formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/emailsub0.png?itok=N7xt8pIv "Raw data: email signups with day of week added with a formula")

And the initial summary looks like this:

![Pivot table: email signups by year, month, and day of week](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/emailsub1.png?itok=_rtQBUcm "Pivot table: email signups by year, month, and day of week")  
_Every email sign-up to date in one tidy little pivot table_

Looking at the data, you realize it would be more useful to show the total signups as a percentage rather than an absolute number. By setting the email count to display a percentage of row, the pivot table will show a breakdown by day of the week. In addition, you add conditional formatting to make the higher and lower percentages stand out. Below, we've used green for higher percentages, and blue for lower percentages.

![Pivot table: email signups by year, month, and day of week by percent, w/ conditional formatting](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/emailsub2.png?itok=MYmgrjAx "Pivot table: email signups by year, month, and day of week by percent, w/ conditional formatting")  
_Now it's clear: most sign-ups are on weekdays. Tuesdays and Wednesdays are especially good days._

### Summary

Hopefully, this short tour of "unconventional" Pivot Tables has inspired you to try some new pivot tables on your data. You don't need to have a huge set of data to see the benefit of using a pivot table. Pivot tables will save you time and energy whenever you need to create a report based on data, especially a report you'll need to update again in the future. Here are a few more helpful links and resources:

*   [Pivot table example: Instrument readings](https://exceljet.net/videos/pivot-table-example-instrument-readings)
     (video)
*   [Pivot table example: movie data](https://exceljet.net/videos/pivot-table-example-imdb-movie-data)
     (video)
*   [Pivot table example: voting results](https://exceljet.net/videos/pivot-table-example-voting-results)
     (video)
*   [Core Pivot](https://exceljet.net/training/core-pivot)
     (video course)

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [Pivot Table Tips](https://exceljet.net/articles/pivot-table-tips)
    
*   [Can pivot tables save your job?](https://exceljet.net/articles/can-pivot-tables-save-your-job)
    

### Training

*   [Core Pivot](https://exceljet.net/training/core-pivot)
    

Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!

Thierry

[More Testimonials](https://exceljet.net/feedback)

Get [Training](https://exceljet.net/training)

----------------------------------------------

### Quick, clean, and to the point training

Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.

[View Paid Training & Bundles](https://exceljet.net/training)

[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)

[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)

[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)

[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)

[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)

[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)