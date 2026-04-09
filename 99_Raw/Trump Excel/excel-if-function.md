# Excel IF Function | Formula Examples + FREE Video

**Source:** https://trumpexcel.com/excel-if-function

---

[Skip to content](https://trumpexcel.com/excel-if-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-if-function/#below-title)

Excel IF Function – Introduction
--------------------------------

![Excel IF Function](https://trumpexcel.com/wp-content/uploads/2014/03/IF-FORMULA-EXCEL.png)

### When to use Excel IF Function

IF function in Excel is best suited for situations where you check whether a condition is TRUE or FALSE. If it’s TRUE, the function returns a specified value/reference, and if not then it returns another specified value/reference.

### What it Returns

It returns whatever value you specify for the TRUE or FALSE condition.

### Syntax

\=IF(logical\_test, \[value\_if\_true\], \[value\_if\_false\])

### Input Arguments

*   **logical\_test –** this is the condition that you want to test. It could be a logical expression that can evaluate to TRUE or FALSE. This can either be a cell reference, a result of some other formula, or can be manually entered.
*   **\[value\_if\_true\]** – (Optional) This is the value that is returned when the logical\_test evaluates to TRUE.
*   **\[value\_if\_false\]** – (Optional) This is the value that is returned when the logical\_test evaluates to FALSE.

### Important Notes About using IF Function in Excel

*   A maximum of 64 nested IF conditions can be tested in the formula.
*   If any of the argument is an array, each element of the array is evaluated.
*   If you omit the FALSE argument (_value\_if\_false_), i.e., there is only a comma after the  _value\_if\_true_ argument, the function would return a 0 when the condition is FALSE.
    *   For example, in the example below, the formula is =IF(A1>20,”Approve”,), where the _value\_if\_false_ is not specified, however, the _value\_if\_true_ argument is still followed by a comma. This would return 0 whenever the checked condition is not met.![Excel If Function - When False is ommitted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20175'%3E%3C/svg%3E)
*   If you omit the TRUE argument (_value\_if\_true_), and specify only the _value\_if\_false argument_, the function would return a 0 when the condition is TRUE.
    *   For example, in the example below, the formula is =IF(A1>20,,”Approve”), where the _value\_if\_true_ is not specified (only a comma is used to then specify the _value\_if\_false value_). This would return 0 whenever the checked condition is met.![Excel If Function - When TRUE is ommitted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20462%20150'%3E%3C/svg%3E)

Excel IF Function – Examples
----------------------------

Here are five practical examples of using the IF function in Excel.

### **Example 1: Using Excel IF function to Check a Simple Numeric Condition**

When using Excel IF function with numbers, you can use a variety of operators to check a condition. Here is a list of operators you can use:

![Excel If Function - Operators](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20367%20192'%3E%3C/svg%3E)

Below is a simple example where students marks are checked. If the marks are more than or equal to 35, the function returns Pass, else it returns Fail.

![Excel If Function - pass fail](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20509%20280'%3E%3C/svg%3E)

### **Example 2: Using Nested IF to Check a Sequence of Conditions**

Excel IF Function can take up to 64 conditions at once. While it’s inadvisable to create long Nested IF functions, in the case of limited conditions, you can create a formula that checks conditions in a sequence.

In the example below, we check for two conditions.

*   The first condition checks whether the marks are less than 35. If this is TRUE it returns Fail.
*   In case the first condition is FALSE, which means that the student scored above or equal to 35, it checks for another condition. It checks if the marks are greater than or equal to 75. If this is true, it returns Distinction, else it simply returns Pass.

![Excel If Function - Nested](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20646%20264'%3E%3C/svg%3E)

### **Example 3: Calculating Commissions Using Excel IF Function**

Excel If Function allows you to perform calculations in the value section. A good example of this is calculating the sales commission for sales rep using the IF function.

In the example below, a sales rep gets no commission if the sales are less than 50K, gets a 2% commission if the sales are between 50-100K and 4% commission if the sales are more than 100K.

Here is the formula used:

\=IF(B2<50,0,If(B2<100,B2\*2%,B2\*4%))

![Excel If Function - Commission](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20602%20252'%3E%3C/svg%3E)

In the formula used in the example above, the calculation is done within the IF function itself. When the sales value is between 50-100K, it returns B2\*2%, which is the 2% commission based on the sales value.

### **Example 4: Using Logical Operators (AND/OR) in Excel IF Function**

You can use logical operators (AND/OR) within the IF function to test multiple conditions at once.

For example, suppose you’ve to select students for the scholarship based on marks and attendance. In the example shown below, a student is eligible only if he scores more than 80 and has the attendance of more than 80%.

![using-excel-if-function-and-operator-data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20411%20310'%3E%3C/svg%3E)

You can use the AND function within the IF function to first check whether both these conditions are met or not. If the conditions are met, the function returns Eligible, else it returns Not Eligible.

Here is the formula that will do this:

\=IF(AND(B2>80,C2>80%),”Yes”,”No”)

![using-excel-if-function-and-operator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20505%20345'%3E%3C/svg%3E)

### **Example 5: Converting all Errors to Zero using Excel IF function**

Excel IF function can also be used to get rid of cells that contain errors. You can convert the error values to blanks or zeros or any other value.

Here is the formula that will do it:

\=IF([ISERROR](https://trumpexcel.com/excel-is-function/)
(A1),0,A1)

The formula returns a 0 when there is an error value, else it returns the value in the cell.

_NOTE: If you’re using Excel 2007 or versions after it, you can also use the [IFERROR function](https://trumpexcel.com/excel-iferror-function/)
 to do this._ 

Similarly, you can also handle blank cells. In case of blank cells, use the ISBLANK function as shown below:

\=IF(ISBLANK(A1),0,A1)

![Excel If Function - isblank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20477%20235'%3E%3C/svg%3E)

Excel IF Function – Video Tutorial
----------------------------------

**Related Excel Functions:**

*   [Excel AND Function](https://trumpexcel.com/excel-and-function/)
    .
*   [Excel OR Function](https://trumpexcel.com/excel-or-function/)
    .
*   [Excel NOT Function](https://trumpexcel.com/excel-not-function/)
    .
*   [Excel IFS Function](https://trumpexcel.com/excel-ifs-function/)
    .
*   [SWITCH Function in Excel](https://trumpexcel.com/excel-functions/switch-function/)
    
*   [Excel IFERROR Function](https://trumpexcel.com/excel-iferror-function/)
    .
*   [Excel FALSE Function](https://trumpexcel.com/excel-false-function/)
    .
*   [Excel TRUE Function](https://trumpexcel.com/excel-true-function/)
    

**Other Excel tutorials you may find useful:**

*   [Avoid Nested IF Function in Excel by using VLOOKUP](https://trumpexcel.com/avoid-nested-if-function-vlookup/)
    
*   [Calculate MEDIAN IF in Excel](https://trumpexcel.com/median-if-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

6 thoughts on “Excel IF Function | Formula Examples + FREE Video”
-----------------------------------------------------------------

1.  Hi, i have required different amount with find out percentage  
    as like below – Required amount against percentage only one columns
    
    800000 0.05%  
    900000 0.09%  
    1000000 0.12%  
    1200000 0.14%  
    1400000 0.15%  
    1600000 0.17%  
    1800000 0.18%  
    2000000 0.19%  
    2200000 0.21%  
    2400000 0.23%  
    2600000 0.24%  
    2800000 0.25%  
    3000000 0.27%
    
    please suggest me.
    
    [Reply](https://trumpexcel.com/excel-if-function/#comment-13552)
    
2.  really good
    
    [Reply](https://trumpexcel.com/excel-if-function/#comment-13372)
    
3.  Nice
    
    [Reply](https://trumpexcel.com/excel-if-function/#comment-12938)
    
4.  How can we get true or false result in if function when we use it to get the information from named range.  
    Eg. Colors name is defined as named range”colour\_name”  
    Now,  
    \=if (and (cellB2 =”red”, cellB2 =named range” colour\_ name”),”true”,”false”.
    
    I couldn’t find the text (color) using “if formula” from the named range.  
    How can i get it.  
    Please guide me.
    
    Many thanks  
    Manish  
    Nepal
    
    [Reply](https://trumpexcel.com/excel-if-function/#comment-12699)
    
5.  nice
    
    [Reply](https://trumpexcel.com/excel-if-function/#comment-12537)
    
6.  Hello I am encountering issue when entering codes in weekends and holidays in leave tracker. The codes do not compile on the list.
    
    [Reply](https://trumpexcel.com/excel-if-function/#comment-11446)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-if-function/#respond)

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