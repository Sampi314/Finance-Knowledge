# Add or Subtract Percentage From a Number in Excel (Formula)

**Source:** https://trumpexcel.com/add-subtract-percentage-from-number-excel

---

[Skip to content](https://trumpexcel.com/add-subtract-percentage-from-number-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/add-subtract-percentage-from-number-excel/#below-title)

Working with percentages is a daily task for many Excel users.

Now you cannot simply add a [percentage value](https://trumpexcel.com/calculate-percentages-excel/)
 to a number to get the right result. For example, you cannot use 10 + 10% to get 11.

Thankfully, Excel gives you a couple of really simple ways to do this. In this tutorial, I’ll show you two easy methods: using a simple formula and using the Paste Special feature for a super-quick update.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/add-subtract-percentage-from-number-excel/#)

Add or Subtract Percentage Using a Formula
------------------------------------------

The easiest way to add or subtract percentage from a number is by using a formula. It keeps your original data intact and gives you a dynamic result that updates automatically if your numbers change.

Let me show you an example.

Below is the dataset where I have the product names in column A and their current prices in column B and I want to increase the prices in column B by 10 percent.

![Dataset to add percentage to a number in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20972%20682'%3E%3C/svg%3E)

Here is the formula that will do this:

\=B2\*(1+10%)

![Formula to write percentage to a number in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20972%20797'%3E%3C/svg%3E)

In the above formula, I have multiplied the original price (which is in B2) by 1+10%. Excel is smart enough to understand that when I use 10% in the backend, I am actually referring to the decimal part which is 0.1.

So the formula actually become

\=B2\*(1+0.1)

In case you have percentage values in a separate column, then you can also use cell references to increase a given number by the given percentage value.

For example, below I have a dataset where I have prices in column B and the percentage that I want to add in column C, and I want to get the result in column D.

![dataset to increase percentage using formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201156%20680'%3E%3C/svg%3E)

Here is the formula that will do this:

\=B2\*(1+C2)

![Formula to write percentage to a number in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20972%20797'%3E%3C/svg%3E)

The logic here is the same as where we multiply the value in cell B2 by 1 + the percentage value, which will finally give us the incremented value.

One caveat here is that your values in column C need to be either in percentages or in decimal. For example, you cannot have 10% as 10, it needs to be 0.1.

And in case you have these values as whole numbers, you will have to convert them to percentages by dividing them by 100.

In the example above, I have shown you how to add a percentage to a number. But if you want to subtract a percentage from a number, the logic remains the same. You just change the sign from plus (+) to minus (-).

**Note:** One good thing about this method is that it’s dynamic. If you change the price in column B, the result in column C will update instantly.

Also read: [Calculate Percentage Change in Excel (% Increase/Decrease Formula)](https://trumpexcel.com/percentage-change-excel/)

Add or Subtract Percentage Using a Paste Special
------------------------------------------------

Another way you can quickly add or [subtract](https://trumpexcel.com/subtract-in-excel/)
 percentages in Excel is by using Paste Special.

Below I have a dataset where I have products in column A and their prices in column B, and I want to increase the prices by 10 percent.

![Dataset to add or subtract percentages using Paste Special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20693%20682'%3E%3C/svg%3E)

Here are the steps to do this using Paste Special:

1.  In any blank cell, enter the value, 110% (we only need this temporarily). For this example, let us put the value in cell D1.
2.  Copy this cell in which we enter 110% (use the keyboard shortcut Ctrl+C or right click and then click on copy)

![Copy the selected percentage value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201184%20684'%3E%3C/svg%3E)

3.  Select the cells that have the numbers to which you want to add 10%. In this example, that would be the prices values in column B
4.  Right-click on any of these cells and then click on the ‘Paste Special’ option. This will open the Paste Special dialog box.

![Click on Paste Special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201160%20967'%3E%3C/svg%3E)

5.  Select the Values option, and then in the operations section, select the [Multiply](https://trumpexcel.com/multiply-in-excel-using-paste-special/)
     option.

![Select the values and multiply option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201320%201082'%3E%3C/svg%3E)

6.  Click the OK button.

This will give you the result where the original values have now been incremented by 10%.

![Result after adding percentage using Paste Special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20689%20676'%3E%3C/svg%3E)

Once done, you can remove the 110% value in the cell that we entered in step 1.

Using the above method, we are not just copying and pasting the value 110%, we are actually multiplying it with the value in the cells in which we are pasting it to.

Now, here is how this is different from the formula method covered earlier:

*   The result you get are static values. So if you change the value 110% to something else, the resulting values in column B would not automatically update.
*   You do not need a helper column to [apply the formula](https://trumpexcel.com/apply-formula-to-entire-column-excel/)
     and get the result. You can apply this technique on your original data set.
*   Your original data is lost unless you make a copy of it.

So there you have it – two simple ways of adding or subtracting percentages in Excel. The formula method is perfect for when you need to preserve your original data and want a dynamic result, while the [Paste Special method](https://trumpexcel.com/excel-paste-special-shortcuts/)
 is fantastic for quick, one-off updates.

I hope you found this tutorial helpful!

**Other Excel articles you may also like:**

*   [Show Negative Numbers in Parentheses (Brackets)](https://trumpexcel.com/show-negative-numbers-parentheses-brackets-excel/)
    
*   [Excel Custom Number Formatting Tricks](https://trumpexcel.com/excel-custom-number-formatting/)
    
*   [Percentage Change Calculator](https://trumpexcel.com/calculator/percentage-change/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/add-subtract-percentage-from-number-excel/#respond)

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