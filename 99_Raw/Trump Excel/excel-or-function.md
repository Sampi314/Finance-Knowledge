# Excel OR Function | Formula Examples + FREE Video

**Source:** https://trumpexcel.com/excel-or-function

---

[Skip to content](https://trumpexcel.com/excel-or-function/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-or-function/#below-title)

Excel OR Function (Example + Video)
-----------------------------------

![Excel OR Function](https://trumpexcel.com/wp-content/uploads/2014/03/OR-FORMULA-EXCEL.png)

### When to use Excel OR Function  

Excel OR function can be used when you want to check multiple conditions.

### What it Returns

It returns TRUE if any one of the conditions evaluates to TRUE, else it returns a FALSE.

### Syntax

\=OR(logical1, \[logical2\],…)

### Input Arguments

*   **logical1 –** the first condition that you want to evaluate for TRUE or FALSE.
*   **\[logical2\]** – (Optional) This is the second condition that you want to evaluate for TRUE or FALSE.

### Additional Notes

*   OR function can be used with other formulas to be more efficient.
    *   For example, in an IF Function, you can test a condition and then specify a value when it’s TRUE and a value when it is FALSE. Using OR function within IF enables users to test multiple conditions at one go.
        *   For example, if you have to test whether if A1 is greater than 0 or less than 100, here is how you can do it in an IF function:  
            \=IF(OR(A1>100,A1<0),”Approve”,”Reject”)
*   The arguments must either evaluate to logical values (TRUE/FALSE), or the arguments must be arrays/references of logical values.
*   Text and empty cells are ignored.
*   If the specified range contains no logical values, the OR function returns [#VALUE! error](https://trumpexcel.com/fix-value-error-in-excel/)
    .
*   You can test a maximum of 255 conditions in a single OR function.

Excel OR Function – Examples
----------------------------

Here are five practical examples of using the Excel OR function.

### **Example 1: Using True/False arguments in the OR function.**

![Excel Or Function - Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20422%20170'%3E%3C/svg%3E)

You can use the True/False arguments directly within the Excel OR function. If any of the given arguments is TRUE, the result would be TRUE. If both the arguments are FALSE, it will return FALSE.

Note: Excel OR function can handle TRUE and FALSE within double quotes. For example, if you use =OR(“TRUE”,”FALSE”), it will return TRUE.

### **Example 2: Using Cell References that contain True/False.**

![Excel Or Function - Example 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20568%20159'%3E%3C/svg%3E)

You can use cell references that contain TRUE/FALSE. If any of the cell references contain TRUE, the result would be TRUE.

### **Example 3: Using Conditions within Excel OR Function.**

![Excel Or Function - Example 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20570%20150'%3E%3C/svg%3E)

You can test conditions within the OR function. If any of the conditions is TRUE, the result would be TRUE.

### **Example 4: Using Numbers within Excel OR Function**.

![Excel Or Function - Example 4](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20267'%3E%3C/svg%3E)

You can use numbers within Excel OR function. While 0 is considered FALSE, any number other than 0 is considered as TRUE (be a positive, negative, or decimal number).

### **Example 5: Using Excel OR Function with other functions**.

You can use Excel OR function along with other Excel functions when you need to test for multiple conditions.

Here is an example of using OR function with IF function.

![Excel Or Function - Example 5](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20626%20249'%3E%3C/svg%3E)

In the above example, IF function uses OR function to test multiple conditions. It checks whether A2 is greater than 70 or A3 is greater than 70. If any of the conditions is TRUE, the OR function returns TRUE. The [If function](https://trumpexcel.com/excel-if-function/)
 then returns the argument when the condition is TRUE (which is Pass in the above example).

Excel OR Function – Video Tutorial
----------------------------------

**Related Excel Functions:**

*   [Excel AND Function](https://trumpexcel.com/excel-and-function/)
    .
*   [Excel NOT Function](https://trumpexcel.com/excel-not-function/)
    .
*   [Excel IF Function](https://trumpexcel.com/excel-if-function/)
    .
*   [Excel IFS Function](https://trumpexcel.com/excel-ifs-function/)
    .
*   [Excel IFERROR Function](https://trumpexcel.com/excel-iferror-function/)
    .
*   [Excel FALSE Function](https://trumpexcel.com/excel-false-function/)
    .
*   [Excel TRUE Function](https://trumpexcel.com/excel-true-function/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-or-function/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

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