# How to Display Numbers as Fractions (Write Fractions in Excel)

**Source:** https://trumpexcel.com/display-numbers-as-fractions-excel

---

[Skip to content](https://trumpexcel.com/display-numbers-as-fractions-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/display-numbers-as-fractions-excel/#below-title)

Getting numbers to show up as fractions in Excel could be a challenge.

In case you try and enter any fraction in a cell in Excel, there is a possibility that Excel may change it to a date or a text string.

This happens because fractions are not one of the data types that Excel understands. So when you give it a fraction, it tries and converts it into a date or a [text string](https://trumpexcel.com/count-cells-that-contain-text/)
 which are the data types that are acceptable for Excel.

So what if you want to get your numbers to get displayed as fractions in excel?

Don’t worry, there is a way around it!

In this short tutorial, I’m going to show you a **couple of methods you can use to display numbers as fractions in Microsoft Excel**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/display-numbers-as-fractions-excel/#)

Show Decimals as Fractions by Changing the Cell Format
------------------------------------------------------

Fractions are essentially decimal numbers. for example, 1/2 is 0.5, and 1/4 is 0.25

While fractions may be something that Excel does not understand by default, decimals are an acceptable data type.

So, you can have a decimal number in a cell in Excel and format it in such a way that it shows up as the desired fraction.

Suppose, I have a data set of some decimals in column A (as shown below) that I want to show as fractions.

![Data with decimals](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20255%20418'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the cells that have the decimals
2.  Click the Home tab

![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20536%20223'%3E%3C/svg%3E)

3.  In the Number group, click on the format drop-down

![Click on the Format drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20546%20223'%3E%3C/svg%3E)

4.  Select Fractions

![Click on Fractions option from the drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20786'%3E%3C/svg%3E)

The above steps would instantly convert all the decimal numbers into fractions.

![Decimals converted to fractions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20276%20432'%3E%3C/svg%3E)

Now there are two things you need to know when you’re using the inbuilt Fraction format to convert decimals into fractions:

1.  You will always get a fraction where the denominator of the fraction is a single-digit
2.  In a case where the decimal cannot be converted into an exact fractional value (while keeping the denominator as a single digit), it will round the number and give you the closest fraction. For example, if you have the decimal 0.9 (which is the decimal value for 9/10), the above method would give you 8/9 (which is an approximate fraction while keeping the denominator to a single digit).

Note: When you change the format of a cell and make a decimal number show up as a fraction, it only changed the way it is being shown to the user. It does not change the original value in the cell. For example, if a cell has 0.9 as the decimal value and you apply fraction format that shows it as 8/9, the value in the cell still remains 0.9

Also read: [How to Write Scientific Notation in Excel?](https://trumpexcel.com/scientific-notation-excel/)

### Other In-Built Fraction Formats in Excel

The default fraction format that you can choose from the drop-down in the ribbon would always give you a fraction where the denominator is a single digit.

But there are other inbuilt fraction formats that you can also use.

Suppose I have a below data set for decimals in column A:

![Data with decimals](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20255%20418'%3E%3C/svg%3E)

Below are the steps to access and use other inbuilt fraction formats in Excel:

1.  Select all the cells in column A
2.  Click the Home tab
3.  In the Number group, click on the dialog box launcher (that looks like a titled arrow). This will open the ‘Format Cells’ dialog box

![Click on the dialog box launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20654%20223'%3E%3C/svg%3E)

4.  In the Format Cells dialog box, within the ‘Number’ tab, click on the ‘Fraction’ category

![Select the Fraction option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20557'%3E%3C/svg%3E)

5.  Select any of the already listed fraction formats

![Select from the different fractions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20557'%3E%3C/svg%3E)

Based on whatever fraction format you choose, the numbers in column A would be displayed in that format.

Below are all the fraction formats that are available to you:

*   Up to one digit (1/4)
*   Up to two digits (21/25)
*   Up to three digits (312/943)
*   As halves (1/2)
*   As quarters (1/4)
*   As eights (1/8)
*   As sixteenths (1/16)
*   As tenths (1/10)
*   As hundreds (1/100)

Also read: [How to Add Parentheses Around Text in Excel](https://trumpexcel.com/add-parentheses-excel/)

### Creating Your Own Fraction Format in Excel

In most cases, the inbuilt fraction formats are sufficient.

But sometimes, there may be a need where you have to have a specific number as the denominator in the fraction format (say I want the denominator to always be 30).

Since I do not have any inbuilt format where the denominator can be 30, I can create my own fraction format in this case.

Below are the steps to create your own custom fraction format in Excel:

1.  Select all the cells with data (in this example, I will select all the item numbers I have in column A)

![Select cells in column A](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20255%20420'%3E%3C/svg%3E)

2.  Click the Home tab
3.  In the Number group, click on the dialog box launcher (that looks like a titled arrow).
4.  In the Format Cells dialog box that opens up, within the Number tab, click on the Custom category

![Select Custom option is Format Cells dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20557'%3E%3C/svg%3E)

5.  In the Type field, enter the following code: # ??/30

![Enter the custom format for the fraction](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20557'%3E%3C/svg%3E)

6.  Click Ok

The above format would convert all the decimal numbers into a fraction where the denominator is always 30.

![Result where decimals show up in fraction with 30 as denominator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20266%20430'%3E%3C/svg%3E)

Let me quickly explain how this custom number format works:

*   The # at the beginning is needed to show mixed fractions (such as 2 1/30 or 17 12/30). This tells the format that In case the decimal number has an integer portion, show it alongside the fraction. A # represents any number of digits in the format
*   ??/30 would force the formatting to always have 30 as the denominator and have space for two digits as the numerator. You can also keep just one ?, but having two question marks would mean that in case you have fractions with one of two digits in the numerator, they would always align in a column (as you can see in the image above).

Similarly, you can create your own custom format from fractions and specify the denominator you want.

Also read: [Calculate Ratios in Excel](https://trumpexcel.com/calculate-ratios-excel/)

Show Decimals as Fractions Using the TEXT Formula
-------------------------------------------------

Another way to convert decimal numbers into fractions is by using the [TEXT function in Excel](https://trumpexcel.com/excel-text-function/)
.

Just like the custom number format method I covered above, the TEXT function allows you to specify the format in which you want to show the decimal number.

One major difference between the TEXT function method and the Custom Number Format method is that the result of the TEXT formula is a text string.

So if you convert 0.1 into 1/10 using the TEXT formula, it would be a text string and you won’t be able to use it in calculations.

Let me first show you how this method works and then I will show you why you may want to use it in some cases.

Suppose you have the decimals in column A as shown below, that you want to convert to fractions:

![Dataset to convert decimals to fractions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20455%20420'%3E%3C/svg%3E)

Below is the formula that will do this:

\=TEXT(A2,"# ?/?")

![TEXT formula to show decimals and fractions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20458%20465'%3E%3C/svg%3E)

The above formula takes the value in cell A2, and then shows it in the specified format. In the above example, I have used the format that shows the fraction that can only contain one digit in numerator and denominator.

You can specify any fraction format you need as the second argument of the formula (and make sure it’s in double quotes).

Now coming back to the question – “_What’s the benefit of using the TEXT formula to show numbers/decimals as fractions?_“.

Since the output of the text formula is a text string, you can add a prefix or suffix to the result of this formula.

Let me show you why that’s important.

Suppose you have the data set as shown below, where you have the product ID in column A and the value in column B.

![Data with Text and Decimals](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20582%20418'%3E%3C/svg%3E)

Below is the formula that you can use to combine the product ID and the value (as a fraction) and get the result in the same cell.

\=A2&" – "&TEXT(B2,"# ?/?")

![formula to get text and fraction together](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20586%20467'%3E%3C/svg%3E)

Since the text formula converted the fraction output into a text string, we were able to append another text string before it.

This is something you will not be able to do if you use the custom format method to convert decimal to fractions.

Writing Fractions in Excel (without Excel changing it)
------------------------------------------------------

If you try and enter some fractions in a cell in excel, you would notice that they are automatically converted into a date.

For example, if you enter 1/10, it will automatically be converted to 10-Jan or 01-Oct (depending on your regional calendar format)

This happens as Excel considers 1/10 as a valid date format, and converts it into one.

But what if you do not want Excel to convert it into a date.

What if you still want to continue using it as a fraction?

One way could be to enter the decimal number and then convert it into a fraction using the methods covered above.

Let me show you two more methods that you can quickly enter a fraction in a cell in excel without excel changing it into a date:

*   The simplest way would be to start the data entry by first [entering an apostrophe](https://trumpexcel.com/convert-numbers-to-text-excel/)
     followed by the fraction. When you add an apostrophe in a cell, anything that follows it is converted into a text string. Since date and time values are stored as numbers in excel, a text string would not be converted into a date

![Enter apostrophe to convert numbers to fractions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20407%20165'%3E%3C/svg%3E)

*   The other method would be to first change the format of the cell and make it text. To do this, click the Home tab and in the Number group, click on the Format drop-down and select Text. Once done, anything you enter in that cell would be considered a text string and the fraction would not be converted into a date

![Change cell format to text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20488'%3E%3C/svg%3E)

In this tutorial, I showed you how to show decimal numbers as fractions using two methods (custom formatting and TEXT formula).

I also covered how to enter fractions in Excel without it getting changed into a date format.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like**:

*   [How to Stop Excel from Rounding Numbers (Decimals/Fractions)](https://trumpexcel.com/stop-excel-from-rounding-numbers/)
    
*   [How to Add Decimal Places in Excel (Automatically)](https://trumpexcel.com/add-decimal-places-excel/)
    
*   [How to Stop Excel from Changing Numbers to Dates Automatically](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/)
    
*   [How to Make Negative Numbers Show Up in Red in Excel](https://trumpexcel.com/negative-numbers-red-excel/)
    
*   [7 Amazing Excel Custom Number Format Tricks (you Must know)](https://trumpexcel.com/excel-custom-number-formatting/)
    
*   [Convert Time to Decimal Number in Excel (Hours, Minutes, Seconds)](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [How to Round to the Nearest Integer or Multiple of 0.5 / 5 / 10 in Excel](https://trumpexcel.com/round-to-nearest-integer/)
    
*   [Convert Scientific Notation to Number or Text in Excel](https://trumpexcel.com/convert-scientific-notation-to-number-text/)
    
*   [Show Negative Numbers in Parentheses (Brackets) in Excel](https://trumpexcel.com/show-negative-numbers-parentheses-brackets-excel/)
    
*   [How to Convert Fraction to Decimal in Excel](https://trumpexcel.com/convert-fraction-to-decimal-excel/)
    
*   [Round to the Nearest 1000 in Excel](https://trumpexcel.com/round-to-nearest-1000-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/display-numbers-as-fractions-excel/#respond)

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