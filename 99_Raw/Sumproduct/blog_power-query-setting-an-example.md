# Power Query: Setting an Example

**Source:** https://sumproduct.com/blog/power-query-setting-an-example/

---

[Home](https://sumproduct.com/)

\> Power Query: Setting an Example

*   September 26, 2017

Power Query: Setting an Example
===============================

Power Query: Setting an Example
===============================

27 September 2017

_Welcome to our Power Query blog. This week, I look at what I can do with the ‘Column from Examples’ feature._

The new feature ‘Column from Examples’ essentially pulls together a number of Power Query functions into one place, so it’s very user friendly. It’s ideal if I have an idea of what I want to do in my new column, but I’d like to try a few things.

In the Query Editor, the ‘Column from Examples’ can be found in the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

I have the option of ‘From All Columns’, which allows me to create my column by using data from any of my columns or I can use ‘From Selection’, which will only allow my new column to transform data from the columns that I have selected. I want to have a look at what I can do with this feature, so I opt for ‘From All Columns’:

![](<Base64-Image-Removed>)

I am presented with a new empty column, which I can type into. I try combining columns of different types to see what happens. I type the following:

**195 8×3 metre marquee**

This effectively combines my **_Amount_** (a currency amount) with my **_Description_** (a text field). The instruction in the pane above my query tells me to type **CTRL + ENTER** to enter my value, but I find that **ENTER** works too.

![](<Base64-Image-Removed>)

Not only has Power Query recognised what I am trying to do, it has filled in the rest of the values in my column so that I can check. It’s like Flash Fill (Excel 2013 onwards) but with formulae! The new column has now been given the name **_Merged_**, and the **M** code behind the transformation is displayed in the pane above my query.

**Text.Combine({Text.From\[Amount\] “en-GB”), ” “, \[Description\]})**

This is a satisfying result. I can choose to accept the values and move on or I can go back and type something else into the first row of my column.

![](<Base64-Image-Removed>)

Power Query tries to make sense of what I am entering as soon as I start typing. ’20’ is likely to be a date, so various date functions are suggested. I find that I am able to type data in up to three rows before Power Query either follows the pattern of what I am doing or issues a message telling me that the transformation is not recognised (and to start again).

The transformations available are listed on the Microsoft help pages for the ‘Column from Examples’ description:

**Number transformations**

*   Average
*   Count distinct values
*   Count values
*   Minimum
*   Maximum
*   Median
*   Percent of
*   Power

**Text transformations**

*   Text.Combine (supports combination of literal strings and entire column values)
*   Text.Replace
*   Text.Start
*   Text.Middle
*   Text.End
*   Text.BeforeDelimiter
*   Text.AfterDelimiter
*   Text.BetweenDelimiters

**Date transformations**

*   Date.Day
*   Date.DayOfWeek
*   Date.DayOfWeekName
*   Date.DayOfYear
*   Date.Month
*   Date.MonthName
*   Date.QuarterOfYear
*   Date.WeekOfMonth
*   Date.WeekOfYear
*   Date.Year
*   Date > Age
*   Date > Year > Start of Year
*   Date > Year > End of Year
*   Date > Month > Start of Month
*   Date > Month > End of Month
*   Date > Quarter > Start of Quarter
*   Date > Month > Days in Month
*   Date > Quarter > End of Quarter
*   Date > Week > Start of Week
*   Date > Week > End of Week
*   Date > Day > Day of Month
*   Date > Day > Start of Day
*   Date > Day > End of Day

**Time transformations**

*   Time.Hour
*   Time.Minute
*   Time.Second

**Date/Time transformations**

*   Subtract days
*   Combine Date and Time
*   Earliest
*   Latest
*   Subtract time

This is a substantial list for now, but I will be hoping for more transformations to be added soon!

Back in my query, I decide to go ahead and create a **_Merge_** column which combines my **Amount** and my **_Description_** columns. I click ‘OK’ in the pane above my query, and my new column appears in the query. The transformation step is added as ‘Inserted Merged Column’:

![](<Base64-Image-Removed>)

I think one of the main benefits of this feature is that it allows access to a lot of **M** code functions without me needing to understand **M** code or needing to know where all the separate functions are on the Ribbon. I look forward to seeing more functions added to this facility in due course.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-setting-an-example/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-setting-an-example/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-setting-an-example/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-setting-an-example/#0)

[](https://sumproduct.com/blog/power-query-setting-an-example/#0 "close")

top