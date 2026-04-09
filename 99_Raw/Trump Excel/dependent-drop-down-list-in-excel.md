# Creating a Dependent Drop Down List in Excel [Step-by-Step Tutorial]

**Source:** https://trumpexcel.com/dependent-drop-down-list-in-excel

---

[Skip to content](https://trumpexcel.com/dependent-drop-down-list-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/dependent-drop-down-list-in-excel/#below-title)

**Watch Video – Creating a Dependent Drop Down List in Excel**

An Excel drop down list is a useful feature when you’re creating data entry forms or [Excel Dashboards](https://trumpexcel.com/creating-excel-dashboard/)
.

It shows a list of items as a drop down in a cell, and the user can make a selection from the drop down. This could be useful when you have a list of names, products, or regions that you often need to enter in a set of cells.

Below is an example of an Excel drop down list:

![Dependent Drop Down List in Excel - Simple list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20195'%3E%3C/svg%3E)

In the above example, I have used the items in A2:A6 to create a drop-down in C3.

**Read:** Here is a detailed guide on how to create an [Excel Drop Down List](https://trumpexcel.com/excel-drop-down-list/)
.

Sometimes, however, you may want to use more than one drop-down list in Excel such that the items available in a second drop-down list are dependent on the selection made in the first drop-down list.

These are called dependent drop-down lists in Excel.

Below is an example of what I mean by a dependent drop-down list in Excel:

![Dependent Drop Down List in Excel - Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20616%20212'%3E%3C/svg%3E)

You can see that the options in Drop Down 2 depend on the selection made in Drop Down 1. If I select ‘Fruits’ in Drop Down 1, I am shown the fruit names, but if I select Vegetables in Drop Down 1, then I am shown the vegetable names in Drop Down 2.

This is called a conditional or dependent drop down list in Excel.

Creating a Dependent Drop Down List in Excel
--------------------------------------------

Here are the steps to create a dependent drop down list in Excel:

*   Select the cell where you want the first (main) drop down list.
*   Go to Data –> Data Validation. This will open the data validation dialog box.![Dependent Drop Down List in Excel - Conditional - Data Validation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20120'%3E%3C/svg%3E)
*   In the data validation dialog box, within the settings tab, select List.![Dependent Drop Down List in Excel - Conditional - List](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20314'%3E%3C/svg%3E)
*   In Source field, specify the range that contains the items that are to be shown in the first drop down list.![Dependent Drop Down List in Excel - Conditional - DD1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20686%20352'%3E%3C/svg%3E)
*   Click OK. This will create the Drop Down 1.![Dependent Drop Down List in Excel - DD1 Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20597%20185'%3E%3C/svg%3E)
*   Select the entire data set (A1:B6 in this example).![Dependent Drop Down List in Excel - Select Entire Range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20259%20186'%3E%3C/svg%3E)
*   Go to Formulas –> Defined Names –> Create from Selection (or you can use the keyboard shortcut Control + Shift + F3).![Dependent Drop Down List in Excel - Create from selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20443%20123'%3E%3C/svg%3E)
*   In the ‘Create Named from Selection’ dialog box, check the Top row option and uncheck all the others. Doing this creates 2 names ranges (‘Fruits’ and ‘Vegetables’). Fruits named range refers to all the fruits in the list and Vegetables named range refers to all the vegetables in the list.![Dependent Drop Down List in Excel - Top row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20260%20173'%3E%3C/svg%3E)
*   Click OK.
*   Select the cell where you want the Dependent/Conditional Drop Down list (E3 in this example).
*   Go to Data –> Data Validation.![Dependent Drop Down List in Excel - Data Validation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20120'%3E%3C/svg%3E)
*   In the Data Validation dialog box, within the setting tab, make sure List in selected.![Dependent Drop Down List in Excel - Settings List](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20314'%3E%3C/svg%3E)
*   In the Source field, enter the formula =INDIRECT(D3). Here, D3 is the cell that contains the main drop down.![Dependent Drop Down List in Excel - Indirect Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20314'%3E%3C/svg%3E)
*   Click OK.

Now, when you make the selection in Drop Down 1, the options listed in Drop Down List 2 would automatically update.

**Download the Example File[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/o26qhy0hft0143o/Dependent-Drop-Down-List-Excel_v2.xlsx?dl=1)
**

**How does this work?** – The conditional drop down list (in cell E3) refers to =INDIRECT(D3). This means that when you select ‘Fruits’ in cell D3, the drop down list in E3 refers to the [named range](https://trumpexcel.com/named-ranges-in-excel/)
 ‘Fruits’ (through the [INDIRECT function](https://trumpexcel.com/excel-indirect-function/)
) and hence lists all the items in that category.

_**Important Note:** If the main category is more than one word (for example, ‘Seasonal Fruits’ instead of ‘Fruits’), then you need to use the formula =INDIRECT(SUBSTITUTE(D3,” “,”\_”)), instead of the simple INDIRECT function shown above._

*   _The reason for this is that Excel does not allow spaces in named ranges. So when you create a named range using more than one word, Excel automatically inserts an underscore in between words. For example, when you create a named range with ‘Seasonal Fruits’, it will be named Season\_Fruits in the backend. Using the [SUBSTITUTE function](https://trumpexcel.com/excel-substitute-function/)
     within the INDIRECT function makes sure that spaces_ are _converted into underscores._

### **Reset/Clear Contents of Dependent Drop Down List Automatically**

When you have made the selection and then you change the parent drop down, the dependent drop down list would not change and would, therefore, be a wrong entry.

For example, if you select the ‘Fruits’ as the category and then select Apple as the item, and then go back and change the category to ‘Vegetables’, the dependent drop down would continue to show Apple as the item.

![Dependent Drop Down List in Excel - Mismatch](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20616%20212'%3E%3C/svg%3E)

You can use VBA to make sure the contents of the dependent drop down list resets whenever the main drop down list is changed.

Here is the VBA code to clear the contents of a dependent drop down list:

Private Sub Worksheet\_Change(ByVal Target As Range)
On Error Resume Next
If Target.Column = 4 Then
 If Target.Validation.Type = 3 Then
 Application.EnableEvents = False
 Target.Offset(0, 1).ClearContents
 End If
End If
exitHandler:
 Application.EnableEvents = True
 Exit Sub
End Sub

_The credit for this code goes to this [tutorial by Debra](http://blog.contextures.com/archives/2014/09/11/clear-dependent-drop-down-cells/)
 on clearing dependent drop down lists in Excel when the selection is changed._ 

Here is how to make this code work:

*   Copy the VBA code.
*   In the Excel workbook where you have the dependent drop down list, go to Developer tab, and within the ‘Code’ group, click on Visual Basic (you can also use the keyboard shortcut – ALT + F11).![Dependent Drop Down List in Excel - developer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20664%20120'%3E%3C/svg%3E)
*   In the VB Editor Window, on the left in the project explorer, you would see all the worksheet names. Double-click on the one that has the drop down list.![Dependent Drop Down List in Excel - double click](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20340%20241'%3E%3C/svg%3E)
*   Paste the code in the code window on the right.![Dependent Drop Down List in Excel - code paste](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20298'%3E%3C/svg%3E)
*   Close the VB Editor.

Now, whenever you change the main drop down list, the VBA code would be fired and it would clear the content of the dependent drop down list (as shown below).

![Dependent Drop Down List in Excel - clear content demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20616%20212'%3E%3C/svg%3E)

_**Download the Example File**_[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/xs0a3flmzan5z0i/Dependent-Drop-Down-List-Excel-Reset-Highlight.xlsm?dl=1)

If you’re not a fan of VBA, you can also use a simple conditional formatting trick that will highlight the cell whenever there is a mismatch. This can help you visually see and correct the mismatch (as shown below).

![Dependent Drop Down List in Excel - highlight](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20616%20212'%3E%3C/svg%3E)

Here are the steps t0 highlight mismatches in the dependent drop down lists:

*   Select the cell that has the dependent drop down list(s).
*   Go to Home –> Conditional Formatting –> New Rule.![Dependent Drop Down List in Excel - new rule](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20194%20377'%3E%3C/svg%3E)
*   In the New Formatting Rule dialog box, select ‘Use a formula to determine which cells to format’.![Dependent Drop Down List in Excel - use formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20371%20334'%3E%3C/svg%3E)
*   In the formula field, enter the following formula: =ISERROR(VLOOKUP(E3,INDEX($A$2:$B$6,,MATCH(D3,$A$1:$B$1)),1,0))![Dependent Drop Down List in Excel - formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20371%20334'%3E%3C/svg%3E)
*   Set the format.![Dependent Drop Down List in Excel - format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20371%20334'%3E%3C/svg%3E)
*   Click OK.

The formula uses the [VLOOKUP function](https://trumpexcel.com/excel-vlookup-function/)
 to check whether the item in the dependent drop down list is the one from the main category or not. If it isn’t, the formula returns an error. This is used by the ISERROR function to return TRUE which tells [conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
 to highlight the cell.

_**Download the Example File**_[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/xs0a3flmzan5z0i/Dependent-Drop-Down-List-Excel-Reset-Highlight.xlsm?dl=1)

**You May Also Like the Following Excel Tutorials**:

*   [Extract Data based on a drop-down list selection](https://trumpexcel.com/extract-data-from-drop-down-list/)
    .
*   [Creating a drop-down list with search suggestions](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/)
    .
*   [Select multiple items from a drop-down list](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/)
    .
*   [Create multiple drop-down lists without repetition](https://trumpexcel.com/multiple-drop-down-lists-in-excel/)
    .
*   [Save Time with Data Entry Forms in Excel](https://trumpexcel.com/data-entry-form/)
    .
*   [Create Data Validation List from Excel Table as Source](https://trumpexcel.com/data-validation-list-from-excel-table/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

75 thoughts on “How to Create a Dependent Drop Down List in Excel”
------------------------------------------------------------------

1.  Thanks, this was awesome.  
    Much simpler than many ways I’ve seen.  
    A little side note:  
    The formula won’t work if the name isn’t exakt.  
    I, for instance, used “:” after my titles. Which couldn’t be picked up by the name manager, and thus it didn’t work, until I removed the colon.
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-41358)
    
2.  Is it also possible to rewrite the formula to apply on whole column ? E.g. in column A I select Vegetable and in column B I will get a drop-down with valid vegetable values. If I change Vegetable value in A to Fruit I would get a drop-down for fruit.
    
    The expanding the data validation pattern cell by cell in excel is not a solution for me as I’m generating the excel file and not creating it manually.
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-14669)
    
3.  Thank you very much for the video!! what I am trying to do is when you select “India” all the names automatically go down in the column without you selecting one name if you select US all the names in the list will be copies in the column. How can i do it. I have 3 supervisors each have 14 team members under their name and they have to fill out a log. I don’t want them to click 14 times to get their team on the log. Can you please help me. thank you.
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-14577)
    
    *   You should instead use the if command. Set each cell below to check if supervisor A is selected in that cell, then set the rest of the cells to fill a certain name. Each cell would be set to only one name per supervisor.
        
        [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-14727)
        
4.  This is great, but I have a problem. My Column headers are 2 words and not a single word like “Fruit” or “Vegetable” but rather “Fruit and Vegetable” and “Grains and Breads.” I require a 2 word header value/name. The “named range” uses underscore (\_) between each word, which is fine, but the secondary/dependent drop-down does not populate.
    
    thanks for any tips or advice on a workaround of this nature.
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-14524)
    
5.  Is it possible to put the data in another worksheet of the same excel and use the indirect function?
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-14445)
    
6.  Doesn’t work. Says “The Source currently evaluates to an error.” anybody with a simpler way of doing this that actually works and doesn’t require someone to know VBA code?
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-14125)
    
7.  Small formula correction for those looking to use a conditional color change as opposed to a VBA script to highlight mismatches.
    
    The original formula: =ISERROR(VLOOKUP(E3,INDEX($A$2:$B$6,,MATCH(D3,$A$1:$B$1)),1,0))
    
    Needs to have a “0” (zero) added to the MATCH function’s third argument. The updated formula is:  
    \=ISERROR(VLOOKUP(E3,INDEX($A$2:$B$6,,MATCH(D3,$A$1:$B$1,0)),1,0))
    
    For MATCH, zero is an implied default, but some of you – like me – may have had formatting issues based on the original formula due to how it processes the range. This error – for me – was being caused by the MATCH function… so forcing a “0” in the third argument makes for an exact match. Otherwise, you have to sort your menu and that’s a pain.
    
    To the author… excellent post and thank you!
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-14071)
    
8.  I want to use 3 or more drop down lists but is showing error  
    Please help
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-13985)
    
9.  Two teammates and I have been unsuccessful in building a spreadsheet with one drop down list and two dependent drop down lists. We can create a drop down list of five “entities” in column one. We can create a dependent drop down list of “expense categories” in column two which only shows the relevant “expense categories” of the “entity” selected in column one. We can not figure out how to create a second dependent drop down list of “expense details” in column three which only shows the relevant “expense details” of the “expense category” selected in column two. Any help would be greatly apreciated! I would be willing to pay for assistance or make a donation to the favorite charity of anyone who could help.
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-13792)
    
10.  This method seem not to be working anymore with the latest version of Excel and Windows. I am running version Office 365 MSO (16.0.12325.20328) on Windows 10 Pro version 1909.
    
    This is extremely frustrating. I have been using this type of lists for years using indirect to “construct” range names, where the range name reference the list to be used.
    
    Can someone please tell me why indirect lost the functionality to construct name ranges in data validation to create lists?
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-13224)
    
    *   Hello Theron.. I am on Office 365 ProPlus and this method is working for me. I am using Version 1908. It’s possible that there could be an issue with a specific version. I have not heard anything about it but will search and see if I can find anything
        
        [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-13227)
        
        *   Thank you Sumit,
            
            If not for your comment I would not have done the above to the letter. It works now.
            
            I can say why it did not worked initially. My name range was defined in the “Refer to:” section as =OFFSET(CatPr,0,0,COUNTA(Data!$L:$L)-2,1). This was to ensure we can add more items and not showing blank spaces. However, it seems that indirect does not like it when the name range has a formula in the “Refer to:” section. Which is silly, is it not?
            
            Regardless, Thanks
            
            [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-13228)
            
        *   Thank you so much for the clear instructive and useful information
            
            [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-13565)
            
11.  What if we have a additional column of “Groceries” with “Vegetable” and “Fruit” ?..i am getting values of main column as Fru./Vege./Groc.. but in dependent column i am not getting values …what i am doing wrong ?
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-13147)
    
12.  I have a 3 dependant drop down list (N dependant on M, M dependant on L). and for some reason my code below seem to work as such, hope it helps:
    
    On Error Resume Next  
    If Target.Column = “$L” Then  
    If Target.Validation.Type = “$M” Then  
    Application.EnableEvents = False  
    Target.Offset(0, 1).ClearContents
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-13138)
    
    *   just realised that for some reason it affects other column not defined by my above codes. any idea how I can prevent that?
        
        [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-13143)
        
13.  hi  
    First of all, this is one of the best tutorial! Thanks.
    
    I had a problem with your guidance. when I used your formula ” =INDIRECT(SUBSTITUTE(E5,” “,”\_”)) ” Excel show me this error: (a named range you specified cannot be found)  
    Please change ” (E3,” “,”\_”) ” to (E5,” ”,”\_”).
    
    Maybe someone like me is enough lazy to just copy the formula!!!  
    Thank you very much.
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-13062)
    
14.  Works great, although when I open the dependent dropdown, it defaults to the last item on the list. Any way to make it default to the top?
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-13053)
    
15.  shit
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-13018)
    
16.  I have everything working correctly for the second drop down, until I get to the end and I hit OK then it tells me “the Source currently evaluates to an error. Do you want to continue?
    
    Could this be because my first drop down has numbers? I don’t know why else it would not work ?! any help would be great!
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-12711)
    
    *   Hi Danielle, it is due to the fact this this method is not supported anymore. I would like someone to comment why the use of the indirect function is not working anymore.
        
        [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-13225)
        
17.  fff
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-12683)
    
18.  The VBA code only works in your sample worksheet, if i shift the dropdown columns to the right and change the vba code accordingly it does not work. How can i get hte code to work?
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-12334)
    
    *   I had a similar problem in that my drop down menus were in columns F and G rather than D and E. To get the VBA code to work, I changed the line “If Target.Column = 4 Then” to “If Target.Column = 6 Then”, since F is the sixth column. The second drop down menu would then clear. Hope this helps someone.
        
        [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-12799)
        
19.  I want to use the VBA code, but I would need to add it to code already existing for the worksheet. How would you make this work?
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-12330)
    
20.  Any thoughts how to select both fruits and vegies as multi select ( in A) followed by list of fruits and vegies in column B
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-12298)
    
    *   Been looking for this as well. Any luck?
        
        [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-13714)
        
21.  How about if fruits and vegetables have different number of items? Let’s say fruits has 5 items and vegetables has 3 items, if vegetables is selected then in drop down 2 has 2 blank items. Is there a way to eliminate those 2 blanks in drop down 2?
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-12135)
    
    *   Use ctrl-select only the cells you wish to use. This allows you to omit any blank cells during the “Formulas -> Create from Selection” step.
        
        [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-12328)
        
        *   I tried that. But it created an error: “This selection isn’t valid. Make sure the copy and paste areas don’t overlap unless they are the same size and shape.”  
            Any ideas, or sample file?
            
            [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-12392)
            
            *   Owh, never mind. Solved it by defining name for each selection. Thanks.
                
                [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-12397)
                
22.  If i need to create named range (dependent) for cars depending on the brand but they don´t have a fixed number of cars. Does this mean I have to define the range manually per brand instead of “create for selection”? is there any way we could use remove the blank spaces automatically?
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-12119)
    
23.  I’m getting an error “A named range ou specified cannot be found.”
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-12112)
    
24.  How can i link this drop down to dashboard or chart? please help me
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-12064)
    
25.  Very useful tutorial. Thanks
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-12023)
    
26.  Thank you. It was pretty clear and useful.
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-11980)
    
27.  Excellent content, thank you for your expertise and help!
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-11876)
    
28.  Thanks mate – very helpful
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-11735)
    
29.  Thank you sooo much.. very useful
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-11492)
    
30.  Very Nicely explained and very useful. Thanks
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-11490)
    
31.  Mine isn’t working. I followed the steps exactly, but my second row for lists shows an arrow for a dropdown list, but doesn’t actually create a dropdown list based on the choice made in the first column.
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-11477)
    
    *   For clarification, when I attempt the second part of the Data Validation, I get an error message saying “The Source currently evaluates to an error.” But the first selection works just fine. Can someone please help me?
        
        [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-11478)
        
        *   Hey Kyle this happen to me as well. You cannot have spaces anywhere you are making a drop down list. Your list may have been two words like yellow car. Instead you would have to put yellow\_car. Put underscores for all of your spaces and it should work
            
            [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-11767)
            
            *   Yeah, that wasn’t it. I was running only one word options, but I forget that this message happens, but wasn’t related to the multi-multi-tiered hierarchy. I still can’t do a three+ level hierarchy of dropdowns.
                
                [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-11768)
                
    *   I am having the same issue. I cant get the 2nd selection to create the drop down. any ideas?
        
        [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-12325)
        
32.  for this formula —- what if I had three columns in my named ranged (not two) how would the match formula change?  
    formula: =ISERROR(VLOOKUP(E3,INDEX($A$2:$B$6,,MATCH(D3,$A$1:$B$1)),1,0))
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-11312)
    
    *   I have the same question!
        
        [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-11880)
        
33.  you’re the best, thank you so much
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-11233)
    
34.  it was the good one
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-11186)
    
35.  I had one excel file with complete functions and formulas along with logic and examples. Unfortunately, I had missed that file. If you have these kind of file, please share the same with me. Thanks…
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-11156)
    
