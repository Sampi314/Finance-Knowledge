# Learn Your First Steps in Microsoft Excel | Beginner's Crash Tutorial | ChallengeJP

**Source:** https://www.challengejp.com/blog/learn-excel-beginner-tutorial

---

Your First Steps in Microsoft Excel – Beginner’s Crash Tutorial
===============================================================

*   ![Jacek Polewski](https://www.challengejp.com/wp-content/cache/flying-press/gravatar-0c5b42d9d6e4.png) [Jacek Polewski](https://www.challengejp.com/blog/author/adminchallengejp-com/ "Posts by Jacek Polewski")
    
*   November 15, 2020March 20, 2024

Last Updated on March 20, 2024

  
This step-by-step tutorial will give you a quick overview of Microsoft Excel with examples of how to use basic calculations, formulas, and Pivot Tables. [Download a sample Excel file](https://www.challengejp.com/wp-content/uploads/2020/12/excel_course_file_extended.xlsx)
 for practical examples and scroll to the bottom of the page to claim your free One-to-One Online Course.

You can also [watch the video version of the tutorial](https://www.challengejp.com/blog/learn-excel-beginner-tutorial#excel_first_steps_video_tutorial)
 at the end of this post.

Table of Contents

Toggle

**Step 1: Your First Excel Workbook**
-------------------------------------

Every Excel workbook is a collection of worksheets. Think of a worksheet as a page and a workbook as a folder that binds those pages together. Also, every sheet consists of rows and columns. A row is marked with a number (e.g. 2, 5, 123), and columns are marked with a letter (e.g. D, G, I).

A cell is an intersection of a row and a column. Each cell has a unique address. For instance, a cell located at the intersection of Column A and Row 3 has an address “A3” (with the letter referring to the spreadsheet column and the number to the row). 

**Step 2: Entering Data into a Spreadsheet**
--------------------------------------------

To create your first spreadsheet, open a new workbook. Then, click on the cell B2 and type in the word “Product”, followed by hitting the Enter key. Finally, click on the cell to the right (cell C2) and type in “Items” and then “Price” in the next cell in your spreadsheet (C3). As a result, you will see a header of a three-column table, which we will fill in with values in the next step.

Now, it’s time to fill in the values corresponding to each header and complete your first data table. [Download the sample Excel file](https://www.challengejp.com/wp-content/uploads/2020/12/excel_course_file_extended.xlsx)
 for your reference. 

**Step 3: Microsoft Excel’s Data Tables**
-----------------------------------------

Excel spreadsheets allow you to use two inputs – number or text. We will use three columns, each with its header. Firstly, we want to fill each column with appropriate values. Type in “Coffee” in the first cell below the header “Product”, then “Water”, then “Tea”, and repeat that step a few more times (the order of the products does not matter). Also, fill the rows beneath the “Items” columns with random numbers (i.e. 2, 5, 8, 6, etc.). Similarly, fill the “Price” column with random prices (i.e. 2.5, 3.2, 2.8, etc.).

Try creating a data table on your own. [Download the sample Excel file](https://www.challengejp.com/wp-content/uploads/2020/12/excel_course_file_extended.xlsx)
 for an example and compare it with your workbook. Congratulations, you have just created your first spreadsheet!

[![Example Simple Data in Excel](https://www.challengejp.com/wp-content/uploads/2020/11/screenshot1.png)](https://www.challengejp.com/wp-content/uploads/2020/11/screenshot1.png)

A Simple Data Table in Microsoft Excel

**Step 4: Basic Calculations in Microsoft Excel**
-------------------------------------------------

Let’s now create another column and introduce the first simple calculation. Although Microsoft Excel has hundreds of advanced formulas, you will discover that most of the time you need basic arithmetic calculations like additions or multiplications.

First, create a column “Subtotal”, which will be an output of multiplying a value from column “Items” by “Price”. To do that, click on the cell E3 and type in “=” followed by “C3”, then “\*” (Shift+8, \* stands for the sign of multiplication) and “D3”. As a result, your formula in the cell E3 should say “=C3\*D3”. When you hit Enter, you should see a number that equals the number of products x the price. Note: If you want to divide numbers, use “/”. Additions are represented by “+” and substractions by “-”.

**Step 5: Relative Referencing**
--------------------------------

Let’s replicate the same formulas in the cells below. The good news is that you won’t have to do it manually, thanks to Microsoft Excel’s ability to update cell references dynamically.

To fill the rest of the column, stay on the cell E3 and left-click on the lower right corner. Then, drag the cell to the bottom of the table and release the mouse. Finally, double-click on one of the cells to inspect the formula – you will see that the cell references updated themselves to the current row (i.e. C3 \* D3 became C5 \* D5, C8 \* D8, C12 \* D12, etc.). That is what is called [Relative Referencing](https://www.excel-easy.com/functions/cell-references.html)
.

[![Example Relative Referencing in Excel](https://www.challengejp.com/wp-content/uploads/2020/11/screenshot2.png)](https://www.challengejp.com/wp-content/uploads/2020/11/screenshot2.png)

Basic Calculations and Relative Referencing in Microsoft Excel

**Step 6: Microsoft Excel’s SUM Function**
------------------------------------------

Now, let’s calculate the totals for each of the columns. First, go to the last row of the table and underneath the last Product value, type in TOTAL. Use the SUM formula to compute the total values from a range of cells. Then, move one cell to the right of column C and type in “=SUM(“. Finally, left-click on the cell with the first value in the column (cell C3) and then drag it to the last value.

You will see that the formula shows “=SUM(C3:C15”. The “:” indicates that we are selecting a range of values between the cell reference to the left and the right of the colon. Close the bracket “)” and hit Enter. You can repeat the same step for the “Subtotal” and “Total” columns. You can also copy (Ctrl+c) the Excel formula you have just created and paste (Ctrl+v) underneath the remaining columns.

**Step 7: Absolute Referencing**
--------------------------------

Let’s create another column and call it “VAT”. Here, we will multiply the values in column “Subtotal” by a fixed percentage value, e.g. 20%. To do that, click on the cell J2 and type in “VAT”. Then, type in 20% in the adjacent cell K2. Finally, go back to the first cell in the VAT Column (cell F2) and type in a formula “=E3 \* $K$2”. Notice the dollar signs before the letter K and the number 2.

If you drag the cell and copy the formulas to the last row of the table, you will notice that the first part of the formula (E3) changes its reference to the current row. However, the $K$2 always stay the same. The dollar signs fix or anchor that part of the formula to a particular cell. This is what in Microsoft Excel is called absolute referencing.

Finally, create a Total column by adding Subtotal and VAT (i.e. “=E3 + F3”). If you change the VAT value in cell K2, the subtotal and total values will update accordingly.

**Step 8: Formatting in Microsoft Excel**
-----------------------------------------

It is important to present your output in a transparent and easy-to-follow way. Keep the numbers apart by changing the column widths, and use different font styles to keep the numbers apart visually. Also, use borders to visually separate the totals from the rest of the table. Likewise, fill the headers with a distinct colour.

To display your with a currency symbol, right-click on a selection of values. Then, click on ‘Format Cells’ and select the currency. You will find the most often used formatting tools in the left section of the Home tab of your Excel workbook.

[![Example Formatting Currency in Excel](https://www.challengejp.com/wp-content/uploads/2020/11/screenshot3.png)](https://www.challengejp.com/wp-content/uploads/2020/11/screenshot3.png)

Changing Currency Format in Microsoft Excel

**Step 9: How to use a V-lookup Formula**
-----------------------------------------

V-lookup function allows you to take an input from your existing spreadsheet, reference it with another data source, and return the related value. To see how it works, [download the sample Excel file](https://www.challengejp.com/wp-content/uploads/2020/12/excel_course_file_extended.xlsx)
 and click on the ‘Extended Data’ sheet. You will notice another column called VAT% (i.e. a sales tax), which has a different VAT or tax value for each product (e.g. Coffee 16.0%, Tea 12.0%, etc.).

To display the appropriate VAT or Sales Tax value, the v-lookup formula takes the look-up value (the first argument), for instance, the product name. Then, it tries to find it in the first column of the reference table (the second argument). In our example, the reference table is located in the ‘VAT Lookup’ sheet. The third argument, col index, describes the position of a column in the reference table from which the value (i.e. the relevant VAT%) will return. Leave the fourth argument (approximate match) as FALSE.

[![excel vlookup example](https://www.challengejp.com/wp-content/uploads/2020/11/excel-vlookup-example.png)](https://www.challengejp.com/wp-content/uploads/2020/11/excel-vlookup-example.png)

A Data Table with Microsoft Excel’s V-lookup Formula

**Step 10: How to create a Pivot Table in Microsoft Excel**
-----------------------------------------------------------

A pivot table is a powerful tool that will help you to present and summarise your data. To create a pivot table, select the entire sheet or data table (click on any value and hold Ctrl + A on your keyboard), but make sure to exclude the ‘Total’ row. Then, go to the ‘Insert’ (or ‘Data’ in some Excel versions) tab and select PivotTable. Finally, choose an option to add the pivot table on a new worksheet.

You will see a blank table on the left side of the newly created sheet. Also, to the right, there will be a list of fields with a grid of four rectangles beneath it. Drag the ‘Product’ field to the ‘rows’ rectangle and ‘Total’ to the values. You will now see the summary of your sales with the subtotal for each product group. You can also drag the ‘Product’ field to filters and select only one of the values. Compare your results with the pivot table in [the sample Excel file](https://www.challengejp.com/wp-content/uploads/2020/12/excel_course_file_extended.xlsx)
.

[![excel pivot table example](https://www.challengejp.com/wp-content/uploads/2020/11/excel-pivot-table-example.png)](https://www.challengejp.com/wp-content/uploads/2020/11/excel-pivot-table-example.png)

Example of an Microsoft Excel’s Pivot Table

**Microsoft Excel Beginner’s Tutorial – Summary**
-------------------------------------------------

To learn Microsoft Excel, start with a blank page and create a simple table with just three columns. Fill the first column with names (for instance, products), the second with the number of items sold, and the third with corresponding prices. To try basic calculations, add a ‘Subtotal’ column and insert a formula that multiplies the number of items by their price. Copy and paste the formulas to the bottom of the table. You can now add the values of each column together by using Microsoft Excel’s SUM formulas.

For more advanced tasks, add a VAT column. Fill this column with a formula to multiply the subtotal by a fixed VAT value. This value will only be located in one cell, so you must use absolute referencing. In other words, you need to enclose the cell reference in dollar ($) signs.

Try using V-lookup formulas to apply different VAT values to different product names. Summarise the data with a pivot table. Place the product in rows or filters, and drag the Totals into the ‘values’ rectangle. [Download the sample Excel file](https://www.challengejp.com/wp-content/uploads/2020/12/excel_course_file_extended.xlsx)
 to compare your results with this tutorial’s workbook.

**Video: Your First Steps in Excel**
------------------------------------

For more tips on starting your journey with Microsoft Excel, watch my video tutorial below:

<span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start"><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span>﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start"><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span>﻿</span>

**Get in Touch**
----------------

_[![challengejp_data_analyst](https://www.challengejp.com/wp-content/uploads/2020/07/jp_photo-300x200.jpg)](https://www.challengejp.com/about/)
Hi, my name is Jacek and I love spreadsheets! I h__ope you’ve enjoyed reading this tutorial as much as I did writing it. If you have any questions about creating spreadsheets in Microsoft Excel, don’t hesitate to **[get in touch](https://www.challengejp.com/contact/)
**._

_[**Explore my other tutorials**](https://www.challengejp.com/blog/)
 to learn more about financial modelling or data analysis. If you need further support, find out about my [**One-to-One Training**](https://www.challengejp.com/services/financial-modelling-data-training/)
 and **[Financial Modelling Services](https://www.challengejp.com/services/financial-modelling/)
**._

Learn More
----------

[Become a Self-Taught Data Analyst](https://www.challengejp.com/blog/learn-to-become-data-analyst/)
 – In this blog, I’m sharing some tips and resources I have found useful on my journey to becoming a data analyst.

[Analyse Data in Microsoft Excel with Power Query and a Pivot Table](https://www.challengejp.com/blog/how-to-analyse-data-excel-tutorial/)
 – Here, you can find an example of using more advanced functions to analyse data.

[Use Cohort Analysis to Calculate Retention and Churn Rate in Microsoft Excel](https://www.challengejp.com/blog/excel-churn-retention-cohort-analysis/)
 – This advanced tutorial will show you how to apply spreadsheets and pivot tables to analyse users’ behaviour.

[Build a Cash Flow Forecast in Microsoft Excel](https://www.challengejp.com/blog/how-to-create-forecast-cash-flow-excel/)
 – This blog introduces you to building financial models and using spreadsheets to forecast revenues and expenses.

[Use Python and Pandas for Data Consolidation and Transformation](https://www.challengejp.com/blog/python-excel-data-consolidation-transformation/)
 – This blog will show you an example of using Python scripts to combine multiple CSV or Excel files.

Tags:[Data Analytics](https://www.challengejp.com/blog/tag/data-analytics/ "Data Analytics")
[Excel Tutorial](https://www.challengejp.com/blog/tag/excel-tutorial/ "Excel Tutorial")

  

**Redirecting to FastSpring for secure payment and local tax handling in your region...**

You’ll see challengejp.onfastspring.com in your address bar.