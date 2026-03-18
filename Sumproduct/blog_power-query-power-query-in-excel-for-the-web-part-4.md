# Power Query: Power Query in Excel for the web Part 4

**Source:** https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-4/

---

[Home](https://sumproduct.com/)

\> Power Query: Power Query in Excel for the web Part 4

*   February 11, 2026

Power Query: Power Query in Excel for the web Part 4
====================================================

_Welcome to our Power Query blog.  This week, we continue to look at some of the features of Power Query in Excel for the web by looking at how to ‘Add a table from examples’._

Recently, I welcomed the arrival of more Power Query functionality to Excel for the web.  I have looked at how I can now create a query from data in the current online workbook (aka project), and this week, I will continue extracting data from other online workbooks.

It’s time to enlist the help of my imaginary salespeople (I know you’ve missed them!).  I plan to extract data from a workbook called **PQ\_StandardExpense\_CSV\_1**.  [Last week](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-3/)
, I successfully linked to a CSV file in my company’s SharePoint:

![](<Base64-Image-Removed>)

I noted that although this looks similar to the Navigator dialog in the desktop version of Excel, the options at the bottom of each dialog are not the same:

![](<Base64-Image-Removed>)

In the desktop version of Excel I can Load to the workbook, ‘Transform Data’ or Cancel.  In Excel for the web, in addition to Cancel and ‘Transform data’ I have the option to ‘Add table using examples’. 

Let’s investigate how the option ‘Add table using examples’ works in Excel for the web (spoiler alert: it doesn’t!).  I choose this option and a new dialog appears:

![](<Base64-Image-Removed>)

The ‘File origin’ and ‘File sample size’ also appeared on the previous dialog box and allow the same choices as I would have in the desktop version of Excel.  I no longer have a choice of delimiter since the commas now appear in the ‘File contents’ box.

The design of this dialog is not very user friendly: there is a large space for the ‘File contents’ and virtually no space to enter the columns.  If any messages appear, they further obscure the columns.  I also think that including the delimiter in the ‘File contents’ instead of allowing it to be specified is a design mistake.  Let’s try it anyway!

I may double-click on the heading of **Column1** to rename it to “Name”.  In the first row I begin typing “Derek Stand”:

![](<Base64-Image-Removed>)

I may choose from the options in the dropdown list.  I click on the full name, but the results are not what I expected!

![](<Base64-Image-Removed>)

It may suggest that I can see the first two \[2\] rows, but they are actually rows 2 and 3.  If I scroll to the top, I can see that the name I selected is in the first row.  However, the algorithm suggests adding the dates next, probably because they occur under “Derek Stand” in ‘File contents’.

![](<Base64-Image-Removed>)

I persist, and add a **Date** column using the plus (**+**) icon:

![](<Base64-Image-Removed>)

When I select the first date, there is a pause and the message ‘Learning values’ appears and hangs.  At this point, my first attempt is halted.  I choose Back and try again.  This time, I enter “Derek Stand” in the first two rows to see if that will help:

![](<Base64-Image-Removed>)

Nope.  Now I can’t see the columns to change them.  Time to use the Back key again.  Having established that I can only enter values in rows that exist in the File contents (with no duplication), this time I ignore the names for now and try to create the rest of the Table, beginning with **Date**:

![](<Base64-Image-Removed>)

Another ‘feature’ is that for the second column name onwards, the algorithm expects it to be in the data in ‘File contents’.  Even when the column names can be found, the process falls over for the third column.  Back again, and this time I don’t enter column names.  As long as I remember to keep scrolling back up to the first row, I manage to create a Table:

![](<Base64-Image-Removed>)

I can only assume that this functionality has been taken from the desktop version of Excel where it is available for web data and is still being developed.  For the time being, it is best avoided.  Let’s ‘Transform data’ to see what I have extracted.

![](<Base64-Image-Removed>)

Since I would expect to see only three \[3\] steps when I extract data from a CSV file in the usual way, this is definitely not more efficient.  I would normally see a Source, ‘Promoted Headers’ and a ‘Changed Type’ step.  You may expect that there will be a step for each column I created.  Not exactly.  The Source step returns the data from the ‘File contents’ box, as you might expect:

![](<Base64-Image-Removed>)

This is then followed by some very illogical steps!

*   ‘Removed top rows’: this removed a single row from the top that contained the column headers

![](<Base64-Image-Removed>)

*   ‘Inserted After Delimiter’: this added **Column2**, repeating some of the data in **Column1**

![](<Base64-Image-Removed>)

*   ‘Extracted text before delimiter’: this extracted the dates, mostly…

![](<Base64-Image-Removed>)

*   ‘Extracted text after delimiter’: which extracted the dates

![](<Base64-Image-Removed>)

*   ‘Split column by delimiter’: this seemed like the approach that should have been taken from the start

![](<Base64-Image-Removed>)

*   The final step, ‘Changed column type’, then brings us back to normality.

Suffice to say, I will not be revisiting the ‘Add table using examples’ functionality for a while.  Normal service will be resumed next time!

Come back next time for more ways to use Power Query!            

*   [Log in](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-4/#0)

[](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-4/#0 "close")

top