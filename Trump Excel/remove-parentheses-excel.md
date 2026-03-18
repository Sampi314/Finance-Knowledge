# Remove Parentheses (Brackets) in Excel [4 Easy Ways]

**Source:** https://trumpexcel.com/remove-parentheses-excel

---

[Skip to content](https://trumpexcel.com/remove-parentheses-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-parentheses-excel/#below-title)

Most of my time working in Excel is spent cleaning data that I get from different sources.

One common task that I have to do quite often is to remove parentheses (or brackets) from the cells in a dataset.

As with almost everything else in Excel, there are multiple ways you can remove the parenthesis from cells.

In this tutorial, I’m going to show you four such methods that you can use depending on the structure of your data set or your personal preference. Each method has its pros and cons, and I would list them so that you can decide which method is best suited for you.

_Note: In this article, I am showing you how to remove parentheses (), but you can use the same methods to remove brackets \[\] as well_.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-parentheses-excel/#)

Using Flash Fill to Remove Parentheses
--------------------------------------

[Flash Fill](https://trumpexcel.com/flash-fill-excel/)
 is a great tool that I often use while doing [basic data clean-ups](https://trumpexcel.com/clean-data-in-excel/)
 in Excel (such as removing parentheses or brackets from cells).

To use Flash Fill, you first need to manually enter the result for one of the cells in the adjacent cell.

When you enter the result for one of the cells in the adjacent cell and then use Flash Fill, it will identify the pattern (using the result that you have specified manually), and apply the same for the entire column.

Let me show you how it works with an example.

Below is a data set where I have the names followed by the state name. The state name is in the parentheses that I want to remove.

![Dataset to remove parentheses](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20332%20340'%3E%3C/svg%3E)

Here are the steps to do this:

1.  In cell B2, which is in the column adjacent to our data set, enter the expected result – _Richard Hanson, Texas_

![Enter expected result in Cell B2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20577%20343'%3E%3C/svg%3E)

2.  Select cell B3
3.  Hold the Control key and press the E key (this is the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     to run Flash Fill)

As soon as you run Flash Fill, you will notice that the entire column gets filled, and the parentheses/brackets have been [removed from the text](https://trumpexcel.com/remove-text-before-after-character-excel/)
.

![flash fill result where the parentheses have been removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20617%20348'%3E%3C/svg%3E)

_You can also run Flash Fill by going to the Home tab, then clicking on the Fill icon (in the Editing group), and then clicking on the Flash Fill icon_.

Note: Since Flash Fill works by identifying the pattern in the result you have provided, there is a possibility that it may identify an incorrect pattern and give you the wrong result. If that happens, try again by giving it two or three examples of the result you want and then running the Flash Fill.

Below are the pros and cons of this method to remove parentheses:

| PROs | CONs |
| --- | --- |
| Quick and Easy | Flash Fill can identify the wrong pattern, so you need to double-check the results. |
|     | You need to manually enter the result in one or two cells before using Flash Fill |
|     | The results you get are static values, so if your original data changes, you need to repeat the steps again. |

Also read: [Show Negative Numbers in Parentheses in Excel](https://trumpexcel.com/show-negative-numbers-parentheses-brackets-excel/)

Find and Replace to Remove Parentheses
--------------------------------------

Find and Replace is another easy way to find and remove all the parentheses in your data set.

Since the parentheses include an opening bracket and a closing bracket, you need to use Find & Replace twice (to remove the two brackets separately).

Below is an example data set where I have the names followed by the US state name in parentheses, and I want to remove the parentheses only.

![Dataset to remove parentheses](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20332%20340'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select the data set from which you want to remove the parentheses
2.  Click the Home tab

![Click the home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20223'%3E%3C/svg%3E)

3.  Click on the Find & Select icon in the Editing group

![Click on the find and select option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20613%20223'%3E%3C/svg%3E)

4.  Click on the Replace option. This will open the Find and Replace dialog box.

![Click on the replace option from the Dropdown](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20252%20569'%3E%3C/svg%3E)

5.  Enter ( in the Find what field.

![Enter parentheses opening bracket in the find what field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20275'%3E%3C/svg%3E)

6.  Click on Replace All. This will replace all the instances of ( in the dataset.

![Click on the replace all button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20275'%3E%3C/svg%3E)

7.  Now, enter ) in the ‘Find what’ field.

![Enter the parenthesis closing character in the find what field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20275'%3E%3C/svg%3E)

8.  Click on Replace All. This will replace all the instances of ) in the dataset.

![Again click on the replace all button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20275'%3E%3C/svg%3E)

And done!

While this method may not be as quick as using Flash Fill, if you’re comfortable using Find and Replace, it’s fast enough.

**Pro Tip**: Use the keyboard shortcut Control + H to open the Find and Replace dialog box. To use this, hold the Control key and then press the H key.

Now let’s look at the pros and cons of this method for removing parentheses in Excel.

| PROs | CONs |
| --- | --- |
| Works as expected. | No need to create an additional column. You can use Find and Replace on your original data column itself. |
|     | It removes all instances of the opening and closing bracket characters. You can not choose which instance of the brackets would be removed. |

Also read: [How to Add Parentheses Around Text in Excel](https://trumpexcel.com/add-parentheses-excel/)

Formulas to Remove Parentheses
------------------------------

If you want more control while removing the parentheses from your data set, you can consider using the formula method.

This can be done using the [SUBSTITUTE function](https://trumpexcel.com/excel-substitute-function/)
, which would identify the position of the opening and closing brackets and replace them with a null string.

Below is a data set where I want to remove the parenthesis from the state names.

![Dataset to remove parentheses](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20332%20340'%3E%3C/svg%3E)

Here is the formula that will do this:

\=SUBSTITUTE(SUBSTITUTE(A2,"(",""),")","")

Enter the above formula in cell B2 and then [apply it to the entire column](https://trumpexcel.com/apply-formula-to-entire-column-excel/)
 (you can copy the cell that has the formula and paste it into other cells or [use the Fill Handle](https://trumpexcel.com/how-to-use-fill-handle-in-excel/)
 and drag it down).

![Formula to remove parentheses in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20644%20405'%3E%3C/svg%3E)

The above formula uses two substitute functions.

The first SUBSTITUTE function finds the position of the opening parenthesis character (“(“) in the cell and substitutes it with a null string.

The result of the first SUBSTITUTE function is then used by the second SUBSTITUTE function to find the closing parenthesis character (“)”) and replace it with a null string.

If you do not need the original data, you can [convert the formula values](https://trumpexcel.com/convert-formulas-to-values-excel/)
 in column B into static values and then remove the original data.

Now let’s look at the pros and cons of using the formula method for removing parentheses/brackets in Excel.

| PROs | CONs |
| --- | --- |
| If your original data changes, the resulting output would automatically update | You get the result in a separate column |
|     | You need to know the syntax of the SUBSTITUTE function to be able to use it. |

Also read: [Remove Asterisk (\*) in Excel](https://trumpexcel.com/remove-asterisk-excel/)

VBA to Remove Parentheses
-------------------------

And the final way to remove parentheses in Excel is by using a simple VBA formula.

Since this method requires a little bit of setup, it is more suited for people who need to do this regularly.

So you can set up the VBA code once and then run it with a simple keyboard shortcut or a click of a button to remove parentheses from the selected data set.

Let me show you how this method works.

Below I have the same data set where I have the names in column A along with the state names in parentheses, and I want to remove these parentheses.

![Dataset to remove parentheses](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20332%20340'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select the data set.
2.  Hold the ALT key and press the F11 key to [open the Visual Basic editor](https://trumpexcel.com/visual-basic-editor/)
    . Alternatively, you can go to the Developer tab and then click on the Visual Basic icon.
3.  In the VB Editor, click on the Insert option in the menu and then click on the Module option. This will insert a new module for the workbook.

![Insert a module in the VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20409%20310'%3E%3C/svg%3E)

4.  Copy and paste the below VBA code into the module code window.

    'Code developed by Sumit Bansal from https://trumpexcel.com
    Sub RemoveParentheses()
        Dim rng As Range
        Dim cell As Range
    
        ' Set the current selection as the range to be used
        Set rng = Selection
    
        ' Loop through each cell in the selection
        For Each cell In rng
            ' Remove parentheses
            cell.Value = Replace(cell.Value, "(", "")
            cell.Value = Replace(cell.Value, ")", "")
        Next cell
    End Sub

![Add code in the module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20339'%3E%3C/svg%3E)

5.  To [run this macro code](https://trumpexcel.com/run-a-macro-excel/)
    , place the cursor anywhere within the code, and then press the F5 Key (or click on the run macro icon in the toolbar)

![Run the macro by clicking on the run macro icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20548%20135'%3E%3C/svg%3E)

As soon as you run the above VBA code, it will go through each cell in the selection, and then replace the opening bracket and closing bracket characters with a null string.

Once you have this macro in your workbook, you can reuse it multiple times in that workbook. You can also assign a keyboard shortcut to the macro so you can run easily without opening the VB Editor.

To assign a keyboard shortcut to a macro, follow the below steps:

1.  Click on the [Developer tab in the ribbon](https://trumpexcel.com/excel-developer-tab/)
    
2.  Click on the Macros option

![Click on the Macro option in the developer tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20194'%3E%3C/svg%3E)

3.  Select the macro name for which you want to assign a keyboard shortcut
4.  Click on the Options button

![Click the options button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20551%20470'%3E%3C/svg%3E)

5.  Specify the shortcut

![Specify the keyboard shortcut](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20318'%3E%3C/svg%3E)

While this is not the fastest way to remove parentheses from Excel, once you have the code in place, you can reuse it multiple times in the workbook that has the code.

If you want to use this code in any workbook on your system, you can put it in the [Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
. A VBA code stored in the Personal macro workbook can be used on any Excel workbook on your system.

**Caution**: Changes done by a VBA macro code cannot be undone. So before you run the code, make sure you have a backup copy of the data.

Now let’s look at the pros and cons of using VBA to remove parentheses/brackets in Excel.

| PROs | CONs |
| --- | --- |
| Once you have the macro code in place, you can reuse it multiple times | Takes more time to set up the VBA code in the back end |
| You can assign a keyboard shortcut to the macro or add the macro icon to the Quick Access Toolbar | The changes done by the VBA code are irreversible. |

So these are four methods you can use to get rid of the parentheses from your cells in Excel.

If you want to do this quickly once or twice, you can use the Flash Fill method or the Find & Replace method. And if you need to do this on a regular basis, you can consider using the VBA method.

I hope you found this article useful.

**Other Excel articles you may also like:**

*   [How to Remove Cell Formatting in Excel (from All, Blank, Specific Cells)](https://trumpexcel.com/remove-cell-formatting-in-excel/)
    
*   [How to Filter Cells with Bold Font Formatting in Excel](https://trumpexcel.com/filter-bold-font-formatting-in-excel/)
    
*   [How to Remove Dashes (-) in Excel?](https://trumpexcel.com/remove-dashes-excel/)
    
*   [How to Remove Dotted Lines in Excel](https://trumpexcel.com/remove-dotted-lines-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “Remove Parentheses in Excel”
------------------------------------------

1.  How does some subscribe to your seminars? Have a few friends that want to join but we can’t find a link to subscribe Are you excepting any? Actually it has been awhile since I received one of you seminar emails
    
    Thoughts?  
    Rich
    
    [Reply](https://trumpexcel.com/remove-parentheses-excel/#comment-15076)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-parentheses-excel/#respond)

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