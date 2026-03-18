# Find Month

**Source:** https://edbodmer.com/find-month

---

In this web page I illustrate a key problem with timing in project finance models.  The problem comes about from including flexible monthly seasonality in models that are typically semi-annual or quarterly.  The programming in this page has been completed my friend Mike Flynn who is a much better programmer than me (see the footnote on Mike below). For renewable generation resources, there is seasonality in production (volumes). Whether a wind or solar project, there is a resource assessment that generally provides a monthly resource factor, or a monthly resource factor can be derived from the assessment.  The amount of production is different for different months — for example a solar project in the northern hemisphere will produce more in the summer months.  But because of the financing structure, the model should be semi-annual and generally not monthly. The objective is to accurately calculate how much production (volume) each model period contains given this monthly resource factor for each semi-annual or quarterly period.  Say your model period is from April to September and you have the seasonal factor for July, then you simply want a flag in July.  This would be really easy if the periods at the top were in monthly order — from example January to June. 

If a model had a monthly periodicity for the entire model timeline, then there would be no issue matching the monthly production with the model month to calculate volumes in a model. The below demonstrates the 1 to 1 match (green cells) that matches the Months in Period (1) to the seasonal production factor (also 1 Month).

![](https://edbodmer.com/wp-content/uploads/2020/08/image-2.png)

But if the dates straddle a year, then the programming is tricky.  The tests are more complex and the programming in excel is very painful.  Mike was very generous and gave me a file that I told him I could share.  This file is attached to the button below.  Mike demonstrates a key point that this type of program works much faster when you use an array function. I explain this below.

**[File that Contains User Defined Functions with Alternative Methods for Deriving Monthly Factors in Semi-Annual Model](https://edbodmer.com/wp-content/uploads/2020/08/FindMonthFunction-2.xlsm)
**

If a model had a monthly periodicity for the entire model timeline, then there would be no issue matching the monthly production with the model month to calculate volumes in a model. The below demonstrates the 1 to 1 match (green cells) that matches the Months in Period (1) to the seasonal production factor (also 1 Month).

I began with a messy program that worked.  But Mike has demonstrated a much more efficient and elegant programming.  I have wrote a little bit about Mike at the bottom of this page. The screenshot is illustrated on the screenshot below.  At the top of the page it is typical to have a start of period date and an end of period date. You want a simple flag the puts an interval in the sheet that depends on whether the date at the left is part of the series or not.  Mote how the flag is marked differently for the monthly and the semi-annual period.  Note also that green area is partially at the top at the beginning of the period and part green at the bottom after the periodicity becomes semi-annual.  Mike has fixed my UDF for doing this.

Note, the approach to calculating volumes is a two-step calculation. The first step is to test (or flag) whether a seasonal production month falls between the start date and end date of a period. This test is performed using a simple true/false test or like in the above using the binary numeral system, which uses 1 as True and 0 as False. The second step is to then apply the actual production factor to the true/false test. The below screenshot depicts the two-steps or parts of the calculation.

![](https://edbodmer.com/wp-content/uploads/2020/08/image-3.png)

The reminder of this explanation will focus on Step 1, the dates test, as this creates the headaches. The problem is that models have changing periodicity. Some go from monthly to quarterly or monthly to semi-annually, or quarterly to semiannually or any other combination. When models have any other periodicity besides monthly (or annual), then it is not going to have the same volumes in one quarter from another quarter or one semiannual period from another. The problem is exacerbated when a model period’s dates (start and end date) straddles a year. If there was no straddling, then the following simple logic would suffice: “If the month of the starting date of the period is less than or equal to the month of the monthly resource factor (“TestMonth”) and the month of the ending date of the period is greater than or equal to the test month (“If Month(Start Date) <= Test Month And Month(End Date) >= Test Month”).” This logic test would work for the below.

![](https://edbodmer.com/wp-content/uploads/2020/08/image-4.png)

![](https://edbodmer.com/wp-content/uploads/2020/07/image-53.png)

You can copy the function that does this at the bottom of the page. You can also find this function in the in the file that is attached to the button above.

![](https://edbodmer.com/wp-content/uploads/2020/08/image-5.png)

The next screenshot illustrates the use of an array function.

Limiting a model’s periodicity to disallow for straddling of calendar years would create serious inflexibility in the model timing assumptions inputs.

The Solution

It is possible to solve this problem using very long, inefficient formulas for each cell in excel. A more efficient approach is to use a User Defined Function that utilizes a multi-dimensional array approach.  The full function solution can be found below:

![](https://edbodmer.com/wp-content/uploads/2020/08/image-6.png)

Line 57 is the same simple logic test as before, except it is not using just the month of the starting and ending period dates for the test, but rather the full dates (year, month, and day). The Starting Date and Ending Date of a period are static inputs to the test. The input that is revised based on additional tests is the TestMonth, which ultimately is modified to “RevisedTest.” More specifically, the day and month of the TestMonth are static inputs, and only the year is modified based on additional tests. This is the key to calendar year straddling, knowing which year to apply to the RevisedTest date. Using the above example if the Start Date is 9/1/2020 and the End Date is 2/28/2021, knowing which year – 2020 or 2021 – to apply to the Test Month of say December is the key to the test.  December 2020 would be within the model period, while December 2021 would not.

Line 32 tests to see if the model period is a straddle period. It tests for straddling by testing to see if the month of the period end date is less than the month of the period start date. If there is no straddle, then the year applied to the “RevisedTestYrInput” is the year of the end date (Line 52), although it makes no difference if used the year of the start date as both periods are in the same calendar year. Note this assumes the model periodicity can not be greater than annual. If the straddle test is True, then it becomes a bit difficult. Before diving into the actual code in Lines 33-50, it is important to understand the strategy before any code is written. The strategy is to keep it as simple as possible. Ultimately, we need another test, we need to know if the TestMonth’s year should be in the year of the starting period or the year of the ending period. The approach taken here is to create a positive or negative test (Line 41). One testing solution is to test the Cumulative total (line 38) of Current Less Prior (line 37). This enables the ability to create a two value (positive or negative) test.

![](https://edbodmer.com/wp-content/uploads/2020/08/image-7.png)

There are a few methods to overcome this looping hurdle; however, one of the more efficient methods is to use the Mod (Modulo) operator. The Mod operator returns the remainder when there is a dividend divided by a divisor; the quotient is irrelevant.  No matter what the dividend, the remainder will not be more than one less the dividend. For each incremental increase of the dividend, the remainder increases, until it reaches one less than the dividend and then the sequence repeats (see below example).

Since a model period being tested, can be monthly, quarterly, semiannual, or annual, or any other periodicity less than or equal to 12 months (annual upper periodicity limit), then this test needs to loop through the months of the year. Thus, a 12-iteration loop is used (line 33). For each model period, the test needs to be applied for each TestMonth (each month under “Seasonal Resource Production” below).  Thus, for Period 11 below, each seasonal resource month is tested, each month that falls within the start and end periods for period 11, results in a True or 1 result, while all others result in a False or 0 result.

![](https://edbodmer.com/wp-content/uploads/2020/07/image-54.png)

This webpage demonstrates how to use and create a function for finding if a month is between two dates.  Finding a month would be easy if the month of the start date was earlier than the month of the end date.  But sometimes if you have a semi-annual model or a quarterly model the start of the month could be something like October while the end of the month could be something like March.  Then if the month is February, that month is between the start date and the end date.  I am sure you can do this with a long formula or several formulas.  But I run into this quite often and I have made a UDF to solve it.  The UDF produces a TRUE or FALSE flag that is illustrated in the screenshot below.

\[pdf-embedder url=https://edbodmer.com/wp-content/uploads/2020/08/Corporate-Modeling-with-MA-May-.2-2018.pdf\]

You can copy the UDF into your model using the code below.

https://edbodmer.com/wp-content/uploads/2020/08/Corporate-Modeling-with-MA-May-.2-2018.pdf

.

Function find\_month(Start\_Date, End\_Date, Test\_Month)

' Set the find month to false to start

find\_month = False

'' When the month of the start date is less than the month of the 

If Month(Start\_Date) <= Month(Start\_Date) Then
      If Month(Start\_Date) <= Test\_Month And Month(End\_Date) >= Test\_Month Then
           find\_month = True
      End If
End If

' Problem is when the start date is after month 6 in semi-annual

If Month(Start\_Date) >= 6 And Month(Start\_Date) > Month(End\_Date) Then

' Example of feb 2 and Nov (11) to April (4)

       If Test\_Month <= 6 And Test\_Month <= Month(End\_Date) Then
           find\_month = True
       End If

      If Test\_Month >= 6 And Test\_Month >= Month(Start\_Date) Then
          find\_month = True
      End If
End If


End Function

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=9924&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11408&rand=0.7975521661122167)