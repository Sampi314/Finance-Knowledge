# Remove Blank Rows in Excel Using a Formula

**Source:** https://trumpexcel.com/remove-blank-rows-formula

---

[Skip to content](https://trumpexcel.com/remove-blank-rows-formula/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-blank-rows-formula/#below-title)

If you want to remove blank rows from a dataset using a formula in Excel, you can do that by using the FILTER function.

Below is an example where I have a dataset on the left, and then I’ve used the filter function to extract only those rows that are not blank on the right.

![Delete blank rows using a formula in Excel](https://trumpexcel.com/wp-content/uploads/2026/01/Delete-blank-rows-using-a-formula-in-Excel.png)

Let me show you how it works.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-blank-rows-formula/#)

Remove Blank Rows Using FILTER Formula
--------------------------------------

Below, I have a dataset where some rows are blank.

I want to use a formula that will remove all the blank rows and stack all the non-blank rows together.

![Dataset with blank rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20661%20941'%3E%3C/svg%3E)

Here is the formula that does this for me:

\=FILTER(A2:C15,NOT(BYROW(ISBLANK(A2:C15),AND)))

![Filter formula to remove blank rows in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201855%201066'%3E%3C/svg%3E)

_If you want to use this with your dataset, just change the range A2:C15 to your data range reference._

**How this formula works:**

_ISBLANK(A2:C15)_ – This part checks each cell in the range A2:C15 and returns TRUE if the cell is blank and FALSE if it contains any value. So you get a grid of TRUE and FALSE values matching your data range.

_BYROW(ISBLANK(A2:C15),AND)_ – Here, the BYROW function looks at each row one by one from the result we got in Step 1. For each row, it uses the AND function to check if all cells in that row are blank (all TRUE values). If all cells in a row are blank, it returns TRUE for that row. If even one cell has a value, it returns FALSE.

_NOT(BYROW(ISBLANK(A2:C15),AND))_ – The NOT function simply flips the results of the BYROW formula. So rows that were TRUE (completely blank) become FALSE, and rows that were FALSE (have at least one value) become TRUE. This gives us a list of TRUE for rows we want to keep and FALSE for blank rows we want to remove.

_FILTER(A2:C15,…)_ – Finally, the FILTER function uses this TRUE/FALSE list to filter your original data range. It only returns the rows where the condition is TRUE, which means it gives you only the rows that have at least one value in them, effectively removing all the completely blank rows.

And that’s it! The formula stacks all your non-blank rows together and removes the blank ones.

Remove Blank Cells from a Single Column
---------------------------------------

If you want to remove blank cells from a single column, then you can use a simplified version of the above formula.

Below, I have a dataset with names in column A, and I want to remove all the blank cells.

![One column of data with blank cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20493%201094'%3E%3C/svg%3E)

Here is the formula that will do this:

\=FILTER(A2:A15,A2:A15<>"")

![Formula to remove blank cells from a column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201356%201210'%3E%3C/svg%3E)

The above formula goes through each cell in the given range and checks whether it is empty or not.

If the cell is blank, the second argument of the FILTER function returns FALSE, and it is removed from the result. If it is not blank, it returns TRUE, and it is retained.

I hope you found this Excel tutorial helpful.

**Other Excel articles you may also like:**

*   [Select Every Other Row in Excel](https://trumpexcel.com/select-every-other-row-excel/)
    
*   [Delete Blank Rows in Excel](https://trumpexcel.com/delete-blank-rows-excel/)
    
*   [How to Delete Alternate Rows in Excel](https://trumpexcel.com/delete-every-other-row-excel/)
    
*   [Delete Blank Columns in Excel](https://trumpexcel.com/delete-blank-columns-excel/)
    
*   [Delete rows based on cell value in Excel](https://trumpexcel.com/delete-rows-based-on-cell-value/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “Remove Blank Rows in Excel Using a Formula”
----------------------------------------------------------

1.  You are Excellent teacher
    
    [Reply](https://trumpexcel.com/remove-blank-rows-formula/#comment-55009)
    
    *   Thanks, Lawrence. Glad you found the article helpful
        
        [Reply](https://trumpexcel.com/remove-blank-rows-formula/#comment-55366)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-blank-rows-formula/#respond)

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