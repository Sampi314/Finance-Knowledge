# Create an Excel Drop Down List with Search Suggestions

**Source:** https://trumpexcel.com/excel-drop-down-list-with-search-suggestions

---

[Skip to content](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#below-title)

We all use Google as a part of our daily routine. One of its features is search suggestion, where Google acts smart and gives us a list of suggestions while we are typing.

![Excel Drop Down list with Search Suggestions - Google](https://trumpexcel.com/wp-content/uploads/2013/10/Google-Suggest-List.png)

In this tutorial, you’ll learn how to create a searchable [drop-down list](https://trumpexcel.com/excel-drop-down-list/)
 in Excel – i.e., a drop-down list that will show the matching items as you type.

Below is a video of this tutorial (in case you prefer watching a video over reading the text).

Searchable Drop Down list in Excel
----------------------------------

For the purpose of this tutorial, I am using the data of Top 20 countries by GDP.

The intent is to create an excel drop down list with a search suggestion mechanism, such that it shows a drop down with the matching options as I type in the search bar.

Something as shown below:

![Searchable Drop Down list in Excel - demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20430%20480'%3E%3C/svg%3E)

_**To follow along, download the example file from here**_[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/10/Dropdown-with-Search-Suggestion_Final.xls)

Creating the searchable drop-down list in Excel would be a three-part process:

1.  _Configuring the search box._
2.  _Setting the Data._
3.  _Writing a short VBA Code to make it work._

### **Step 1 – Configuring the Search Box**

In this first step, I will use a combo-box and configure it so that when you type in it, the text is also reflected in a cell in real time.

Here are the steps to do this:

1.  Go to Developer Tab –> Insert –> ActiveX Controls –> Combo Box (ActiveX Control).
    *   There is a possibility you may not find the developer tab in the ribbon. By default, it is hidden and needs to be enabled. [Click here](https://trumpexcel.com/excel-developer-tab/)
         to know how to get the developer tab in the ribbon in Excel.![Excel Drop Down list with Search Suggestions - Combo Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20203%20225'%3E%3C/svg%3E)
2.  Move your cursor to the worksheet area and click anywhere. It will insert a combo box.
3.  Right-click on the Combo Box and select Properties.![Excel Drop Down list with Search Suggestions - Combo Box Properties](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20184%20221'%3E%3C/svg%3E)
4.  In the properties dialogue box, make the following changes:
    *   AutoWordSelect: _False_
    *   LinkedCell: _B3_
    *   ListFillRange: _DropDownList (we will create a [named range](https://trumpexcel.com/named-ranges-in-excel/)
         with this name in step 2)_
    *   MatchEntry: _2 – fmMatchEntryNone_

![Excel Drop Down list with Search Suggestions - Combobox settings](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20370%20517'%3E%3C/svg%3E)_(Cell B3 is linked to the Combo Box, which means that anything you type in the Combo Box is entered in B3)_

1.  Go to Developer tab and click on Design Mode. This will enable you to enter text in the Combo Box. Also, since cell B3 is linked to the combo box, any text that you enter in the combo box would also be reflected in B3 in real-time.

### Step 2 – Setting the Data

Now that the search box is all set, we need to get the data in place. The idea is that as soon as you type anything in the search box, it shows only those items that have that text in it.

To do this, we will use

*   Three helper columns.
*   One [dynamic named range](https://trumpexcel.com/named-ranges-in-excel/)
    .

**Helper Column 1**

Put the following formula in cell F3 and drag it for the entire column (F3:F22)

\=--ISNUMBER(IFERROR(SEARCH($B$3,E3,1),""))

_This formula returns 1 when the text in the Combo Box is there in the name of the country on the left. For example, if you type UNI, then only the values for **Uni**ted States and **Uni**ted Kingdom are 1 and all the remaining values are 0.![Excel Drop Down list with Search Suggestions - Helper Column 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20163%20385'%3E%3C/svg%3E)_

**Helper Column 2**

Put the following formula in Cell G3 and drag it for the entire column (G3:G22)

\=IF(F3=1,COUNTIF($F$3:F3,1),"") 

_This formula returns 1 for the first occurrence where Combo Box text matches the country name, 2 for the second occurrence, 3 for the third and so on. For example, if you type UNI, G3 cell will display 1 as it matches United States, and G9 will display 2 as it matches United Kingdom. The rest of the cells will be blank.![Excel Drop Down list with Search Suggestions - Helper Column 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20222%20388'%3E%3C/svg%3E)_

**Helper Column 3**

Put the following formula in cell H3 and drag it for the entire column (H3:H22)

\=IFERROR(INDEX($E$3:$E$22,MATCH(ROWS($G$3:G3),$G$3:$G$22,0)),"") 

_This formula stacks all the matching names together without any blank cells in between them. For example, if you type UNI, this column would show 2 and 9 together, and rest all cell would be blank.![Excel Drop Down list with Search Suggestions - Helper Column 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20318%20386'%3E%3C/svg%3E)_

#### Creating the Dynamic Named Range

Now that the helper columns are in place, we need to create the dynamic named range. This named range will only refer to those values that match the text entered in the combo box. We will use this dynamic named range to show the values in the drop-down box.

**_Note_****_:_** _In step 1 we entered DropDownList in the ListFillRange option. Now we will create the named range with the same name__._

Here are the steps to create it:

1.  Go to Formulas –> Name Manager.
2.  In the name-manager dialogue box click New. It will open a New Name dialogue box.
3.  In the Name Field enter DropDownList
4.  In the Refers to Field enter the formula:  \=$H$3:INDEX($H$3:$H$22,MAX($G$3:$G$22),1)

### Step 3 – Putting the VBA Code to Work

We are almost there.

The final part is to write a short [VBA code](https://trumpexcel.com/excel-macro-examples/)
. This code makes the drop down dynamic such that it shows the matching items/names as you are typing in the search box.

To add this code to your workbook:

1.  Right-click on the Worksheet tab and select View Code.
2.  In the VBA window, Copy and Paste the following code:
    
    _Private Sub ComboBox1\_Change()_
    _ComboBox1.ListFillRange = "DropDownList"_
    _Me.ComboBox1.DropDown_
    _End Sub_
    

That’s it!!

You are all set with your own Google type Search bar that shows matching items as you type in it.

For a better look and feel, you can cover cell B3 with the Combo Box and hide all the helper columns. You can now show off a little with this amazing Excel trick.

_**To follow along, download the file from here**_ [![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/10/Dropdown-with-Search-Suggestion_Final.xls)

What do you think? Would you be able to use this search suggestion drop-down list in your work? Let me know your thoughts by leaving a comment.

**_If you have enjoyed this tutorial, I am sure you would like the following Excel tutorials too:_**

*   [Dynamic Filter – Extract matching data while you type](https://trumpexcel.com/dynamic-excel-filter/)
    .
*   [Extract Data based on a Drop Down list selection](https://trumpexcel.com/extract-data-from-drop-down-list/)
    .
*   [Creating Dependent Drop Down Lists in Excel](https://trumpexcel.com/dependent-drop-down-list-in-excel/)
    .
*   [The Ultimate Guide to Using Excel VLOOKUP Function](https://trumpexcel.com/excel-vlookup-function/)
    .
*   [How to make multiple selections in a drop-down list in Excel](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/)
    .
*   [How to Insert and Use a Checkbox in Excel](https://trumpexcel.com/insert-checkbox-in-excel/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

309 thoughts on “Creating a Searchable Drop Down list in Excel – Step by Step Guide”
------------------------------------------------------------------------------------

1.  Super Tutorial.  
    Two questions:  
    1- Now in the formules $H$3:INDEX($H$3:$H$22,MAX($G$3:$G$22),1) the range are absolute and limited to row 22. Is there a way to make 22 depend to the number of arguments in the list ($E$3:$E$(number of arguments)) ?  
    2- Now the DropDownList is also absolute. Is it possible to make it depend to the number of arguments?
    
    Hope you understand my question. English is not my native language
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-14590)
    
2.  Thanks a lot for your wonderful tutorial.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-14478)
    
3.  Hello Sumit, First of all thanks for the above tutorial. I used it for creating a searchable list in my excel sheet. However I have a slight problem, The dropdown list keep popping up in different worksheets of same file and even in different excel files. How can this be resolved?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-14452)
    
4.  Hello,  
    Can you please advise if possible to have below  
    when i select department from drop down list then person name from that department appear in another cell.  
    Thank you
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-13894)
    
5.  Hi How do you create multiple copies of the same searchable dropdown box. At the moment I copy the cell but it does not operate independently of the original
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-13871)
    
6.  now how do i used this searchable dropdown in another workbook using same data?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-13529)
    
7.  Hello, thanks for solution, but when we move on item, first item will chose and other disappear. We need combo box search so filter combo box.  
    Please help and hint to use this on a data entry worksheet with multiple choice of data based on validation list.  
    Thanks so much
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-13400)
    
8.  I have the same question with Judd.  
    Is it possible to have two separate searchable drop down lists on the same sheet? I managed to get it to work with one but as soon as I add another, the two seem to interfere with each other…..  
    Kindly share with me how can I make it. Thanks.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-13377)
    
    *   I got below solution from the older comment. Thanks.
        
        Private Sub ComboBox1\_GotFocus()  
        ComboBox1.ListFillRange = “=DropDownList”  
        Me.ComboBox1.DropDown  
        End Sub
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-13378)
        
9.  Is it possible to have two separate searchable drop down lists on the same sheet? I managed to get it to work with one but as soon as I add another, the two seem to interfere with each other…..
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-13132)
    
10.  Amazing
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-12931)
    
11.  Excellent tutorial ! Well done.. It was useful
    
    But i am struggling with one thing. My Combo.text does not display the selected ite item in the list. Don’t know why
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-12909)
    
12.  Hi Sumit, this works perfectly ! However, I would like to improve it for my needs.  
    My list in column F contains cell with many words, separated by a coma : “,”  
    Example :  
    F3 : house, cat, hospital, game  
    F4 : house, game, hospital  
    F5 : hospital, cat, game, house  
    etc.
    
    I would like to be able to find the cell depending the names I’m typing in the B3 combobox.  
    Example, I type this :  
    house, cat  
    OR  
    cat, house  
    \=> I must have as option in the dropdown list the F3 and F5 cells.  
    (the order of the names must be able to be exchanged)  
    Is it possible ?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-12863)
    
13.  If i need to use multiple Lists from Name Manager into one Single Combo Box, How we can do that? What should be the Code? Is this really possible or not, or we need multiple Combo Boxes for Different Search
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-12498)
    
14.  Hi, Thanks for the info and spreadsheet.
    
    This method only allows the results to be inserted into one cell.  
    What if this is required for data entry and each result must be in a different cell?
    
    Awaiting your feedback
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-12419)
    
15.  I’m looking for a way to combine selecting multiple items and allowing deleting a selection by repetitive clicking, and searchable drop down in a range. So instead of using a control box to do the search, every cell in a certain column gets to search results from multi-select drop down that refers to the same drop down list.
    
    I tried out another tutorial about dynamic array, but failed to combine it with the multi-select code I found in your other article (the one with repetition). No matter where I put the “application.Calculate” in that code, I get the result to be, e.g. “int; business intelligence; int; business intelligence” if my search word is “int”.
    
    Please let me know how to tweak my code.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-12235)
    
16.  Very nice work excellent
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-12215)
    
17.  Hi, I used this function for a while and it worked well under Windows 7.  
    Now with Windows 10 this function stops working when I use the arrow-keys to choose an entry from the list. Actually the whole excel crashes.  
    Do you have a solution for that problem?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-12094)
    
    *   Hi Lorenz, I have the same problem with Excel 2013. It keeps crashing Excel. Did you get a solution or find a good alternative?
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-12220)
        
18.  Thank you soo much for this help my friend. I was trying to do this for a long time and now I got a solution. Please keep up the good work.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-12006)
    
