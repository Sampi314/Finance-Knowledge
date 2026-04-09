# How to Calculate and Format Percentages in Excel

**Source:** https://trumpexcel.com/calculate-percentages-excel

---

[Skip to content](https://trumpexcel.com/calculate-percentages-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/calculate-percentages-excel/#below-title)

Often, there are two types of percentages that one needs to calculate in Excel.

*   Calculating the percentage as a proportion of a specified value (for example, if you eat 4 out of 5 mangoes, what percentage of mangoes have you eaten).
*   Calculating the percentage change (YoY or MoM). This is usually used in sales reporting where the manager would want to know what’s the sales growth Year on Year, or Quarter on Quarter.

In this tutorial, I will show you the **formula to calculate percentages in Excel** as well as to format the cell so that the numbers show up as percentages (and not decimals).

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/calculate-percentages-excel/#)

Calculating Percentage as a Proportion
--------------------------------------

Examples of this would be to find sales coverage or project completion status.

For example, your sales manager may want to know what percentage of the total prospective customers can be reached effectively in a region.

This is known as sales coverage. Based on this, he/she can work on the sales coverage model and/or channels to reach more customers.

Here is a sales coverage example for three regions:

![Calculate Percentages in Excel - Sales Coverage](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20559%20114'%3E%3C/svg%3E)

Looking at the example above, it would be instantly clear that the coverage is lowest in Region C, where the manager may plan some new initiatives or campaigns.

Here is the Exxcel formula to calculate the percentage in Excel:

\=Effectively Reached/Total Prospective Customers

Within Excel, you can enter =B3/B2 to calculate the percentage for Region A.

Note that this would give a value in General/Number format and not in the percentage format. To make it look like a percentage, you need to apply the percentage format (shown later in this tutorial).

Calculating Percentage Change in Excel
--------------------------------------

Percentage change is widely used and monitored in various areas of business. Analysts usually talk about a company’s revenue growth or Profit growth in percentage.

Companies often track the percentage change in costs on a monthly/quarterly basis.

Here is a simple example of using Percentage change:

![Calculate Percentages in Excel - Growth percentage](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20116'%3E%3C/svg%3E)

Column D has the YoY percentage change value for Revenue, Cost, and Profit. It can be easily deduced that the revenue growth was healthy but costs grew at a staggering 86.1% and lead to a decline in profits.

Here is how to calculate percentage changes in Excel:

Revenue Percentage Change = (2016 Revenue – 2015 Revenue)/2015 Revenue

In this example, the percentage formula in cell D2 is

\=(C2-B2)/B2

Again, note that this would give a value in General/Number format and not in the percentage format. To make it look like a percentage, you need to apply the percentage format (shown later in this tutorial).

So let’s see how to apply the percentage formatting in Excel.

Also read: [How to Square a Number in Excel](https://trumpexcel.com/square-number-excel/)

Applying Percentage Formatting in Excel
---------------------------------------

There are various ways you can apply the percentage formatting in Excel:

1.  Using the Keyboard Shortcut.
2.  Using the Ribbon.
3.  Using the Number Format Cells Dialog Box.

### Method 1 – Using the Keyboard Shortcut

To apply the percentage format to a cell or a range of cells:

*   Select the cell(s).
*   Use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     – **Control + Shift + %** (hold the Control and Shift keys and then press the % key).

Note that this applies the percentage format with no decimal places. So if you use it on 0.22587, it will make it 23%.

Also read: [Add or Subtract Percentage From a Number in Excel](https://trumpexcel.com/add-subtract-percentage-from-number-excel/)

### Method 2 – Applying Percentage Format Using the Ribbon

To apply percentage format to a cell (or a range of cells):

*   Select the cell (or the range of cells).
*   Go to Home –> Number –> Percent Style.

![Calculate Percentages in Excel - Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20652%20131'%3E%3C/svg%3E)

Note that this applies the percentage format with no decimal places. So if you use it on 0.22587, it will make it 23%.

![Calculate Excel Percentages in Excel - Using Ribbon Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20252'%3E%3C/svg%3E)

If you want to have the percentage value to have decimals as well, you can use the increase decimal icon right next to the percentage icon in the ribbon.

![Calculate Excel Percentages in Excel - Increase Decimal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20343%20129'%3E%3C/svg%3E)

### Method 3 – Applying Percentage Format Using Format Cells Dialog Box

Using the Format Cells Dialog box gives a lot of flexibility to the user when it comes to formatting.

Here is how to apply percentage format using it:

*   Select the cell (range of cells).
*   Go to Home –> Number and click on the dialog launcher (a tilted arrow icon at the bottom right of the group). This will open the Format Cell dialog box.
    *   _You can also use the keyboard shortcut – Control + 1 (hold the control key and press 1).![Calculate Excel Percentages in Excel - dialog launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20239%20134'%3E%3C/svg%3E)_

*   In the Format Cells dialog box, within the Number tab, select Percentage in the Category list.![Calculate Excel Percentages in Excel - Format Cell Percentage](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20539%20322'%3E%3C/svg%3E)
*   If you want to change the number of decimal places to be displayed, use the Decimal places option on the right. For example, if you want to display the value with 2 decimal places, make it 2.![Calculate Excel Percentages in Excel - change decimal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20536%20324'%3E%3C/svg%3E)
*   Click OK.

So these are the methods you can use to calculate percentages in Excel with a formula. I also covered some methods you can use to format the number to show it as a percentage.

I hope you found this tutorial useful!

**You May Also Like the Following Excel Tutorials:**

*   [How to Calculate Weighted Average in Excel.](https://trumpexcel.com/weighted-average-in-excel/)
    
*   [How to Calculate Square Root in Excel](https://trumpexcel.com/calculate-square-root-in-excel/)
    
*   [How to Calculate CAGR in Excel](https://trumpexcel.com/calculate-cagr-excel/)
    .
*   [Calculating Standard Deviation in Excel](https://trumpexcel.com/standard-deviation/)
    .
*   [Excel Data Entry Tips](https://trumpexcel.com/excel-data-entry-tips/)
    
*   [Clean Data in Excel Spreadsheets](https://trumpexcel.com/clean-data-in-excel/)
    
*   [How to Find Range in Excel](https://trumpexcel.com/find-range-in-excel/)
    
*   [Calculate Percentage Change in Excel (% Increase/Decrease Formula)](https://trumpexcel.com/percentage-change-excel/)
    
*   [Free Percentage Change Calculator](https://trumpexcel.com/calculator/percentage-change/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/calculate-percentages-excel/#respond)

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