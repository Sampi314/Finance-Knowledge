# 7 Amazing Excel Custom Number Format Tricks (you Must know)

**Source:** https://trumpexcel.com/excel-custom-number-formatting

---

[Skip to content](https://trumpexcel.com/excel-custom-number-formatting/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-custom-number-formatting/#below-title)

Excel Custom Number formatting is the clothing for data in excel cells. You can dress these the way you want. All you need is a bit of know-how of how Excel Custom Number Format works.

With custom number formatting in Excel, you can change the way the values in the cells show up, but at the same time keeping the original value intact.

For example, I can make a date value show up in different Date formats, while the underlying value (the number that represents the date) would remain the same.

In this tutorial, I will cover everything about custom number format in Excel, and also show you some really useful examples that you can use in your day-to-day work.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-custom-number-formatting/#)

Excel Custom Number Format Construct
------------------------------------

Before I show you the awesomeness of it, let me briefly explain how custom number formatting works in Excel.

By design, Excel can accept the following four types of data in a cell:

*   A positive number
*   a negative number
*   0
*   Text strings (this can include pure text strings as well as alphanumeric strings)

Another data type that Excel can accept is dates, but since all date and [time values](https://trumpexcel.com/calculate-time-in-excel/)
 are stored as numbers in Excel, these would be covered as a part of the positive number.

For any cell in a worksheet in Excel, you can specify how each of these data types should be shown in the cell.

And below is the syntax in which you can specify this format.

<Format for POSITIVE Numer>;<Format for NEGATIVE Numer>;<Format for ZERO>;<Format for TEXT>

Note that all these are separated by semi-colons (;).

Anything that you enter in a cell in Excel would fall in either of these four categories and hence a custom format for it can be specified.

If you mention only:

*   **One format**: It is applied to all four sections. For example, if you just write General, it will be applied for all four sections.
*   **Two formats**: The first one is applied to positive numbers and zeros, and the second one is applied to negative numbers. Text format by default becomes General.
*   **Three Formats**: The first one is applied to positive numbers, the second one is applied to negative numbers, the third is applied to zero, and the text disappears as nothing is specified for text.

If you want to learn more about custom number formatting, I would highly recommend the [Office Help](https://office.microsoft.com/en-in/excel-help/create-a-custom-number-format-HP010342372.aspx)
 section.

How this works and where to enter these formats are covered later in this tutorial. For now, just keep in mind that this is the syntax for the format for any cell

How Custom Number Format Works in Excel
---------------------------------------

Then you open a new Excel workbook, by default all the cells in all the worksheets in that workbook have the General format where:

*   **Positive numbers** are shown as is (aligned to the left)
*   **Negative numbers** are shown with a minus sign (and aligned to the left)
*   **Zero** is shown as 0 (and aligned to the left)
*   **Text** is shown as is (aligned to the right)

_And in case you enter a date, it’s shown based on your regional setting (in DD-MM-YYYY or MM-DD-YYYY format)._

So by default, the cell’s number formatting is:

General;General;General;General

Where each data type is formatted as General (and follow the rules I mentioned above, based on whether it’s a positive number, negative number, 0, or text)

Now the default setting is alright, but how do you change the format. For example, if I want my negative numbers to show up in red color or I want my dates to show up in a specific format then how do I do that.

### Using the Format Drop Down in the Ribbon

You can find some of the commonly used number formats in the Home tab within the Number group.

It’s a drop-down that shows many of the commonly used formats that you can apply to a cell by simply selecting the cell and then selecting the format from this list.

![Existing formats in Excel ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20728'%3E%3C/svg%3E)

For example, if you want to convert numbers into percentages or converted dates into short date format or long-form date format, then you can easily do it by using the options in the dropdown.

### Using Format Cells Dialog Box

Format cells dialog boxes where you get the maximum flexibility when it comes to applying formats to a cell in Excel.

It already has a lot of premade formats that you can use, or if you want to create your own custom number format, then you can do that as well.

Here is how to open the Format Cells dialog box;

1.  Click the Home Tab![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20498%20202'%3E%3C/svg%3E)
2.  In the Number group, click on the dialog box launcher icon (the small tilted arrow at the bottom-right of the group).![Format cells dialog box launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20430%20214'%3E%3C/svg%3E)

This will open the Format Cells dialog box. Within it, you will find all the formats in the Number tab (along with the option to create Custom cell formats)

You can also use the following [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
 to open the format cells dialog box:

CONTROL + 1 (all the Control key and then press the 1 key).

In case you’re using Mac, you can use **CMD + 1**

Now let’s have a couple of practical examples where we will create our own custom number formats.

Also read: [Cell References in Excel](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
 (Absolute, Relative, and Mixed)

Examples of Using Custom Number Formatting in Excel
---------------------------------------------------

Now let’s have a couple of practical examples where we will create our own custom number formats.

### Hide a Cell Value (or Hide All values in a Range of Cells)

Sometimes, you may have a need to hide the content of the cell (without hiding the row or column that has the cell).

A practical case of this is when you are creating an Excel dashboard and there are a couple of values that you use in the dashboard but you do not want the users to see it. so you can simply hide these values

Suppose you have a dataset as shown below and you want to hide all the numeric values:

![Dataset to hide values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20465'%3E%3C/svg%3E)

Here is how to do this using custom formatting in Excel:

1.  Select the cell or the range of cells for which you want to hide the cell content
2.  Open the Format Cells dialog box (keyboard shortcut Control + 1)
3.  In the Number tab, click on the Custom
4.  Enter the following format in the Type field:
    
    ;;;
    

![Three semicolons to hide all the cell values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20417'%3E%3C/svg%3E)

**How does this work?**

The format for four different types of data types is divided by semicolons in the following format:

_<Format for POSITIVE Numer>;<Format for NEGATIVE Numer>;<Format for ZERO>;<Format for TEXT>_

In this technique, we have removed the format and only specified the semicolon, which indicates that we do not want any formatting for the cells. This is an indication for Excel to hide any content that is there in the cell.

Note that while this hides the content of the cell, it’s still there. so if you have numbers that you have hidden, you can still use these in calculations (which makes this a great trick for [Excel dashboards](https://trumpexcel.com/creating-excel-dashboard/)
 and reports).

### Display Negative Numbers in Red Color

By default, negative numbers show up with a minus sign (or within parenthesis in some regional settings).

You can use custom number formatting to change the color of the [negative numbers](https://trumpexcel.com/negative-numbers-red-excel/)
 and make them show up in red color.

Suppose you have a dataset as shown below and you want to highlight all the negative values in red color.

![Dataset to hilight negative values in red](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20548'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the range of cells where you want to show negative numbers in red
2.  Open the Format Cells dialog box (keyboard shortcut Control + 1)
3.  In the Number tab, click on the Custom
4.  Enter the following format in the Type field:

General;\[Red\]-General

![Format to color negative values in red](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20429'%3E%3C/svg%3E)

The above format will make your cells with negative values show in red color.

![Negative values highlighted as red](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20434%20546'%3E%3C/svg%3E)

**How does this work?**

When you only specify two formats as the custom number format, the first one is considered for positive numbers and 0, and the second one is considered for negative numbers (the next value by default becomes the general format).

In the above format that we have used, we have specified the color that we want that format to take up in the square brackets.

So while the negative numbers take the general format, they are shown in red color with a minus sign.

In case you want to make the negative numbers stop in red color within parenthesis (instead of the minus sign), you can use the below format:

General;\[Red\](General)

![Negative numbers in parenthesis](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20436%20545'%3E%3C/svg%3E)

Also read: [Show Negative Numbers in Parentheses (Brackets) in Excel (Easy Ways)](https://trumpexcel.com/show-negative-numbers-parentheses-brackets-excel/)

### Add text to Numbers (such as Millions/Billions)

One amazing thing about custom number formatting is that you can add a prefix or a suffix text to a number, while still keeping the original number in the cell.

For example, I can have ‘100’ show up as ‘$100 Million’, while still having the original value in the cell so that I can use it in calculations.

[![Excel Custom Number Format - Numbers as Text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20382%20139'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2013/12/Numbers-as-Text.png)

Suppose you have a dataset as shown below and you want to show these numbers with a dollar sign and the word million in front of it.

![Dataset to show values in millions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20271%20397'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the dataset where you want to add the text to the numbers
2.  Open the Format Cells dialog box (keyboard shortcut Control + 1)
3.  In the Number tab, click on the Custom
4.  Enter the following format in the Type field:

$General "Million"

![Format to show numbers with dollar and million](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20427'%3E%3C/svg%3E)

Note that this custom number format will only affect numbers. If you enter text in the same cell, it would appear as it is.

**How does this work?**

In this example, to the general format, I have added the word million in double-quotes. anything that I add in double-quotes to the format is shown as is in the cell.

I also added the [dollar sign](https://spreadsheetplanet.com/what-does-dollar-sign-mean-in-excel-formulas/)
 before the general format so that all my numbers also show the dollar sign before the number.

_Note: If you’re wondering why the dollar sign is not in double-quotes while the word Million is in double-quotes, it’s because Excel recognizes dollar as a symbol that is often used in custom number formatting, and doesn’t require you to add double quotes to it. You can go ahead and add double quotes to the dollar sign, but when you close the format cells dialog box and open it again, you will notice that Excel has removed it_

Also read: [Format Numbers to Show in Millions in Excel](https://trumpexcel.com/millions-format-excel/)

### Disguise Numbers and Text

With custom number formatting, you can assess a maximum of two conditions, and based on these conditions you can apply a format to the cell.

For example, suppose you have a list of scores for some students, you want to show the text Pass or Fail based on the score (where any score less than 35 should show ‘Fail’, else it should show ‘Pass’.

![Score that needs to be converted into text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20433%20453'%3E%3C/svg%3E)

Below are the steps to show scores as Pass or Fail instead of the value using custom number format:

1.  Select the dataset where you have the scores
2.  Open the Format Cells dialog box (keyboard shortcut Control + 1)
3.  In the Number tab, click on the Custom
4.  Enter the following format in the Type field:
    
    \[<35\]"Fail";"Pass"
    

![Custom formatting to show numbers as Text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20452'%3E%3C/svg%3E)

Below is how your data would look after you have applied the above format.

![Resulting scores that show pass and fail](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20430%20712'%3E%3C/svg%3E)

Note that it does not change the value in the cells. The cell continues to have the scores in numeric values while displaying ‘Pass’ or ‘Fail’ depending on the cell value.

**How does this work?**

In this example, the condition needs to be specified within the square brackets. custom number formatting then evaluates the value in the cell and applies the format accordingly.

So if the value in the cell is less than 35, then the number is hidden, and instead the text ‘Fail’ is shown, adding all other cases, ‘Pass’ is shown.

Similarly, if you want to convert a range of cells that have 0’s and 1’s into TRUEs and FALSEs, you can use the below format:

\[=0\]"FALSE";\[=1\]"TRUE"

Remember that you can only use two conditions in custom number formatting. If you try and use more than two conditions, it is going to so your prompt letting you know that it cannot accept that format.

### Hide Text but Display Numbers

Sometimes, when you download your data from databases since there are empty are filled with value such as Not Available or NA or –

With custom number formatting, you can hide all the text values while keeping the numbers as is. this also ensures that your original data is intact (as you are not deleting the text value, you’re just simply hiding it)

[![Excel Custom Number Format Hide Text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20201%20186'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2013/12/Number-formattign-Hide-Text.png)

Suppose you have a data set as shown below where you want to hide all the text values:

![KPI Data with text values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20231%20420'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the dataset where you have the data
2.  Open the Format Cells dialog box (keyboard shortcut Control + 1)
3.  In the Number tab, click on the Custom
4.  Enter the following format in the Type field:

General; -General; General;

![Formatting to hide all text values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20436'%3E%3C/svg%3E)

Note that I have used the General format for numbers. You can any format you wish (such as 0, 0.#, #0.0%). Also, note that there is a negative sign (-) before the second General format, as it represents the format for negative numbers.

**How does this work?**

In this example, since we wanted to hide all the text values, we simply didn’t specify the format for it.

And since we specified the format for the other three data types (positive number, negative number, and zero), Excel understood that we have purposefully left the format for the text value empty, and it should not show anything if a cell has a text string.

### Display Numbers as Percentages (%)

With custom number formatting, you can also change the numbers and make them show up in percentages.

[![Excel Custom Number Format number as percentage](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20205%20170'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2014/01/Number-formattign-number-as-percentage.png)

Suppose you have a data set as shown below, and you want to convert these numbers to show the equivalent percentage value:

![Data that needs to be converted to percentage](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20231%20417'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the cells where you have the numbers (that you want to convert to percentage)
2.  Open the Format Cells dialog box (keyboard shortcut Control + 1)
3.  In the Number tab, click on the Custom
4.  Enter the following format in the Type field:

0%

![Formatting to show numbers in percentage](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20430'%3E%3C/svg%3E)

This will change the numbers to their percentages. For example, it changes from 0.11 to 11%.

If all you want to do is converted a number into its equivalent percentage value, a better way to do this would be to use the percentage option in the format cells dialog box.

Where custom formatting can be useful is when you want more control over how you want to show the percentage value.

For example, if you want to show some additional text with the percentage, all you want to show negative percentages in red color then it is better to use custom formatting

Also read: [How to Change Date Format In Excel?](https://trumpexcel.com/change-date-format-excel/)

### Display Numbers in a Different Unit (Millions as Billions or Grams as Kilograms)

If you work with large numbers, you may want to show these in a different unit. for example, if you have the sales data of some companies, you may want to show the sales in millions or billions (while still keeping the original sale value in the cells)

Thankfully, you can easily do that with custom number formatting.

Suppose you have a data set as shown below, and you want to show these sales values in millions.

![Data where numbers need to be converted into millions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20506%20545'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the cells where you have the numbers
2.  Open the Format Cells dialog box (keyboard shortcut Control + 1)
3.  In the Number tab, click on the Custom
4.  Enter the following format in the Type field:

0.0,,

![Custom format to show numbers in millions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20436'%3E%3C/svg%3E)

The above would give you the result as shown below (values in millions in one digit after the decimal):

![Resulting data where numbers are in millions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20509%20546'%3E%3C/svg%3E)

**How does this work?**

In the above format, a zero before the decimal indicates that Excel should show the entire number (exactly as it is in the cell), and a 0 after the decimal indicates that it should show only one significant digit after the decimal point.

So 0.0 would always be a number with one digit after the decimal point.

When you add a comma after the 0.0, it will shave off the last three-digit of the number. For example, 123456 would become 123.4 (the last three digits are removed, and since it has to show 1 digit after the decimal point, it shows 4)

If you think about it, it’s similar to dividing the number by 1000. So if you want to show a number in the ‘millions’ unit, you need to add 2 commas, so that it would shave off the last 6 digits.

And if you also want to show the word million or the alphabet M after the number, use the below format

0.0,, "M"

**You May Also Like the Following Excel Tutorials:**

*   [Disguise Numbers as Text in a Drop Down List in Excel.](https://trumpexcel.com/format-numbers-as-text-excel/)
    
*   [Color Negative Chart Data Labels in Red with a downward arrow.](https://trumpexcel.com/chart-data-labels-in-red-with-arrows/)
    
*   [How to Copy Conditional Formatting to Another Cell in Excel](https://trumpexcel.com/copy-conditional-formatting-another-cell-excel/)
    
*   [How to Remove Cell Formatting in Excel (from All, Blank, Specific Cells)](https://trumpexcel.com/remove-cell-formatting-in-excel/)
    
*   [How to Remove Table Formatting in Excel](https://trumpexcel.com/remove-table-formatting-excel/)
    
*   [How To Convert Date To Serial Number In Excel?](https://trumpexcel.com/convert-date-to-serial-number-excel/)
    
*   [Change the Default Font in Excel](https://trumpexcel.com/change-default-font-excel/)
    
*   [How to Format Phone Numbers in Excel?](https://trumpexcel.com/format-phone-numbers-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

9 thoughts on “Excel Custom Number Formatting Tricks”
-----------------------------------------------------

1.  I hope you can still answer.  
    How would you format a custom cell that includes both numbers and characters, e.g., 12345abcd678e9 to 12345-abc-d78-e9
    
    [Reply](https://trumpexcel.com/excel-custom-number-formatting/#comment-32786)
    
    *   Hello Francisco… You can’t do this using Custom Number formatting. It can only allow you to specify the format for Positive numbers, Negative numbers, zero and text. The text you mentioned would be considered text value (as it’s alphanumeric). With custom formatting, you can show 12345abcd678e9 as is or specify what else you want to show instead of this. What you’re trying to achieve can be done using formulas (if there is a consistent pattern that can be followed)
        
        [Reply](https://trumpexcel.com/excel-custom-number-formatting/#comment-32787)
        
2.  Sir, 7th May,2020.  
    Very nicely and clearly you have shown every item.So, understanding clearly.  
    thanking you and expect to receive such useful notes in future too.  
    Once again Thanking you.  
    Kanhaiyalal Newaskar.
    
    [Reply](https://trumpexcel.com/excel-custom-number-formatting/#comment-14010)
    
3.  I have been following your excel module guide and it has taught me a lot of things I was missing out on in Excel.  
    These shortcuts are very well explained, extremely helpful, and time saving.  
    Thank you.
    
    [Reply](https://trumpexcel.com/excel-custom-number-formatting/#comment-13717)
    
4.  I am really happy to read all your article. You did a Amazing JOB!!! Very Appreciate!!!!!BIG BLESS~~~
    
    [Reply](https://trumpexcel.com/excel-custom-number-formatting/#comment-12589)
    
5.  Excellent!  
    Except ;;;; should be ;;; surely?
    
    [Reply](https://trumpexcel.com/excel-custom-number-formatting/#comment-11866)
    
    *   Thanks for letting me know. Yes, it should have been three semi-colons only. Have corrected it
        
        [Reply](https://trumpexcel.com/excel-custom-number-formatting/#comment-11867)
        
6.  Hi, thank for the tips, but once we’ve created the format we want, is there a way to create a shortcut to the new custom number format?
    
    [Reply](https://trumpexcel.com/excel-custom-number-formatting/#comment-2196)
    
    *   I can’t find a way that answers what you’re probably after, Manu, but if you select a cell that has the formatting you want, and press Ctrl+1 it will take you straight to that format.  
        Which, now I think about it, is a useful way to check what format a cell (or range of cells) is. If the range of cells comes up with no format (not even “General”), then you have a mixture of formats in that range.
        
        [Reply](https://trumpexcel.com/excel-custom-number-formatting/#comment-11868)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-custom-number-formatting/#respond)

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