19.  The dropdown list keep popping up in different worksheets. How can this resolved?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-11799)
    
    *   Hi EC, Did you get s solution for this popping of dropdown list?
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-14458)
        
20.  Thank you very much, you were very comprehensive.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-11708)
    
21.  Excellent, the dynamic range with Index function is the hack trick! Thanks
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-11647)
    
22.  hi i have complete your toturial and it works fine with a combobox in an excel spredsheet.  
    I would like to use this in a Userform but I just can’t figure out how to do it and how to make it work.  
    Because i cannot choose LinkedCell and ListFilRange in a combobox that is made on a form, do you have an idea of ​​how it can be done.
    
    Thanks for your wonderful guide
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-11453)
    
23.  Thank You So Much, Brother! It helped me a lot!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-11108)
    
24.  Can you use the same searchable drop down list to multiple cells?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-11097)
    
25.  I downloaded your sample file. When I type “u”, even though named range is correct, dropdown gives all the options (others are empty, but the scrolling bar is minimal)
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-11047)
    
26.  hi there, ‘Creating a Searchable Drop Down list in Excel – Step by Step Guide’ is very useful.. thanks for that.
    
    i want more combo boxes one after another with same functionality. you can consider that i am making a recipe and i will choose ingredients one by one in each combo box. how can i copy the whole formula.
    
    please guide.
    
    thanks in anticipation
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-11043)
    
27.  In the step of Configuring the Search Box I am not able to change Listfillrange.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-10914)
    
28.  how i can apply this formula on entire cells of the columns (combobpx for each cell in column)
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-10805)
    
29.  How do I write vba code for 2 independent Combo bixes on the auto search from down list?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-10717)
    
30.  What if my list of names is on one sheet and your code etc is on another sheet.  
    How will the code be updated ??
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-10465)
    
31.  Great article, but this is for one combobox- what if I want a whole column with same combobox- that means kind of column template
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-10371)
    
32.  Very useful thanks for this. can you please send sample sheet at [dsthapa1@gmail.com](mailto:dsthapa1@gmail.com)
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-10336)
    
33.  This seems like a great resolution for what i need. I’ve gone through all the steps and created all my helper columns, however, i believe I may need to change some details of the VBA code because my actual dropdown list on a separate sheet (Sheet1) while all my data in contained in my hidden sheet (Sheet2). Any idea what I may need to alter?
    
    Thanks,
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-10211)
    
34.  Hi, that’s great. But how can I create multiple comboboxes in same sheet using same source (Country) and with same google search function?? Thanks
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-10075)
    
35.  hi,  
    can i make the same type of combo box in a user form?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9887)
    
36.  Hello, and thank you for this tutorial! I am having one issue that it seems no one else had, and that is this. Every time I type in the combobox, “DropDownList1” (I placed the 1 for personal reasons, to determine among several comboboxes) disappears from the “ListFillRange” property. I’m hoping this site is still being monitored. If so, is there a solution to this?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9884)
    
    *   You need to create the Dynamic Name Range FIRST. So go through all the steps till the final one. Then go back to your combo box’s properties and enter the “DropDownList1”. It will now remain there.
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-10779)
        
37.  Thank you so much for this tutorial. Is there a way wherein I can update the details of the result in the search bar? If you search by her name, you can add new or edit information thus updating the database.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9754)
    
38.  Following your instructions and this works brilliantly. I’m wondering though how i can make this only display words which follow the order of the entered text as if i have the following;
    
    allimere  
    allimoor  
    sandall  
    random
    
    if i enter the search text all i only want to see – allimere and allimoor but your example will also show sandall as it’s finding the search text “all” anywhere within the word.
    
    Can i set this to only check at the start of a word?
    
    thank you.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9748)
    
39.  Thanks, also please suggest how to apply this on multiple worksheet.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9713)
    
40.  Hi Sumit,
    
    we have more than 90 product with different type of packing packing with each product. So can you help me to provide excel file where i can choose one product with searchable drop down menu .  
    and provide me your email id i ll send our product list
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9450)
    
41.  This is Great.. Is there anyway to enable the arrow key buttons when selecting the items on the list?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9416)
    
42.  Great utility! This was exactly what i was looking for! The search behavior is perfect.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9407)
    
43.  That’s quite an amazing trick.. Any way to interact with the Arrow Keyboard to select the item on the list?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9400)
    
44.  I need to the following done multiple times instead of just one time how do you do that?
    
    The final part is to write a short VBA code. This code makes the drop down dynamic such that it shows the matching items/names as you are typing in the search box.
    
    To add this code to your workbook:
    
    Right click on the Worksheet tab and select View Code.
    
    In the VBA window, Copy and Paste the following code:
    
    Private Sub ComboBox1\_Change()  
    ComboBox1.ListFillRange = “DropDownList”  
    Me.ComboBox1.DropDown  
    End Sub
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9324)
    
45.  Hi Sumit!  
    I found the tutorial very helpful. However I am facing some issues:  
    1)When I type the complete string of a suggestion, I am unable to select the suggestion.  
    For ex: Lets say the dropdown if of countries. Now when I am typing complete string say “india” I am unable to select the single suggestion “India”.  
    2) Also, in some cases when I am selecting a value from dropdown, it is picking other value from the list. However the linked cell is showing correct pick.  
    Will be great if you could help me out
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9187)
    
46.  Hi, Really appreciated your tutorial.  
    I try to create multiple combo boxes in one page and I managed to make the helper columns work properly, I have added more dynamic named ranges and added replicate the VBA codes for each combo box.  
    The problem I have is that after I finished picking a suggestion from the first combo’s list and type in the 2nd box, instead of it showing a suggestion list correspond to what I just typed box 2, the first combo box “reacted” and show only the item which I previously picked.  
    I have to clear the first combo box entry before the 2nd combo box start working properly.  
    my English is not very eloquent, I hope you can understand what I meant.  
    Thank you very much again.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9090)
    
    *   Sorted, used focus() instead of change()
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9093)
        
47.  HOW TO CONTROL Combo Box (ActiveX Control) WITH KEY BOARD. PLZ SUGGEST. IT’S NOT CONTROLLING THROUGH KEY BOARD.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9084)
    
48.  Thank you very much for sharing, very useful for my excel database.
    
    Cheers,  
    Agus
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-8758)
    
49.  I created the active x combobox and the corresponding data columns and the dropdown with type suggestion works perfectly. My issue that I continue to run into is that when I select another cell or enter data into another cell, I am prompted to select an option from the dropdown. I have already made this selection, but everytime I do anything in this worksheet or any other worksheet in this workbook, I am prompted to select an option from the dropdown. How can I resolve this so that I am only prompted to select an option from the dropdown when I am actively using the combobox?
    
    Thank you.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-8720)
    
    *   I’m having the same problem
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-10854)
        
50.  You made my day, awesome.  
    Things like this make excel interesting
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-8680)
    
51.  [https://youtu.be/\_LOiY2Nsuig](https://youtu.be/_LOiY2Nsuig)
      
    Right here, 2 ways to create drop down list in excel
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-8670)
    
52.  Hello – I followed the steps and I get the search drop down to appear in the Combo Box when I start typing. However, when I try to add another search drop down, i change the Combo Box to 2, and change VBA code to ComboBox2, it is not working? how to make second search drop down box?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-8653)
    
53.  Hi, Anyone know how to add another drop list with suggestion in the same excel sheet with same raw data? I am able to add one search box, but how to add another one,and more? Please help
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-8652)
    
    *   I need the same information. Hopefully, someone will respond.
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9086)
        
54.  Thank you for showing this. I have been searching everywhere for a drop down predictive text list for some time now. Will this work if the list is located in another worksheet?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-7830)
    
55.  I want to navigate in the suggestions but when I press DownKey it automatically selects the first match, without letting me keep on navigating to my target value (which is actually not the first one…). Any ideas of how can I solve this problem? For ex: I have 3 value xxxFAHxxx xxFAHxxxx and xFAHxxxxx, when I type FAH it will sort it alphabetically, but I want to navigate with up/down keys it will select the first one, taking out the possibility of scroll down to 3rd one (target). Thank you very much!!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-7258)
    
56.  Hi, I have to lists that I need the combo box to work for, can it be done?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-5816)
    
57.  Thank you for this wonderful trick. It is working exactly as I expected, however I have a question regarding an issue I am seeing when I add and remove worksheets. It seems when I remove a worksheet the combobox will display on other worksheets and even workbooks when I have more than one open. Any suggestions on how I can limit the combobox to only display on the worksheet it was created on? [https://uploads.disquscdn.com/images/06cd4d5e75f8c6bcd460916da9bfd89b38b1f77e2a2be7ba6bf64c98508d834d.png](https://uploads.disquscdn.com/images/06cd4d5e75f8c6bcd460916da9bfd89b38b1f77e2a2be7ba6bf64c98508d834d.png)
     [https://uploads.disquscdn.com/images/20f0fd400fbee5a58613a5935ad29551222cb5835567fcb52e938ef7ed729ced.png](https://uploads.disquscdn.com/images/20f0fd400fbee5a58613a5935ad29551222cb5835567fcb52e938ef7ed729ced.png)
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-5573)
    
58.  HI, I see that this topic is quit old, but I just discovered this as I had a need for exactly this option.
    
    Ive tried creating a new workbook from scratch and I’ve tried downloading the example and then inserting by data in it.
    
    In my workbook I have separate worksheets for say banks, nursing homes, and funeral homes.  
    There are 100-200 of each of these. IN each worksheet I wanted to use this option, BUT I can not get the vba portion of it to work.
    
    I setup every thing and it looks fine. when I type in the combo box I can see it narrowing the search in column H  
    BUt in the combo box I do not get the interactive list and the option to select the sorted names it just keeps showing the entire list.
    
    Any suggetsions?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3991)
    
59.  Not work properly with similar values with numbers.  
    If the list is “value 1, value 2, value 3, …, value 100”, selecting from a list of “Value 2”, insert the “Value 20”.  
    Instead of “Value 3” – “Value 31”, etc.  
    How to fix?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3902)
    
