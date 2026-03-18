# How to Make Negative Numbers Red in Excel

**Source:** https://trumpexcel.com/negative-numbers-red-excel

---

[Skip to content](https://trumpexcel.com/negative-numbers-red-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/negative-numbers-red-excel/#below-title)

**Watch Video – Show negative numbers in Red (and in brackets)**

If you work with a lot of numbers in Excel, it’s a good practice to highlight negative numbers in red. This makes it easier to read the data.

There are various techniques you can use to highlight negative numbers in red in Excel:

*   Using Conditional Formatting
*   Using Inbuilt Number Formatting
*   Using [Custom Number Formatting](https://trumpexcel.com/excel-custom-number-formatting/)
    

Let’s explore each of these techniques in detail.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/negative-numbers-red-excel/#)

Highlight Negative Numbers in Red – Using Conditional Formatting
----------------------------------------------------------------

[Excel Conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
 rules are applied to a cell based on the value it holds.

In this case, we will check whether the value in a cell in less than 0 or not. If it is, then the cell can be highlighted in a specified color (which would be red in this case).

Here are the steps to do this:

1.  Go to Home → Conditional Formatting → Highlight Cell Rules → Less Than.![Make Negative Numbers Show Up in Red in Excel - Less than](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20376%20423'%3E%3C/svg%3E)
2.  Select the cells in which you want to highlight the negative numbers in red.![Make Negative Numbers Show Up in Red in Excel - Select Cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20167%20297'%3E%3C/svg%3E)
3.  In the Less Than dialog box, specify the value below which the formatting should be applied. If you want to use formatting other than the ones in the drop-down, use the Custom Format option.![Make Negative Numbers Show Up in Red in Excel Less than dialog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20484%20142'%3E%3C/svg%3E)
4.  Click OK.

All the cells with a value less than 0 would get highlighted in Light Red color with dark red text in it.

![Make Negative Numbers Show Up in Red in Excelhig hlighted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20184%20333'%3E%3C/svg%3E)

Using conditional formatting is also helpful when you want to print the reports. While you may not see a significant difference in the font color in a black and white printout, since conditional formatting highlights the entire cell, it makes the highlighted cells stand out.

_Caution: Conditional Formatting is volatile, which means that it recalculates whenever there is a change in the workbook. While the impact is negligible on small data sets, you may see some drag because of it when applied to large datasets._

Highlight Negative Numbers in Red – Using Inbuilt Excel Number Formatting
-------------------------------------------------------------------------

Excel has some inbuilt number formats that make it super easy to make negative numbers red in Excel.

When you apply the ‘Number’ format, it [adds two decimals](https://trumpexcel.com/add-decimal-places-excel/)
 to the numbers and makes the negative numbers show up in red.

Something as shown below:

![make-negative-numbers-show-up-in-red-in-excel-numbers-in-red](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20152%20252'%3E%3C/svg%3E)

To do this:

1.  Select the cells in which you want to highlight the negative numbers in red.
2.  Go to the Home tab → Number Format group and click on the dialog launcher (it is the small tilted arrow icon at the bottom right of the group. This will open the Format Cell dialog box _(or you can use the keyboard shortcut Control + 1).![Make Negative Numbers Show Up in Red in Excel - dialog launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20212%20132'%3E%3C/svg%3E)_
3.  In the Format Cells dialog box, within the Number tab, select Number in the Category list. In the option on the right, select the red text in the ‘Negative numbers’ options.![make-negative-numbers-show-up-in-red-in-excel-number-format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20533%20467'%3E%3C/svg%3E)
4.  Click OK.

This would automatically add two decimal points and make the negative numbers red with a minus sign.

Note that none of the techniques shown in this tutorial change the value in the cell. It only changes the way the value is displayed.

Also read: [Show Negative Numbers in Parentheses (Brackets) in Excel](https://trumpexcel.com/show-negative-numbers-parentheses-brackets-excel/)

Highlight Negative Numbers in Red – Using Custom Number Formats
---------------------------------------------------------------

If the inbuilt formats are not what you want. Excel allows you to create your own custom formats.

Here are the steps:

1.  Select the cells in which you want to highlight the negative numbers in red.
2.  Go to the Home tab → Number Format group and click on the dialog launcher. This will open the Format Cell dialog box _(or you can use the keyboard shortcut Control + 1).  
    ![Make Negative Numbers Show Up in Red in Excel - dialog launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20212%20132'%3E%3C/svg%3E)_
3.  In the Number tab, select Custom from the Category list and use the below format in type:  
    General;\[Red\]-General![Make Negative Numbers Show Up in Red in Excel - format cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20536%20470'%3E%3C/svg%3E)
4.  Click OK.

This will make the negative numbers show up in red, while everything else remains the same.

![Make Negative Numbers Show Up in Red in Excel Format cells result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20185%20333'%3E%3C/svg%3E)

**How this works:**

There are four format types that you can customize in Excel:

_<Positive Numbers>;<Negative Numbers>;<Zeroes>;<Text>_

These formats are separated by a semicolon.

You can specify the format for each type and it will show up that way in Excel.

For using colors, you can specify the color in square brackets at the beginning of the format. Not all colors are supported in custom number formatting, but you can use common colors such as red, blue, green, yellow, cyan, etc.

You can specify a format for any or all of these four parts. For example, if you write General;General;General;General then everything is in the General format.

But if you write **0.00;-0.00;0.00;General**, positive numbers are displayed with 2 decimals, negative with a negative sign and 2 decimals, zero as 0.00, and text as normal text.

Similarly, you can specify the format for any of the four parts.

If you mention only:

*   One format: It is applied to all the four sections. For example, if you just write General, it will be applied for all the four sections.
*   Two formats: The first one is applied to positive numbers and zeros, and the second is applied to negative numbers. Text format by default becomes General.
*   Three Formats: The first one is applied to positive numbers, the second is applied to negative numbers, the third is applied to zero, and the text disappears as nothing is specified for text.

If you want to learn all about custom number formatting, I would highly recommend [Office Help](http://office.microsoft.com/en-in/excel-help/create-a-custom-number-format-HP010342372.aspx)
 section.

**You May Also Like the Following Excel Tutorials:**

*   [Remove Leading, Trailing, and Doble Spaces in Excel](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
    .
*   [How to Add Plus Sign Before Numbers in Excel](https://trumpexcel.com/add-plus-sign-before-numbers-excel/)
    
*   [Highlight Every Other Row in Excel using Conditional Formatting](https://trumpexcel.com/highlight-every-other-row-excel/)
    .
*   [Change Negative Number to Positive in Excel](https://trumpexcel.com/change-negative-to-positive-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

10 thoughts on “How to Make Negative Numbers Show Up in Red in Excel”
---------------------------------------------------------------------

1.  PERFECT
    
    [Reply](https://trumpexcel.com/negative-numbers-red-excel/#comment-14845)
    
2.  THIS IS GREAT FOR A BEGINNER LIKE ME SELF TEACHING
    
    [Reply](https://trumpexcel.com/negative-numbers-red-excel/#comment-13671)
    
3.  How we can show highlighted 0 in red in excel pivot charts?
    
    [Reply](https://trumpexcel.com/negative-numbers-red-excel/#comment-10888)
    
4.  I can’t figure out how to do this when it is pulling the data into the cell from another tab. The formatting doesn’t seem to apply
    
    [Reply](https://trumpexcel.com/negative-numbers-red-excel/#comment-10013)
    
5.  check this  
    [http://tutorialway.com/microsoft-excel-font-formatting/](http://tutorialway.com/microsoft-excel-font-formatting/)
    
    [Reply](https://trumpexcel.com/negative-numbers-red-excel/#comment-7371)
    
6.  I have a formatting problem that you might be able to help me with. My objective is to have a comma format with floating decimal. #,###,### almost gets the result I want except whole numbers are displayed with a decimal. For example, “1001.001” appears as “1,001.001”, exactly as I want it, but “1001” appears as “1,001.” (includes decimal point) when I want it to appear as “1,001” (no decimal point). Other than using VBA to test and format each entry or a conditional format for every cell in the workbook, I cannot seem to find a solution. Any ideas?
    
    [Reply](https://trumpexcel.com/negative-numbers-red-excel/#comment-4021)
    
    *   Hello Jim, As far as I know, there is no way to get floating decimal using custom number formatting or any other non-VBA method
        
        [Reply](https://trumpexcel.com/negative-numbers-red-excel/#comment-4027)
        
7.  using number format and currecncy format colour is not getting changed. Do i need to set something else?
    
    [Reply](https://trumpexcel.com/negative-numbers-red-excel/#comment-3999)
    
    *   Hey.. You need to open the format cells dialog box and then select the number format (with red text). I have updated the tutorial to show the steps.
        
        [Reply](https://trumpexcel.com/negative-numbers-red-excel/#comment-4015)
        
        *   got it. tks
            
            [Reply](https://trumpexcel.com/negative-numbers-red-excel/#comment-4022)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/negative-numbers-red-excel/#respond)

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