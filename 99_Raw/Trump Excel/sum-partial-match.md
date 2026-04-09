# SUM cells Based on Partial Text Match (SUMIF / SUMIFS)

**Source:** https://trumpexcel.com/sum-partial-match

---

[Skip to content](https://trumpexcel.com/sum-partial-match/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/sum-partial-match/#below-title)

Excel has the SUMIF and SUMIFS functions that allow you to add a range of cells based on one or more criteria.

And sometimes, you may want to get the sum of cells based on partial match in the dataset.

For example, suppose I have a dataset as shown below and I want to get the sum of all the cells where the country in cells in column A is US.

As you can see, I need to check each cell and see if the string “US” appears in the cell or not, and if it does, I need to include the value in the adjacent cell in column B while doing the sum.

This is a case of a partial match, where I need to sum cells based on the partial match.

And thanks to wildcard characters in Excel, this is possible (I would even say it’s fairly easy).

So, let me show you some examples of how to sum cells based on partial text match using SUMIF and Wildcard characters.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/sum-partial-match/#)

A little about Wildcard Characters
----------------------------------

Before I get into the mechanics and show you how to add cells that have a partial text match, let me quickly explain what wildcards are.

There are [three wildcard characters](https://trumpexcel.com/excel-wildcard-characters/)
 in Excel:

*   **Asterisk (\*)** – An asterisk represents any number of characters in Excel. So, if you want to add all the cells where the string ends with US, you can use “\*US” as the criteria. Here, as long as the string in the cell has US in the end, it can have any number of characters in the beginning.
*   **Question Mark (?)** – A question mark represents one single character. So if I use the criteria as “?US”, only those cells that have three characters in the string and end with the word US would satisfy the criteria.
*   **Tilde (~)** – It is used to identify a wildcard character (~, \*, ?) in the text. It’s less used, and we won’t need it in this tutorial (it’s rarely used, and I have never used it)

Examples to SUM Cells Based on Partial Text Match
-------------------------------------------------

Now, let me show you some practical examples where you can use a combination of Excel formulas and wildcard characters to get the sum when there is a partial match.

### SUM Cells When Partial Text Matches the End of the String

Below, I have a dataset where I have some names in column A, along with their country at the end (after the name).

![Dataset to SUM Cells When Partial Text Matches the End of the String](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20348%20407'%3E%3C/svg%3E)

I want to add the values in column B for only those cells where the country in cells column A is the US.

Since there are different names in column A, I will have to use the [SUMIF function](https://trumpexcel.com/excel-sumif-function/)
 with a wildcard to add only the cells for names that have the US as the country.

Below is the formula that will do this:

\=SUMIF(A2:A16,"\*US",B2:B16)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20720%20509'%3E%3C/svg%3E)

In the above SUMIF formula, I have used the below arguments:

*   **A2:A16** – This is the range where the formula checks for the criteria. In our example, these would be the cells with names.
*   **“\*US”** – This is the criteria that is used to check every cell, and only those cells that satisfy these criteria are considered. Since I want to get the sum of all the cells in B2:B16, where the cells in A2:A16 ends with US, I have used **“\*US”**. Asterisk (\*) means that there could be any number of characters before the string US. Also, remember to have the criteria in double-quotes.
*   **B2:B16** – This is the range that has the values that we want to sum

Also read: [](https://trumpexcel.com/check-if-cell-contains-partial-text-excel/)
[Check IF Cell Contains Partial Text in Excel (Formulas)](https://trumpexcel.com/check-if-cell-contains-partial-text-excel/)

### SUM Cells When Partial Text Matches the Starting of the String

Below, I have a dataset where I have some names in column A, along with their country in the beginning (before the name).

![Dataset to SUM Cells When Partial Text Matches the Starting of the String](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20340%20407'%3E%3C/svg%3E)

I want to add the values in column B for only those cells where the country in cells column A is the US.

I can do this using a SUMIF formula along with a wild card character (asterisk).

Below is the formula that will do this:

\=SUMIF(A2:A16,"US\*",B2:B16)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20722%20506'%3E%3C/svg%3E)

Below are the arguments I have used in the above SUMIF formula:

*   **A2:A16** – This is the range where the formula checks for the criteria (cells with names in our example)
*   **“US\*”** – Since I want to get the sum of all the cells in B2:B16, where the cells in A2:A16 start with US, I have used **“US\*”**. This means that any cell that starts with the string **US** will satisfy the criteria, no matter what comes after it
*   **B2:B16** – This is the range that has the values that we want to sum

Also read: [How to Use VLOOKUP with Multiple Criteria](https://trumpexcel.com/vlookup-with-multiple-criteria/)

### SUM When Cell Starts and Ends with Specific Text

Below, I have a data set where I have names in column A and their sales values in column B, and I want to get only the sum of sales values where the name starts with US and ends with A.

![Dataset to SUM When Cell Starts and Ends with Specific Text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20371%20408'%3E%3C/svg%3E)

Here is the formula that will do this:

\=SUMIF(A2:A16,"US\*A",B2:B16)

![Formula to SUM When Cell Starts and Ends with Specific Text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20731%20510'%3E%3C/svg%3E)

In the above formula, I have used the following arguments:

*   **A2:A16** – This is the range where the formula checks for the criteria (names in column A in our example)
*   **“US\*A”** – This is the criteria that would only be satisfied in those cells that start with ‘US’ and end with ‘A’. An asterisk symbol in the middle represents that there could be any number of characters between US and A.
*   **B2:B16** – This is the range that has the values that we want to sum

Also read: [Compare Two Columns in Excel (for matches & differences)](https://trumpexcel.com/compare-two-columns/)

### SUM When a String Appears Anywhere in the Cell

Now, let’s look at an example where you want to get the sum of cells where a specific text string can appear anywhere in the cell.

Below, I have a data set where I have names in column A, and I want to get the sum of their sales for only those names that have the country as the US.

![Dataset to SUM When a String Appears Anywhere in the Cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20348%20407'%3E%3C/svg%3E)

Here is the formula that will do this:

\=SUMIF(A2:A16,"\*US\*",B2:B16)

![Formula to SUM When a String Appears Anywhere in the Cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20728%20509'%3E%3C/svg%3E)

In the above formula, I have used the following arguments:

*   **A2:A16** – This is the range where the formula checks for the criteria (names in column A)
*   **“\*US\*”** – This criteria that would only be satisfied in those cells that has the string US anywhere in the cell. Since I’ve added an asterisk symbol before and after the string US, It means that there could be any number of characters before or after US.
*   **B2:B16** – This is the range that has the values that we want to sum

Also read: [Multiple Criteria in Excel COUNTIF / COUNTIFS Function](https://trumpexcel.com/multiple-criteria-in-excel-countif/)

### SUM Based on Multiple Criteria and Partial Match

Let’s now look at a little more complicated example where I want some cells based on multiple criteria and a partial match.

Below I have a data set where I have names in column and their category in column B and I want to get the sum of all the cells where the country is US and the category is A.

![Dataset to SUM Based on Multiple Criteria and Partial Match](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20455%20408'%3E%3C/svg%3E)

Since there are two conditions that I need to check for, I will have to use a [SUMIFS formula](https://trumpexcel.com/excel-sumifs-function/)
 with the asterisk wildcard character.

Below is the formula that will do this:

\=SUMIFS(C2:C16,A2:A16,"\*US",B2:B16,"A")

![Formula to SUM Based on Multiple Criteria and Partial Match](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20837%20511'%3E%3C/svg%3E)

In the above SUMIFS formula, I have used the following arguments:

*   **C2:C16** – This is the range that has the values that we want to add
*   **A2:A16** – This is the range where I need to check for the first criteria. In this example, it is the range that contains the name where I want to check whether it ends with US or not.
*   **“\*US”** – This is the criteria that would be checked against the range A2:A16 (which is the argument before it in the formula)
*   **B2:B16** – This is the range where I need to check for the second criterion. In this example, it has the category codes.
*   **“A”** – This is the second criterion that we need to check for

Also read: [How to Sum by Color in Excel](https://trumpexcel.com/sum-by-color-excel/)

### SUM Cells that Contain Asterisk Character

A less common but possible situation could be when you have to get the sum of all the cells where another cell contains the \* character.

The problem with this is that when I use an asterisk symbol as a criteria in my SUMIF or SUMIFS function, it would be treated as a wild card character and would represent any number of characters.

Let’s see how to tackle this situation.

Below, I have a data set where I have names in column A, and I only want to get the sum of their sales in column B if the name has an asterisk symbol in the cell.

![Dataset to SUM Cells that Contain Asterisk Character](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20341%20408'%3E%3C/svg%3E)

Here is a formula that will do this:

\=SUMIF(A2:A16,"\*_~\*_",B2:B16)

![Formula to SUM Cells that Contain Asterisk Character](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20722%20510'%3E%3C/svg%3E)

In the above SUMIFS formula, I have used the following arguments:

*   **A2:A16** – This is the range that has the names
*   **“\*_~\*_“** – This is the criterion. Here, I have used \*~\*. When I add a ~ character before the \* symbol, It will treat it as any other character instead of a wild card. So when my criteria is \*_~\*_, The first asterisk symbol represents any number of characters, and ~\* represents just the asterisk character at the end.
*   **B2:B16** – This is the range that has the numbers that I need to add based on the condition

In this article, I have covered some examples to show you how to Sum cells based on partial text match using SUMIF or SUMIFS function.

I hope you found this article useful.

I would love to know your thoughts in the comments section below.

**Other Excel articles you may also like:**

*   [How to Combine Duplicate Rows and Sum the Values in Excel](https://trumpexcel.com/combine-duplicate-rows-and-sum-values-excel/)
    
*   [How to Count Cells that Contain Text Strings](https://trumpexcel.com/count-cells-that-contain-text/)
    
*   [How to Sum Across Multiple Sheets in Excel? (3D SUM Formula)](https://trumpexcel.com/sum-across-multiple-sheets-excel/)
    
*   [How to SUM Values Between Two Dates (using SUMIFS formula)](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

5 thoughts on “SUM Based on Partial Text Match in Excel (SUMIF)”
----------------------------------------------------------------

1.  That should have been Found not Sound …sigh.
    
    [Reply](https://trumpexcel.com/sum-partial-match/#comment-32127)
    
2.  Sound the article SUM Based on Partial Text Match in Excel (SUMIF) very interesting — especially the last example. Thanks.
    
    [Reply](https://trumpexcel.com/sum-partial-match/#comment-32126)
    
3.  Thank You.
    
    [Reply](https://trumpexcel.com/sum-partial-match/#comment-32114)
    
4.  Extremely Clever. Bravo…  
    Sincerely,  
    Ted Olshansky
    
    [Reply](https://trumpexcel.com/sum-partial-match/#comment-32041)
    
5.  Thanks Sumit. This was very helpful. I always look forward to your emails to be able to enhance my excel skills and use it in my day-to-day work.  
    Thanks!
    
    [Reply](https://trumpexcel.com/sum-partial-match/#comment-32025)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/sum-partial-match/#respond)

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