60.  Is It possible to have multiple drop down boxes? or have the dropdown box move down one once a name have been entered? Thank you
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3776)
    
61.  Hi,
    
    Is there a way of doing this in a normal cell and not a floating one?
    
    I want to add the result into a vlookup formula for which i need to refer to rows and columns.
    
    Thank you,  
    Ben
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3749)
    
62.  My drop down list works pretty well but for some reason from time to time it acts kind of funky.
    
    Image 1 shows what the ddl looks like before using it.  
    Image 2 shows what it looks like when i type in ten and hover my mouse over the 2nd item (1015)  
    Image 3 shows what it looks like when i CLICK on the 1015  
    — notice that it put i1015 in the ddl but 1015 (that’s correct) in the bound cell to the right  
    Image 4 shows the data  
    — (column a is the data for the ddl)  
    — (columns b,c,d are done to the instruction set shown at the top of this web page)  
    — notice it picked out the two values that have 1015 in them  
    — there is an i1015 about 70 rows down that is not shown n image 4  
    Image 5 shows what the ddl looks like …  
    …when i click ONLY the down arrow on the ddl  
    …and am careful to NOT hover over anything BUT the down arrow  
    — i1015 is selected
    
    \=====>> Why does it select the 2nd item from image 4?
    
    it does not behave like this for any other selection.
    
    See images 21,22,23,24 – it does not do that for other items.  
    Just type in ten then use mouse to select the item you want  
    1010 has 1010 and i1010 – works fine – click 1030, shows 1030 in DDL and bound col  
    1030 has 1030 and i1030 – works fine – click 1030, shows 1030 in DDL and bound col  
    1015 has 1015 and i1015 – problem – click 1015, shows i1015 in DDL and 1015 in bound col
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3707)
    
63.  (NewVersion of comment due to incorrect images uploaded.)
    
    Thanks for writing this article – it was very helpful and I have performed the instructions you outline above and everything works fantastic!
    
    During my testing I ran into a snag.
    
    While testing it, I noticed that if I type in ONLY 1 CHARACTER and that character happens to be the first character of the first item in my list of data…. it populates my DDL with the entire first value in the data list and then only shows me other data values that match that. \[see images 1 and 2\]  
    ///////  
    For example my first 5 values are: 1010, 1015, 1020, 1030, 1040 \[see image 3\]  
    (and there are 80 more values \[for future reference… the value in cell 80 is i1010 …\] ) \[see image 4\]  
    There are more values that begin with the number 1 \[see image 3\] but I’m just listing the first 5
    
    See the attached images…  
    – When I type in a 1 into the DDL \[see image 2\]  
    — it immediately puts in the DDL 1010 with the 010 being highlighted in blue \[see image 2\] and  
    — it drops down the DDL and shows me 1010 and i1010 \[see image 2 again\]  
    — BUT as you can see from the actual data list \[see images 3 and 4\] there are other data values that have a 1 in them
    
    — What I don’t want is for the DDL to be populated with the entire item it found (thus limiting the search results to what EXCEL decided put into the DDL) \[image 2 is what I don’t want it to do\]  
    — I was searching for 1 …  
    — but my DDL list has been filtered to all items that have 1010 in them \[see image 2\]
    
    I would like the DDL field to remain empty except for what I typed into it. All I typed in was a 1 so that should be the entire search term.
    
    Thanks for any help you can provide.  
    H
    
    (NewVersion of comment due to incorrect images uploaded.)
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3700)
    
    *   Just figured it out:  
        —–Step 4: In the properties dialogue box, make the following changes:  
        —–4th bullet – MatchEntry: 2 – fmMatchEntryNone  
        Somehow missed that step.
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3701)
        
64.  The search function is just what i needed, what I would like to do is create a list from my searches, say in cell J1 – j15, eg, populate a list of countries selected – Japan, Brazil and so on, really hope you can help, many thanks
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3601)
    
65.  I would recommend the following case study about Excel Drop-Down List :
    
    – Creating A Combobox Containing Only Unique Distinct Alphabetically Sorted Values –
    
    Sometimes unique values need to fill the combobox and need to sort alphabetic..In this way, the processes may be easier.The cells in Column A were selected to fill combobox in this example :
    
    For x = 2 To Cells(Rows.Count, 1).End(xlUp).Row – “1” in the code indicates Column A.
    
    Also,data is filtered with combobox and copied to the other pages in our study.
    
    Details and for example file :[https://merkez-ihayat.blogspot.com.tr/2016/07/creating-combobox-containing-only.html](https://merkez-ihayat.blogspot.com.tr/2016/07/creating-combobox-containing-only.html)
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3577)
    
66.  Hi Sumit, How do I get multiple suggestions to populate? so far it is only giving me 1 at a time as I type?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3532)
    
67.  First off, great website. It’s very well put together and very informative.
    
    Is there a way to speed up the queries for a large column of items? I’m setting up something that uses a 45,000 row list of items and I’ve noticed that I have to wait five or seconds for each keystroke that I enter in the ComboBox.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3507)
    
68.  Thank you sir for this Idea, but I need to fill column depend on specific list with suggestions way, how we can do that please, can anyone help me
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3427)
    
69.  Hi, Made the drop down list but how can repeat same thing in every below rows
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3339)
    
70.  The drop down list is not working when combo boxes are on a user form. Is it possible to create the same drop down list in a user form?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3284)
    
71.  Hi Sumit. Thanks for this great tool! I have followed your instructions and was able to create a tool with 20 different dropdown lists and comboboxes. For the VBA code, I used the one you mentioned in one of your comments:
    
    Private Sub ComboBox1\_GotFocus()  
    ComboBox1.ListFillRange = “=DropDownList”  
    Me.ComboBox1.DropDown  
    End Sub
    
    However, sometimes, when I click on a combo and start writing the name of the country, the size of the box starts getting bigger and bigger the more I come back on it and click on it, or the size of the font starts getting smaller and smaller the more I come back to the same box to change what I have written. Would you have an idea why this is, and how to solve it? Is there something to add in the VBA code maybe, in order to lock the size of the box and the size of font? Thanks in advance! 🙂
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3215)
    
72.  I have done all of the above and also the changed to the comboBox code in the thread below and they are all working great. However when I combine these with an Advanced Search filter Via a macro it doesn’t work. any ideas?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3204)
    
73.  Hi Sumit, with great thanks for your thoroughly explanation on this matter. With your help I managed it. But I do need more than one (appr. 70) of these dropdownlists with the same reference information. You cannot copy the dropdownbox and just replace the reference cell, right? Any suggestions for me?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3187)
    
74.  thanks for this can we copy multible drop list to different cell with out showing the same name twice.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3115)
    
    *   Hello Mohamed.. Have a look at this tutorial:[http://trumpexcel.com/2014/07/multiple-drop-down-lists-in-excel/](http://trumpexcel.com/2014/07/multiple-drop-down-lists-in-excel/)
        
        It shows how to have multiple drop downs without repetition.
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3134)
        
        *   I have an array of strings I’m using to populate a combo box in a UserForm. It auto-fills your entry if you start typing from the beginning, but I want users to be able to search using any part of each string.  
            I can envision a sloppy way of checking each entry manually, but I know there’s a better way. The stuff I found on Google isn’t helping – some of the suggestions use functions that aren’t even listed in my object browser =/  
            Thanks for any help and for this awesome sub in general.
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-8575)
            
75.  Hi Sumit, can i create multiple combo box in one worksheet? i mean, same combo box in different cells in one worksheet
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3072)
    
    *   Hello Juls.. I would suggest against it. To creating multiple such combo box, you’ll have to manually create and link each one of it. I would rather suggest you use drop downs
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3092)
        
76.  is it possible to create multiple combo box?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3071)
    
77.  Hi Sumit,
    
    Thanks for the detailed tutorial it is really helpful. Few issues while working on the drop boxes
    
    I have created two drop boxes “ComboBox21”, “ComboBox22” and used the above macro twice
    
    Private Sub ComboBox21\_Change()
    
    ComboBox21.ListFillRange = “DropDownList”
    
    Me.ComboBox21.DropDown
    
    End Sub
    
    Private Sub ComboBox22\_Change()
    
    ComboBox22.ListFillRange = “DropDownList1”
    
    Me.ComboBox22.DropDown
    
    End Sub
    
    Now the problem is if I select value on one of the search drop down box it doesnt show dropdown suggestions while entering the values in second drop box. and open up the filter of the first drop box.
    
    Appreciate if you can provide a solution around that.
    
    If required I can send my file for your review
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3040)
    
78.  Dear Sumit Bansal,
    
    This tutorial worked fine for me.  
    I have one question only.  
    Is it also possible to make a restricted list of this?  
    For example the list to choose from is:
    
    Netherlands  
    Belgium  
    Germany
    
    What i want is when i fill in ”England” a popup screen says: This is not a chooseable country.  
    You know what i mean?
    
    Waiting for an solution.
    
    Thanks in advance.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2987)
    
79.  But Cannot Select the text from list by up/down arrows.is it possible?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2888)
    
80.  I am using excel 2010 btw. I can see a few other users have this same problem, was there any fix in the end?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2881)
    
81.  Here is a screen shot of the combo box box reappearing as I enter data into another cell
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2880)
    
82.  Hi Sumait, love the functionality however I am having an issue where the drop down box reappears as the rest of my form is being filled out. Do you know why this is occurring?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2879)
    
83.  Superb, was searching for long time. Can you just let me know how to add said search box in each line of excel? Eg I have Item list and people will make data entry. So row 1, row 2 row 3 and daily it will happen for thousand of row. how to replicate this Dropdown list continuosly on each row..? My email id is [pragneshchoksy@gmail.com](mailto:pragneshchoksy@gmail.com)
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2849)
    
84.  Hi Sumait.. This is awesome.. But i would very much like to know how to do this in VBA so that i could use a userform to search.. I am trying to make a customer list (only their names no additional details required) a very simple one. Here is a dropbox link to a sample file i found on the internet. [https://www.dropbox.com/s/945u0rks0yuccdz/DynamiskSearchDropDownList.xlsm?dl=0&preview=DynamiskSearchDropDownList.xlsm](https://www.dropbox.com/s/945u0rks0yuccdz/DynamiskSearchDropDownList.xlsm?dl=0&preview=DynamiskSearchDropDownList.xlsm)
      
    I would like to edit it so that it only sorts customer names while type and adds it to list if the name doesn’t exist. Hope you can help me with this. Thank you 😀
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2828)
    
85.  Hi Sumit, this is very smart! Thanks a lot 🙂
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2786)
    
    *   Thanks Rick. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2789)
        
86.  hai sumith thanks for this article but my question is i want add names dynamically means first i have 10 persons name after i want add more 10 new person names and i want matins combo-box in one sheet and persons name in another sheet please help me
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2767)
    
