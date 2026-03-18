# How to Find External Links and References in Excel

**Source:** https://trumpexcel.com/find-external-links-excel

---

[Skip to content](https://trumpexcel.com/find-external-links-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/find-external-links-excel/#below-title)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/find-external-links-excel/#)

What are External Links or References?
--------------------------------------

When you create formulas in Excel and refer to a data point in an another workbook, Excel creates a link to that workbook.

So your formula may look like something as shown below:

![Find External Links and References in Excel - example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20729%20134'%3E%3C/svg%3E)

Note that the part highlighted in yellow is the external link (also called external reference). This part of the formula tells Excel to go to this workbook (Score.xlsx) and refer to the specified cell in the workbook.

The benefit of having an external link in your formula is that you can automatically update it when the data in the linked workbook changes.

However, the drawback is that you always need to have that linked workbook available. If you delete the linked workbook file, change its name, or change its folder location, the data would not update.

If you’re working with a workbook that contains externals links and you have to share it with colleagues/clients, it’s better to remove these external links.

However, if you have a lot of formulas, doing this manually can drive you crazy.

How to Find Externals Links and References in Excel
---------------------------------------------------

Here are a couple of techniques you can use to quickly find external links in Excel:

*   Using Find and Replace.
*   Using Edit Links Option.

Let’s see how each of these techniques work.

### Find External Links using Find and Replace

Cells with external links contain the name of the workbook to which it links. This would mean that the reference would have the file name with .xlsx/.xls/.xlsm/.xlb extension.

We can use this to find all the external links.

Here are the steps to find external links in Excel using [Find and Replace](https://trumpexcel.com/find-and-replace-in-excel/)
:

*   Select all the cells.
*   Go to the Home tab –> Editing –> Find & Select –> Find.![Find Externals Links and References in Excel - find opton](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20210%20149'%3E%3C/svg%3E)
*   In the Find and Replace dialog box, enter \*.xl\* in the ‘Find what’ field.![Find Externals Links and References in Excel - xl](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20443%20194'%3E%3C/svg%3E)
*   Click on Find All.![Find Externals Links and References in Excel - find all](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20443%20194'%3E%3C/svg%3E)

This will find and show all the cells that have external links in it.

![Find Externals Links and References in Excel - find result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20482%20335'%3E%3C/svg%3E)

Now you can select all these cells (select the first record, hold the Shift key and then select the last record) and [convert the formulas to values](https://trumpexcel.com/convert-formulas-to-values-excel/)
.

### Find External Links using Edit Links Option

Excel has this inbuilt tool that will find all the externals references.

Here are the steps to find external links using Edit Links Option:

*   Go to the Data Tab.
*   In the Connections group, click on Edit Links. It opens the Edit Links dialog box will list all the workbooks that are being referenced.![Find Externals Links and References in Excel - edit links](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20189%20124'%3E%3C/svg%3E)
*   Click on Break Links to convert all linked cells to values.![Find Externals Links and References in Excel - break links](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20269'%3E%3C/svg%3E)

Be aware that once you break the links, you can undo it. As a best practice, create a backup before doing this.

### Still Getting the External Links Prompt?

Sometimes, you may find and remove all the external links, but still get a prompt as shown below:

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20670%20116'%3E%3C/svg%3E)

Don’t go crazy and start cursing Excel.

So if you’re getting the update links prompt, also check the following for external links:

*   Named Ranges
*   Conditional Formatting
*   Data Validation
*   Shapes
*   Chart Titles

Using ‘Find and Replace’ or ‘Edit Links’ as shown above would not identify external links in these above-mentioned features.

Here are the steps to find external links in these places:

*   **Named Ranges:** Go to the Formula tab and click on Name Manager. It will show you all the [named ranges](https://trumpexcel.com/named-ranges-in-excel/)
     in the workbook. You can check the ‘Refers to’ column to spot external references.
*   **Conditional Formatting:** The only way an external link can land up in [Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
     is through the custom formula. Go to the Home tab –> Conditional Formatting –> Manage Rules. In the Conditional Formatting Rules Manager, check the formulas for external links.
*   **Data Validation:** It is possible that the data validation [drop down list](https://trumpexcel.com/excel-drop-down-list/)
     refers to a named range that in turn has external links. Checking Named Ranges should take care of this issue as well.
*   **Shapes:** If you’re using shapes that are linked to cells, check these for external links. Here is a quick way to go through all the shapes:
    *   Press the F5 key. It will open the Go to Dialog Box.
    *   Click on Special.
    *   In the Go To Special dialog box, select Objects.
    *   Click OK. This would select all the shapes. Now you can use the Tab key to cycle through these.
*   **Chart Titles:** Select the chart title and check in the formula bar if it refers to an external link.

You can learn more about External Links from these tutorials:

*   [Finding External Links in Excel – Contextures Blog](http://blog.contextures.com/archives/2013/11/12/find-external-links-in-an-excel-file/)
    .
*   [Finding External Links – Microsoft Excel Support](https://support.office.com/en-us/article/Find-links-external-references-in-a-workbook-fcbf4576-3aab-4029-ba25-54313a532ff1)
    .

There is also an add-in available to find external links in Excel. [Click here](http://www.manville.org.uk/software/findlink.htm)
 to learn more and download the add-in.

**You May Also Like the Following Excel Tutorials:**

*   [How to Lock Cells in Excel](https://trumpexcel.com/lock-cells-in-excel/)
    .
*   [Find and Remove Hyperlinks in Excel](https://trumpexcel.com/find-hyperlinks-in-excel/)
    .
*   [Creating Dynamic Hyperlinks](https://trumpexcel.com/create-dynamic-hyperlinks-in-excel/)
    .
*   [Using FIND function in Excel](https://trumpexcel.com/excel-find-function/)
    .
*   [How to Reference Another Sheet or Workbook in Excel](https://trumpexcel.com/reference-another-sheet-or-workbook-in-excel/)
    
*   [How to Find Circular Reference in Excel](https://trumpexcel.com/find-circular-reference-excel/)
    
*   [Extract URL from Hyperlinks in Excel](https://trumpexcel.com/extract-url-from-hyperlinks-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

8 thoughts on “How to Find External Links and References in Excel”
------------------------------------------------------------------

1.  Also good to note to check pivot tables. If you have moved the files around, a pivot table will still source the original data source.
    
    [Reply](https://trumpexcel.com/find-external-links-excel/#comment-18395)
    
2.  Great advice, many thanks for posting!  
    One thing that would be great to add though, is how to check where the external links are used? I am following the step of “Edit Links” and before I Break the link I want to see which cells are using it and what I am actually breaking. Can I see that?
    
    [Reply](https://trumpexcel.com/find-external-links-excel/#comment-14894)
    
3.  Thank you so much!
    
    [Reply](https://trumpexcel.com/find-external-links-excel/#comment-14447)
    
4.  Hello Sumit.. Thanks for this informative article.
    
    As you suggested to use of find and searching for .xls or other file extension would be nice idea. But I am trying to copy all these links in search result… and I am not able to do it.. how do I do it…??
    
    Please suggest.
    
    Thanks
    
    [Reply](https://trumpexcel.com/find-external-links-excel/#comment-13704)
    
5.  Thank you so much! I found a broken link in conditional formatting. Once I followed your step-by-step recommendations, I solved the problem in 30 seconds 🙂
    
    [Reply](https://trumpexcel.com/find-external-links-excel/#comment-13478)
    
6.  Awesome tips on finding external links. Best advice I have ever seen.
    
    [Reply](https://trumpexcel.com/find-external-links-excel/#comment-10689)
    
7.  Sumit, Thanks for the neat summary. I figured most of this out over the years but you’ve enlightened me with your list of things to check.
    
    [Reply](https://trumpexcel.com/find-external-links-excel/#comment-9390)
    
8.  Thank you.
    
    [Reply](https://trumpexcel.com/find-external-links-excel/#comment-9189)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/find-external-links-excel/#respond)

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