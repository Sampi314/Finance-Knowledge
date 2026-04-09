# Count Cells Less than a Value in Excel (COUNTIF Less Than)

**Source:** https://trumpexcel.com/countif-less-than

---

[Skip to content](https://trumpexcel.com/countif-less-than/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/countif-less-than/#below-title)

It’s a common data analysis task to count the number of cells with a value that is less than a specific threshold.

For example, if you have sales figures of different sales reps in a column, you may want to know how many sales reps were not able to meet the given sales target.

Or if you have student scores in a column, then you may want to know how many students have scored less than the passing marks.

In this tutorial, I will show you some simple formulas you can use to count cells that have a value less than a given value in Excel. This can easily be done using the COUNTIF or the COUNTIFS function.

[**Click here to Download the Example File.**](https://www.dropbox.com/s/khp8mkrthlc5pki/CountIF%20Less%20Than.xlsx?dl=1)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/countif-less-than/#)

COUNTIF Function to Count Cells Less Than a Value
-------------------------------------------------

[COUNTIF](https://trumpexcel.com/excel-countif-function/)
 is a simple Excel function that allows you to count the number of cells when a given condition is met.

Let me show you how it works with a simple example.

Below I have a data set where I have the student names in column A, and their scores in column B, and I want to count the total number of cells where the score is less than 35.

![Dataset to countif less than](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20323%20502'%3E%3C/svg%3E)

Here is the formula that will give me the count of cells that score less than 35.

\=COUNTIF(B2:B20,"<50")

![COUNTIF function to count cells less than a value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20514%20608'%3E%3C/svg%3E)

The above COUNTIF function takes two arguments:

*   **B2:B20** – This is the range that has the cells that we want to count in case the given criterion is met
*   **“<50”** – This is the condition that is used to evaluate every cell in the range, and the cell is counted if this criterion is met. Note that we need to put the criterion within double quotes.

In the above example, I’ve hard-coded the criteria into the formula itself. However, you can also use a cell reference Of a cell that has the value that is to be considered for the criteria.

For example, if I have the value 50 in cell D2, then I can use the below formula as well:

 =COUNTIF(B2:B20,"<"&D2)

Note that in the above formula, only the less than sign (“<“) needs to be in double quotes.

Also read: [Count Between Two Numbers in Excel (COUNTIF / COUNTIFS)](https://trumpexcel.com/count-between-two-numbers-excel/)

SUM Function to Count Cells Less Than a Value
---------------------------------------------

While the county function is the best way to count sales that have a value less than a given value, you can also do the same thing using another simple function – the [SUM function](https://trumpexcel.com/excel-sum-function/)
.

Let me show you how it works.

Below I have the same data set where I have students’ names in column A and their scores in column B, and I want to count the number of cells where the score is less than 35.

![Dataset to countif less than](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20323%20502'%3E%3C/svg%3E)

[**Click here to Download the Example File.**](https://www.dropbox.com/s/khp8mkrthlc5pki/CountIF%20Less%20Than.xlsx?dl=1)

Here is the SUM formula that will do this:

\=SUM(--(B2:B20<50))

![SUM function to count cells less than a value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20480%20607'%3E%3C/svg%3E)

In the above formula, we use the condition (B2:B20<50) To check the entire range B2:B20, and it returns an array of TRUEs and FLASEs, where it gives it True when the value is less than 50 and False when the value is not less than 50.

A double negative sign is now used before this condition to convert the Trues and Falses into 1’s and 0’s.

And then, the SUM function is used that counts the total number of 1s in the array, which would also be the total number of cells that meet our given criterion.

Also read: [Count Unique Values in Excel Using COUNTIF Function](https://trumpexcel.com/count-unique-values-in-excel-countif/)

COUNTIFS Function to Count Cells Less Than a Value (Multiple Columns)
---------------------------------------------------------------------

In the above examples, we have counted the number of cells that have a value less than a specified value in a single column.

With the [COUNTIFS function](https://trumpexcel.com/excel-countifs-function/)
, you can also count the number of instances where multiple criteria are being met.

Let me explain with an example.

Below I have a data set where I have the student’s name and column A, their score in Math in column B, and their score in Physics in column C.

![Two column Dataset to countif less than](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20502'%3E%3C/svg%3E)

[**Click here to Download the Example File.**](https://www.dropbox.com/s/khp8mkrthlc5pki/CountIF%20Less%20Than.xlsx?dl=1)

Now I want to count the number of students who have scored less than 50 in both Maths and Physic.

So, in this case, instead of analyzing just one column, we would have to simultaneously analyze two columns and then count only those instances of cells Where the value is less than 50 in both columns.

Below is the formula that will do this for us:

\=COUNTIFS(B2:B20,"<50",C2:C20,"<50")

![COUNTIFS function to count cells less than value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20617%20602'%3E%3C/svg%3E)

The above COUNTIF function uses four arguments:

*   **B2:B20** – This is the range that contains the Math score (which is our criteria\_range1)
*   **“<50”** – This is the first criterion that is checked against criteria\_range1
*   **C2:C20** – This is the range that contains the Physics score (which is our criteria\_range2)
*   **“<50”** – This is the second criterion that is checked against criteria\_range2

Our formula returns 4, which means that four students have scored less than 50 in both Math and Physics.

**Note**: In the above formula, I have hard-coded the criterion value (“<50”). You can also have this value in a cell reference and then use that cell reference in the formula (such as “<“&D2)

So these are three simple formulas you can use to count cells if they have a value less than the specific value.

If there is only one column in which you want to count the cells, you can use the COUNTIF function, and if there are multiple columns, then you can use the COUNTIFS function.

I hope you found this Excel tutorial useful.

**Other Excel articles you may also like:**

*   [Check IF a Date is Between Two Given Dates in Excel](https://trumpexcel.com/check-if-date-is-between-two-dates/)
    
*   [How to Count Filtered Rows in Excel?](https://trumpexcel.com/count-filtered-rows-excel/)
    
*   [Count Characters in a Cell (or Range of Cells) Using Formulas](https://trumpexcel.com/count-characters-in-excel/)
    
*   [How to Use Multiple Criteria in Excel COUNTIF and COUNTIFS Function](https://trumpexcel.com/multiple-criteria-in-excel-countif/)
    
*   [Insert Less Than Or Equal To Sign in Excel](https://trumpexcel.com/excel-insert-symbols/less-than-or-equal/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/countif-less-than/#respond)

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