36.  hi, i have the same trouble as Abhishek Goyanka,
    
    was this solved?
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-11112)
    
37.  Creating a Dependent Drop Down List in Excel  
    I have categories name with White spaces, drop down is not working in that case.  
    Any solution
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-11099)
    
38.  Excellent stuff  
    Thanks
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-10832)
    
39.  good
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-10810)
    
40.  Very excellent job, thank you very much.
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-10763)
    
41.  Very Helpfull task
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-10485)
    
42.  Wow! This was so helpful and exactly what I was looking for. I knew the solution had to be much more simple than I was originally planning to try.
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-10364)
    
43.  Hi Could you possibly help me with a slightly bigger formula?
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-9817)
    
44.  Where did my comment go?
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-9734)
    
45.  I have a issue with name box in excel, which does not accept hypen “/” for eg: “AM/NAME” , please give me suggestion for this issue.  
    i am trying to populate dependent drop down box
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-9727)
    
46.  HI, How can I make the drop down list works for multiple cells and not just in a unique cell?
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-9574)
    
47.  thanks alot very usefull trick
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-8607)
    
48.  Hi Sumit,  
    How to update the dependent list when you change primary list after initially making some selection? Right now if you select the US and then Alaska, after that if you change it to India, the state still remains Alaska. Please help.  
    Thanks
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-7886)
    
    *   Hello Abhishek.. This can be done using VBA. Will try and create it and share with you
        
        [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-8539)
        
        *   Hi Sumit,
            
            Really appreciate the help. Please let me know if you are able to write VBA script which accomplishes the task. Thanks again.
            
            [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-8544)
            
