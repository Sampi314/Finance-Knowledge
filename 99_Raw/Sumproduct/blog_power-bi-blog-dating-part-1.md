# Power BI Blog: Dating Part 1

**Source:** https://sumproduct.com/blog/power-bi-blog-dating-part-1/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Dating Part 1

*   November 10, 2021

Power BI Blog: Dating Part 1
============================

Power BI Blog: Dating Part 1
============================

11 November 2021

_Welcome back to this week’s edition of the Power BI blog series. This week, we look at Auto Date/Time._

A Date Table or Calendar has exactly one row (record) per day for the time period that covers the dataset in the Power BI model. The Date Table allows a date hierarchy to be applied to any table in the model which includes a date.

There are a number of ways of creating a Date Table. There is some inbuilt functionality in Power BI Desktop which will create the date hierarchy for any table that includes a date. This means that we do not have to create a Date Table.

From the File tab, we can access an ‘Options’ menu (through ‘Options and settings’), where, under ‘GLOBAL’ clicking on ‘Data Load’, there is a ‘Time intelligence’ checkbox _(pictured)_. By default, this box will be checked. There is a prompt next to the box to ‘Learn More’ which will take us to the Microsoft help pages.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-110.jpg)

The important part to note from the help pages is this:

The Auto date/time is a data load option in Power BI Desktop. The purpose of this option is to support convenient time intelligence reporting based on date columns loaded into a model. Specifically, it allows report authors using your Data Model to filter, group, and drill down by using calendar time periods (years, quarters, months, and days). What’s important is that you don’t need to explicitly develop these time intelligence capabilities.

When the option is enabled, Power BI Desktop creates a hidden auto date/time table for each date column, providing all of the following conditions are true:

*   The table storage mode is Import
*   The column data type is date or date/time
*   The column isn’t the “many” side of a model relationship.

This may sound like a great idea, saving us work since we don’t need to create anything to get drill down ability on date fields. However, there are disadvantages. If we have one table with a date field, then one hierarchy and a hidden auto date/time table is created for us. If there are a couple of tables, then two hierarchies and two hidden tables are created. However, if we have an accounting model where every table has at least one date, then the convenient time intelligence reporting becomes a large overhead, with lots of hidden tables we can’t get at. There is no way to selectively enable the creation of hidden date / time tables; it is an all or nothing scenario.

There is another drawback to allowing these hidden tables to be created. The hidden tables come with their own hierarchy for year, quarter month and day. This is useful, but it is fixed. If I am creating slicers based upon this hierarchy, I can choose a day, but not a weekday or even a week. Further, the year and quarters assume that the year begins on January 1st and finishes on December 31st. This cannot be customised.

If we decide to turn ‘Time intelligence’ off, we can do so on the ‘Data Load’ tab for the ‘CURRENT FILE’. We also need to turn it off for the ‘GLOBAL’ settings, which will affect any new reports. When changing ‘Time intelligence’ for the ‘CURRENT FILE’ for other existing reports, we should take care in case we have created any visuals which rely on hidden date / time tables. These would need to be fixed using a manually created Date Table. There are a few ways we can do this, which we will explore next time.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-dating-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-dating-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-dating-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-dating-part-1/#0)

[](https://sumproduct.com/blog/power-bi-blog-dating-part-1/#0 "close")

top