87.  Hi thanks for the nice trick, however the search look for the alphabet in the whole word hence can it be modified to show the drop down only if the alphabet matched in series
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2737)
    
88.  Hi is there a way to have dynamic cascaded drop down created from the data table . The drop down should not include the duplicates and blanks. Its like we have table with data and we wanted to create a front end with drop down . when the item is selected from dropdown we get the aggregated number for the selected list
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2658)
    
89.  Hey. Great work. superb. It works. what I want more in this is. I am working on recipe costing where I have to select different ingredients to make one recipe. The dropdownlist contains all the ingredients, but how I will select separate items. eg. say X recipe has 4-5 ingredients then how do I select in each line ? pls solve this. It will save my lots of time. Thanks….
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2647)
    
90.  Hi Eka and @sumitbansal23:disqus  
    You may perform the following tutorial to achieve Filter as You Type to shortlist your Equipment Lists.  
    Link for tutorial is : Filter as You Type ( See Image Below )  
    [http://chandoo.org/wp/2015/08/22/filter-as-you-type-excel/](http://chandoo.org/wp/2015/08/22/filter-as-you-type-excel/)
    
    Hope I have answered your Query !!  
    Regards  
    Pratik Parmar
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2625)
    
    *   Hello Pratik.. Thanks for sharing. The tutorial in this post shows how to show the items in the same drop where you are typing. The one you have shared filters the data in a separate range. Here is a non-vba way to do this kind of filtering – [http://trumpexcel.com/2015/01/dynamic-excel-filter/](http://trumpexcel.com/2015/01/dynamic-excel-filter/)
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2626)
        
        *   Thank you Sumit, for such a good example. It helps a lot when we’re short of time. Such are very useful for my ECommerce Calculations.
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3473)
            
91.  thanks superb bro
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2608)
    
92.  For people that want a dropdown menu they can navigate with their keyboard keys use this. Btw reallly good explanation author love you. Also you can link your combobox to somewhere else too with this code. It also fixes the crashes that you get using the keyboard keys.
    
    Private sub Private Sub Combobox1\_got focus()
    
    ActiveSheet.Combobox1.ListFillRange = “DropDownList”
    
    End Sub
    
    ‘—–
    
    Private Sub Combobox1\_change()
    
    Dim lLoc2 As Long
    
    lLoc2 = URUNLER.ListIndex
    
    ‘check for a valid entry
    
    If Not lLoc2 = -1 Then Exit Sub
    
    Range(“b3”).Value = ActiveSheet.Combobox1.Value
    
    lLoc = ActiveSheet.Combobox1.ListIndex
    
    ‘check for a valid entry
    
    If lLoc = -1 And ActiveSheet.Combobox1.Value Empty Then
    
    ActiveSheet.Combobox1.ListFillRange = “DropDownList”
    
    End If
    
    Me.Combobox1.DropDown
    
    End Sub
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2603)
    
93.  thank you very much !
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2598)
    
94.  Great, I have been looking for this for some time and I am really gratefull.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2594)
    
95.  Dear Sumit, great tool but I cannot get the search function working. It displays the whole data range but typing in letters does not lead to anything 🙁 \[using xlsm\]
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2581)
    
96.  G’day Sumit
    
    Firstly this is brilliant; it may be the most useful excel trick I’ve seen on the net.
    
    I am having some trouble with it though. I’m not sure why, but when I do anything elsewhere in my spreadsheet (click a button, check a check box or just type in an empty cell and hit enter) the search suggestions drop down of their own accord.
    
    I’m not sure what’s triggering it, although I am quite a novice at excel so I’ve probably just made some tiny foolish mistake along the way but I can’t seem to work it out.
    
    Do you have any idea what I could have done wrong?
    
    Regards  
    MattRNR
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2580)
    
97.  This how can using with ‘Data Validation’ drop down list
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2542)
    
98.  really that’s great working !!! thanks buddy. still we need to select from drop down list by clicking the mouse. can you please suggest like, just type some name and then come down by down or alt+down errow.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2526)
    
99.  Hi there – I have recreated this for a file I use that has 1000 rows. When I search for an entry, say ‘Payroll’ I have about 5 options to choose from. However, my search box just loops my selections like this:
    
    Payroll 1  
    Payroll 2  
    Payroll 3  
    Payroll 4  
    Payroll 5  
    Payroll 1  
    Payroll 2  
    Payroll 3  
    Payroll 4  
    Payroll 5
    
    …And it keeps looping them inside the search box. Any way to get rid of the extra entries so that it just shows the 5?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2521)
    
100.  Hi I wanted to search phone numbers, and everything seems perfect. but problem arrives when the selected comes to the cell it becomes text format. how can I keep it number format please help me
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2518)
    
101.  if i want that search drop down list for full row then how is it possible
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2502)
    
102.  Hi,  
    Love your work but i have an issue with the combobox. I can search the data and all works but when i’m continueing entering data in my excel the dropdown keeps randomly appearing even if i selected the data.  
    is this a bug or did i do something wrong? i have to admit i changed the functions a bit.  
    since my list was very long where the data is and i add data every day i just added J:J to look for data, not between values.  
    Can someone help me please?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2481)
    
    *   i think i have the same issue as usman. 4 or 5 posts above. so i use this list to look for names in a client list. what i just noticed is that with some clients the search accepts it and i get a result for my search (the name dissepears in the search field, for other clients the client name stays visible and i constantly get the dropdown… the contactdetails however are filled in so its working correctly
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2482)
        
103.  Hey Sumit, thanks again for this awesome tutorial it worked great for me! I am having problems tho when I try to use two on the same sheet. It’s hard to explain but they step on each other, sometimes even causing excel itself to crash. Also when one is selected it shows on the other sheets of the workbook as well. It’s not for work or anything, I just enjoy doing these little projects in excel for my own use. In this case it’s a tool to help me run a gaming server. It’s hard to explain so here’s the file itself… [https://www.dropbox.com/s/xnnwyvispzr332b/ARK%20Cheat%20Generator%203.0.xlsm?dl=0](https://www.dropbox.com/s/xnnwyvispzr332b/ARK%20Cheat%20Generator%203.0.xlsm?dl=0)
    
    If you could have a quick look it’d be great but I’ll understand if you’re too busy. Thanks in advance!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2463)
    
104.  thank you very much
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2426)
    
105.  It took me several attempts to get this correct, but your instructions helped me get through it. Thank you so much!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2424)
    
106.  Hi Sumit,
    
    Thanks for this amazing article – it worked seamlessly when applied to a template I am currently developing. The explanation and code is very easy to follow and implement – so thanks!
    
    I read all the comments, and I’m sure nobody brought this up. I am using the dropdown right now as a reference to pull up entries from a separate datasheet using another activex button. The problem I am encountering is that when the button is clicked, it only runs through part of its code. Currently the logic behind the button is structured as:
    
    If input (cell that dropdown is linked to) is empty, then msgbox “Please select an activity” (action 1)
    
    Else:  
    If input entry matches an entry in list of activities then call function 1 and function 2 (action 2)  
    Else msgbox “Cannot find the activity you are looking for” (action 3)
    
    I find that the linkedcell area is always empty once the button is clicked so action 2 never runs. I created another button that just calls function 1 and function 2 (so action 2) and it works, but now the error handling code that I wrote no longer applies (so runtime error every time the cell is empty or if the entry does not match the list).
    
    Any ideas why this happening?
    
    Much thanks!  
    Amy
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2409)
    
107.  I really like your search suggestions in the combo box dropdown list – it is wonderful.  
    How do I create multiple Combo Box with the same dropdown list within the same worksheet? Using data validation is not good as I have a long list of data.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2394)
    
    *   Hello Megan.. Thanks for commenting.. If you have a huge list, I would suggest you use data validation only. For this technique, you need to create the drop down search bar again and again for each cell.
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2401)
        
108.  I have used this formula for a long list of stores i have and it works fine, i tried to just use part of this formula to make it work with my list, i want it to show different columns together as opposed to numbers as you have it here.. for example i have this:
    
    storename | address | phone #
    
    so i used the formula that shows the actual result name, copy pasted into 3 other columns to the left of these, and then i hid the original ones so to only show the resuts after typing in the bar, and i wanted it to give me the results as you see on top so if i have a store i just type the store name and it would show all 3 columns name address and phone #…. but it partially works…. it worked at first when i had 360 rows… then i had to add more stores to the list and then proceeded to modify the formulas accordingly to fit the rows… say i had 380 rows now… i change the formula to row 380 as the end, but then i get an error that it cant work with the formula…. and if i leave it as it was before… it would select more rows than i have… if i have 380 the formula would read like the last row was 760… so it ended up selecting empty rows… if i try to just select the total rows i have it would keep giving me the INCONSISTENT FORMULA error….im confused… all i changed was the total rows in the formula… nothing else … it worked fine before but not now.
    
    what do i do ? what am i missing? please help.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2387)
    
109.  Hi,
    
    The drop down works, but its temperamental. when the drop down appears sometimes it stays there even when i click on another cell. in fact when i enter content in a completely different cell the list from the drop down just appears as though it has a life of its own. any advice on this
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2381)
    
    *   Hello Usman.. It seems to working fine on my system. What version of excel are you using?
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2402)
        
110.  hi sir, it works but it’s really slow and when i select an item from the list it doesn’t appear immedietly in the box i have to select it and double click it  
    .
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2344)
    
    *   Hello.. Do have a huge data set? I assume it would become slow when you have a huge data set as there are multiple helper columns at play here.
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2403)
        
111.  Brilliant this makes my job a lot easier, thank you. I have some problem…I do this and when using it..type to search in that searchable-dropdown and delete it to type new word….and after then I save and all my data in column “H” gone.Thought it causes from deleting..so my question is how can I have searchable drop down with non-editable option.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2321)
    
112.  i created the drop downlist as above.Now how could i extend it to whole column as i want it to each and every cell. I am unable to select the dropdown control box to paste it to remaining columns.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2306)
    
113.  Thank you! Not only for your help with the activeX component, but also your reference below to the VBA method 🙂 That is what I’m going to use! 🙂
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2278)
    
    *   Thanks for commenting.. Glad you found it useful 🙂
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2404)
        
114.  Hi.
    
    Thank you so much for this tip!
    
    Is there any way to make the link cell dinamic? I want to apply this combobox to work in diferent cells from the same column. Also the list of data is in another worksheet within the same workbook.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2250)
    
115.  WOW! This is ALMOST exactly what I was looking for. Is there a way to have multiple search boxes linked to corresponding cells in the “B” column? I’d like to have the entire B column to be linked to separate search boxes.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2245)
    
116.  Great tutorial Sumit!!! I have only one, even simple question. Each time when I open the worksheet the last entered or chosen value is shown. Is it possible that when opening the worksheet the value is reset (the data in the dropbox should remain intact, only the previous value should not be shown, should be blank)  
    Thanks in advance
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2243)
    
