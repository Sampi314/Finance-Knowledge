# 7 Quick & Easy Ways to Number Rows in Excel

**Source:** https://trumpexcel.com/number-rows-in-excel

---

[Skip to content](https://trumpexcel.com/number-rows-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/number-rows-in-excel/#below-title)

**Watch Video – 7 Quick and Easy Ways to Number Rows in Excel**

When working with Excel, there are some small tasks that need to be done quite often. Knowing the ‘right way’ can save you a great deal of time.

One such simple (yet often needed) task is to number the rows of a dataset in Excel (also called the serial numbers in a dataset).

![How to Number Rows in Excel - Example dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20464%20255'%3E%3C/svg%3E)

Now if you’re thinking that one of the ways is to simply enter these serial number manually, well – you’re right!

But that’s not the best way to do it.

Imagine having hundreds or thousands of rows for which you need to enter the row number. It would be tedious – and completely unnecessary.

There are many ways to number rows in Excel, and in this tutorial, I am going to share some of the ways that I recommend and often use.

Of course, there would be more, and I will be waiting – with a coffee – in the comments area to hear from you about it.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/number-rows-in-excel/#)

How to Number Rows in Excel
---------------------------

The best way to number the rows in Excel would depend on the kind of data set that you have.

For example, you may have a continuous data set that starts from row 1, or a dataset that start from a different row. Or, you might have a dataset that has a few blank rows in it, and you only want to number the rows that are filled.

You can choose any one of the methods that work based on your dataset.

### 1\] Using Fill Handle

[Fill handle](https://trumpexcel.com/how-to-use-fill-handle-in-excel/)
 identifies a pattern from a few filled cells and can easily be used to quickly fill the entire column.

Suppose you have a dataset as shown below:

![How to Number Rows in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20465%20396'%3E%3C/svg%3E)

Here are the steps to quickly number the rows using the fill handle:

*   Enter 1 in cell A2 and 2 in cell A3.
*   Select both the cells (A2 and A3).
*   Note that there would be a small square at the bottom-right of the selection.![How to Number Rows in Excel - Fill Handle square](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20469%20135'%3E%3C/svg%3E)
*   Hover the cursor over this square, and you will notice that the cursor changes to a plus icon.![How to Number Rows in Excel - cursor changes to plus sign](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20464%20105'%3E%3C/svg%3E)
*   Double-click on the fill handle square (while the cursor is in the plus icon form) and it will automatically fill all the cells until the end of the dataset.

Note that Fill Handle automatically identifies the pattern and fill the remaining cells with that pattern. In this case, the pattern was that the numbers were getting incrementing by 1.

In case you have a blank row in the dataset, fill handle would only work till the last contiguous non-blank row.

Also, note that in case you don’t have data in the adjacent column, double-clicking the fill handle would not work. You can, however, place the cursor on the fill handle, hold the right mouse key and drag down. It will fill the cells covered by the cursor dragging.

### 2\] Using Fill Series

While Fill Handle is a quick way to number rows in Excel, Fill Series gives you a lot more control over how the numbers are entered.

Suppose you have a dataset as shown below:

![How to Number Rows in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20465%20396'%3E%3C/svg%3E)

Here are the steps to use Fill Series to number rows in Excel:

*   Enter 1 in cell A2.
*   Go to the Home tab.![Home Tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20293%20134'%3E%3C/svg%3E)
*   In the Editing Group, click on the Fill drop-down.![Fill Series Option in the editing group](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20202%20110'%3E%3C/svg%3E)
*   From the drop-down, select ‘Series..’.![Fill Series option to number rows Columns in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20181%20252'%3E%3C/svg%3E)
*   In the ‘Series’ dialog box, select ‘Columns’ in the ‘Series in’ options.![Number rows in Excel - selected columns in Fill series](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20278%20229'%3E%3C/svg%3E)
*   Specify the Stop value. In this case, since we have 26 records, we can enter 26. If you don’t enter any value, Fill Series will not work.![Specify the Stop Value in Fill Series](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20278%20229'%3E%3C/svg%3E)
*   Click OK.

This will instantly number the rows from 1 to 26.

Using ‘Fill Series’ can be useful when you’re starting by entering the row numbers. Unlike Fill Handle, it doesn’t require the adjacent columns to be filled already.

Even if you have nothing on the worksheet, Fill Series would still work.

Note: In case you have blank rows in the middle of the dataset, Fill Series would still fill the number for that row.

### 3\] Using the ROW Function

You can also use [Excel functions](https://trumpexcel.com/excel-functions/)
 to number the rows in Excel.

In the Fill Handle and Fill Series methods above, the serial number inserted is a static value. This means that if you move the row (or cut and paste it somewhere else in the dataset), the row numbering will not change accordingly.

This shortcoming can be tackled using formulas in Excel.

You can use the [ROW function](https://trumpexcel.com/excel-row-function/)
 to get the row numbering in Excel.

To get the row numbering using the ROW function, enter the following formula in the first cell and copy for all the other cells:

**\=ROW()-1**

The ROW() function gives the row number of the current row. So I have subtracted 1 from it as I started from the second row onwards. If your data starts from the 5th row, you need to use the formula =ROW()-4.

![ROW formula to enter row numbers in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20467%20257'%3E%3C/svg%3E)

The best part about using the ROW function is that it will not screw up the numberings if you delete a row in your dataset.

Since the ROW function is not referencing any cell, it will automatically (or should I say AutoMagically) adjust to give you the correct row number. Something as shown below:

![Automatically number rows in Excel when a row is deleted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20468%20296'%3E%3C/svg%3E)

Note that as soon as I delete a row, the row numbers automatically update.

Again, this would not take into account any blank records in the dataset. In case you have blank rows, it will still show the row number.

You can use the following formula to hide the row number for blank rows, but it would still not adjust the row numbers (such that the next row number is assigned to the next filled row).

**IF(ISBLANK(B2),"",ROW()-1)**

### 4\] Using the COUNTA Function

If you want to number rows in a way that only the ones that are filled get a serial number, then this method is the way to go.

It uses the [COUNTA function](https://trumpexcel.com/excel-functions/counta-function/)
 that counts the number of cells in a range that are not empty.

Suppose you have a dataset as shown below:

![Number rows in Excel - Using COUNTA function to insert serial numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20464%20436'%3E%3C/svg%3E)

Note that there are blank rows in the above-shown dataset.

Here is the formula that will number the rows without numbering the blank rows.

**\=IF(ISBLANK(B2),"",COUNTA($B$2:B2))**

The [IF function](https://trumpexcel.com/excel-if-function/)
 checks whether the adjacent cell in column B is empty or not. If it’s empty, it returns a blank, but if it’s not, it returns the count of all the filled cells till that cell.

### 5\] Using SUBTOTAL For Filtered Data

Sometimes, you may have a huge dataset, where you want to filter the data and then copy and paste the filtered data into a separate sheet.

If you use any of the methods shown above so far, you will notice that the row numbers remain the same. This means that when you copy the filtered data, you will have to update the row numbering.

In such cases, the SUBTOTAL function can automatically update the row numbers. Even when you filter the data set, the row numbers will remain intact.

Let me show you exactly how it works with an example.

Suppose you have a dataset as shown below:

![Data set for SUBTOTAL functon - insert serial numbers in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20464%20410'%3E%3C/svg%3E)

If I filter this data based on Product A sales, you will get something as shown below:

![Filtered Data row numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20467%20305'%3E%3C/svg%3E)

Note that the serial numbers in Column A are also filtered. So now, you only see the numbers for the rows that are visible.

While this is the expected behavior, in case you want to get a serial row numbering – so that you can simply copy and paste this data somewhere else – you can use the SUBTOTAL function.

Here is the SUBTOTAL function that will make sure that even the filtered data has continuous row numbering.

**\=SUBTOTAL(3,$B$2:B2)**

The 3 in the SUBTOTAL function specifies using the COUNTA function. The second argument is the range on which COUNTA function is applied.

The benefit of the SUBTOTAL function is that it dynamically updates when you filter the data (as shown below):

![Subtotal automatically numbers rows in Excel when filtered](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20468%20376'%3E%3C/svg%3E)

Note that even when the data is filtered, the row numbering update and remains continuous.

### 6\] Creating an Excel Table

[Excel Table](https://trumpexcel.com/excel-table/)
 is a great tool that you must use when working with tabular data. It makes managing and using data a lot easier.

This is also my favorite method among all the techniques shown in this tutorial.

Let me first show you the right way to number the rows using an Excel Table:

*   Select the entire dataset.
*   Go to the Insert Tab.![insert Tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20205%20133'%3E%3C/svg%3E)
*   Click on the Table icon (you can also use the keyboard shortcut Control + T).![create a Table from the Ribbon Icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20205%20133'%3E%3C/svg%3E)
*   In the Create Table dialog box, make sure the range is correct.![Check Table Range in the dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20230%20151'%3E%3C/svg%3E)
*   Click OK. This will convert your tabular data into an Excel Table.
*   In cell A2, enter the following formula. Note that as soon as you enter the formula, it will automatically fill it in all the cells in that column (you can read more about [calculated columns here](https://support.office.com/en-gb/article/Use-calculated-columns-in-an-Excel-table-873fbac6-7110-4300-8f6f-aafa2ea11ce8?CorrelationId=82339b42-829b-4022-b65b-5aacc5c81d9e&ui=en-US&rs=en-GB&ad=GB&ocmsassetID=HA010342380)
    ).
    
     =ROW()-ROW(Table2\[#Headers\])
    

![Number Rows in Excel - Calculated Column in Excel table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20469%20282'%3E%3C/svg%3E)

Note that in the formula above, I have used **Table2**, as that is the name of my Excel table. You can replace Table2 with the name of the table you have.

There are some added benefits of using an Excel Table while numbering rows in Excel:

1.  Since Excel Table automatically inserts the formula in the entire column, it works when you insert a new row in the Table. This means that when you insert/delete rows in an Excel Table, the row numbering would automatically update (as shown below).![Inserting Row Numbers in an Excel Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20468%20296'%3E%3C/svg%3E)
2.  If you add more rows to the data, Excel Table would automatically expand to include this data as a part of the table. And since the formulas automatically update in the calculated columns, it would insert the row number for the newly inserted row (as shown below).![Excel Table - Automatically Add row Number on adding a row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20468%20256'%3E%3C/svg%3E)

### 7\] Adding 1 to the Previous Row Number

This is a simple method that works.

The idea is to add 1 to the previous row number (the number in the cell above). This will make sure that subsequent rows get a number that is incremented by 1.

Suppose you have a dataset as shown below:

![How to Number Rows in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20465%20396'%3E%3C/svg%3E)

Here are the steps to enter row numbers using this method:

*   In the cell in the first row, enter 1 manually. In this case, it’s in cell A2.
*   In cell A3, enter the formula, =A2+1
*   Copy and paste the formula for all the cells in the column.

![Add 1 to insert row numbers in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20466%20201'%3E%3C/svg%3E)

The above steps would enter serial numbers in all the cells in the column. In case there are any blank rows, this would still insert the row number for it.

Also note that in case you insert a new row, the row number would not update. In case you delete a row, all the cells below the deleted row would show a reference error.

These are some quick ways you can use to [insert serial numbers](https://trumpexcel.com/number-rows-in-excel/)
 in tabular data in Excel.

In case you are using any other method, do share it with me in the comments section.

**You May Also Like the Following Excel Tutorials:**

*   [Delete Blank Rows in Excel (with and without VBA)](https://trumpexcel.com/delete-blank-rows-excel/)
    .
*   [How to Insert Multiple Rows in Excel (4 Methods](https://trumpexcel.com/how-to-insert-multiple-rows-in-excel/)
    ).
*   [How to Split Multiple Lines in a Cell into a Separate Cells / Columns](https://trumpexcel.com/split-multiple-lines/)
    .
*   [7 Amazing Things Excel Text to Columns Can Do For You](https://trumpexcel.com/excel-text-to-columns-examples/)
    .
*   [Highlight EVERY Other ROW in Excel.](https://trumpexcel.com/highlight-every-other-row-excel/)
    
*   [How to Compare Two Columns in Excel.](https://trumpexcel.com/compare-two-columns/)
    
*   [Insert New Columns in Excel](https://trumpexcel.com/insert-columns-in-excel/)
    
*   [SEQUENCE Function in Excel](https://trumpexcel.com/excel-functions/sequence/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

13 thoughts on “7 Quick & Easy Ways to Number Rows in Excel”
------------------------------------------------------------

1.  The information shared here is good, however I need the serial numbers to start from 1 again after a blank. Is that possible. Say for ex. if there are 5 rows and a space, then 11 rows, then space, then 6 rows….I need 1 to 5 serial number, then after space, again 1 to 11 as serial numbers, and similarly 1 to 6 as serial number. Please advise if this is possible.
    
    [Reply](https://trumpexcel.com/number-rows-in-excel/#comment-14376)
    
2.  Sumit,  
    The coverage and explanation are superb. I like the ROW() fn. I used to write “=ROW($A1)” and copy down, but when deleting rows the serial does not adjust automatically. Now I know I can use “=ROW()-T” where T is the no. of top rows above my starting cell.
    
    [Reply](https://trumpexcel.com/number-rows-in-excel/#comment-14074)
    
3.  The explantion is good but video visual is unable to see if that would been there it would help beginers to understand easily.
    
    [Reply](https://trumpexcel.com/number-rows-in-excel/#comment-13906)
    
4.  excellent
    
    [Reply](https://trumpexcel.com/number-rows-in-excel/#comment-12230)
    
5.  I need help to add rows to eparate a strig of names which has norow spacing in between. I need to add rows to separate the names.
    
    [Reply](https://trumpexcel.com/number-rows-in-excel/#comment-12116)
    
6.  How to add cells in a sheet row
    
    [Reply](https://trumpexcel.com/number-rows-in-excel/#comment-11539)
    
7.  Thanks!! 😀
    
    [Reply](https://trumpexcel.com/number-rows-in-excel/#comment-11201)
    
8.  This is quite detailed and good. But I have a few difficulties: I want to be able to customize my numbering; that is, instead of just 1, 2, 3, … suppose I want 1.01, 1.02, 1.03, …, how can I achieve that?
    
    [Reply](https://trumpexcel.com/number-rows-in-excel/#comment-11160)
    
9.  COUNTA saved me!!! thanx a bunch!!!!!!
    
    [Reply](https://trumpexcel.com/number-rows-in-excel/#comment-11054)
    
10.  Thank you! I was looking everywhere for a way to make my rows auto-update their count when I inserted a new cell – the Microsoft Help indicated that I should make a table but it did not provide the helpful code you did (with your sixth tip – also my favourite!).
    
    [Reply](https://trumpexcel.com/number-rows-in-excel/#comment-10865)
    
11.  Another one, using structured references and building a dynamic range:
    
    \=ROWS(INDEX(\[AnyField\],1):\[@AnyField\])
    
    AnyField is the name of a field of the range (anyone).
    
    [Reply](https://trumpexcel.com/number-rows-in-excel/#comment-9912)
    
12.  Great post, bringing all those ideas and techniques together.
    
    In no. 7\] I get round problems inserting or deleting rows by using the OFFSET function and referencing the current cell (or row) and a row offset of -1. That way it always works when rows are inserted or deleted.
    
    [Reply](https://trumpexcel.com/number-rows-in-excel/#comment-9909)
    
    *   Hi Wainers, can you explain yourself more clearly please?  
        I’m kind of interested in solution number 7 because it seems the simplest one, and your addition seems very valuable… Only I don’t understand what the formula should look like at all. 🙂
        
        Can’t understand that something as simple as numbering should require complicated formulas…
        
        [Reply](https://trumpexcel.com/number-rows-in-excel/#comment-11454)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/number-rows-in-excel/#respond)

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