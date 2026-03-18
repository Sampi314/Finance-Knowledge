# Excel Conditional Formatting Based on Another Cell (Easy Steps)

**Source:** https://trumpexcel.com/conditional-formatting-based-on-another-cell-excel

---

[Skip to content](https://trumpexcel.com/conditional-formatting-based-on-another-cell-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/conditional-formatting-based-on-another-cell-excel/#below-title)

Conditional formatting in Excel allows you to format cells based on the values in the cells.

The built-in formatting settings and Conditional Formatting are made to format cells based on the value in the cell itself.

But what if you want to apply conditional formatting to a cell based on the value in some other cell?

That can also be done using the formula technique in Conditional Formatting.

In this article, I am going to show you some examples where you can apply [Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
 to a cell or range of cells based on another cell’s value.

**_[Download the example file and follow along](https://www.dropbox.com/scl/fi/7c611fv9e95ik7ffzwvxa/Conditional-Formatting-Based-on-Another-Cell.xlsx?rlkey=oo3gmtit30x1nyt44k5pged80&dl=1)
_**

This Tutorial Covers:

[Toggle](https://trumpexcel.com/conditional-formatting-based-on-another-cell-excel/#)

Conditional Format Cell Based on Another Cell (Text Value)
----------------------------------------------------------

Let’s start with a simple example.

Below I have a data set where I have the Names of people in column A, their Region in column B, and their Sales values in column c.

![Data set to apply conditional formatting based on another cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20395%20448'%3E%3C/svg%3E)

I want to highlight only those names where the region value is ‘US’.

This is an example where I want to format a cell based on the value in the adjacent cell.

Here are the steps to do this:

1.  Select range A2:A15 (since I only want to highlight the cells with names, I’m only going to select the range that has the names)

![Select the range that contains the names that you want to highlight](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20395%20448'%3E%3C/svg%3E)

2.  Click the Home tab

![Click the home tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20407%20223'%3E%3C/svg%3E)

3.  Click on the Conditional Formatting icon in the ribbon.

![Click on conditional formatting icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20501%20223'%3E%3C/svg%3E)

4.  Click on the New Rule option. This will open the New Rule dialog box.

![Click on the new rules option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20249%20478'%3E%3C/svg%3E)

5.  Select the option – ‘Use a formula to determine which cells to format’

![Select the option use a formula to determine which cells to format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

6.  Enter the below formula in the formula field

\=$B2="US"

![Enter the formula in the formula field in conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

7.  Click on the Format button

![Click on the format button for](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

8.  Click on the Fill tab and then select the color in which you want to highlight the cells.

![Select the color to highlight the cells using conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20597'%3E%3C/svg%3E)

9.  Click Ok
10.  Click OK

The above steps would highlight only those names where the region is US in column B.

![Data set where names have been highlighted based on the value in the region column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20398%20448'%3E%3C/svg%3E)

Note that in this example, I have hardcoded the text US in the formula, But you can also use a reference to a cell that contains the text based on which you want to highlight the cells in column A.

### Role of Cell References in Conditional Formatting Formulas

When working with formula and conditional formatting, it is important to understand the role of cell references.

In the above example, I used the below formula:

\=$B2="US"

Here, I have used $B2 (which is a [mixed cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
 where I have locked the column but not locked the row).

When you add a dollar sign ($) before the column alphabet or the row number, it ensures that when you copy this formula down to other cells, the part that has been locked with the dollar symbol will not change.

For example, in our case, I have used $B2, which means that when the Conditional Formatting formula analyzes cell A2, it checks cell B2 (as I locked column B, so it would always refer to column B even when analyzing the cells in column A).

And then, when it moves to cell A3, the formula Conditional Formatting uses is:

\=$B3="US"

This is because I only locked column B and not the row, so when conditional formatting moves to the next cell in column A (from A2 to A3), it also adjusts the reference from $B2 to $B3.

This same logic could be used in this entire article, where I would use the dollar sign to lock references based on what I want.

Also read: [Apply Conditional Formatting Based on Another Column in Excel](https://trumpexcel.com/conditional-formatting-based-on-another-column-excel/)

Apply Conditional Formatting to an Entire Row Based on a Cell Value
-------------------------------------------------------------------

In the above example, I highlighted names based on the region value.

But what if I want to highlight the entire record?

For example, below, I have the same data set, and I want to highlight all the records for the US region.

![Data set to apply conditional formatting based on another cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20395%20448'%3E%3C/svg%3E)

This can easily be done using a conditional formatting formula using the below steps:

1.  Select the entire dataset (A2:C15 in this example)
2.  Click the Home tab
3.  Click on the Conditional Formatting icon in the ribbon.

![Click on conditional formatting icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20501%20223'%3E%3C/svg%3E)

4.  Click on the New Rule option.

![Click on the new rules option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20249%20478'%3E%3C/svg%3E)

5.  Select the option – ‘Use a formula to determine which cells to format’

![Select the option use a formula to determine which cells to format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

6.  Enter the below formula in the formula field

\=$B2="US"

![Enter the formula and conditional formatting to highlight entire row based on another cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

7.  Click on the Format button

![Click on the format button for](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

8.  Click on the Fill tab and then select the color in which you want to highlight the cells.

![Select the color to highlight the cells using conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20597'%3E%3C/svg%3E)

9.  Click Ok
10.  Click OK

The above steps would highlight all the rows where the region value is US.

![Entire row highlighted with conditional formatting based on another cells value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20391%20448'%3E%3C/svg%3E)

You will notice that my formula is exactly the same as in the previous example. The only change I have made when highlighting just the names in column A instead of the entire record is the range on which I have applied the conditional formatting.

When I just wanted to highlight the names in column A, I only selected the cells in column A and applied conditional formatting to it.

And when I wanted to highlight the entire record, I selected the entire data set but used the same formula.

The logic here is again the same where each cell in the data set is analyzed using the formula which is =$B2=”US”

Since I’ve locked the column, when all the cells in row 2 in the data set are analyzed, it only uses the formula =$B2=”US” To determine whether the cell in that row should be highlighted or not.

So for all three cells in the first row of the dataset (A2, B2, and C2), it checks the formula =$B2=”US”, and if the formula returns True, then it highlights the cells, and if it returns False, then it won’t highlight the cells.

Then when it moves to the next row and analyzes the cells A3, B3, and C3, it uses the formula =$B3=”US”

**_[Download the example file and follow along](https://www.dropbox.com/scl/fi/7c611fv9e95ik7ffzwvxa/Conditional-Formatting-Based-on-Another-Cell.xlsx?rlkey=oo3gmtit30x1nyt44k5pged80&dl=1)
_**

Conditional Format Cell Based on Another Cell (Numeric Value)
-------------------------------------------------------------

You can also use Conditional Formatting with numerical values to highlight cells in a data set.

For example, below, I have a data set where I want to highlight all the records where the sales value is more than 75000.

![Data set to apply conditional formatting based on another cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20395%20448'%3E%3C/svg%3E)

Here are the steps to do this using Conditional Formatting:

1.  Select the entire dataset (A2:C15 in this example)
2.  Click the Home tab
3.  Click on the Conditional Formatting icon in the ribbon.

![Click on conditional formatting icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20501%20223'%3E%3C/svg%3E)

4.  Click on the New Rule option.

![Click on the new rules option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20249%20478'%3E%3C/svg%3E)

5.  Select the option – ‘Use a formula to determine which cells to format’

![Select the option use a formula to determine which cells to format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

6.  Enter the below formula in the formula field

\=$C2>75000

![Formula and conditional formatting to highlight rows based on sales values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20457'%3E%3C/svg%3E)

7.  Click on the Format button
8.  Click on the Fill tab and then select the color in which you want to highlight the cells. I will go with the green color.
9.  Click Ok
10.  Click OK

The above steps would highlight all the records where the sales value is more than 75,000.

![Data highlighted with conditional formatting based on sales value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20392%20448'%3E%3C/svg%3E)

Each cell in the second row is analyzed against =$C2>75000. If this condition is True, then all the cells in the row are highlighted; if it is not True, then they are not highlighted.

Then, when conditional formatting analyzes the cells in the next row, the formula adjusts accordingly.

For example, when analyzing cells in row 3, the formula used would be =$C3>75000

Using AND in Conditional Formatting Formulas
--------------------------------------------

Using the [AND function](https://trumpexcel.com/excel-and-function/)
, you can also use multiple conditions within a formula in Conditional Formatting.

You can use any formula within conditional formatting as long as it returns a True or a False

Below is a data set where I want to highlight all the rows where the region is US and the sales value is more than 75,000.

![Data set to apply conditional formatting based on another cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20395%20448'%3E%3C/svg%3E)

Here are the steps to do this using a formula in Conditional Formatting:

1.  Select the entire dataset (A2:C15 in this example)
2.  Click the Home tab
3.  Click on the Conditional Formatting icon in the ribbon.

![Click on conditional formatting icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20501%20223'%3E%3C/svg%3E)

4.  Click on the New Rule option.
5.  Select the option – ‘Use a formula to determine which cells to format’

![Select the option use a formula to determine which cells to format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

6.  Enter the below formula in the formula field

\=AND($B2="US",$C2>75000)

![AND formula in conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

7.  Click on the Format button
8.  Click on the Fill tab and then select the color in which you want to highlight the cells. I go with the green color.
9.  Click Ok
10.  Click OK

The AND formula used in the above example analyzes each cell in a row based on the value in the region column and the sales value column.

![And formula to highlight cells based on another cell using conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20498'%3E%3C/svg%3E)

If in a row, the region is the US and the sales value is more than 75,000, the AND formula would return a True, and this would highlight the entire row.

Also read: [How to Count Colored Cells in Excel?](https://trumpexcel.com/count-colored-cells-in-excel/)

Using OR in Conditional Formatting Formulas
-------------------------------------------

Just like the AND formula, you can also use an [OR function](https://trumpexcel.com/excel-or-function/)
 in Conditional Formatting.

Below is a data set in which I want to highlight all the rows where either the region is the US, or the sales value is more than 75,000. So, if any one of these conditions is satisfied, I want the entire road to be highlighted.

![Data set to apply conditional formatting based on another cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20395%20448'%3E%3C/svg%3E)

Below are the steps to do this using the OR formula in Conditional Formatting:

1.  Select the entire dataset (A2:C15 in this example)
2.  Click the Home tab
3.  Click on the Conditional Formatting icon in the ribbon.

![Click on conditional formatting icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20501%20223'%3E%3C/svg%3E)

4.  Click on the New Rule option.
5.  Select the option – ‘Use a formula to determine which cells to format’

![Select the option use a formula to determine which cells to format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

6.  Enter the below formula in the formula field

\=OR($B2="US",$C2>75000)

![Or formula in conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

7.  Click on the Format button
8.  Click on the Fill tab and then select the color in which you want to highlight the cells. I go with the green color.
9.  Click OK
10.  Click OK

In the above case, when Conditional Formatting analyzes each cell in a row, it returns True if the region value is US, the sales value is more than 75,000, or both.

![Or formula to highlight cells based on another cell using conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20498'%3E%3C/svg%3E)

The row will not be highlighted if none of the criteria are satisfied.

Also read: [Copy Conditional Formatting to Another Cell in Excel](https://trumpexcel.com/copy-conditional-formatting-another-cell-excel/)

Conditional Formatting to Highlight Rows with Blank Cells
---------------------------------------------------------

Another useful scenario is when you [have blank cells](https://trumpexcel.com/highlight-blank-cells-in-excel/)
 and want the entire row to be highlighted.

This is even more useful when you have a large data set that spans across multiple columns, and there is a possibility that you may miss out on a few blank cells.

So, if there are blank cells in any specific column or columns, you can use conditional formatting to highlight the entire row.

Below, I have a data set with some blank cells in column C. If a row contains a blank cell in column C, I want to highlight it.

Here are the steps to do this:

1.  Select the entire dataset (A2:C15 in this example)
2.  Click the Home tab
3.  Click on the Conditional Formatting icon in the ribbon.

![Click on conditional formatting icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20501%20223'%3E%3C/svg%3E)

1.  Click on the New Rule option.
2.  Select the option – ‘Use a formula to determine which cells to format’

![Select the option use a formula to determine which cells to format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

1.  Enter the below formula in the formula field

\=$C2=""

![Conditional formatting to highlight blank cells rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

7.  Click on the Format button
8.  Click on the Fill tab and then select the color in which you want to highlight the cells.
9.  Click OK
10.  Click OK

The above formula checks each cell in a row using the formula =$C2=””, and if this formula is TRUE (which means that the cell in column C is blank), it highlights all the cells in that row.

![Rows with blank cells are highlighted using conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20438%20497'%3E%3C/svg%3E)

You can also use a variation of this formula in different scenarios:

*   If you only want to highlight only the blank cells and not the entire row, use the below formula

\=A2=""

*   If you want to highlight the entire row if any cell in that row is blank, use the below formula

\=COUNTIF($A2:$C2,"")

In this article, I’ve covered multiple examples to show you how to apply Conditional Formatting based on value in another cell.

While this cannot be done using the built-in Conditional Formatting options, you can easily do this using a formula.

I hope you found this article useful. If you have any questions or suggestions, do let me know in the comments section.

**Other Excel articles you may also like:**

*   [Conditional Formatting Not Working in Excel](https://trumpexcel.com/conditional-formatting-not-working/)
    
*   [How to Sum by Color in Excel (Formula & VBA)](https://trumpexcel.com/sum-by-color-excel/)
    
*   [How to Remove Conditional Formatting in Excel (Shortcut + VBA)](https://trumpexcel.com/remove-conditional-formatting-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “Excel Conditional Formatting Based on Another Cell”
-----------------------------------------------------------------

1.  Thanks! Very helpful!
    
    [Reply](https://trumpexcel.com/conditional-formatting-based-on-another-cell-excel/#comment-40846)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/conditional-formatting-based-on-another-cell-excel/#respond)

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