117.  i am not able to write file name “DropDownList” in list fill range whenever i write after clicking file name disappear??? please help
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2228)
    
    *   same here, please help
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9594)
        
118.  Thank you thank you thank you! This is precisely what I wanted, not to mention perfectly explained!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2225)
    
    *   Thanks for commenting.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2400)
        
119.  Can you do this with multiple cells (say 400) without having to continuously redo every step?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2208)
    
    *   Hello Lexi..This can not be done for a lot of cells at once. It needs to be one by one for all cells. If you want to do this for 400 cells, I suggest you use data validation drop down list
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2399)
        
120.  Hi Sumit,
    
    First of all, thanks a lot for this great tutorial and this great idea.
    
    I am now working to implement this, such that the combobox is invoked inside of the cell I am presently in, and it works accordingly. I am relying on the Workbook.SelectionChange event for this. However, I am having some trouble in doing this. I believe it is because the
    
    With  
    .ListFillRange = DropDownList  
    .LinkedCell = LinkingCell  
    End With
    
    is creating some problem. Any suggestions?
    
    Have you already got something like this?
    
    Also, I am working on reducing the 3 lines of helper columns into a small VBA code (using arrays to handle the data), mainly for performance reasons. I will share it with you as I get done.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2172)
    
121.  I want to use a list on a different worksheet. I created the 3 helper cells but in the first one, I tried inserting the worksheet name where the combobox is placed (worksheet named “AGENTS”) with the following formula =–ISNUMBER(IFERROR(SEARCH((AGENTS!$K$2),E3,1),””)) . For some reason the only name it returns is the name on row E11 and it completely fills rows F and G with 1 and row H with the name on row 11. Is it possible to do this with the drop down list being on a separate worksheet?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2168)
    
122.  Hi this works for me, however when I type data into another worksheet the drop down shows up there as if I need to re-select my option. Any help would be greatly appreciated
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2116)
    
    *   Change VBA code like this:
        
        Private Sub ComboBox1\_GotFocus()  
        ComboBox1.ListFillRange = “DropDownList”  
        Me.ComboBox1.DropDown  
        End Sub
        
        Just copy and paste answer from Sumit Bansal :d
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2158)
        
        *   on backspace the content entered and typing again, it wont suggest
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-11060)
            
123.  easily guided……thanks a lot
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2085)
    
124.  Sumit – this is absolutely great, thanks for posting it. I tested the file and it worked fine. But then I tried adapting this for a similar problem, where instead of countries I have a list of about 250 Part IDs (which can be numeric, alpha, or a combination thereof). The issue I have is that Excel seems to crash every time I’m in the Combobox and happen to hit the down arrow key. Maybe it’s something specific with the down arrow key, or maybe 250 rows is “too much” for the formulas? Have you experienced this? Any thoughts?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2050)
    
    *   Thanks for commenting. When I press the down arrow key, it doesn’t crash, but I am also unable to navigate through the list (it just picks up the first matching entry). I tried it with about 500 records and works fine with more data. It seems its the down arrow key creating the trouble
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2051)
        
    *   Even same issue in my excel as well.. please help to resolve this.. every time it crashes when I press down arrow.
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-12185)
        
125.  Thanks a lot. I did it with work sheet but encountered an error that is whenever i search something excel shows same thing in blue color below the combo box or somewhere else on the page. see below screen shot:
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2048)
    
    *   Hi did you ever find a solution to this, I’m having the same issue.
        
        Thanks
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2117)
        
126.  hi sir how to add more countries or another things? i add more but the combobox is not showing it can u help me sir
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2036)
    
127.  Hello, thank you very much for the nice tutorial! It’s really great! I have however an issue. I have Excel 2013, the dropdown works as expected, however when I have the values in my dropdown and I click the ‘down arrow key’ from my keyboard Excel freezes and shuts down. Moreover, this dropdown appears also spontaneously on other sheets(!). Any idea? Moreover, is it possible that this dropdown is integrated as a native dropdown from excel? (maybe using the Data validation?)
    
    Thanks a lot!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2033)
    
128.  We would like to use multiple combo boxes on the same sheet with this approach and have the problem that the comboboxes interfere with each other. Do you have any possible solution here?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1995)
    
129.  Dear, Trumpexcel  
    can see from the video the created combo box is linked to a cell now my question is can the combo box link to multiple cells in the same column?  
    Thanks so much in advance
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1975)
    
130.  similarly, i need to do it in cell ? please help!!!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1974)
    
131.  Thanks so much for sharing this amazing trick! But i have almost a problem, the combo box shows all the time in another sheets or another excel file…how do I prevent this? I ve read alla the posts before, but the solutions didn’t Work so far…(i meam the vba focus one)…  
    Thanks in advance  
    Greetings from italy
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1968)
    
132.  First and foremost, Thank You for sharing this information. I have one question that I hope you or someone in this Discussion can answer for me. I used the Drop Down List technique in a form and it worked, but the only thing is that when I tab to my next field in my form, the drop down menu opens the list back up. I provided a screen shoot of what I am talking about. Is there a way to keep the combo box from making the list show the selected data again?
    
    I’m sorry the picture is a bit small but if you can manage to see, the top half shows the selected item in the list and everything is fine. The bottom half shows when I type something else in another field in the same sheet and tab out of that field, the list provides the same selected item in blue again.
    
    Thank You for your assistance!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1966)
    
    *   Nevermind about the picture being small, when I was uploading it, the picture seemed small but when it posted …. whoa, it was huge. Sorry about that you all.
        
        DV
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1967)
        
    *   I am facing the same issue, please let me know if you have resolved it. Many thanks
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2049)
        
        *   I copy the answer for you :
            
            Private Sub ComboBox1\_GotFocus()  
            ComboBox1.ListFillRange = “=DropDownList”  
            Me.ComboBox1.DropDown  
            End Sub
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2147)
            
133.  Thank you for sharing this .
    
    However I am getting issue When I use arrow keys (down) to move the selection down the dropdown list to select say 3rd item. Only the first item is selected and dropdown list disappears .  
    What I want is , when I use arrow keys(up/down) to move the selection up and down the dropdown list, it should only scroll up/down and it should not change the value of the combobox (and fire the change event) until the user hits enter or tab .
    
    Please help.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1935)
    
134.  Hi, one question. How i can do to have the same drop down list with search suggestions in the diferents sheets?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1905)
    
135.  I am trying this since two days, I found difficulty, search suggestion below combo box is not populated, I think I am erring in combo box property set or in macro setting, I put all data according to your video, also downloaded your excel, In your excel file it works, but in my file search suggestion is not showing in drop down list, I think I am missing some thing, can you please guide me in setting, Thanks a lot in advance
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1894)
    
136.  how to make a bill using this search box to include those item only which require on respected cells
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1890)
    
137.  Hello again,  
    I’m not very confident with ComboBox so I tried using data validation for a simpler solution.  
    I used the same helper columns and put my data validation list box below B3 (i.e. B4). The data validation source is =OFFSET($H$3,0,0,MAX($G$3:$G$22),1)  
    The drawback of this method is that the dropdown list does not change as you type and you type into a different cell from the dropdown (you just enter/press return when you have keyed your search text).  
    As I say, not as complete or elegant as your method but it means that you don’t need to use Developer or Visual Basic. May be of use for people with large and/or complicated spreadsheets.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1850)
    
    *   HI Joe,  
        Still at basic Excel level but I have replicated Sumit’s amazing solution exactly – it works wonderfully. I am trying to use your method since I
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2255)
        
    *   HI Joe,  
        Still at basic Excel level but I have replicated Sumit’s amazing solution exactly in a test file – it works wonderfully. I am trying to use your method since I have a worksheet with a long item list, have already created the Validation drop down in another worksheet form – it all works but I would love to be able to search. To try your solution before adding it to my work, I have used your formula as the Data validation source, copied all of Sumit’s formulas and columns skipping the first step of configuring the search box and also no VBA code. However, typing India into cell B3 brings the choice of Turkey in the drop down box, I have tried it several times. Is there something I am missing, would really appreciate your help, I am almost there!
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2256)
        
    *   Joe, I tried something ridiculous, changed the cell address of Sumit’s formula in Helper 1, then changed it back to it’s proper address – it suddenly began to work, with your method! Thank you for this solution, and thank you Sumit for this site, even for an absolute beginner like me it is totally amazing!
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2257)
        
        *   Hi Lillian,
            
            I’m glad you were able to sort it out.
            
            I’ve added some screenshots for reference showing the data validation source, various cell formulas and the resulting drop down list.
            
            Cheers,
            
            Joe
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2258)
            
            *   Thank you Joe. When my workbook was perfect, I tried to Lock/Hide the cells containing formulas and then to Protect the worksheet. Suddenly the drop down list did not work even when I unchecked Hide, Unprotected the sheet, and Re-Saved. Gave up for the day, opened it today and now it works perfectly although I did not change anything at all! Since I had flaky seeming trouble last week, I repaired Office then, hoping that was the issue, but obviously I have a problem – or maybe Excel needs some time to ‘register’ changes:-) Since I am new at excel but with your and Sumit’s help I have done something so way above my level – is this behaviour normal? Also, is there a problem with Protection and Drop Down Validation?  
                Thanks, Lillian
                
                [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2263)
                
                *   Hello again Lillian,  
                    Hiding columns will have no effect on how your spreadsheet works. Locking cells and protecting the worksheet is different. By default all cells in the worksheet will be locked when you protect the worksheet so the data validation cell will be locked and therefore will stop working. You can change the default so that all cells are unlocked and then specify just the cells you want to lock. Use Ctrl+Shift+F to get to the Format cells dialog box and use the Protection tab. So highlight the whole worksheet, press Ctrl+Shift+F and unclick the locked cells box in the Protection tab. Then highlight the cells you want locked and click the locked cells box. Then protect your worksheet.  
                    Hope this works ok for you, Joe
                    
                *   Thanks, worked perfectly. Next thing to try, your solution to only result in all records starting with ‘a’. It did work on my sample file which replicates Samit’s tutorial using his version of your solution, but not with my own workbooks. I assume it should work the same way with my list, which is a combination of numbers and also text, but the entire column is formatted as text (I am discovering that this is quite a confusing issue). I will go through your screenshots carefully and hope I can find where I went wrong. Since my source is in another workbook there is ample opportunity for a newbie like me to err with these long formulas…
                    
                    Thank you so much for doing this, Lillian
                    
138.  Hi, Thanks for sharing this. Can I be so bold as to suggest a possible improvement.
    
    My list is very long so when I type in, for example, “a” I get all the records with an “a” anywhere in them.
    
    What I really wanted was just those records STARTING with “a”.
    
    So I created a new formula in cell J3 which was =LEN(B3).
    
    Then I edited cell F3 to be =–ISNUMBER(IFERROR(SEARCH($B$3,LEFT(E3,$J$3),1),””)) and copied down.
    
    Any thoughts?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1808)
    
    *   Hi Joe.. Thanks for sharing.. And it makes sense when you have a big list. Here is another formula that would work
        
        \=–ISNUMBER(MATCH($B$3&”\*”,E3,0))
        
        I used it in F3 and copied down.
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1809)
        
        *   Hi,
            
            Yes thanks, much more elegant than my attempt.
            
            Cheers
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1811)
            
