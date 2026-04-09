# Sort Dates By Month in Excel (Easy Formula)

**Source:** https://trumpexcel.com/sort-dates-by-month-excel

---

[Skip to content](https://trumpexcel.com/sort-dates-by-month-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/sort-dates-by-month-excel/#below-title)

Dates are stored as numbers in the backend in Excel and can easily be sorted.

But what if you want to sort dates by month (irrespective of the year value)?

For example, below, I have the birthday dates for some people, and I want to sort and get all the January birthdays together, all the February birthdays together, and so on.

![Dates dataset to sort by month](https://trumpexcel.com/wp-content/uploads/2024/05/Dates-dataset-to-sort-by-month.png)

I can not sort the above dataset using the Date of Birth column as it will also consider the year’s value.

Thankfully, this can be done using a simple formula.

In this article, I will show you how to sort dates by month in Excel using the SORTBY function as well as the helper column technique (in case you do not have the SORTBY function in your Excel).

[**_Click here to download the example file and follow along_**](https://www.dropbox.com/scl/fi/ci3noss1lwg195hakmu8e/Sort-Dates-by-Month.xlsx?rlkey=wfkgaze1sar6szwhl9w8ku4bh&dl=1)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/sort-dates-by-month-excel/#)

Sort Dates By Month Using SORTBY Function
-----------------------------------------

Let’s start with an example, assuming you have the SORTBY function in your Excel (this is a new function and is available in Excel for Microsoft 365 Windows and Mac, Excel for the web, and Excel 2021).

Below, I have a dataset with birthday dates in column B, and I want to sort these birthdays by month.

![Dates dataset to sort by month](https://trumpexcel.com/wp-content/uploads/2024/05/Dates-dataset-to-sort-by-month.png)

You can do this using the below formula:

\=SORTBY(A2:B11,TEXT(B2:B11,"mmdd"))

This will give you an array result as shown below:

![SORTBY Formula to sort dates by month](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20599%20326'%3E%3C/svg%3E)

Note that the dates in the resulting array are shown as numbers.

You can change the format of the resulting dates by selecting the cells that have the numbers, then clicking the Home tab, and then selecting the _Long Date_ format.

![Select the Long date format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20663'%3E%3C/svg%3E)

This will change the format of the cells, and the numbers would now be shown as dates.

![Dates shown as dates after changing the format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20599%20281'%3E%3C/svg%3E)

Now, let me explain the formula.

The _TEXT(B2:B11,”mmdd”)_ part of the formula takes the dates and gives us the values that only have the month and the day part of the formula in the mmdd format.

This is what we will be using as the basis for our sorting in the SORTBY function. Note that by doing this, I have removed the year value from the dates so that the dates can now be sorted only based on the month and the date value.

The SORTBY function is then used to sort the dataset (A2:B11), where the sorting criteria are the values returned by the _TEXT(B2:B11,”mmdd”)_ part of the formula.

Since I wanted to sort the data in ascending order, I didn’t specify the third argument in the SORTBY function, which is optional. When omitted, it would automatically sort the data in an ascending order.

_One benefit of this method is that the result is dynamic, which means that if I change the dates in the original dataset, the resulting sorted dates dataset will automatically update._

Also read: [How to Sort by the Last Name in Excel](https://trumpexcel.com/sort-by-last-name-excel/)

Sort Dates By Month Using a Helper Column
-----------------------------------------

If you do not have the SORTBY function in your Excel, you can use the helper column technique I will cover here.

Below, I have the same dataset where I want to sort the birthdays by month (so that I have all the birthdays for January together and all in February together and so on).

![Dates dataset to sort by month](https://trumpexcel.com/wp-content/uploads/2024/05/Dates-dataset-to-sort-by-month.png)

Here are the steps to do this:

1.  In the column adjacent to the column with dates, enter Helper as the column header. This will be the helper column that I will be using.

![Create a Helper column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20476%20360'%3E%3C/svg%3E)

2.  In cell C2, enter the following formula and then copy it for all the other cells in the column:

\=--TEXT(B2,"mmdd")

![Enter the TEXT formula in the helper column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20564%20414'%3E%3C/svg%3E)

This formula gives the month and the day values in the mmdd format, and then I added two negative signs to convert the text values into numbers. Adding these double negatives is important as it allows us to sort our data using the helper column values and numerical values.

3.  Select the entire dataset, including the helper column and the headers. In this example, I am selecting A1:C11.
4.  Click the Data tab.

![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20501%20198'%3E%3C/svg%3E)

5.  In the Sort and Filter group, click on the Sort icon. This will open the Sort dialog box.

![Click the Sort icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20207'%3E%3C/svg%3E)

6.  In the Sort dialog box,
    *   Make sure that the My Data has headers option is checked
    *   Click on the Sort by drop-down and select the Helper column (if not selected already).
    *   In the Sort On drop-down, select Cell Values (if not selected already).
    *   In the Order drop-down, select Smallest to Largest.

![Make the selections in the SORT dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20275'%3E%3C/svg%3E)

7.  Click OK.
8.  \[Optional\] Delete the Helper column

The above steps will sort the dates dataset by month.

![Dates sorted by month](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20381%20361'%3E%3C/svg%3E)

Note that this method is not dynamic, so if I make any changes in the dataset, I will have to sort it again to get the sorted dataset.

In this article, I covered two easy ways to sort dates by months and days in Excel. If you’re using the newer versions of Excel, you will have access to the SORTBY function, and you can use my first method of using a simple formula.

In case you do not have access to the SORTBY function, you can use the helper column technique I showed in the second method.

I hope you found this article helpful. If you have any questions or suggestions for me, please let me know in the comments section.

**Other Excel articles about Sorting you may also like:**

*   [How to Undo Sort in Excel (Revert to Original)](https://trumpexcel.com/undo-sort-excel/)
    
*   [How to Sort by Length in Excel?](https://trumpexcel.com/sort-by-length-excel/)
    
*   [How to SORT in Excel (by Rows, Columns, Colors, Dates, & Numbers)](https://trumpexcel.com/sort-excel/)
    
*   [How to Sort By Color in Excel](https://trumpexcel.com/sort-by-color/)
    
*   [How to Sort Worksheets in Excel using VBA (alphabetically)](https://trumpexcel.com/sort-worksheets/)
    
*   [Convert Month Name to Number in Excel](https://trumpexcel.com/convert-month-name-to-number-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/sort-dates-by-month-excel/#respond)

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