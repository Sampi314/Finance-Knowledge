# Applying Conditional Formatting to a Pivot Table in Excel

**Source:** https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel

---

[Skip to content](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/#below-title)

Applying [conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
 in a Pivot Table can be a bit tricky.

Given that Pivot Tables are so dynamic and the data in the backend can change often, you need to know the right way to use conditional formatting in a pivot table in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/#)

The Wrong Way to Apply Conditional Formatting to a Pivot Table
--------------------------------------------------------------

Let’s first look at the regular way of applying conditional formatting in a pivot table.

Suppose you have a pivot table as shown below:

![Apply Conditional Formatting in a Pivot Table in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20449%20289'%3E%3C/svg%3E)

In the above dataset, the date is in the rows and we have store sales data in columns.

Here is the regular way of applying conditional formatting to any dataset:

*   Select the data (in this case, we are applying the conditional formatting to B5:D14).
*   Go to Home –> Conditional Formatting –> Top/Bottom Rules –> Above Average.![Apply Conditional Formatting in a Pivot Table in Excel - Above Average](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20484%20442'%3E%3C/svg%3E)
*   Specify the format (I am using “Green Fill with Dard Green Text”).![Apply Conditional Formatting in a Pivot Table in Excel - Above Average Rule](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20370%20137'%3E%3C/svg%3E)
*   Click OK.

This will apply the conditional formatting as shown below:

![Apply Conditional Formatting in a Pivot Table in Excel - Data Highlight](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20444%20290'%3E%3C/svg%3E)

All the data points which are above the average of the entire dataset have been highlighted.

The issue with this method is that it has applied the conditional format to a fixed range of cells (B5:D14). If you add data in the backend and refresh this pivot table, the conditional formatting would not get applied to it.

For example, I go back to the dataset and add data for one more date (11 January 2015). This is what I get when I refresh the Pivot Table.

![Apply Conditional Formatting in a Pivot Table in Excel - New Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20445%20319'%3E%3C/svg%3E)

As you can see in the pic above, the data for 11 January 2015 doesn’t get highlighted (while it should as the values for Store 1 and Store 3 are above average).

The reason, as I mentioned above, is that the conditional formatting has been applied on a fixed range (B5:D14), and it doesn’t get extended to new data in the pivot table.

The Right Way to Apply Conditional Formatting to a Pivot Table
--------------------------------------------------------------

Here are two methods to make sure conditional formatting works even when there is new data in the backend.

### Method 1 – Using Pivot Table Formatting Icon

This method uses the Pivot Table Formatting Options icon that appears as soon as you apply conditional formatting in a pivot table.

Here are the steps to do this:

*   Select the data on which you want to apply conditional formatting.
*   Go to Home –> Conditional Formatting –> Top/Bottom Rules –> Above Average.
*   Specify the format (I am using “Green Fill with Dard Green Text”).
*   Click Ok.
    *   When you follow the above steps, it applies the conditional formatting on the data set. On the bottom right of the data set, you will see the Formatting Options icon:

![Apply Conditional Formatting in a Pivot Table in Excel - Formatting Option Icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20441%20285'%3E%3C/svg%3E)

*   Click on the icon. It will show three options in a drop down:
    *   Selected Cells (which would be selected by default).
    *   All cells showing “Sum of Revenue” Values.
    *   All cells showing “Sum of Revenue” values for “Date” and “Store”.![Apply Conditional Formatting in a Pivot Table in Excel - Formatting Options Dropdown](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20756%20366'%3E%3C/svg%3E)
*   Select the third option – All cells showing “Sum of Revenue” values for “Date” and “Store”.![Apply Conditional Formatting in a Pivot Table in Excel - third option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20744%20371'%3E%3C/svg%3E)

Now when you add any data in the back end and refresh the pivot table, the additional data would automatically be covered by conditional formatting.

**Understanding the three options:**

*   _Selected Cells:_ This is the default option where conditional formatting in applied only on the selected cells.
*   _All cells showing “Sum of Revenue” Values:_ In this option, it considers all the cells that show the Sum of Revenue values (or whatever data you have in the values section of the pivot table).
    *   The issue with this option is that it will also cover the Grand Total values and apply conditional formatting to it.
*   _All cells showing “Sum of Revenue” values for “Date” and “Store”__:_ This is the best option in this case. It applies the conditional formatting to all the values (excluding Grand Totals) for the combination of Date and Store. Even if you add more data in the back end, this option will take care of it.

_**Note:**_

*   The Formatting Options icon is visible right after you apply conditional formatting on the data set. If goes away if you do something else (edit a cell or change font/alignment, etc.).
*   Conditional formatting goes away if you change the row/column fields. For example, if you remove Date field and apply it again, conditional formatting would be lost.

### Method 2 – Using Conditional Formatting Rules Manager

Apart from using the Formatting Options icon, you can also use the Conditional Formatting Rules Manager dialogue box to apply conditional formatting in a pivot table.

This method is useful when you have already applied the conditional formatting and you want to change the rules.

Here is how to do it:

*   Select the data on which you want to apply conditional formatting.
*   Go to Home –> Conditional Formatting –> Top/Bottom Rules –> Above Average.![Apply Conditional Formatting in a Pivot Table in Excel - Above Average](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20484%20442'%3E%3C/svg%3E)
*   Specify the format (I am using “Green Fill with Dard Green Text”).![Apply Conditional Formatting in a Pivot Table in Excel - Above Average Rule](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20370%20137'%3E%3C/svg%3E)
*   Click Ok. This will apply the conditional formatting to the selected cells.
*   Go to Home –> Conditional Formatting –> Manage Rules.![Apply Conditional Formatting in a Pivot Table in Excel - Manage Rules](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20323%20408'%3E%3C/svg%3E)
*   In the Conditional Formatting Rules Manager, select the rule you want to edit and click on Edit Rule button.![Apply Conditional Formatting in a Pivot Table in Excel - Edit Rule](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20638%20305'%3E%3C/svg%3E)
*   In the Edit Rule dialogue box, you will see the same three options:
    *   Selected Cells.
    *   All cells showing “Sum of Revenue” Values.
    *   All cells showing “Sum of Revenue” values for “Date” and “Store”.![Apply Conditional Formatting in a Pivot Table in Excel - Edit Rule Dialogue](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20503%20452'%3E%3C/svg%3E)
*   Select the third option and click OK.

This will apply the conditional formatting to all the cells for ‘Date’ and ‘Store’ fields. Even if you change the backend data (add more store data or date data), the conditional formatting would be functional.

_**Note:**_ Conditional formatting goes away if you change the row/column fields. For example, if you remove Date field and apply it again, conditional formatting would be lost.

**You May Also Like the Following Excel Tutorials:**

*   [Highlight Every Other Row in Excel using Conditional Formatting](https://trumpexcel.com/highlight-every-other-row-excel/)
    .
*   [Creating a Pivot Table in Excel – A Step by Step Tutorial](https://trumpexcel.com/creating-excel-pivot-table/)
    .
*   [Preparing Source Data For Pivot Table.](https://trumpexcel.com/source-data-for-pivot-table/)
    
*   [How to Group Numbers in Pivot Table in Excel.](https://trumpexcel.com/group-numbers-in-pivot-table/)
    
*   [How to Group Dates in Pivot Tables in Excel.](https://trumpexcel.com/group-dates-in-pivot-tables-excel/)
    
*   [How to Refresh Pivot Table in Excel](https://trumpexcel.com/refresh-pivot-table-excel/)
    .
*   [Delete Pivot Table in Excel](https://trumpexcel.com/delete-pivot-table/)
    .
*   [Using Slicers in Excel Pivot Table.](https://trumpexcel.com/slicers-excel-pivot-table/)
    
*   [How to Add and Use an Excel Pivot Table Calculated Field.](https://trumpexcel.com/excel-pivot-table-calculated-field/)
    
*   [Pivot Cache in Excel – What Is It and How to Best Use It?](https://trumpexcel.com/pivot-cache-excel/)
    
*   [How to Replace Blank Cells with Zeros in Excel Pivot Tables.](https://trumpexcel.com/replace-blank-cells-with-zeros-excel-pivot-tables/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

11 thoughts on “How to Apply Conditional Formatting in a Pivot Table in Excel”
------------------------------------------------------------------------------

1.  Very useful article. I used Method 2 to fix the conditional formatting that I had already implemented. Thank you!
    
    [Reply](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/#comment-33239)
    
2.  hi there! Im on a mac and I dont show the same options when I click ‘edit rule’ can you help navigate me on how to get my cond. formatting to stick to my pivots on a mac?
    
    [Reply](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/#comment-14673)
    
3.  This is helpful
    
    [Reply](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/#comment-12985)
    
4.  Dear brother Sumit, you are really amazing. You did great job by sharing your knowledge… I strongly believe in sharing knowledge. Sincere appreciation. God bless you dear… I would like to interact with you for Business and personal related requirements, if possible, you may whats up your number on my whats up number 00966535084476. Sanjeeb Rath
    
    [Reply](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/#comment-12289)
    
5.  Thank You for posting this.
    
    [Reply](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/#comment-11758)
    
6.  I’m trying to conditional format my shared sites. This reporting is different there are no values meaning counting. We are actually reporting site names. Its hard could you help?
    
    [Reply](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/#comment-10834)
    
7.  Help! I’m not seeing the icon or the option in ‘Edit Rule’ you are referring to. Is there another route?  
    I’m in Excel 2013 and I am using “Use a formula to determine which cells to format”, if one of those makes he difference.
    
    [Reply](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/#comment-8874)
    
8.  Special thanks, same as usual it was wonderful. wish u the best wherever you are .
    
    [Reply](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/#comment-3257)
    
9.  i would like your help with my data of vehicles that i am having problem with doing pivot line chart
    
    [Reply](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/#comment-2639)
    
10.  Nice tip. I learned something new today!
    
    [Reply](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/#comment-2627)
    
    *   Thanks for commenting Mike.. Glad you found this useful 🙂
        
        [Reply](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/#comment-2628)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/#respond)

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