139.  Thanks much for the tip. After getting it to work, I tried to create a second combo box to do the same thing. I created three more helper cells and a new named range, that part works. The trouble is when I am entering data in the second box. I can add data in the firs all works great. When I attempt to add data in the second, the choices in the first re-appear, and nothing appears in the second????
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1792)
    
140.  Thank you for posting this topic it was very helpful, but I have a question about how to create multiple cells having that drop down list and giving me the suggestions, is there any way to do it without the box, I would like to have it in the actual cell and for every single cell in the column, Thank you very much
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1769)
    
    *   Hi David  
        did you managed to get answer to your question? if do kindly share with me at [danny.tan9090@gmail.com](mailto:danny.tan9090@gmail.com)
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1976)
        
141.  Hello very good articel. There is one thing you might can help me with. How can i search the data in more then one column? For a better understanding. My data has a title column and a matchcode column. In the title are more detailed informations and in the matchcode its only a single string. But i need to search both of them for the same search string and then combine the results in one named range. Thank you in advance. Greets from Berlin. 🙂
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1760)
    
142.  Hi Sumit,  
    Great job. I’m trying now to adjust it for myself on VBA Form.  
    Almost everything works….But.  
    I have combo box on my form and procedure for it. I’m adding to cell B3 what I’m typing.
    
    Private Sub ComboBox1\_Change()  
    Dim vCombo As Variant  
    vCombo = Me.ComboBox1.Value  
    Sheet6.Cells(3, 2).Value = vCombo ‘ add combobox value to cell B3  
    End Sub
    
    Filtered Dynamic DropDownList is appearing, but I can select only FIRST item from list.  
    If i’m selecting any following items – it’s becoming blank..
    
    Earlier I used the same as yours formulas before. Just without Combo box on sheet.  
    Instead of that I used formula =CELL(“contents”) in cell B3 (referring to your lesson) – with this you will get value to B3 from any cell in sheet you will type in.  
    And I have copied Name Validation to all cells I need. It filters list only after I press drop down arrow, but i was enough for me. Now I would like to create that in VBA form.
    
    I’m not professional in Excel, but thinking about possibilities to create that using dynamic arrays and filter them only using VBA code. I need ~30 combo boxes on the form doing the same..  
    Waiting for you tutorial about it on VBA form..
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1733)
    
143.  have you invoice and inventroy software in excel tutorial?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1732)
    
144.  This was incredibly helpful! Thank you very much! My search suggestion seems to be populating options that do not appear in formula, any clues as to why?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1707)
    
    *   Hello Carlos.. Thanks for commenting.. The drop down would show the values in the named range (DropDownList in this example). This would indicate an issue in the formula in named range (=$H$3:INDEX($H$3:$H$22,MAX($G$3:$G$22),1)). Make sure that the reference are absolute (such as $H$3). If this doesn’t work, it would be great if you could share the workbook so that I can have a look
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1708)
        
        *   my references are absolute. My formula seems a little different than what you posted but matches what you had in your video. I have COUNTIF instead of MAX… would that be it? How can I share my workbook through here?
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1709)
            
            *   You can share your workbook in Dropbox or Onedrive and share the link here
                
                [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1711)
                
                *   [https://www.dropbox.com/s/7uanb2fjj60m2dz/ECC%20PreReqs.xlsm?dl=0](https://www.dropbox.com/s/7uanb2fjj60m2dz/ECC%20PreReqs.xlsm?dl=0)
                    
                    If you enter CIS into any of the search bars you will see what I am talking about (hopefully). Also, I just noticed when I choose CIS 13 it populates CIS 136 (another choice).
                    
                *   Thanks for sharing the file. Everything else works perfectly. The reason CIS 13 entry shows both CIS 13 and CIS 136 as it matches both. But it takes the first matching value, which is CIS 13. Also, use the below code (use change instead of getfocus)
                    
                    Private Sub ComboBox1\_Change()  
                    ComboBox1.ListFillRange = “DropDownList”  
                    Me.ComboBox1.DropDown  
                    End Sub
                    
                *   Sumit, Thank you very much for taking the time to look over my file. I wanted to really express my appreciation for the website that you have built. I cannot thank you enough for taking the time to share your knowledge and expertise. THANK YOU!
                    
        *   PS thank you for your prompt response!
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1710)
            
        *   Thank you for your prompt response! My formula looks a little different than yours but I followed your video very closely. My reference is absolute but I am using COUNTIF instead of MAX. This is my formula: =$E$2:INDEX($E$2:$E$410, COUNTIF($E$2:$E$410,”?\*”)).
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1712)
            
            *   Both formulas are fine. Your formula is correct for the named range. Would be great if you could share the file (a link of the file in dropbox or onedrive)
                
                [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1714)
                
                *   [https://www.dropbox.com/s/7uanb2fjj60m2dz/ECC%20PreReqs.xlsm?dl=0](https://www.dropbox.com/s/7uanb2fjj60m2dz/ECC%20PreReqs.xlsm?dl=0)
                    
                    sorry I think I keep posting twice, it doesn’t seem to register the first time but then it does.
                    
                *   Its when I type CIS that I notice it gives me all those extra options. I also noticed when I choose CIS 13 it populates CIS 136
                    
145.  This is so awesome, thank you! I have a question: (I haven’t checked all my dropdown choices but) One of my drop down choices, once selected, read something else. For example I choose CIS 13 but it shows up as CIS 136 (which is also one of my dropdown choices). The formulas are working correctly and showing all the appropriate choices… I have no clue why it is happening.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1706)
    
146.  Dear Sumit Bansal,
    
    You are great and wonderful working on excel and I want to give you specially thanks and appreciate for your working . I m also teaching advance excel in our local area and I have a question regarding your working “excel drop down list with search…..”
    
    Dear I want to this kind of search engine in one particular column for typing data entry, I want to working on active cell and don’t want combobox, creating search engine on each cell with list (Data validation) or through vba…
    
    Is it possible??
    
    Hope you are understand what I mean to say.. 🙂
    
    Regards,  
    Mehar Khatri
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1690)
    
    *   Hello Mehar.. Thanks for commenting and for your kind words. The above mentioned process can work for a single or a couple of drop downs. For getting it in all active cells, VBA would be the way to go. I will soon write the code for it and share with you. It is definitely on my To Do list now 🙂
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1701)
        
147.  This is brilliant!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1680)
    
    *   Thanks for the comment. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1683)
        
    *   Thanks for commenting.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1700)
        
148.  Hi Sumit!  
    Good job! Just one remark. I found that this option works much better.
    
    Got focus -> Change
    
    Private Sub ComboBox1\_Change()  
    ComboBox1.ListFillRange = “=DropDownList”  
    Me.ComboBox1.DropDown  
    End Sub
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1675)
    
    *   Hi Dennis.. Thanks for commenting and sharing the code. I tried this and it work perfectly.
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1702)
        
149.  Thank you very much from Romania, too!!! 🙂
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1645)
    
    *   Hello Ionita.. Welcome to TrumpExcel and thanks for commenting.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1703)
        
150.  Hi Sumit,
    
    Great tool you have there, I have it set up and working now!  
    However, I am using this for a list containing quite a few duplicates, which I would like to remove from the drop down list suggestions.
    
    Would you have a solution for this? I tried some VBA coding, but I can’t seem to combine it with your method.
    
    Any help would be greatly appreciated!
    
    Thank you
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1642)
    
    *   Hello.. Welcome to Trump Excel and thanks for commenting. You can first remove duplicates and then use this method.
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1705)
        
151.  Dear Sumit, absolutely great stuff!!  
    my query is, how should I get it in a VBA userform combo box?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1636)
    
    *   Hello Sameer.. Welcome to Trump Excel and thanks for commenting. I will soon be coming up with the code to get this done for userform.. will share with you
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1704)
        
152.  Hello there,
    
    This article is amazing. I am facing a problem when trying to scroll the mouse on the list of suggestions. The whole Sheet moves and the combobox stays on the correct cell, therefore the suggestions roll down the sheet and it’s terrible.  
    Any ideas how to fix it?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1628)
    
153.  Hello – I have meticulously followed your procedure and replicated it almost to the keystroke. Here is the error I am encountering:  
    Run-time error ‘-2147417848 (80010108)’:  
    Method ‘ListFillRange’ of object ‘IMdcCombo’ failed  
    It appears to be a VBA issue, but I duplicated your VBA code flawlessly. I’ve attached a screen shot for your reference.  
    Please help me with this.. I have a lot of time invested in its outcome.  
    Thank you!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1613)
    
154.  Great work!! I want to clear the search field by pushing a button and tried to record a macro. Did not work. Do you have an idea about how to solve this?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1608)
    
155.  Thanks for such a handy trick!..  
    Is it possible to automatically change the range within the formula’s name manager if the list is getting longer or shorter?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1595)
    
    *   Yes it can be done. You will just have to create the named ranges and use it instead of cell references.
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1610)
        
156.  Thanks Sumit for this great info .. is there a way that when I have the suggested list I can move through it with the keyboard arrows instead of the mouse ?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1593)
    
    *   Hi Khaled..Welcome to Trump Excel.. Glad you liked the post.. unfortunately the arrow key would not let you select a country from a list that is shown. However, if you have the country you want to select at the top of the shown list, you can use the down arrow key to select it (so that you don’t have to type the full name)
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1594)
        
        *   Thanks Sumit for your fast reply .. as I cannot use arrow keys to select, is there any way to keep the drop down list open as long as the cell is active? it will close only when I pick another cell somewhere else
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1603)
            
157.  Nice trick Sumit. Can this be applied to a user form
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1586)
    
    *   Hi Anil.. Glad you liked it 🙂 I have not tried this trick in userform, but I believe it may be a bit more complicated in that case. Sometime soon I will give it a shot and post and update on it
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1587)
        
158.  Hey Sumit,
    
    Great tutorial! I have a slight problem I hope you can help. My combo search box only shows 1 data even tho there should be more more.
    
    My look-up table is in columns and not in rows like yours. You mentioned in your video (around 12:30) that since the array only has 1 column, there is no need to add the column number. Could this be the problem? If so, where or how do I add the column numbers?
    
    Here’s my formula:  
    \=$C$2:INDEX($C$2:$KF$2;COUNTIF($C$2:$KF$2;”?\*”))
    
    Your help is much appreciated.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1570)
    
