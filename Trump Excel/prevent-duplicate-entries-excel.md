# Prevent Duplicate Entries in Excel

**Source:** https://trumpexcel.com/prevent-duplicate-entries-excel

---

[Skip to content](https://trumpexcel.com/prevent-duplicate-entries-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/prevent-duplicate-entries-excel/#below-title)

When doing data entry work in Excel, you may want to prevent entering duplicate entries in a column or a range of cells.

Thankfully, there is a feature in Excel that allows you to do precisely this – and it’s called **Data Validation**.

In this article, I will show you how to prevent duplicate entries in Excel using Data Validation. I will also cover a method that instantly highlights duplicate entries using Conditional Formatting.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/prevent-duplicate-entries-excel/#)

Prevent Duplicate Entries Using Data Validation
-----------------------------------------------

Below, I have a data set where I am entering names in column A, and I want Excel to prevent me from entering a duplicate name in the column:

![Data set to prevent duplicate entries in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20285%20412'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the range of cells in which you want to prevent the duplicate entry. In this example, I will select the entire column A.

![Select the entire column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20287%20446'%3E%3C/svg%3E)

2.  Click the Data tab.
3.  In the _Data Tools_ group, click on the _Data Validation_ icon. This will open the Data Validation dialog box.

![Click on the data validation icon in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20698%20161'%3E%3C/svg%3E)

4.  In the _Settings_ tab, click the _Allow_ drop-down and select the _Custom_ option.

![Click the custom option in the allowed dropdown in data validation to prevent duplicate entry](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20412'%3E%3C/svg%3E)

5.  In the formula field, enter the below formula.

\=COUNTIF(A:A,A1)=1

![And the formula to prevent duplicate entry](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20412'%3E%3C/svg%3E)

In the above formula, I have used _A:A_ as the first argument of the [COUNTIF function](https://trumpexcel.com/excel-countif-function/)
, but you can use any range on which you want to apply this data validation rule.

6.  Click the ok button.

Now, when you are [doing a data entry](https://trumpexcel.com/excel-data-entry-tips/)
 in column A, and you repeat a name (or any text string that has already been entered in column A), it will show you an error prompt, as shown below.

![Yellow box shown when you have duplicate entry in the range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20453%20221'%3E%3C/svg%3E)

**How does this work?**

Whenever you enter anything in any cell in column A, it checks whether it satisfies the formula we used in [data validation](https://trumpexcel.com/learn-all-about-data-validation-in-excel/)
.

The formula _\=COUNTIF(A:A,A1)=1_ checks the content of the cell and counts whether the same also appears in any other cell or not.

If the cell content is unique, our formula would return TRUE, and Data Validation would allow you to make that entry in the cell. If more than one instance of that name appears in the column, our formula will return FALSE, and Data Validation will not allow us to enter that value by showing us the Error Prompt.

### Customizing the Error Alert Dialog Box

You can customize the error dialog box to make it more useful for the user.

By default, the title of the dialog box says _Microsoft Excel_, but you can change it and make it something more meaningful such as ‘Duplicate Names Not Allowed’.

Here is how to do this:

1.  Open the Data Validation dialog box (Data tab –> Data Tools Group –> Data Validation).
2.  Set the Data Validation rule as covered in the previous section.
3.  Click the Error Alert tab

![Select the error alert tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20412'%3E%3C/svg%3E)

4.  Enter the customized title and error message that you want to show on the Error Alert Dialog Box.

![enter the customized title and description](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20412'%3E%3C/svg%3E)

Now, when you make a duplicate entry in the column, you will see a dialog box, as shown below.

![Duplicate entry not allowed customized dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20241'%3E%3C/svg%3E)

Note: If you copy a cell and paste it over the cells where data validation rules have been applied, it will remove the data validation rules. So this method would only work if you are manually entering the data.

Also read: [How to Create a Data Entry Form in Excel](https://trumpexcel.com/data-entry-form/)

Prevent Duplicate Entries By Highlighting Them
----------------------------------------------

Another method that can be helpful in preventing duplicate entries is by highlighting the duplicate entry in a different color as soon as it is entered.

This can easily be done using [Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
.

Let me show you how it works.

Below, I have a dataset where I’m entering names and column A, and I want to prevent duplicate name entries in the column.

![Data set to prevent duplicate entries in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20285%20412'%3E%3C/svg%3E)

Here are the steps to highlight duplicate entries as soon as you type it:

1.  Select the column or range of cells in which you want to prevent duplicate entries. In this example, I’m going to select the entire column A.
2.  Click the Home tab.
3.  Click on the Conditional Formatting option.

![Click on the conditional formatting icon in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20140'%3E%3C/svg%3E)

4.  Go to the _Highlight Cell Rules_ option, and in the additional options that show up, select the _Duplicate Values_ option.

![Click on the duplicate values option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20473%20604'%3E%3C/svg%3E)

5.  This opens the _Duplicate Values_ dialog box, where you can specify the formatting to be applied to cells that contain duplicate values. In this example, I will go with the default _Light Red Fill with Dark Red Text_. You can choose from any other pre-set formatting or create your own by clicking on the drop-down and then selecting _Custom Format._

![Duplicate values dialog box in conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20422%20167'%3E%3C/svg%3E)

6.  Click OK

That’s it!

Now, as soon as you enter a name that is already there in column A, it will instantly highlight the cell in the specified format.

![duplicate values are highlighted in the column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20282%20445'%3E%3C/svg%3E)

Also read: [How to Highlight Blank Cells in Excel](https://trumpexcel.com/highlight-blank-cells-in-excel/)

So, these are two methods you can use to prevent duplicate entries in a column in Excel.

You can use Data Validation to stop the user from entering a duplicate entry by showing an error prompt or use Conditional Formatting that allows you to enter a duplicate value but highlights it so that you know it is a repeat of an existing value.

I hope you found this article helpful. If you have any feedback or suggestions for me, do let me know in the comments section.

**Other Excel articles you may also like:**

*   [Remove Formulas (but Keep Data) in Excel](https://trumpexcel.com/remove-formulas-keep-data-excel/)
    
*   [Select Till End of Data in a Column in Excel](https://trumpexcel.com/select-end-of-data-in-column-excel/)
    
*   [Conditional Data Entry using Data Validation](https://trumpexcel.com/conditional-data-entry-in-excel/)
    
*   [Enable Data Entry in a Cell in Excel only if a Dependent Cell is Filled](https://trumpexcel.com/enable-data-entry-in-a-cell-in-excel-only-if-a-dependent-cell-is-filled/)
    
*   [Quickly Enter Data in Excel in a Specific Order in Non-Contiguous Cells](https://trumpexcel.com/enter-data-in-excel-in-specific-order/)
    
*   [Remove Duplicates Within a Cell in Excel](https://trumpexcel.com/remove-duplicates-from-cell-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

3 thoughts on “Prevent Duplicate Entries in Excel”
--------------------------------------------------

1.  Love Excel, and you for your generous social service. Appreciate your effort to make us (the world) more productive.  
    \-Thilak Wijesinghe (Sri Lanka)
    
    [Reply](https://trumpexcel.com/prevent-duplicate-entries-excel/#comment-28922)
    
2.  It is really helpful and congratulations for your effort!!!!
    
    [Reply](https://trumpexcel.com/prevent-duplicate-entries-excel/#comment-28341)
    
    *   Glad you found it helpful Gheni!
        
        [Reply](https://trumpexcel.com/prevent-duplicate-entries-excel/#comment-28352)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/prevent-duplicate-entries-excel/#respond)

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