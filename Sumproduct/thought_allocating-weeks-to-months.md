# Allocating Weeks to Months

**Source:** https://sumproduct.com/thought/allocating-weeks-to-months/

---

[Home](https://sumproduct.com/)

\> Allocating Weeks to Months

*   May 14, 2025

Allocating Weeks to Months
==========================

How to allocate weekly calculations to the correct reporting month.

Are your Monthly Modelling Skills Week?
=======================================

A common modelling problem is taking weekly outputs and aggregating it with the correct reporting month. What’s the best way to do it? By Liam Bastick, director with SumProduct Pty Ltd.

Query
-----

Due to needing to model cashflow forecasts reasonably accurately, my forecast model summarises sales on a weekly basis. However, these sales have to be allocated to a particular month. What’s the best way to do this?

Advice
------

Many businesses prepare their forecasts on a weekly basis, due to needing to manage their cashflows carefully or take account of five-week rather than four-week months for performance analysis, etc.

There are three common methods of converting weekly outputs to monthly outputs:

1.  **New financial month starts with the week containing the 1st of that month:** In other words, if one of the days in the reporting week contains the first day of a particular month, then that week “belongs” to that month;
2.  **The financial month is determined by which month the majority of the days in that month belong:** For example, if the week commences 28 June, then the week is 28 June to 4 July inclusive, i.e. three days in June and four in July – so this week “belongs” to July as more days in the week are from that month;
3.  **Week is pro-rated between the two months the week straddles:** For weeks that have dates in two months, the output is assumed to accrue evenly over the period, e.g. for the week commencing 28 June three-sevenths of the output would be included in June and four-sevenths would be included in July.

There are other methods used (e.g. retail often works on a 5 / 4 / 4 week quarter), but these methods will require adjustments every now and then as there are not precisely 52 weeks in a year.

Therefore, for the purposes of this article we will only consider the three methods above (examples of which can be found in the [attached Excel file](https://sumproduct.com/assets/user-upload/sp-allocating-weeks-to-months-example.xls)
).

### New financial month starts with the week containing the 1st of that month

This might seem awkward until you actually think through what this means. If the first of the month is in a particular week then the latest date in that month will be the seventh and the earliest will be the first. Given every month contains seven days or more (!), the allocation of weeks to a particular month is simply based on which month the last day of the reporting week resides.  
If we want to have the month end, we cannot simply take any date and add a constant to it, since the numbers of days in months vary. Fortunately, there is a function in Excel that will perform this calculation for us:

EOMONTH(specified\_date,number\_of\_months).

The ‘end of month’ function therefore calculates the end of the month as the **number\_of\_months** after the **specified\_date**. For example:

*   **EOMONTH(31-Jul-15,0)** = 31-Jul-15
*   **EOMONTH(3-Apr-15,2)** = 30-Jun-15
*   **EOMONTH(29-Feb-16,-12)** = 28-Feb-15.

Although the examples use typed in dates, for it to work in Excel, it is best to have the specified\_date either as a cell reference to a date or else use the **DATE** function to ensure that Excel understands it is a date (otherwise the formula may calculate as #VALUE!). For more information on this useful function, please refer to [Asking for a Date](https://www.sumproduct.com/thought/asking-for-a-date)
.

With this borne in mind, the correct month end for any date would be

\=EOMONTH(Final\_Date\_in\_Week,0).

The financial month is determined by which month the majority of the days in that month belong. This is a common approach, but the formula is more awkward. Consider the following example:

![](<Base64-Image-Removed>)

Month Allocation Formula

In the above illustration, cell **J12** determines which month the week reported in cell **J10** should reside using the following formula:

\=EOMONTH(Final\_Date\_in\_Week-3,0).

Minus 3? Regular readers will know I deplore using hard code in a formula, but worse, here, the value ’3? appears a little arbitrary as well.

But it’s not.

If the final day of the week is the first, second or third of the month, then the majority of days in that week will be in the previous month (where there will be a corresponding six, five or four days). From the fourth of the month onwards, the majority of days will be in that month. Therefore, this simple formula works – and believe me, I have seen much more complex versions of this calculation!

For both of these approaches, a simple **SUMIF** calculation will then aggregate the outputs associating them with the correct reporting month, viz.

![](<Base64-Image-Removed>)

Simple SUMIF Calculation

In the above illustration, imagine the time series is for a period of time extending from columns **J to BQ**. Cell **J24** contains the following formula:

\=SUMIF($J$12:$BQ$12,J23,$J$15:$BQ$15).

### Week is pro-rated between the two months the week straddles

The final method is simply pro-rating where a week straddles two months. The example in the attached Excel file uses days of the week as the pro-rata basis, but this could be workdays or hours worked, etc.

Consider the following example.

![](<Base64-Image-Removed>)

Pro-Rata Example

In this example (using the same assumptions as in the earlier example), rows 33 and 34 determine the end of the month where the first day in the week and the last day of the week reside using the formulae

\=EOMONTH(Final\_Date\_in\_Week-Days\_in\_Week+1,0) and  
\=EOMONTH(Final\_Date\_in\_Week,0)

respectively. If these two end dates coincide then the pro-rated percentage for the month is simply 100% (i.e. all dates in the week lie in the same month).

If these two dates differ then a calculation needs to be performed. For example, the formula in cell **J38** is:

\=IF(J34<>J33,DAY(J31)/Days\_in\_Week,),

i.e. for the final date in the week, the day of the month divided by seven is the pro-rated percentage that will occur in the later month end.

The final date of the week for a “straddling” date can only be one, two, three, four, five or six, so this simple formula readily works. The percentage in row 37 is then simply 100% less this percentage calculated.

To aggregate monthly, we simply use the **SUMPRODUCT** function, which has been discussed previously.

To recap, at first glance, **SUMPRODUCT(vector1,vector2,…)** appears quite humble. Before showing an example, though, look at the syntax carefully:

*   A **vector** for Excel purposes is a collection of cells either one column wide or one row deep. For example, **A1:A5** is a column vector, **A1:E1** is a row vector, cell **A1** is a unit vector and the range **A1:E5** is not a vector (it is actually an array, but more on that later). The ranges must be contiguous; and
*   This basis functionality uses the comma delimiter (,) to separate the arguments (vectors). Unlike most Excel functions, it is possible to use other delimiters, but this will be revisited shortly below.

Consider the following sales report:

![](<Base64-Image-Removed>)

Example Sales Report

The sales in column **H** are simply the product of columns **F** and **G**, e.g. the formula in cell **H12** is simply **\=F12\*G12**. Then, to calculate the entire amount cell **H23** sums column **H**. This could all be performed much quicker using the following formula:

\=SUMPRODUCT(F12:F21,G12:G21),

i.e. **SUMPRODUCT** does exactly what it says on the tin: it sums the individual products.

In the context of the example above, the monthly output may be summarised as follows:

![](<Base64-Image-Removed>)

Pro-Rate using SUMPRODUCT

For example, the formula in cell **J46** is

\=SUMPRODUCT(($J$33:$BQ$33=J$45)\*$J$37:$BQ$37\*$J$40:$BQ$40)  
+SUMPRODUCT(($J$34:$BQ$34=J$45)\*$J$38:$BQ$38\*$J$40:$BQ$40),

where the two rows of pro-rata percentages are cross-multiplied with the outputs if the month is the month under review (in this example, April 2015).

### Word to the Wise

There are other methods as I mentioned above, but the three bases mentioned are by far the most common. No method is perfect though:

*   Allocating full weeks to a month will mean some months are 25% greater than others (i.e. five-week rather than four-week), which can mean forecasting and performance KPIs may need to be manipulated; and
*   Pro-rating may overcome this issue, but assumes that outputs accrue evenly over each week, which is not always the norm. In this case, this technique may be modified to ensure greater accuracy – but users may be confused by the ensuing model complexity.

The key point is to ensure forecasts are calculated on a consistent basis.

If you have a query for this section, please feel free to drop Liam a line at [liam.bastick@sumproduct.com](mailto:liam.bastick@sumproduct.com)
 or visit the website [www.sumproduct.com](https://www.sumproduct.com/)

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/allocating-weeks-to-months/#0)
    
*   [Register](https://sumproduct.com/thought/allocating-weeks-to-months/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/allocating-weeks-to-months/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/allocating-weeks-to-months/#0)

[](https://sumproduct.com/thought/allocating-weeks-to-months/#0 "close")

top