# Enable Conditional Data Entry in Excel using Data Validation

**Source:** https://trumpexcel.com/conditional-data-entry-in-excel

---

[Skip to content](https://trumpexcel.com/conditional-data-entry-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/conditional-data-entry-in-excel/#below-title)

Excel is more than a [data entry](https://trumpexcel.com/excel-data-entry-tips/)
 tool. But if you only talk about data entry in Excel, it’s a damn good one. Using the [data validation](https://trumpexcel.com/learn-all-about-data-validation-in-excel/)
, you can enable data entry in cell(s) based on a predefined condition.

Conditional Data Entry in Excel Using Data Validation
-----------------------------------------------------

Here are a few examples of conditional data entry rules:

*   Allow data entry from a pre-defined list only (using drop-down lists).
*   Allow data entry only when the specified cell(s) are filled.
*   Allow DATE entry between two specified dates only.

You can also combine multiple conditions to create a data entry rule.

This type of conditional data entry in excel can be done using the data validation feature in Excel. It can enable data entry in the specified cells only when the specified conditions are met, else it shows an error.

### Allow Data Entry from a Pre-defined List

You can restrict the user to choose from a list by creating a [drop-down list](https://trumpexcel.com/excel-drop-down-list/)
. For example, suppose you have a list of countries as shown below, and you want to allow the entry of only one of these names in cell C1:

![conditional data entry in excel - drop down data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20324%20132'%3E%3C/svg%3E)

You can create a drop-down list that will restrict the entries to only the ones mentioned in the list. If you try to enter any other text string, it will show an error (as shown below):

![conditional data entry in excel - drop down list error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20844%20372'%3E%3C/svg%3E)

Here is how you can create a drop-down list:

*   Select the cell where you want to show the drop down list. In this example, it is cells C1.
*   Go to Data –> Data Tools –> Data Validation.  
    ![conditional data entry in excel - data validation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20127'%3E%3C/svg%3E)
*   In the data validation dialogue box, select the settings tab and make the following changes:
    *   Allow: List
    *   Source: $A$1:$A$6 (you can use the range where you have the data).
    *   Ignore Blank: Checked (uncheck this if you don’t want the user to enter blank).
    *   In-cell dropdown: Checked (this would enable the drop down feature).  
        ![conditional data entry in excel - drop down data settings](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20401%20320'%3E%3C/svg%3E)

This will create a drop-down list in the selected cell.

Now you can either select them from the drop-down list, or manually enter the data in it. If you enter any data that is not from the source data, it will show an error.

_**CAUTION**__**:**_ If you copy and paste over the cell which has the data validation rules, the data validation rules disappear.

_**Download the Example File**_  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2015/10/Condiitonal-Data-Entry.xlsx)

Also read: [Prevent Duplicate Entries in Excel](https://trumpexcel.com/prevent-duplicate-entries-excel/)

### Data Entry when a Dependent Cell is Filled

This could be the case when you want the user to go in a sequence and complete filling a form/questionnaire/survey.

Let’s say I have a something as shown below:

![conditional data entry in excel - form](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20286%20150'%3E%3C/svg%3E)

In this data set, I want the user to first fill the name (first name and last name is mandatory) and then move on to fill the date. If the user skips entering the name, then I want to show an error (as shown below):

![conditional data entry in excel - dependent entry](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20844%20372'%3E%3C/svg%3E)

This can easily be done using data validation. To do this:

*   Select the cell where you want to apply this condition. In the above example, it is cell B5.
*   Go to Data –> Data Tools –> Data Validation  
    ![conditional data entry in excel - data validation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20127'%3E%3C/svg%3E)In the data validation dialogue box, select the settings tab and make the following changes:
    
    *   Allow: Custom
    *   Formula: \=AND($B$1<>””,$B$3<>””).
    *   Ignore Blank: Unchecked (make sure this is unchecked else it will not work).

![conditional data entry in excel - check dependent cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20402%20323'%3E%3C/svg%3E)

In this case, we have used an [AND](https://trumpexcel.com/excel-and-function/)
 function that checks whether both B1 and B3 have already been filled. If not, then it shows an error.

_**CAUTION**__**:**_ If you copy and paste over the cell which has the data validation rules, the data validation rules disappear.

### Date Entry Between Two Specified Dates

There is an inbuilt feature in data validation that will let you do this. You can specify the upper and lower date limits, and if the user enters a date which is outside of this range, he/she will get an error.

To do this:

*   Select the cell where you want to apply this condition. In the above example, it is cell B5.
*   Go to Data –> Data Tools –> Data Validation  
    ![conditional data entry in excel - data validation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20127'%3E%3C/svg%3E)In the data validation dialogue box, select the settings tab and make the following changes:
    
    *   Allow: Date
    *   Data: Between
    *   Start Date: Enter the start date here (any date that is before this date will not be accepted).
    *   End Date: Enter the end date here (any date that is after this date will not be accepted).![conditional data entry in excel - date limits](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20401%20321'%3E%3C/svg%3E)

You can also use a cell reference or a formula to specify the date. For example, you can use [TODAY()](https://trumpexcel.com/excel-today-function/)
 function as one of the date limits (if you want the lower limit to the current date).

Since Excel stores the dates as numbers, you can also use numbers instead of dates. For example, instead of using 01-01-2015, you can also use the number 42005.

_**CAUTION**__**:**_ If you copy and paste over the cell which has the data validation rules, the data validation rules disappear.

_**Download the Example File**_  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2015/10/Condiitonal-Data-Entry.xlsx)

##### Multiple Data Entry Conditions

You can combine multiple conditions as well. For example, let’s say you want to enter a date in cell B5 with the following conditions:

*   First Name and the Last have already been filled by the user.
*   The entered date is between 01-01-2015 and 10-10-2015.

To do this:

*   Select the cell where you want to apply this condition. In the above example, it is cell B5.
*   Go to Data –> Data Tools –> Data Validation![conditional data entry in excel - data validation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20127'%3E%3C/svg%3E)
*   In the data validation dialogue box, select the settings tab and make the following changes:
    *   Allow: Custom
    *   Formula: \=AND($B$1<>””,$B$3<>””,B5>=DATE(2015,10,1),B5<=DATE(2015,10,10))
    *   Ignore Blank: Unchecked (make sure this is unchecked else it will not work)

![conditional data entry in excel - multiple conditions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20403%20322'%3E%3C/svg%3E)

This formula checks for four conditions – whether the two cells (B1 and B3 are already filled, and whether the date entered in cell B5 is within the specified date range).

_**CAUTION**__**:**_ If you copy and paste over the cell which has the data validation rules, the data validation rules disappear.

_**Download the Example File**_  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2015/10/Condiitonal-Data-Entry.xlsx)

Similarly, you can create and test for multiple conditions while allowing data entry in Excel.

**You May Also Like the Following Excel Tips and Tutorials:**

*   [Excel Data Entry Form](https://trumpexcel.com/data-entry-form/)
    .
*   [Using Drop-down Lists in Excel](https://trumpexcel.com/excel-drop-down-list/)
    .
*   [100+ Excel Interview Questions and Answers](https://trumpexcel.com/excel-interview-questions/)
    .
*   [How to Remove Drop-Down List in Excel?](https://trumpexcel.com/remove-drop-down-list-excel/)
    
*   [Create Data Validation List from Excel Table as Source](https://trumpexcel.com/data-validation-list-from-excel-table/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Enable Conditional Data Entry in Excel using Data Validation”
-----------------------------------------------------------------------------------

1.  For Data Entry when a Dependent Cell is Filled, I have 6-8 previous cells that must be filled prior to the 9th cell being filled. Is there a short cut in the AND formula for the column of cells that must be filled so each cell does not have to be entered with $A$1″”,$A$2 etc…. all the way to $A$8″”?
    
    Thank you for any help.
    
    [Reply](https://trumpexcel.com/conditional-data-entry-in-excel/#comment-13266)
    
2.  Sir,  
    I am interested to know  
    How to allow or prevent Data entry in a cell based on condition of another cell.
    
    [Reply](https://trumpexcel.com/conditional-data-entry-in-excel/#comment-12710)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/conditional-data-entry-in-excel/#respond)

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