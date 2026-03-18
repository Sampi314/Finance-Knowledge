# Format Numbers to Show in Millions in Excel

**Source:** https://trumpexcel.com/millions-format-excel

---

[Skip to content](https://trumpexcel.com/millions-format-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/millions-format-excel/#below-title)

Whenever I’m working with financial data, I have to clean and format it so it’s more readable.

One of the things I often have to do is change the format of the cells that contain figures such as revenue or profit to show them in millions.

For example, instead of showing 5735241, it’s better to show 5.7 Million or 5.73 Million.

Formatting numbers in millions is super easy in Excel thanks to functionalities such as Custom Number Formatting and the TEXT function.

In this short tutorial, I will show you a couple of methods to format numbers to show them in millions.

I will also show you how you can change the format of the numbers and charts (such as in data labels or axis labels) and show them in millions.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/millions-format-excel/#)

Using Custom Number Formatting to Format Numbers in Millions
------------------------------------------------------------

The best way to format your numbers to show them in millions is by using [custom number formatting](https://trumpexcel.com/excel-custom-number-formatting/)
.

This method does not change the values in the cell. However, it changes the way these values are shown in the cells. So while the cell would continue to have the same value, it would be shown in millions to the users.

Let me show you how it works.

Below is a data set where I have Sales values for different companies in column B, and I want to show these sales figures in millions.

![Data set to format numbers in millions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20337'%3E%3C/svg%3E)

Here are the steps to do this using custom number formatting:

1.  Select the cells that have the values that you want to format to millions

![Select the cells you want to format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20441%20338'%3E%3C/svg%3E)

2.  Click the Home tab and then click on the dialog box launcher in the number group (the small tilted arrow icon at the bottom right part of the group). This will open the Format Cells dialog box. Alternatively, you can also use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     Control + 1 (hold the control key and then press the 1 key)

![Click on the dialog box launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20702%20157'%3E%3C/svg%3E)

3.  In the ‘Number’ tab, click on the ‘Custom’ category option.
4.  In the type field, enter the following format:

0,, "M"

![Enter million format in the type field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20628'%3E%3C/svg%3E)

5.  Click Ok

That’s It!

The above steps would change the format of the cell so that you’re now shown the values in millions along with the alphabet ‘M’.

![Numbers shown in millions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20438%20336'%3E%3C/svg%3E)

And as I mentioned earlier, the value in the cell remains to be the original number, and you can continue to use them in your calculations.

**How does this work?**

Let me explain each component in the custom format:

*   0 – The 0 indicates the number of digits that needs to be shown after the number has been converted into millions. For example, 801908459 will become 802, and 32677858 will become 33. _Using 0 Ensures that at least one digit would be shown even if the value is less than a million._
*   comma (,) – When you add one comma to the custom format, it’s equivalent to dividing that number by 1000. This is equivalent to shifting the decimal point three digits to the left. And when you add two commas, It’s equivalent to dividing the number by 1000000 (Or shifting the decimal .6 digits to the left). In our case, since we want to show our numbers in millions, we need to remove the last six digits, and hence we have used two commas in the format.
*   “M” – Anything that you add in double quotes will be shown as is as part of the format. So whatever value we get using 0,, format, an M is added to that.

Now that you understand how the format is being constructed, here are some other custom formats that you can consider:

| Format | What it does? |
| --- | --- |
| 0,, | This will show the number in Million. So, 801908459 will be shown as **802.** |
| 0.0,, | This will show the number with one decimal place. So, 801908459 will be shown as **801.9** (using a 0 in the format will ensure one decimal is always shown) |
| 0,, “Million” | This will show the number along with the word Million. So, 801908459 will be shown as **802 Million.** |

Sometimes, you will see people using # (hash symbol) Instead of 0. This is fine in most cases with one simple difference – when you use 0,, as the format, it will ensure that you get at least one digit visible in the cell even when the value is well less than a million. In case you use #,, and the value is smaller than 1,000,000, it would show you a [blank cell](https://trumpexcel.com/highlight-blank-cells-in-excel/)
.

In case you want to remove the Million formatting and get the General formatting back (where the numbers are shown as is), select the cells, click the Home tab, then click on the formatting drop-down (in the ‘Number’ group) and select the ‘General’ option

Also read: [Clean Data in Excel](https://trumpexcel.com/clean-data-in-excel/)
 (10 Smart Ways)

Using TEXT Function
-------------------

Another quick and easy way to format numbers in millions is by using the [TEXT function](https://trumpexcel.com/excel-text-function/)
.

TEXT function allows you to take any number and then show it in the specified format.

Let me show you how it works.

Below is the dataset where I have the Sales value in column B that I want to show in millions.

![Data set to format numbers in millions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20337'%3E%3C/svg%3E)

Here is the text formula that will do this for me:

\=TEXT(B2,"0.0,,")

And enter this formula in cell C2, and then copy it for all the other cells.

![TEXT Formula to show values in millions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20606%20386'%3E%3C/svg%3E)

The above TEXT function takes two arguments:

*   **B2** – This is the value that we want to show in millions.
*   **0.0,,** – This is the format that would be applied to the value supplied by the first argument (B2 in this example).

Note that all the formats I have covered in the custom number formatting method above (see the table in the previous section) would also work within the TEXT function.

One major difference between the Custom Number Formatting method and the TEXT function is that the result that you get from the TEXT function is a text string. This means unlike the Custom Formatting method, you won’t be able to use the result of the TEXT function in numeric calculations.

Note that in this method, you will get your result in another column (the one in which you have used the formula).

In case you want to remove the original values, make sure that you have [converted your formulas into values](https://trumpexcel.com/convert-formulas-to-values-excel/)
 (or else it will show you an error when you delete the original data set)

Using MROUND Function to Format Numbers in Millions
---------------------------------------------------

One simple way to show values in a cell in millions is by dividing every cell by 1000000.

Doing this would change the value in the cell, but if you do not need the original value and just want the values in millions, this is also an acceptable way.

Once you have the divided value, you can use the MROUND function to round it up.

Let me show you how it works.

Below I have the same data set, and I want to show the values in column B in millions.

![Data set to format numbers in millions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20337'%3E%3C/svg%3E)

Here is the formula to do this:

\=MROUND(B2/1000000,1)

And enter this formula in cell C2, then copy it for all the other cells.

![MROUND Formula to show numbers as millions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20387'%3E%3C/svg%3E)

The above formula first divides the value in cell B2 by 1000000, which would give us 801.908459.

Since I do not want so many digits after the decimal, I’ve used the MROUND function to remove all these decimal digits.

In case you want to show one digit after the decimal, you can use the below formula:

\=MROUND(B2/1000000,0.1)

Similarly, if you want to show every value as a multiple of 10, you can use the below formula:

\=MROUND(B2/1000000,10)

Format Numbers to Millions in Charts in Excel
---------------------------------------------

One common situation where you may want to format numbers to show in millions is when you are plotting the data in a chart.

When you add values in millions to the data label or the axis label in a chart, it takes up a lot of space.

Below is an example where I have created a column chart using the sales data, and you can see that the data labels and the axis labels are taking up too much space.

![Chart showing data labels in millions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20344'%3E%3C/svg%3E)

Let me show you how to convert the values of data labels to millions.

1.  Right-click on any of the data labels in the chart
2.  Click on the ‘Format Data Labels..’ option. This will open the ‘Format Data Labels’ pane on the right

![Click on the format data labels option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20376'%3E%3C/svg%3E)

3.  In the ‘Label’ options category, scroll down and click on the ‘Numbers’ option. This will expand to show more of the Number options.

![Click on the numbers option in the format data labels pane](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20375%20759'%3E%3C/svg%3E)

4.  In the ‘Format Code’ field, enter the below custom code:

0.0,,

![Enter the format code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20340%20225'%3E%3C/svg%3E)

5.  Click on the Add button

![Click on the add button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20340%20225'%3E%3C/svg%3E)

As soon as you do the above steps, the data label format will be changed, and they will now be shown as millions.

![Data labels are now shown in millions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20346'%3E%3C/svg%3E)

You can follow the same steps to format the numbers in the Axis labels as well. Right-click on any of the Axis labels, click on the ‘Format Axis’ option, and then follow the same steps in the right pane that opens.

In this tutorial, I’ve covered three methods you can use to format values to show in millions. The best method is to use a custom format code that can be applied using the ‘Format Cells’ dialog box or the TEXT function. You can also use the MROUND method that divides the value by 1000000 to convert it to millions.

I’ve also covered how to format the Data labels and Axis labels in charts in Excel to format the values in millions.

I hope you found this Excel tutorial useful.

**Other Excel tutorials you may also like:**

*   [Show Trend Arrows in Excel Chart Data Labels](https://trumpexcel.com/excel-chart-data-labels-trend-arrows/)
    
*   [Show Negative Numbers in Parentheses (Brackets)](https://trumpexcel.com/show-negative-numbers-parentheses-brackets-excel/)
    
*   [How to Change Date Format In Excel?](https://trumpexcel.com/change-date-format-excel/)
    
*   [Format Numbers as Text in a Drop Down List in Excel](https://trumpexcel.com/format-numbers-as-text-excel/)
    
*   [TRANSLATE Function in Excel](https://trumpexcel.com/excel-functions/translate/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/millions-format-excel/#respond)

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