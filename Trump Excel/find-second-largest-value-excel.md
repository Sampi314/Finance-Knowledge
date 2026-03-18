# Find the Second Largest Value in Excel (3 Easy Ways)

**Source:** https://trumpexcel.com/find-second-largest-value-excel

---

[Skip to content](https://trumpexcel.com/find-second-largest-value-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/find-second-largest-value-excel/#below-title)

If you want to get the highest value in a column or a range, you can easily do that using the built-in [MAX function in Excel](https://trumpexcel.com/excel-max-function/)
.

But what if you want to get the second largest value, the third largest value, or the nth largest value from the same data set?

In this scenario, you will have to use another function called **LARGE** that allows you to get any nth highest value from a range.

In this article, I will show you how to find the second-largest value in a dataset under different scenarios. I will show you how you can fetch the second largest value, highlight it, or get any other corresponding data from the same row or column.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/find-second-largest-value-excel/#)

Find the Second Largest Number in a Column
------------------------------------------

Let’s start with a simple example.

Below, I have the data set where I have the scores of students in column B, and I want to get the second largest score in this column.

![Data set of students score to find second largest value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20381'%3E%3C/svg%3E)

Here is the formula that will do this:

\=LARGE(B2:B11,2)

I entered this formula in cell D2 and pressed the Enter key to get the result.

![Large formula to find second highest value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20590%20427'%3E%3C/svg%3E)

Here is how the [LARGE functions](https://trumpexcel.com/excel-large-function/)
 works in Excel:

*   **B2:B11** – This is the first argument in the function, which is the range from which we want to find the value
*   **2** – This is where we specified that we want the second largest value. If I change this to 1, it will give me the largest value. If I make this 3, this will give me the third highest value.

Find the Second Largest Number in a Range
-----------------------------------------

You can also find the second largest number using the LARGE function from a range that has multiple rows and columns.

Below, I have a data set where I have student names and their scores in three different subjects, and I want to know the second-highest score across all the subjects.

![Students scores in multiple subjects](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20675%20337'%3E%3C/svg%3E)

Here is the formula that will do this:

\=LARGE(B2:D11,2)

![Large formula to find second highest value in range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20681%20385'%3E%3C/svg%3E)

The above formula analyzes the entire range B2:D11 and gives us the second-largest value in the entire range.

Also read: [How to Rank within Groups in Excel](https://trumpexcel.com/rank-within-groups-excel/)

Find the Second Largest Value Based on a Criteria
-------------------------------------------------

Sometimes, you may want to know the second-highest value based on certain criteria.

In such cases, you will have to use a combination of formulas that allows you to first fetch the data based on the criteria and then give you the 2nd largest value.

Let me show you using an example.

Below, I have a data set of students’ scores in three different subjects, and I want to get the second-highest score of the subject mentioned in cell F1 (Physics in this example).

![Students scores data set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20531%20340'%3E%3C/svg%3E)

Here is the formula that will do this:

\=LARGE(INDEX($B$2:$D$11,,MATCH(F1,B1:D1,0)),2)

Put this formula in cell F2 and press enter to get the result.

![Large and index function to find second largest value by criteria](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20341'%3E%3C/svg%3E)

The above formula first uses an [Index Match combination](https://trumpexcel.com/index-match/)
 to fetch the data only for the subject in cell F1.

Once we have the data for the selected subject, the LARGE function then gives us the second-highest value from that data.

Note that this formula is dynamic, which means that if you change the subject name in cell F1 from Physics to Math or Chemistry, the result will automatically update to give you the second-highest score in that subject.

_You can also use this same concept to get the highest or third highest or any Nth highest value based on criteria._

Highlighting the Second Largest Value (Conditional Formatting)
--------------------------------------------------------------

If you want to highlight the cell that contains the second largest value, you can do that using [Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
.

To do this, we will use a formula within Conditional Formatting that will analyze each cell in the given range and check whether it contains the second-largest value or not. If it does contain the second largest value, it is going to format the cell with the specified color.

Let me show you how this works using an example.

Below, I have a dataset where I have students’ scores in Math, and I want to highlight the 2nd highest score in the column.

![Student data set to highlight second largest value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20252%20373'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select the cells that contain the scores.
2.  Click the **Home** tab.

![Click the home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20486%20223'%3E%3C/svg%3E)

3.  Click on the **Conditional Formatting** option in the Styles group.
4.  Click on the **New Rules** option.

![Click on new rule in conditional formatting drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20381%20578'%3E%3C/svg%3E)

5.  In the new formatting rules dialog box, select the option ‘**Use a formula to determine which cells to format**‘.

![Select user formula to determine which cells to format option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

6.  In the formula field, enter the below formula:

\=B2=LARGE($B$2:$B$11,2)

![Enter the formula in the field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

7.  Click on the Format button

![Click the format button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

7.  Within the Fill tab, select the color in which you want to highlight the cell that has the second-highest value (I will go with yellow color here)

![Select the color with which to fill the cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20673'%3E%3C/svg%3E)

7.  Click OK
8.  Click OK

The above steps would highlight the cell that contains the second largest value.

![Second largest cell value highlighted in yellow color by conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20266%20378'%3E%3C/svg%3E)

**How does this work?**

We have used a formula in Conditional Formatting that checks each cell in the selected range for the condition =B2=LARGE($B$2:$B$11,2)

In this case, we’ve used B2, which is the first cell in the range. But since this is a [relative cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
, when Conditional Formatting is analyzing each cell, it is going to pick up the value from that cell.

So when it’s analyzing cell B3, the formula would become:

\=B3=LARGE($B$2:$B$11,2)

and when analyzing cell B4, the formula would become

\=B4=LARGE($B$2:$B$11,2)

Any cell where conditional formatting gets True as the result of the formula will be highlighted in the specified color. This would only be true for cells that contain the second-largest value.

If there is more than one cell that contains the second largest value, all of these cells will be highlighted.

Also read: [Highlight Cells With Formulas in Excel](https://trumpexcel.com/highlight-cells-with-formulas-excel/)

Fetch Corresponding Data for the Second Highest Value
-----------------------------------------------------

So far, we have used formulas that give us the second-highest value. But in many cases, what you really need is a corresponding data point in the same row or column.

For example, below, I have a data set where I have student’s scores, and I want to know the name of the student who has scored the 2nd highest marks.

![Data set to fetch the name of student with second highest score](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20472%20347'%3E%3C/svg%3E)

Here is the formula that will do this:

\=INDEX(A2:A11,MATCH(LARGE(B2:B11,2),B2:B11,0))

I have entered this formula in cell D2 and pressed Enter to get the result.

![Index function to fetch the name of the student based on the score](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20346'%3E%3C/svg%3E)

In the above formula, I first used the LARGE function to fetch the second-highest value and then used that within the MATCH function to get the position of the second-highest value in that column.

In this example, the match portion of the formula would return 2 because Tim has the second-highest score, which is in the second cell in the range B2:B11 (position-wise).

Now that I know the position of the second-highest score, I can fetch the corresponding name from column A by using the INDEX function.

In the INDEX function, my first argument is the range from which I want to fetch the data (which are the names in this case in A2:A11), and the second argument is the [MATCH function](https://trumpexcel.com/excel-match-function/)
, which gives us the position of the second highest value, that will be used to get the name from A2:A11.

In case you are using newer versions of Excel and have access to the [XLOOKUP function](https://trumpexcel.com/xlookup-function/)
, you can use the below formula as well:

\=XLOOKUP(LARGE($B$2:$B$11,2),B2:B11,A2:A11,,0)

So these are some methods you can use to get the second highest, the third highest, or any Nth highest value in a range in Excel.

I have covered the formulas to fetch the exact value, highlight the value using Conditional Formatting, or fetch a corresponding data point for that value in a data set.

I hope you found this Excel tutorial useful.

**Other Excel articles you may also like**:

*   [How to Use Excel RANK Function](https://trumpexcel.com/excel-rank-function/)
    
*   [Use VLookup to Get the Last Number in a List in Excel](https://trumpexcel.com/get-the-last-number-in-excel-vlookup/)
    
*   [How to Sort by Length in Excel?](https://trumpexcel.com/sort-by-length-excel/)
    
*   [How to Find the Largest Value in Excel](https://spreadsheetplanet.com/find-largest-value-excel/)
    
*   [Lookup the Second, the Third, or the Nth Value in Excel](https://trumpexcel.com/lookup-second-value/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/find-second-largest-value-excel/#respond)

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