# Power BI Blog: Improved DAX Time Intelligence

**Source:** https://sumproduct.com/blog/power-bi-blog-improved-dax-time-intelligence/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Improved DAX Time Intelligence

*   October 9, 2025

Power BI Blog: Improved DAX Time Intelligence
=============================================

_Welcome back to this week’s edition of the Power BI blog series._  _This week, we look at the improvements to **DAX** time intelligence (currently in Preview only)._

A brand new, calendar-based approach to time intelligence in Power BI has finally arrived.  With this update, you can now define custom calendars, such as fiscal years or 4-5-4 retail calendars, directly in your data model.  This gives you precise control over how your data maps over time, enabling more accurate and flexible analysis.  It also allows you to do week-based calculations.

For example, here is how to use calendars to perform a total month-to-date calculation on a Gregorian calendar:

*   To get started, simply turn on the ‘Enhanced DAX Time Intelligence’ feature in the Preview settings
*   Select ‘Calendar options’ from the context menu on your date table

![](<Base64-Image-Removed>)

*   Create a calendar by associating columns in your date table into categories.  For example, the Gregorian Calendar below maps the Year, Quarter, Month, Month of Year and Date categories to primary and associated columns (columns can be named as desired)

![](<Base64-Image-Removed>)

*   Perform calculations based upon your calendar.  For example, if you have a calendar called ‘**Gregorian Calendar**’ defined in your model, you can use **TOTALMTD** to calculate a month-to-date total sales value based on that, _viz._  
      
    **Sales MTD = TOTALMTD(\[Total Sales\], ‘Gregorian Calendar’)**  
      
    In addition to expanding existing functions with support for calendars, Microsoft has also added several new functions that allow you to do week-based calculations as well, such as T**OTALWTD**, **PREVIOUSWEEK**, and more
*   You may show your result in a visual.  For example, this chart shows the **Total Sales** and **Sales MTD** value calculated previously:

  

![](<Base64-Image-Removed>)

Many calendars, particularly fiscal calendars, are shifted Gregorian calendars, in which the year does not being on January 1st, but for example on July 1st.  May Australian companies use such a shifted fiscal calendar.

In this instance, a date table would include columns for the fiscal periods, such as fiscal year, fiscal quarter and fiscal month:

![](<Base64-Image-Removed>)

Now, you can define a Fiscal Calendar:

![](<Base64-Image-Removed>)

You can use the calendar in the calculations.  For example, the following calculates the **SAMEPERIODLASTYEAR** value using the Fiscal Calendar:

> **Sales Same Period Last Fiscal Year = CALCULATE(\[Total Sales\],SAMEPERIODLASTYEAR(‘Fiscal Calendar’))**

This can then be visualised as follows:

![](<Base64-Image-Removed>)

As already mentioned, you can now also perform week-based calculations, including 4-5-4 and other patterns.  After making sure your data table contains week information, associate the relevant categories in your calendar as done below for a 4-5-4 calendar:

![](<Base64-Image-Removed>)

Next, create your **DAX** calculation.  For example, a week-to-date calculation can be made using **TOTALWTD**:

> **Sales WTD 454 = TOTALWTD(\[Total Sales\],’RETAIL-454′)**

The column chart shows the actual and the week-to-date sales value based on the RETAIL-454 calendar.

![](<Base64-Image-Removed>)

This just touches the tip of the iceberg.  There is much more to learn about this feature – why not start playing!

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/training)
.  If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
 . 

*   [Log in](https://sumproduct.com/blog/power-bi-blog-improved-dax-time-intelligence/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-improved-dax-time-intelligence/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-improved-dax-time-intelligence/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-improved-dax-time-intelligence/#0)

[](https://sumproduct.com/blog/power-bi-blog-improved-dax-time-intelligence/#0 "close")

top