159.  Hi Bansal,
    
    Great to see your trick here..  
    if I have many cell to get this search suggestion from dropdownlist, can we do it?
    
    usually I use dropdown list with Data Validation (list), and now i’ll try to improve with auto completion, can we do that? many thanks
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1568)
    
    *   Hi Edmon, Glad you liked it 🙂
        
        This can be done with multiple drop downs but it becomes cumbersome. If you have more than a couple of drop downs, I suggest sticking to data validation drop down (as they are easy to replicate)
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1569)
        
160.  Hi Sumit Bansal,
    
    I have followed all ur istructions. But when I type in the combobox the 1st letter A then nothing appears in the list. When i type in letter B then all the letters of names that starts with A appears but no B.  
    Have I missed something ??
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1564)
    
161.  Hi Sumit,  
    This is great and amazing technique.  
    I do need some help. Will I be able to send you the file and see if you can fix it for me? Please.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1563)
    
162.  Hi Sumit, I have been able to follow your instruction successfully but i have couple questions. first if i typed a word for example united then two sample will display, is it possible to use the scroll down/up button to select which one i wanted to select, and second question is how do i copy the selected option into a particular cell. Thank you
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1555)
    
163.  Superb piece of work.  
    I have now used this in designing an invoice report. I have a prob;em though, whenever I run another macro on within the file the private sub runs and gives me a box with the contents of the Combo Box in it ‘floating’ about. How can I stop the private sub running when I run other macros (The same thing happens whenever I edit anything in the file).
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1554)
    
164.  Thanks you.  
    wonderful
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1552)
    
165.  Hi Sumit! I want to use the same Combo Box with this type of search suggestion in a user form. But there is no option of List Fill Range available. Hence I am unable to get search suggestions on a user form. Is there a solution to it?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1549)
    
166.  Love the work here. Problem I need help with. Within the same workbook, I have created 2 different combo boxes that are referencing two different data lists…if ComboBox1 has a selected value, ComboBox2 will not work. ComboBox2 will only start working if I clear ComboBox1. I made sure to change the appropriate names in the VBA code, the “fill range” names are different as well. I have noticed that when I click on either ComboBox the formula bar displays =Embed(“Forms.ComboBox.1″,””) for both Combobox1 and ComboBox2. I tried messing with this formula, but i get an error when doing so. Any help would be great.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1547)
    
167.  Amazing tip!!  
    Suggestion for small improvement: In step 5, change =–ISNUMBER(IFERROR(SEARCH($B$3,E3,1),””))  
    to =–ISNUMBER(IFERROR(SEARCH($B$3,LEFT(E3,LEN($B$3)),1),””)) and then copy the formula down.  
    This makes the search always start at the left of each country name, so typing U into the combo box now just brings up United States and United Kingdom, and not Russia, Australia, etc.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1539)
    
168.  Thank you very much for this tutorial. I have gotten everything working, however, when I start typing in the search box with the drop down list showing (single clicking on the search box), it always crashes my Excel file. Alternatively, when I type in the search box after double clicking (this removes the drop down list showing) it does not crash. Have any ideas of why this might be happening?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1538)
    
169.  Thank you!!! very useful 😉 great job, you’re amazing
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1537)
    
170.  Hi Sumeet, Thanks for this Very good Trick 🙂 .. this is too slow with the list i have it has over 15000 items, any suggestions  
    Thanks & Regards,  
    Shardul
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1534)
    
    *   Hi Shardul,, Since there are a lot of rows of data, this is bound to become a bit slow. Also depends on your systems configuration. Here are some tips that can help improve speed in general – [http://trumpexcel.com/2014/04/suffering-from-slow-excel-spreadsheets/](http://trumpexcel.com/2014/04/suffering-from-slow-excel-spreadsheets/)
        
        Hope this helps!
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1535)
        
171.  thanks summit ji,  
    but arrow keys are not working in the list  
    please help
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1512)
    
    *   Hi Dinesh.. Unfortunately, the arrow keys doesn’t work in this case. It is better to either use mouse, or type manually
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1521)
        
        *   Hi Dinesh and Sumit.  
            Sumit is right that the arrow keys generally don’t work as they do with a standard combobox.  
            However if, by typing sufficient letters, the country you require is at the top of the combobox list then pressing UP arrow auto-completes it and selects it. So to select “India” I only have to type “In” and then press the up-arrow.  
            Thought you might like to know!
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1540)
            
172.  Hi, Thank you for your trick. I download your file but I can’t make it work in Excel 2007, is there any limitations?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1502)
    
173.  Thank for this code, I am trying to do exactly the for combo box in an excel UserForm. As am a novice and am really struggling to do this, have you an Excel UserForm example of this code.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1501)
    
174.  This is a great technique, but it is not really convenient for me to use combo boxes. I am working on a bill of Lading and for the products I would like to create that kind of drop down list. I would like to do it without combo boxes. Is it possible to have the same google like search suggestions and yet use just a drop down box in a normal cell? Also I need that for several product lines. I would really appreciate if you could help me out.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1496)
    
175.  Hi Sumit, its amazing  
    but I can’t use this for my purpose,  
    I have a dropdown list, it is used for accounting. my list contains our services. these services varies with customer.  
    how can i use this in my worksheet.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1495)
    
176.  This is really awesome 🙂
    
    I am working on a Vessel Crew program and by finding the crew under last name is now working with this cool function. Although they are not related I have here 3 men with same last name, How can I add a second combobox giving me the opportunity to select the correct person?
    
    Thanks inadvance
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1487)
    
    *   Glad you find this useful. If I understand correctly, you want another drop down that display the full name (or first name) when you have selected the last name. To do this, as you stack up last names, you can also stack up full names (or first names) and then use it as a source of your drop down list.
        
        Hope this helps!
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1488)
        
        *   Thanks Sumit 🙂  
            Can I use the same Combo box for 2 columns?
            
            Not sure if we fully understand each other but to be sure 🙂
            
            I have one table with 40 Columns and 1000+ Rows and I can search key ID like Birthday or Employee number, (This information is not allays available to end user by default)
            
            With your help I can also find persons by Last name in Combo Box by looking at “Last Name” (column J) but when i need to find a person that has same Last name as another person i would like to be able to select the correct first name in the same combo box or a different one
            
            FYI This search is not on the same Sheet as table but on a separate “Form Sheet”
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1489)
            
177.  Great trick…Some questions.
    
    1\. I would to get the full list any time I trigger the dropdown unless the user has started typing in a value – even if a value was previously selected. How do I change the ListFillRange to accomplish this (assume I change the Named Range) ?  
    2\. I would like the list to automatically dropdown when the user starts typing in a value in the textbox portion of the combobox.  
    3\. I would like to display additional column(s) in the dropdown for display purposes only to provide more info about the item to the user. How do I modify the DropDownList named Range to include additional columns?
    
    4\. Is there anyway, I can speed this up. I have a large range of data that gets evaluated when the user manually types in a value.
    
    Thanks
    
    Steve
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1481)
    
178.  How could i make multiple combo boxes in one worksheet(but same filter)? i tryed multiple things and nothing works-.-
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1471)
    
    *   Hi Gregor.. This technique is good enough if you wish to create a couple of these search combo box in a worksheet.. If you wish to create many, I suggest a data validation drop would be the best way to go
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1473)
        
        *   Yes, Sumit Bansal is right. I also try and follow Sumit Bansal’s instruction to make 2 combo boxes in one worksheet, for 2 filter columns (exam: first name and last name). So, you will have one more Helper column 3 (one for first name and one for last name). Formulas are the same, just differ the range. For example :
            
            \=IFERROR(INDEX($B$68:$B$81,MATCH(ROWS($G$68:G68),$G$68:$G$81,0)),””) (first name – set 1 row to display)
            
            \=IFERROR(INDEX($C$68:$C$81,MATCH(ROWS($G$68:G68),$G$68:$G$81,0)),””) (last name)
            
            And then, there are two drop lists (drop1,drop2) to engage to combobox 1 and combobox2, and ListFillRange:
            
            drop1=$H$68:INDEX($H$68:$H$81,MAX($G$68:$G$81),1) (first name)
            
            drop2=$I$68:INDEX($I$68:$I$81,MAX($G$68:$G$81),1) (last name)
            
            Last thing, VBA is also the same for each of combobox.
            
            I can do follow him. You too 😀
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2157)
            
179.  thanks u so much boss…
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1470)
    
    *   Thanks Ravi.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1474)
        
