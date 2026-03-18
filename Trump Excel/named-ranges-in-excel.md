# How to Create Named Ranges in Excel (A Step-by-step Guide)

**Source:** https://trumpexcel.com/named-ranges-in-excel

---

[Skip to content](https://trumpexcel.com/named-ranges-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/named-ranges-in-excel/#below-title)

_What’s in the name?_

If you are working with Excel spreadsheets, it could mean a lot of time saving and efficiency.

In this tutorial, you’ll learn how to create Named Ranges in Excel and how to use it to save time.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/named-ranges-in-excel/#)

Named Ranges in Excel – An Introduction  

------------------------------------------

If someone has to call me or refer to me, they will use my name (instead of saying a male is staying in so and so place with so and so height and weight).

Right?

Similarly, in Excel, you can give a name to a cell or a range of cells.

Now, instead of using the cell reference (such as A1 or A1:A10), you can simply use the name that you assigned to it.

For example, suppose you have a data set as shown below:

![Creating Named Ranges in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20406%20285'%3E%3C/svg%3E)

In this data set, if you have to refer to the range that has the Date, you will have to use A2:A11 in formulas. Similarly, for Sales Rep and Sales, you will have to use B2:B11 and C2:C11.

While it’s alright when you only have a couple of data points, but in case you huge complex data sets, using cell references to refer to data could be time-consuming.

Excel Named Ranges makes it easy to refer to data sets in Excel.

You can create a named range in Excel for each data category, and then use that name instead of the cell references. For example, dates can be named ‘Date’, Sales Rep data can be named ‘SalesRep’ and sales data can be named ‘Sales’.

![Creating Named Ranges in Excel - named ranges created](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20421%20356'%3E%3C/svg%3E)

You can also create a name for a single cell. For example, if you have the sales commission percentage in a cell, you can name that cell as ‘Commission’.

Benefits of Creating Named Ranges in Excel
------------------------------------------

Here are the benefits of using named ranges in Excel.

### Use Names instead of Cell References

When you create Named Ranges in Excel, you can use these names instead of the [cell references](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
.

For example, you can use =SUM(SALES) instead of =SUM(C2:C11) for the above data set.

Have a look at ṭhe formulas listed below. Instead of using cell references, I have used the Named Ranges.

*   Number of sales with value more than 500: \=[COUNTIF](https://trumpexcel.com/excel-countif-function/)
    (Sales,”>500″)
*   Sum of all the sales done by Tom: =SUMIF(SalesRep,”Tom”,Sales)
*   Commission earned by Joe (sales by Joe multiplied by commission percentage):  
    \=[SUMIF](https://trumpexcel.com/excel-sumif-function/)
    (SalesRep,”Joe”,Sales)\*Commission

You would agree that these formulas are easy to create and easy to understand (especially when you share it with someone else or revisit it yourself.

### No Need to Go Back to the Dataset to Select Cells

Another significant benefit of using Named Ranges in Excel is that you don’t need to go back and select the cell ranges.

You can just type a couple of alphabets of that named range and Excel will show the matching named ranges (as shown below):

![Creating Named Ranges in Excel - Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20144'%3E%3C/svg%3E)

### Named Ranges Make Formulas Dynamic

By using Named Ranges in Excel, you can make [Excel formulas](https://trumpexcel.com/excel-functions/)
 dynamic.

For example, in the case of sales commission, instead of using the value 2.5%, you can use the Named Range.

Now, if your company later decides to increase the commission to 3%, you can simply update the Named Range, and all the calculation would automatically update to reflect the new commission.

How to Create Named Ranges in Excel
-----------------------------------

Here are three ways to create Named Ranges in Excel:

### Method #1 –  Using Define Name

Here are the steps to create Named Ranges in Excel using Define Name:

*   Select the range for which you want to create a Named Range in Excel.![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20453%20316'%3E%3C/svg%3E)
*   Go to Formulas –> Define Name.![How to Create Named Ranges in Excel - Define Name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20135'%3E%3C/svg%3E)
*   In the New Name dialogue box, type the Name you wish to assign to the selected data range. You can specify the scope as the entire workbook or a specific worksheet, If you select a particular sheet, the name would not be available on other sheets.![Creating Named Ranges in Excel - Define name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20232'%3E%3C/svg%3E)
*   Click OK.

This will create a Named Range SALESREP.

### Method #2: Using the Name Box

*   Select the range for which you want to create a name (do not select headers).
*   Go to the [Name Box on the left of the Formula bar](https://trumpexcel.com/name-box-excel/)
     and Type the name of the with which you want to create the Named Range.![How to Create Named Ranges in Excel - Name Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20352%2041'%3E%3C/svg%3E)
*   Note that the Name created here will be available for the entire Workbook. If you wish to restrict it to a worksheet, use Method 1.

### Method #3: Using Create From Selection Option

This is the recommended way when you have data in tabular form, and you want to create named range for each column/row.

For example, in the dataset below, if you want to quickly create three named ranges (Date, Sales\_Rep, and Sales), then you can use the method shown below.

![Creating Named Ranges in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20406%20285'%3E%3C/svg%3E)

Here are the steps to quickly create named ranges from a dataset:

*   Select the entire data set (including the headers).
*   Go to Formulas –> Create from Selection (_Keyboard shortcut – Control + Shift + F3_). It will open the ‘Create Names from Selection’ dialogue box.![How to Create Named Ranges in Excel - Create from Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20438%20125'%3E%3C/svg%3E)
*   In the Create Names from Selection dialogue box, check the options where you have the headers. In this case, we select top row only as the header is in the top row. If you have headers in both top row and left column, you can choose both. Similarly, if your data is arranged when the headers are in the left column only, then you only check the Left Column option.![How to Create Named Ranges in Excel - Top Row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20269%20182'%3E%3C/svg%3E)

This will create three Named Ranges – Date, Sales\_Rep, and Sales.

Note that it automatically picks up names from the headers. If there are any space between words, it inserts an underscore (as you can’t have spaces in named ranges).

### Naming Convention for Named Ranges in Excel

There are certain naming rules you need to know while creating Named Ranges in Excel:

*   The first character of a Named Range should be a letter and underscore character(\_), or a backslash(\\). If it’s anything else, it will show an error. The remaining characters can be letters, numbers, special characters, period, or underscore.
*   You can not use names that also represent cell references in Excel. For example, you can’t use AB1 as it is also a cell reference.
*   You can’t use spaces while creating named ranges. For example, you can’t have Sales Rep as a named range. If you want to combine two words and create a Named Range, use an underscore, period or uppercase characters to create it. For example, you can have Sales\_Rep, SalesRep, or SalesRep.
    *   While creating named ranges, Excel treats uppercase and lowercase the same way. For example, if you create a named range SALES, then you will not be able to create another named range such as ‘sales’ or ‘Sales’.
*   A Named Range can be up to 255 characters long.

Too Many Named Ranges in Excel? Don’t Worry
-------------------------------------------

Sometimes in large data sets and complex models, you may end up creating a lot of Named Ranges in Excel.

What if you don’t remember the name of the Named Range you created?

_Don’t worry_ – here are some useful tips.

### Getting the Names of All the Named Ranges

Here are the steps to get a list of all the named ranges you created:

*   Go to the Formulas tab.
*   In the Defined Named group, click on Use in Formula.![Creating Named Ranges in Excel - Use in Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20129'%3E%3C/svg%3E)
*   Click on ‘Paste Names’. ![Creating Named Ranges in Excel - Paste Names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20430%20179'%3E%3C/svg%3E)

This will give you a list of all the Named Ranges in that workbook. To use a named range (in formulas or a cell), double click on it.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20257%20199'%3E%3C/svg%3E)

### Displaying the Matching Named Ranges

*   If you have some idea about the Name, type a few initial characters, and Excel will show a drop down of the matching names.![How to Create Named Ranges in Excel - Named Range Suggest](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20234%2096'%3E%3C/svg%3E)

How to Edit Named Ranges in Excel
---------------------------------

If you have already created a Named Range, you can edit it using the following steps:

*   Go to the Formulas tab and click on Name Manager.![Creating Named Ranges in Excel - Name Manager](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20446%20124'%3E%3C/svg%3E)
*   The Name Manager dialog box will list all the Named Ranges in that workbook. Double click on the Named Range that you want to edit.![Creating Named Ranges in Excel - Name Manager Edit](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20552%20432'%3E%3C/svg%3E)
*   In the Edit Name dialog box, make the changes.![Creating Named Ranges in Excel - Edit Name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20302%20232'%3E%3C/svg%3E)
*   Click OK.
*   Close the Name Manager dialog box.

Useful Named Range Shortcuts (the Power of F3)
----------------------------------------------

Here are some useful [keyboard shortcuts](https://trumpexcel.com/excel-keyboard-shortcuts/)
 that will come handy when you are working with Named Ranges in Excel:

*   To get a list of all the Named Ranges and pasting it in Formula: **F3**
*   To create new name using Name Manager Dialogue Box: **Control + F3**
*   To create Named Ranges from Selection: **Control + Shift + F3**

Creating Dynamic Named Ranges in Excel
--------------------------------------

So far in this tutorial, we have created static Named Ranges.

This means that these Named Ranges would always refer to the same dataset.

For example, if A1:A10 has been named as ‘Sales’, it would always refer to A1:A10.

If you add more sales data, then you would have to manually go and update the reference in the named range.

In the world of ever-expanding data sets, this may end up taking up a lot of your time. Every time you get new data, you may have to update the Named Ranges in Excel.

To tackle this issue, we can create Dynamic Named Ranges in Excel that would automatically account for additional data and include it in the existing Named Range.

For example, For example, if I add two additional sales data points, a dynamic named range would automatically refer to A1:A12.

![Creating Named Ranges in Excel - Dynamic Named Ranges in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20241%20232'%3E%3C/svg%3E)

This kind of Dynamic Named Range can be created by using [Excel INDEX function](https://trumpexcel.com/excel-index-function/)
. Instead of specifying the cell references while creating the Named Range, we specify the formula. The formula automatically updated when the data is added or deleted.

Let’s see how to create Dynamic Named Ranges in Excel.

Suppose we have the sales data in cell A2:A11.

![Creating Named Ranges in Excel - Dynamic Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20123%20313'%3E%3C/svg%3E)

Here are the steps to create Dynamic Named Ranges in Excel:

1.  1.  Go to the Formula tab and click on Define Name.![Dynamic Named Ranges Using INDEX Function in Excel - Defined Name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20451%20127'%3E%3C/svg%3E)
    2.  In the New Name dialogue box type the following:
        *   Name: Sales
        *   Scope: Workbook
        *   Refers to: \=$A$2:INDEX($A$2:$A$100,COUNTIF($A$2:$A$100,”<>”&””))![Name New dialog box to created a named range in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20311%20243'%3E%3C/svg%3E)
    3.  Click OK.

Done!

You now have a dynamic named range with the name ‘Sales’. This would automatically update whenever you add data to it or remove data from it.

### How does Dynamic Named Ranges Work?

To explain how this work, you need to know a bit more about Excel INDEX function.

Most people use INDEX to return a value from a list based on the row and column number.

But the INDEX function also has another side to it.

It can be used to **return a cell reference** when it is used as a part of a cell reference.

For example, here is the formula that we have used to create a dynamic named range:

\=$A$2:INDEX($A$2:$A$100,COUNTIF($A$2:$A$100,"<>"&""))

INDEX($A$2:$A$100,COUNTIF($A$2:$A$100,”<>”&””) –> This part of the formula is expected to return a value (which would be the 10th value from the list, considering there are ten items).

However, when used in front of a reference (=**$A$2:**INDEX($A$2:$A$100,COUNTIF($A$2:$A$100,”<>”&””))) it returns the reference to the cell instead of the value.

Hence, here it returns \=$A$2:$A$11

If we add two additional values to the sales column, it would then return \=$A$2:$A$13

When you add new data to the list, [Excel COUNTIF](https://trumpexcel.com/excel-countif-function/)
 function returns the number of non-blank cells in the data. This number is used by the INDEX function to fetch the cell reference of the last item in the list.

**Note:**

*   This would only work if there are no blank cells in the data.
*   In the example taken above, I have assigned a large number of cells (A2:A100) for the Named Range formula. You can adjust this based on your data set.

You can also use [OFFSET function](https://trumpexcel.com/excel-offset-function/)
 to create a Dynamic Named Ranges in Excel, however, since OFFSET function is [volatile](https://trumpexcel.com/excel-volatile-formulas/)
, it may lead a [slow Excel workbook](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/)
. INDEX, on the other hand, is semi-volatile, which makes it a better choice to create Dynamic Named Ranges in Excel.

**You may also like the following Excel resources:**

*   [Free Excel Templates](https://trumpexcel.com/free-excel-templates/)
    .
*   [Free Online Excel Training](https://trumpexcel.com/)
     (7-Part Online Video Course).
*   [Useful Excel Macro Code Examples](https://trumpexcel.com/excel-macro-examples/)
    .
*   [10 Advanced Excel VLOOKUP Examples](https://trumpexcel.com/excel-vlookup-function/)
    .
*   [Creating a Drop Down List in Excel](https://trumpexcel.com/excel-drop-down-list/)
    .
*   [Creating a Named Range in Google Sheets](https://productivityspot.com/named-ranges-in-google-sheets/)
    .
*   [How to Reference Another Sheet or Workbook in Excel](https://trumpexcel.com/reference-another-sheet-or-workbook-in-excel/)
    
*   [How to Delete Named Range in Excel?](https://trumpexcel.com/delete-named-range-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

11 thoughts on “How to Create Named Ranges in Excel”
----------------------------------------------------

1.  excellent, valid and clear information
    
    [Reply](https://trumpexcel.com/named-ranges-in-excel/#comment-14423)
    
2.  Sumit..you mentioned that the offset command may make excel slow. Please share the command nevertheless and Offset command is meant to be used in these situations while defining dynamic ranges isnt it.
    
    [Reply](https://trumpexcel.com/named-ranges-in-excel/#comment-13855)
    
3.  I am working on a spreadsheet created by another person. They created about 500 dynamic named ranges using OFFSET. I’d like to modify the named range definitions but I’d rather not have to do all 500 individually. Is there a way to use Find/Replace and automatically change the formula which defines the named range?
    
    [Reply](https://trumpexcel.com/named-ranges-in-excel/#comment-13264)
    
    *   That would entirely depend on how they were done. I often use a placeholder when using Find/Replace on a large section of formulas. Replace the bad section with “XYZXYZ” or similar. The formula may error out if replacing more than one section this way.
        
        [Reply](https://trumpexcel.com/named-ranges-in-excel/#comment-13697)
        
4.  I use dynamic named ranges a lot for source data used in pivots, like described in this article. But sometimes when i copy files, the pivot source data referencing the dynamic range is linked to the original file.  
    Do others experience this or have an idea about why this happens?
    
    [Reply](https://trumpexcel.com/named-ranges-in-excel/#comment-9068)
    
5.  Hi,
    
    For named dynamic range i would recommend using “table”.  
    With table no need to define names as they are made by excel itself and no need to define some complex formula to define the range.
    
    i.e. Let say table is named Sales with 2 columns Salesman and Amount, i can easily refer the table as Excel can autocomplete for me the names. So i can have very readable formulas=SUMIF(Sales\[Salesman\];”joe”;Sales\[Amount\]).  
    As you can see i address the column “Salesman” in the table “Sale” with “Sales\[Salesman\]”
    
    [Reply](https://trumpexcel.com/named-ranges-in-excel/#comment-9013)
    
    *   Hey.. Thanks for sharing.. Yes Excel Tables are great too. It’s easy to create and use. And structured references make it easy as well.
        
        There are, however, a few differences that make Named Ranges useful. For example, you can not use a structured reference in conditional formatting formula. Also, with named ranges, you can create formulas that can result in the values of named ranges. Also you can use named ranges to get intersection of ranges, which can not be done with Tables.
        
        You can read more about tables here: [https://trumpexcel.com/excel-table/](https://trumpexcel.com/excel-table/)
        
        [Reply](https://trumpexcel.com/named-ranges-in-excel/#comment-9015)
        
        *   What do you do in case of blanks in between. Will it make sense to add the number of blank cells at the end of the countif to get the desired range.
            
            [Reply](https://trumpexcel.com/named-ranges-in-excel/#comment-13854)
            
6.  I want to name a range but not in this way. I did it years ago but forgot. I was able to celect a range of cells and name them in such a way that you could read the title in the background of all the selected cells. EG “WEEK 7” would be displayed behined those selected cells. Help appreaciated 🙂
    
    [Reply](https://trumpexcel.com/named-ranges-in-excel/#comment-2583)
    
    *   reduce the zoom to less than 40%
        
        [Reply](https://trumpexcel.com/named-ranges-in-excel/#comment-3503)
        
7.  helpful….  
    very nicely explained…
    
    [Reply](https://trumpexcel.com/named-ranges-in-excel/#comment-1324)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/named-ranges-in-excel/#respond)

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