49.  I want to create two cells dependent on the data entered into the first cell. So say I have a list of Company Branches listed by city. Then I have 6 multiple lists that list the Foremen that work in each city AND I have 6 lists of Superintendents that work in each city. I created the city list in cell B2. In the Superintendents cell E3 I used =Indirect(B2) and it lists all the Superintendents working in the city showing. Now in cell E2 I want to have the Foremen that work in each city. I tried =Indirect(B2) which gives me the same list in cell E3. How do I get E2 tied to B2????
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-3191)
    
50.  i have my drop down all done, but when i to look at the list , there is nothing showing, can you help me please
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-2623)
    
51.  Hi there, is there any way you know to do this but with a list of all countries and regions of the world without having to create as many columns as countries exist? I have the list with two columns, each row per region/country… When I select one of the countries, I need the drop down list to display all the regions of that country.
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-2290)
    
52.  Thanks Sumit for sharing this! However, I have find two errros:
    
    1 – While addition to the data set (As states) and consequently using indirect formula as Indirect(States Name) doesn’t show any options in list.
    
    2 – Is there any way in which cells should appear empty for that particular row if we change any data set?
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-1891)
    
53.  Hey Sumit, I have a doubt – when you choose US in Cell -E2 then the other drop down list in cell:F2 shows US cities. Lets assume, we select Alaska as city in F2 but at the same time we change the country again US to India in E2, then F2 field still shows Alaska.
    
    Is there a way cell should appear empty if we change the country ?
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-1741)
    
54.  How do i fix this? its not letting me do the data validation following the exact steps.
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-1582)
    
    *   I also have the same mistake…anybody could fix it?  
        Thanks!!!
        
        [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-2230)
        
55.  How would you this with a third drop down based on BOTH the previous drop downs? For instance, adding a “City.”
    
    [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-1523)
    
    *   Hi Tyler.. Thanks for dropping in.. You can create the third drop down in the similar way. In this case. city would be dependent on selected state. You would need to create named ranges for all states, and the formula would be =INDIRECT(States Name)
        
        [Reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#comment-1526)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/dependent-drop-down-list-in-excel/#respond)

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