180.  I got a problem, I used your method, works great for one combo box, but when I insert a second one, that\`s when problems arise. Whenever I try to write in the second combo box, the drop down menu of the first combo box drops down showing the very same name I had selected for the first combo box. Hope all of this makes sence. Anything I am doing wrong ?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1462)
    
    *   Hi Nick. if you are using multiple combo-box, use this vba code instead:
        
        Private Sub ComboBox1\_GotFocus()  
        ComboBox1.ListFillRange = “=DropDownList”  
        Me.ComboBox1.DropDown  
        End Sub
        
        I hope this works for you!!
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1463)
        
        *   I’m having the same issue and can’t figure out what’s going wrong with it…  
            Tried the new code but same issue.
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2512)
            
        *   I am also having this issue. Adding the GotFocus part did not work for me either.
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3045)
            
        *   Well That doesn’t work for me too
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-10263)
            
181.  This is perfect! Its a fairly simply solution to an aggravating issue with data validation drop downs. One issue though, how would I change the VBA code to account for multiple drop-downs on a single sheet? I keep running into an issue where I have 2 separate instances of the code you provided, each one unique for the combobox it pertains to, but when I start to type in the first box the second one is the one that pulls up the “suggestions” in the drop down list. This renders the first combo box useless since I cant ever get the list to offer suggestions as it always reverts down to the next box. I have double checked that my names are correct in the code and that there isnt any cross over, but I cant get it to work. Would you have any suggestions for having multiple combo-boxes one sheet?
    
    Thanks.
    
    \-Joe
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1459)
    
    *   Hi Joe, If you are using multiple combo-box, try this vba code instead:
        
        Private Sub ComboBox1\_GotFocus()  
        ComboBox1.ListFillRange = “=DropDownList”  
        Me.ComboBox1.DropDown  
        End Sub
        
        Hope this works for you.
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1464)
        
182.  Hee, Lovin it! Only one thing, The combobox is showing te dropdown after every random action in Excel. Is there a trick to only show the suggestions when i click on the combobox??
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1447)
    
    *   I am also encountering this, the combo box shows all the time in another sheets or another excel file…how do I prevent this?
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1454)
        
        *   Someone a solution? 🙂
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1467)
            
            *   Hi Erwin.. Try this VBA code instead:
                
                Private Sub ComboBox1\_GotFocus()  
                ComboBox1.ListFillRange = “=DropDownList”  
                Me.ComboBox1.DropDown  
                End Sub
                
                Hope this works!!
                
                [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1468)
                
                *   It Works! Thanks a lot!!
                    
                *   Thank you ! It works. But I have another trouble.
                    
                    I don;t know why but when I click on combo Box –> type text (exam: An ) –> chose 1 item in the list ( Exam: An Binh hosp)–> press Enter –> LinkedCell (C3) is ok (=An Binh hosp) but Combo Box.value is blank (properties and appearance on screen) –> click the arrow of combo box, choose “An Binh hosp” again –> Combo box appears “An Binh hosp” in it.  
                    Did I miss something when following your instruction ?  
                    Here my file:
                    
                    [https://onedrive.live.com/redir?page=view&resid=79FB6F76781A1D6A!195&authkey=!AFNZEOKhnwEb6ds](https://onedrive.live.com/redir?page=view&resid=79FB6F76781A1D6A!195&authkey=!AFNZEOKhnwEb6ds)
                    
                    Please help me take a look and give me solution.
                    
                    Thank you in advance.
                    
                *   I’ve got the same problem. Thanks to your solutions, it works!
                    
183.  Hi Sumit, I have listened to your great tutorial many times and followed all the directions. Everything works well except for the search suggestion. I don’t get a drop down list. When I return to the properties of the combo box I notice that I am unable to save “DropDownList” in the ListFillRange. Can you help? Thank you!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1435)
    
184.  I love this – worked for me – when i followed your instructions! THANK YOU!
    
    BUT- the only difference is when i used to use regular Data Validation list- it was easy to copy that drop down into an entire column. How can i do that with this Active X control Drop down? Because i want to use it for at least a thousand student records… need to line up with the other student data.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1434)
    
    *   Hey Missy.. Glad you liked it!! If you have hundreds or thousands of records, that this would be very time consuming, as the combo box has to be inserted manually. You can try Data Validation drop down list (although it may not be searchable), it is easy to execute
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1436)
        
185.  Love the search as you type combo box, how can I make the ranges dynamic? I would love to just keep adding data to the end of the country list not have to recreate the formulas and named ranges every time.  
    Thanks
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1430)
    
    *   Thanks Bob.. Glad you like it!
        
        Here is how you can make named range dynamic – [http://trumpexcel.com/2014/01/formula-hack-16-create-dynamic-named-ranges/](http://trumpexcel.com/2014/01/formula-hack-16-create-dynamic-named-ranges/)
        
        Or even better, use excel table feature – [http://trumpexcel.com/2014/03/excel-table-the-hidden-treasure-in-excel/](http://trumpexcel.com/2014/03/excel-table-the-hidden-treasure-in-excel/)
        
        Hope this helps!!
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1431)
        
186.  Hi Sumit!
    
    You save me with my problem…you are so good in excel and learned so much on your website.
    
    I hope to learn more from you!
    
    Thanks so much for this amazing website.
    
    Is there a way to communicate directly to you…really want to learn more 🙂
    
    Thank you.
    
    Janice Nunez.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1414)
    
    *   Hi Janice.. Glad you found this useful 🙂
        
        You can reach out to me at [sumitbansal23@gmail.com](mailto:sumitbansal23@gmail.com)
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1415)
        
        *   Hi Sumit,
            
            Thanks. I have just send you an email.  
            I hope you will have spare time to read it and would really need some help.
            
            Thanks so much.
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1416)
            
            *   Hi Summit,  
                I tried adding up another combo box in the same sheet, hoping of the same result from another source, but ListFillRange doesn’t allow me to save what I have typed in.  
                Any idea?  
                Thanks.
                
                [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1418)
                
187.  Sumit: trick 20 is awesome! Thank you so much for sharing this! Any suggestion as to how I could arrange for a column that the values in the column get entered through the Data Validation list thing with a combo-box with the search capabilities you explained?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1409)
    
188.  Hi. I have tried this method and it does work, however every time I enter a letter it gives me an error that there are not enough resources to display properly. I am unsure why this is happening. Thanks for your help
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1398)
    
    *   Hi Arielle.. This happened with me once, and changing the zoom of the worksheet made it go away. Try once with 100% zoom (hope it works for you too)
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1399)
        
189.  I have been looking for this type of functionality for some time now. Now is it possible to have a range of cells in the same column with type of functionality. The example only has the one combobox that links to B3. Could this work for cells from say B3:B10? If you have a solution for this, could you e-mail me a sample at [jstriker@oh.rr.com](mailto:jstriker@oh.rr.com)
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1391)
    
    *   I’d like to have this solution as well
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2246)
        
    *   yes , how do we do this ?
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3193)
        
190.  hi, I create one Worksheet contain Master Data in A\_Master sheet and in another sheet i have to select master from drop down list. i use your Tip#20, its work perfect but when i try to select any master by pressing down arrow, Excel stop working and start recovery!!!! i don’t know what’s wrong. i down load your given file from here and try same things, as soon as i press down arrow key excel stop working in your file too. please give me any solutions for that.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1381)
    
    *   Hi Dhiren.. Seems to be working fine on my system. Can you try once without the macro.. May work for you
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1382)
        
        *   I am having the same issue with the arrow keys. Everything works great, but if I hit the down arrow, excel crashes. I commented out the lines in the macro and it didn’t crash, but when I use the macro it crashes.
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-2901)
            
        *   Mine is also crashing with arrow keys. I’m using Excel 2016 please help. Thanks
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-3846)
            
    *   Hi, had the same issue, and i cant find a solution, but there is a workaround, which is to disable the arrow keys when user activates the combo box. arrow key use will be restored once outside the combo box.
        
        Private Sub ComboBox1\_KeyDown(ByVal KeyCode As \_  
        MSForms.ReturnInteger, ByVal Shift As Integer)  
        ‘Disable Up&Down-arrow key – causing problems in ComboBox selections  
        If KeyCode = vbKeyDown Then KeyCode = vbNull  
        If KeyCode = vbKeyUp Then KeyCode = vbNull  
        End Sub
        
        source: [https://www.reddit.com/r/excel/comments/3zkz8f/a\_way\_to\_disable\_arrow\_keys\_in\_a\_combobox/](https://www.reddit.com/r/excel/comments/3zkz8f/a_way_to_disable_arrow_keys_in_a_combobox/)
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-9609)
        
        *   It works well. Thank you!
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-11296)
            
191.  Hey Bansal, thats an awesome one. Im searching for this type of Drop  
    list, but this is only a one time search, for example consider a  
    invoice(a table), where we have to enter ‘n’ number items, can you  
    please give a solution for that? (OR) can we use the same tool without  
    combobox? Im preparing a sales estimate for my firm, can you please give  
    a solution for multi search tool. contact me on [sumanthvzm@yahoo.co.in](mailto:sumanthvzm@yahoo.co.in)
      
    or 9966939396
    
    Thanks in advance
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1378)
    
    *   Hey Sumanth.. Not sure if I understand you correctly.. Have a look at this – [http://trumpexcel.com/2013/07/extract-data-based-on-a-drop-down-list-selection-in-excel/](http://trumpexcel.com/2013/07/extract-data-based-on-a-drop-down-list-selection-in-excel/)
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1379)
        
        *   with reference to the above query… i have seen the link you have provided. That is not the solution. Eg. I am making a list or records and I want it to auto suggest the location from a list of locations, but how do you replicate a combo box for each line separately? pls email me [sad00007@gmail.com](mailto:sad00007@gmail.com)
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1395)
            
            *   Hi Saajidh.. I am not sure I understand your query.. Can you upload sample data and mention what you wish to do
                
                [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1396)
                
                *   let me show with data..
                    
                    Date  
                    Invoice no.  
                    Telephone  
                    Name  
                    Address  
                    Pcs
                    
                    16-03-14
                    
                    55544596  
                    Mohamed Al Marri  
                    Muaither  
                    1
                    
                    23-03-14
                    
                    66633221  
                    Khalid Ibrahim  
                    Al Aziziya  
                    1
                    
                    24-03-14
                    
                    66553898  
                    Mohamed Ali  
                    Dafna  
                    1
                    
                    I want the “Address” field to come from a search box and the list in infinite…
                    
                *   You can upload the file on dropbox and share the link here. Would be easy to understand when I have the data in Excel
                    
                *   [https://www.dropbox.com/s/vz2dmjcbe8a9bf2/sample.xlsx](https://www.dropbox.com/s/vz2dmjcbe8a9bf2/sample.xlsx)
                    
                    pls see file…
                    
192.  Great work, I like it. but I’m just curious how could I make it work if I want it to show me more columns of the same item. Let’s say If I search for United States so it will show me “United States” but in addition will also show me … I don’t know “number of people” – “latitud” – etc etc etc . Hope you can understand me. Thank you 🙂
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1365)
    
    *   Hey.. Have a look at this.. [http://trumpexcel.com/2013/07/extract-data-based-on-a-drop-down-list-selection-in-excel/](http://trumpexcel.com/2013/07/extract-data-based-on-a-drop-down-list-selection-in-excel/)
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1366)
        
193.  Hello – I followed the steps but I can’t get the search drop down to appear in the Combo Box when I start typing. What am I missing?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1352)
    
    *   Hi Alia – I have created a video tutorial that might be helpful (at the end of the blog). Alternatively, you can also use the excel sheet download, and change the data and ranges accordingly. Hope this works!!
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1353)
        
194.  how can i do That in VBA
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1347)
    
    *   Hello Jesus Miranda – I am sure there is a way to do this in VBA, but I haven’t gone that way yet. I try to stay away from VBA if the stuff can be done without it in Excel. But to your point, it can definitely be tried.
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1351)
        
    *   Hi Jesus Miranda.. I am sure there is a way to do this all using VBA, but I have explored that much. Will definitely share when I come up with the VBA method
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1354)
        
        *   Any update on a VBA method?  
            I have 4 columns that one dropdown needs to handle (one at a time) and the columns needs to be filtered as it dont contrain unique data + length of list can change
            
            [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1408)
            
            *   To know how to do in VBA check last post in this….[https://groups.google.com/d/msg/excel-macros/UFqFSDz4ufM/0NfYRBmZRDQJ](https://groups.google.com/d/msg/excel-macros/UFqFSDz4ufM/0NfYRBmZRDQJ)
                
                [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1545)
                
                *   Dear Vabz, it is very useful to us, but how to set different form boxes in different columns.
                    
    *   To know how to do in VBA check last post in this…….[https://groups.google.com/d/msg/excel-macros/UFqFSDz4ufM/0NfYRBmZRDQJ](https://groups.google.com/d/msg/excel-macros/UFqFSDz4ufM/0NfYRBmZRDQJ)
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1546)
        
195.  Thank you very much from indonesia for this amazing trick =)
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1340)
    
    *   Thanks Eka 🙂
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-1355)
        
196.  Everytime I return to the Control Box, the text entered and the dropdown below it get smaller and smaller. Advice on how I can stop that from happening? (I set the Properties of the Control Box to a specific font and size but that did not help.)
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-334)
    
    *   Hi Truman.. It seems to be working fine on my system. Let me check it on other systems if this happens, What version of excel are you using?
        
        [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-340)
        
197.  It is good trick man.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-225)
    
198.  Its really good .. Thanks for sharing
    
    [Reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#comment-212)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/#respond)

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