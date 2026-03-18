# An Introduction to Data Validation in Excel

**Source:** https://trumpexcel.com/learn-all-about-data-validation-in-excel

---

[Skip to content](https://trumpexcel.com/learn-all-about-data-validation-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/learn-all-about-data-validation-in-excel/#below-title)

Data Validation in Excel lets you control the data that can be entered in a cell. You can restrict the user to enter only a specified range of numbers or text or date.

You can also use data validation functionality to create an [Excel drop down list](https://trumpexcel.com/excel-drop-down-list/)
 (which is definitely one of the coolest and most powerful features in Excel)

Accessing Data Validation in Excel
----------------------------------

Data Validation in Excel can be accessed through the Data tab in the Ribbon.

![Data Validation In Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%2090'%3E%3C/svg%3E)

In most cases, there are three situations where you would want to use Data Validation in Excel:

*   When you want to restrict data entry to certain numbers/text/dates. Data that does not meet the validation criteria is not allowed.
*   When you want to inform user whenever out-of-range data is entered. However, all kinds of data entry is allowed.
*   When you guide the user on what data to enter. All kinds of data entries are allowed.

Let’s us go through these situations one by one:

### Restricting data entry to certain numbers/text/dates

Data validation allows you to specify a condition for data entry in a cell/cells in Excel.

Once specified, it does not allow the user to enter anything that is out of that specified range.

This feature can be accessed by opening the data validation dialogue box and selecting the Settings option

![Data Validation In Excel Data Entry Restricted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20240'%3E%3C/svg%3E)

In the drop-down list, you can choose the condition you want to apply for a range of cells

*   Any Value – Allows any value to be entered in a cell.
*   Whole Number – Allows only whole numbers to be entered, with additional conditions such as greater/less than, between/not between, equal to/not equal to.
*   Decimal – Allows numbers with decimals to be entered, with additional conditions such as greater/less than, between/not between, equal to/not equal to.
*   List – Creates a drop down by taking a list of items (through range selection or named range).
*   Date – Allows dates (or its number value) to be entered, with additional conditions such as greater/less than, between/not between, equal to/not equal to.
*   Time – Allows time (or its number  value) to be entered, with additional conditions such as greater/less than, between/not between, equal to/not equal to.
*   Text Length – Allows text with the condition on its length.
*   Custom – Allows values that meets the specified criteria. For example, if I use the formula =A1>10, then only numbers greater than 10 are allowed in cell A1.

Whenever you enter any data in a cell that violates the specified condition, it shows an error.  
![Data Validation in Excel - Error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20412%20132'%3E%3C/svg%3E)

Also read: [Prevent Duplicate Entries in Excel](https://trumpexcel.com/prevent-duplicate-entries-excel/)

### Inform User Whenever out-of-range Data is Entered (all kinds of data entry is allowed)

While the earlier section was about restricting the user to a specified range while entering data, this section is about warning the user if any out-of-range data is entered. However, the data entry is still allowed. This can be enabled by changing the error message settings.

You can customize the error message by going to the Error Alert tab in the Data Validation dialogue box. There are three options:

*   **Stop Error** – Displays the stop error and does not let user enter the data which is out of the specified range.
*   **Warning Error** – Displays the warning error but lets user enter the data which is out of the specified range.
*   **Information Error** – Displays the information error but lets user enter the data which is out of the specified range.

![Data Validation in Excel - Error Messages Types](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20198'%3E%3C/svg%3E)

### When You Guide the User on What Data to Enter (all kinds of data entry is allowed)

Suppose you have a list of employees and you want to get their joining date. There could be multiple formats to enter the date (such as 01/01/2014, or 01 Jan, 2014, or 1st Jan 2014). However, for the sake of consistency, it is better to get all the dates in one format. However, it is alright of people enter it in any other format, as capturing the data is of prime importance.

![Data Validation In Excel Display Message](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20265%20150'%3E%3C/svg%3E)

_Here is how this can be done:_

1.  Select any cell and then go to Data tab –> Data Validation
2.  In Data Validation dialogue box, select Input Message tab
3.  Ensure that ‘Show [input message](https://trumpexcel.com/input-message-in-excel/)
     when cell is selected’ check box is selected
4.  In the Input message tab, enter Title (max 32 characters, optional) and Input Message (max 256 characters)  
    ![Data Validation In Excel Display Message Dialogue Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20240'%3E%3C/svg%3E)
5.  Click ok. Now whenever you either click on the cell or select it using keyboard, it would display the message.

_Caution: If you move the message box from its position, then all the message box will be shown at that position only. So it is safe not to move the message box._

###### **Related Tutorials on Data Validation in Excel:**

*   [Enable data entry only if a dependent cell is filled](https://trumpexcel.com/enable-data-entry-in-a-cell-in-excel-only-if-a-dependent-cell-is-filled/)
    .
*   [Disguise numbers as text in a data validation drop down](https://trumpexcel.com/format-numbers-as-text-excel/)
    .
*   [Create a dependent validation drop down list](https://trumpexcel.com/dependent-drop-down-list-in-excel/)
    .
*   [How to Remove Drop-Down List in Excel?](https://trumpexcel.com/remove-drop-down-list-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “An Introduction to Data Validation in Excel”
----------------------------------------------------------

1.  Excellent courses
    
    [Reply](https://trumpexcel.com/learn-all-about-data-validation-in-excel/#comment-13970)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/learn-all-about-data-validation-in-excel/#respond)

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