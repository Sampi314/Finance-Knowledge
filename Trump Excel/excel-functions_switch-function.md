# SWITCH Function in Excel - Easy Examples

**Source:** https://trumpexcel.com/excel-functions/switch-function

---

[Skip to content](https://trumpexcel.com/excel-functions/switch-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-functions/switch-function/#below-title)

SWITCH is a new Excel function that evaluates an expression (which returns a value) and matches this value with a list of values to return the corresponding result from the first matching value.

You will find the SWITCH function easier to use compared to using nested IF functions (that can quickly get complicated as the number of criteria increases).

In this article, I will tell you everything you need to know about the SWITCH function in Excel, show you a couple of examples that will give you an idea of how you can use it in practical situations, and also cover some of the shortcomings of this function.

Let’s get to it then.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-functions/switch-function/#)

SYNTAX of SWITCH Function in Excel
----------------------------------

Below is the syntax of the SWITCH function in Excel:

SWITCH(expression, value1, result1, \[default or c, result2\],…\[default or value3, result3\])

Where:

*   **_expression_**: This is the value that would be compared against _Value 1, Value 2, Value 3… Value 126_. This could be a number, date, or text, and could also be a result of a formula.
*   **_value1, value2…value126_**: These are the values against which the expression is compared.
*   **_result1, **_result_**2…**_result_**126_**: This is the result that you get when the expression matches the corresponding value
*   _**default**_ (Optional) – In case the SWITCH function doesn’t find any matching value, it will give you the default value. The default value needs to be the last argument in the function and should not have any corresponding result expression.

Note that the SWITCH function can take up to 254 arguments, Which comes out to be 126 pairs of _value_ and _result_ combinations.

If you’re feeling a bit lost so far, don’t worry.

Let me explain how the SWITCH function works with very simple examples.

Example 1 – Return Status Based on Numeric Code
-----------------------------------------------

Below, I have a data set with different database names in column A and their current status codes in column B. I want to return descriptive text that tells me what each code means.

![Data set for the switch function example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20468%20299'%3E%3C/svg%3E)

This can be done using the below formula where I have specified within the SWITCH formula itself what each code means:

\=SWITCH(B2:B8, 1, "Operational", 2, "Maintenance", 3, "Idle", 4, "Down", "Status Unknown")

Enter this formula in cell C2, and It will spill and cover the entire column with the result.

![SWITCH formula to get codes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20349'%3E%3C/svg%3E)

The above SWITCH formula takes the value in cell B2 as the first argument and then compares that value with all the value arguments provided in the formula.

When it finds a match, it returns the corresponding result value. I’ve also provided the default argument “_Status Unknown_“, so when none of the values match, it returns this as the result.

Note that you can also achieve the same result by using the IF or the [IFS function](https://trumpexcel.com/excel-ifs-function/)
. So, while the SWITCH function is not completely unique and does something that no other function can do in Excel, it is definitely better than using multiple nested IF functions.

Example 2 – Analyze Date Using SWITCH Function
----------------------------------------------

Here is another simple example of the SWITCH function.

Below, I have dates in column A, and I want to find out whether it’s a Weekday or a Weekend in column B.

![Date dataset for the SWITCH function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20433'%3E%3C/svg%3E)

Here is the SWITCH formula I will do this for me:

\=SWITCH(WEEKDAY(A2:A14,2),6,"Weekend",7,"Weekend","Weekday")

![SWITCH function to get weekday or weekend](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20745%20517'%3E%3C/svg%3E)

The above formula uses the WEEKDAY(A2:A14,2) formula as the first argument, and the value of this formula will be compared with different values in the SWITCH formula, and the corresponding result will be returned.

So if the [WEEKDAY formula](https://trumpexcel.com/excel-weekday-function/)
 returns 6 or 7, the SWITCH formula returns _Weekend_; otherwise, it returns the default value, which is _Weekday_.

If you are curious, you can also do this using the following IFS function:

\=IFS(WEEKDAY(A2,2)>5,"Weekend",WEEKDAY(A2,2)<=5,"Weekday")

As you will notice, both the SWITCH function and the IFS function are similar in terms of complexity, and you can use any of the two based on your preference.

Personally, I gravitate more towards the IFS function because I’ve already been using the [IF function](https://trumpexcel.com/excel-if-function/)
 for a long time, and the syntax of IF and IFS are quite similar.

Also read: [Excel Functions List with Examples](https://trumpexcel.com/excel-functions/)

Example 3 – SWITCH Function with TRUE as First Argument (Smart Trick)
---------------------------------------------------------------------

One limitation of the SWITCH function is that it can only perform an exact match.

So, whatever value is returned by the expression (the first argument of the SWITCH function), it will try to find that exact value in the following value arguments and return the corresponding result argument if it finds it.

Let me show you a smart workaround.

Below, I have student names in column A and their scores in column B. I want to get their grades in column C (where the grading criteria are mentioned in a separate table on the right

![Students dataset for SWITCH function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20435'%3E%3C/svg%3E)

While this can easily be done using the IFS function (which can handle multiple criteria), you can also do this using the below SWITCH function:

\=SWITCH(TRUE,B2>=90,"A",B2>=80,"B",B2>=60,"C",B2>=50,"D",B2>=30,"E","F")

Enter this formula in cell C2 and then copy it for all the other cells.

![SWITCH formula to get students grade](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20803%20520'%3E%3C/svg%3E)

Note that in the above formula, I’ve used TRUE as the first argument, and instead of the regular values arguments, I have used expressions that evaluate to TRUE or FALSE.

So, the above function looks for any value argument that returns a true value and then gives us the corresponding result value.

For example, if the score is 77, the ‘B2>=60’ part of the formula would return TRUE, and we will get C as a result.

Also, remember that as soon as the function finds the first TRUE value, it returns the corresponding result and then stops.

In our example, if the score is more than 90, it is going to satisfy all the specified conditions in the formula, but since it is met with the TRUE in the very beginning itself, it returns A, and the formula stops.

So, if you’re working with a situation where you need to evaluate multiple conditions, you can use this SWITCH function hack, where you can use a TRUE or a FALSE as the first argument.

_Note: Another easy way to do this is by using approximate match in VLOOKUP function. I cover how to do this [here](https://trumpexcel.com/avoid-nested-if-function-vlookup/)
._

SWITCH Function vs IFS Function
-------------------------------

_Both SWITCH and IFS functions are available in Excel 2019, 2021, and Excel with Microsoft 365._

While I’ve already mentioned that the SWITCH function is better than using the IF function when you have multiple conditions, how does it compare against the IFS function?

One major difference between these two functions is that with the SWITCH function, you need to specify the expression only once, but with its function, you need to repeat the expression as many times as you want to check it.

In almost all cases, I have seen that these functions can be used interchangeably and are often of a similar complexity. So you can choose which one to use based on your preference.

Below is a table that gives you a detailed comparison of the two functions:

| Feature | SWITCH Function | IFS Function |
| --- | --- | --- |
| **Purpose** | Evaluates one expression against a list of values and returns the corresponding result | Evaluates multiple conditions and returns the corresponding result |
| **Primary Use Case** | Simplifies the evaluation of a single expression against multiple possible values | Simplifies the evaluation of multiple logical conditions |
| **Default Result** | Yes, an optional default value can be provided as the last argument | No, but you can simulate a default by adding _TRUE, default\_result_, at the end |
| **Error Handling** | If no match is found and no default is provided, it returns #N/A error | If no condition is met and _TRUE, default\_result_ is not provided, returns #N/A error |
| **Nesting Limitations** | Simplifies nested IFs where multiple comparisons are made against the same expression | Simplifies nested IFs where multiple different conditions need to be checked |
| **Excel Version Availability** | Available in Excel 2019, 2021, and Excel 365 | Available in Excel 2019, 2021, and Excel 365 |

I hope this article has helped you understand how to best use the SWITCH function in Excel.

If you have any questions or suggestions for me, please let me know in the comments section.

**Other Excel articles you may also like:**

*   [SUM Based on Partial Text Match in Excel (SUMIF)](https://trumpexcel.com/sum-partial-match/)
    
*   [INDEX & MATCH Functions Combo in Excel](https://trumpexcel.com/index-match/)
    
*   [Excel IFERROR Function](https://trumpexcel.com/excel-iferror-function/)
    
*   [Using Excel AVERAGEIFS function](https://trumpexcel.com/excel-averageifs-function/)
    
*   [Using Excel COUNTIFS Function](https://trumpexcel.com/excel-countifs-function/)
    
*   [20 Advanced Excel Functions and Formulas (for Excel Pros)](https://trumpexcel.com/advanced-excel-functions-formulas/)
    
*   [TAKE Function in Excel](https://trumpexcel.com/excel-functions/take-function/)
    
*   [DROP Function in Excel](https://trumpexcel.com/excel-functions/drop-function/)
    
*   [LET Function in Excel](https://trumpexcel.com/excel-functions/let-function/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK