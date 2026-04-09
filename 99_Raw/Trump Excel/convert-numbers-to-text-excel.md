# How to Convert Numbers to Text in Excel - 4 Super Easy Ways

**Source:** https://trumpexcel.com/convert-numbers-to-text-excel

---

[Skip to content](https://trumpexcel.com/convert-numbers-to-text-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/convert-numbers-to-text-excel/#below-title)

Excel is a great tool which can be used for data entry, as a database, and to analyze data and [create dashboards](https://trumpexcel.com/creating-excel-dashboard/)
 and reports.

While most of the in-built features and default settings are meant to be useful and save time for the users, sometimes, you may want to change things a little.

Converting your numbers into text is one such scenario.

In this tutorial, I will show you some easy ways to **quickly convert numbers to text in Excel**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/convert-numbers-to-text-excel/#)

Why Convert Numbers to Text in Excel?
-------------------------------------

When working with numbers in Excel, it’s best to keep these as numbers only. But in some cases, having a number could actually be a problem.

Lets look at a couple of scenarios where having numbers creates issues for the users.

### **Keeping Leading Zeros**

For example, if you enter 001 in a cell in Excel, you will notice that Excel automatically removes the leading zeros (as it thinks these are unnecessary).

While this is not an issue in most cases (as you wouldn’t [leading zeros](https://trumpexcel.com/add-leading-zeroes-excel/)
), in case you do need these then one of the solutions is to convert these numbers to text.

This way, you get exactly what you enter.

One common scenario where you might need this is when you’re working with large numbers – such as SSN or employee ids that have leading zeros.

### **Entering Large Numeric Values**

Do you know that you can only enter a numeric value that is 15 digits long in Excel? If you enter a 16 digit long number, it will change the 16th digit to 0.

So if you are working with SSN, account numbers, or any other type of large numbers, there is a possibility that your input data is automatically being changed by Excel.

And what’s even worse is that you don’t get any prompt or error. It just changes the digits to 0 after the 15th digit.

Again, this is something that is taken care of if you convert the number to text.

### **Changing Numbers to Dates**

This one erk a lot of people (including myself).

Try entering 01-01 in Excel and it will automatically change it to date (01 January of the current year).

So if you enter anything that is a valid date format in Excel, it would be converted to a date.

A lot of people reach out to me for this as they want to enter scores in Excel in this format, but end up getting frustrated when they see dates instead.

Again, changing the format of the cell from number to text will help keep the scores as is.

Now, let’s go ahead and have a look at some of the methods you can use to convert numbers to text in Excel.

Also read: [How to Write Scientific Notation in Excel?](https://trumpexcel.com/scientific-notation-excel/)

Convert Numbers to Text in Excel
--------------------------------

In this section, I will cover four different ways you can use to convert numbers to text in Excel.

Not all these methods are the same and some would be more suitable than others depending on your situation.

So let’s dive in!

### Adding an Apostrophe

If you manually entering data in Excel and you don’t want your numbers to change the format automatically, here is a simple trick:

**Add an apostrophe (‘) before the number**

So if you want to enter 001, enter ‘001 (where there is an apostrophe before the number).

And don’t worry, the apostrophe is not visible in the cell. You will only see the number.

![Number converted to text by adding an apostrophe](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20278%20142'%3E%3C/svg%3E)

When you add an apostrophe before a number, it will change it to text and also add a small green triangle at the top left part of the cell (as shown in th image). It’s Exel way to letting you know that the cell has a number that has been converted to text.

When you add an apostrophe before a number, it tells Excel to consider whatever follows as text.

A quick way to visually confirm whether the cells are formatted as text or not is to see whether the numbers align to the left out to the right. **When numbers are formatted as text, they align to the right by default (as they alight to the left)**

![Number with an without apostrophe](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20372%20357'%3E%3C/svg%3E)

Adding an apostrophe changes cell alignment to left

Even if you add an apostrophe before a number in a cell in Excel, you can still use these as numbers in calculations

Similarly, if you want to enter 01-01, adding an apostrophe would make sure that it doesn’t get changed into a date.

Although this technique works in all cases, it is only useful if you’re manually entering a few numbers in Excel. If you enter a lot of data in a specific range of rows/columns, use the next method.

### Converting Cell Format to Text

Another way to make sure that any numeric entry in Excel is considered a text value is by changing the format of the cell.

This way, you don’t have to worry about entering an apostrophe every time you manually enter the data.

You can go ahead entering the data just like you usually do, and Excel would make sure that your numbers are not changed.

Here is how to do this:

1.  Select the range or rows/column where you would be entering the data
2.  Click the Home tab

![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20384%20223'%3E%3C/svg%3E)

3.  In the Number group, click on the format drop down

![Click on the format drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20431%20165'%3E%3C/svg%3E)

4.  Select Text from the options that show up

![Select the Text formatting option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20318%20650'%3E%3C/svg%3E)

The above steps would change the default formatting of the cells from General to Text.

Now, if you enter any number or any text string in these cells, it would automatically be considered as a text string.

This means that Excel would not automatically change the text you enter (such as truncating the leading zeros or converting entered numbers into dates)

In this example, while I changed the cell formatting first before entering the data, you can also do this with cells that already have data in them.

But remember that if you already had entered numbers that were changed by Excel (such as removing leading zeros or changing text to dates), that won’t come back. You will have to make that [data entry](https://trumpexcel.com/excel-data-entry-tips/)
 again.

Also, keep in mind that cell formatting can change in case you copy and paste some data to these cells. With regular copy-paste, it also copied the formatting from the copied cells. So it’s best to copy and paste values only.

Also read: [How to Format Phone Numbers in Excel?](https://trumpexcel.com/format-phone-numbers-excel/)

### Using the TEXT Function

Excel has an in-built [TEXT function](https://trumpexcel.com/excel-text-function/)
 that is meant to convert a numeric value to a text value (where you have to specify the format of the text in which you want to get the final result).

This method is useful when you already have a set of numbers and you want to show them in a more readable format or if you want to add some text as suffix or prefix to these numbers.

Suppose you have a set of numbers as shown below, and you want to show all these numbers as five-digit values (which means to add leading zeros to numbers that are less than 5 digits).

![Dataset with numbers of different digits](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20175%20338'%3E%3C/svg%3E)

While Excel removes any leading zeros in numbers, you can use the below formula to get this:

\=TEXT(A2,"00000")

![TEXT formula result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20444%20387'%3E%3C/svg%3E)

In the above formula, I have used “00000” as the second argument, which tells the formula the format of the output I desire. In this example, 00000 would mean that I need all the numbers to be at least five-digit long.

You can do a lot more with the TEXT function – such as add currency symbol, add prefix or suffix to the numbers, or change the format to have comma or decimals.

Using this method can be useful when you already have the data in Excel and you want to format it in a specific way.

This can also be helpful in saving time when doing manual data entry, where you can quickly enter the data and then use the TEXT function to get it in the desired format.

Also read: [Convert Month Name to Number in Excel](https://trumpexcel.com/convert-month-name-to-number-excel/)

### Using Text to Columns

Another quick way to convert numbers to text in Excel is by using the Text to Columns wizard.

While the purpose of Text to Columns is to split the data into multiple columns, it has a setting that also allows us to quickly select a range of cells and convert all the numbers into text with a few clicks.

Suppose you have a data set is shown below, and you want to convert all the numbers in columns A into text.

![Dataset with numbers of different digits](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20175%20338'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the numbers in Column A
2.  Click the Data tab

![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20606%20220'%3E%3C/svg%3E)

3.  Click on the Text to Columns icon in the ribbon. This will open the text to columns wizard this will open the text to column wizard

![Click in the Text to Columns icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20436%20166'%3E%3C/svg%3E)

4.  In Step 1 of 3, click the Next button
5.  In Step 2 of 3, click the Next button
6.  In Step 3 of 3, under the ‘Column data format’ options, select Text

![Select Text option in the Text to Columns Wizard](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20428'%3E%3C/svg%3E)

7.  Click on Finish

The above steps would instantly convert all these numbers in Column A into text. You notice that the numbers would now be aligned to the right (indicating that the cell content is text).  

![Numbers converted to text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20172%20342'%3E%3C/svg%3E)

There would also be a small green triangle at the top left part of the cell, which is a way Excel informs you that there are numbers that are stored as text.

So these are four easy ways that you can use to quickly **convert numbers to text in Excel**.

In case you only want this for a few cells where you would be manually entering the data, I suggest you use the apostrophe method. If you need to do data entry for more than a few cells, you can try changing the format of the cells from General to Text.

And in case you already have the numbers in Excel and you want to convert them to text, you can use the TEXT formula method or the Text to Columns method I covered in this tutorial.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [Convert Text to Numbers in Excel](https://trumpexcel.com/convert-text-to-numbers-excel/)
    
*   [How to Convert Serial Numbers to Dates in Excel](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)
    
*   [Convert Date to Text in Excel – Explained with Examples](https://trumpexcel.com/convert-date-to-text-excel/)
    
*   [How to Convert Formulas to Values in Excel](https://trumpexcel.com/convert-formulas-to-values-excel/)
    
*   [Convert Time to Decimal Number in Excel](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [How to Convert Inches to MM, CM, or Feet in Excel?](https://trumpexcel.com/convert-inches-to-mm-cm-feet-excel/)
    
*   [Convert Scientific Notation to Number or Text in Excel](https://trumpexcel.com/convert-scientific-notation-to-number-text/)
    
*   [Separate Text and Numbers in Excel](https://trumpexcel.com/separate-text-and-numbers-in-excel/)
    
*   [Convert Number to Words in Excel](https://trumpexcel.com/number-to-words-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/convert-numbers-to-text-excel/#respond)

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