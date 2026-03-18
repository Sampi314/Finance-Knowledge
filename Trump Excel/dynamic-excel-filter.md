# Dynamic Excel Filter Search Box (Extract data as you Type)

**Source:** https://trumpexcel.com/dynamic-excel-filter

---

[Skip to content](https://trumpexcel.com/dynamic-excel-filter/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/dynamic-excel-filter/#below-title)

Excel Filter is one of the most used functionalities when you work with data. In this blog post, I will show you how to create a Dynamic Excel Filter Search Box, such that it filters the data based on what you type in the search box.

Something as shown below:

![Dynamic Excel Filter Search Box - Demo of the excel functionality where you can filter data as you type](https://trumpexcel.com/wp-content/uploads/2015/01/Dynamic-Filter.gif)

There is a dual functionality to this – you can select a country’s name from the [drop-down list](https://trumpexcel.com/excel-drop-down-list/)
, or you can manually enter the data in the search box, and it will show you all the matching records. For example, when you type “I” it gives you all the country names with the alphabet I in it.

**[Download Example File and Follow Along](https://trumpexcel.com/wp-content/uploads/2015/01/Dynamic-Excel-Filter.xlsx)
**

**Watch Video – Creating a Dynamic Excel Filter Search Box**

This Tutorial Covers:

[Toggle](https://trumpexcel.com/dynamic-excel-filter/#)

Creating a Dynamic Excel Filter Search Box
------------------------------------------

This Dynamic Excel filter can be created in 3 steps:

1.  Getting a unique list of items (countries in this case). This would be used in creating the drop down.
2.  Creating the search box. Here I have used a Combo Box (ActiveX Control).
3.  Setting the Data. Here I would use three helper columns with [formulas](https://trumpexcel.com/excel-functions/)
     to extract the matching data.

**Here is how the raw data looks:**

![Dynamic Excel Filter Search Box - This is how the raw data looks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20351%20497'%3E%3C/svg%3E)

_USEFUL TIP: It is almost always a good idea to convert your data into an [Excel Table](https://trumpexcel.com/excel-table/)
. You can do this by selecting any cell in the dataset and using the keyboard shortcut Control + T._

### Step 1 – Getting a unique list of items

1.  Select all the Countries and paste it into a new worksheet.
2.  Select the country list –> Go to Data –> Remove Duplicates.![Clean Data in Excel - Remove Duplicates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%2081'%3E%3C/svg%3E)
3.  In the [Remove Duplicates](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
     dialogue box, select the column in which you have the list and click Ok. This will remove duplicates and give you a unique list as shown below:![Dynamic Excel Filter - Getting a unique list of values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20103%20190'%3E%3C/svg%3E)
4.  One additional step is to create a [named range](https://trumpexcel.com/named-ranges-in-excel/)
     for this unique list. To do this:
    *   Go to Formula Tab –> Define Name
    *   In Define Name Dialogue Box:
        *   Name: CountryList
        *   Scope: Workbook
        *   Refers to: \=UniqueList!$A$2:$A$9 (I have the list in a separate tab named UniqueList in A2:A9. You can refer to wherever your unique list resides)![Dynamic Excel Filter - Named Range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20323%20246'%3E%3C/svg%3E)

NOTE: If you use ‘Remove Duplicates’ method and you expand your data to add more records and new countries, you will have to repeat this step again. Alternately, you can also you a formula to make this process dynamic.

_See Also: [How to use a formula to get a list of Unique items.](https://trumpexcel.com/unique-items-from-a-list-in-excel/)
_

### Step 2 – Creating The Dynamic Excel Filter Search Box

For this technique to work, we would need to create a ‘Search Box’ and link it to a cell.

We can use the Combo Box in Excel to create this search box filter. This way, whenever you enter anything in the Combo Box, it would also be reflected in a cell in real-time (as shown below).

![Dynamic Excel Filter - Text reflected in real time](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20288%2092'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Go to Developer Tab –> Controls –> Insert –> ActiveX Controls –> Combo Box (ActiveX Controls).
    *   _If you do not have the Developer Tab visible, [here are the steps to enable it.](https://trumpexcel.com/excel-developer-tab/)
        [![Search Box to Filter in Excel - Combo Box from Developer Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20312%20198'%3E%3C/svg%3E)](https://trumpexcel.com/excel-developer-tab/)
        _
2.  Click anywhere on the worksheet. It will insert the Combo Box.![Dynamic Excel Filter - Combo Box Inserted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20115%2048'%3E%3C/svg%3E)
3.  Right-click on Combo Box and select Properties.
4.  In Properties window, make the following changes:
    *   Linked Cell: K2 (you can choose any cell where you want it to show the input values. We will be using this cell in setting the data).
    *   ListFillRange: CountryList (this is the named range we created in Step 1. This would show all the countries in the drop down).
    *   MatchEntry: 2-fmMatchEntryNone (this ensures that a word is not automatically completed as you type)![Creating a Dynamic Excel Filter Search Box - Combo Box Properties](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20433%20441'%3E%3C/svg%3E)
5.  With the Combo Box selected, Go to Developer Tab –> Controls –> Click on Design Mode (this gets you out of design mode, and now you can type anything in the Combo Box. Now, whatever you type would be reflected in cell K2 in real time)![Dynamic Excel Filter - Text reflected in real time](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20288%2092'%3E%3C/svg%3E)

### Step 3 – Setting the Data

Finally, we link everything by helper columns. I use three helper columns here to filter the data.

**Helper Column 1:** Enter the serial number for all the records (20 in this case). You can use [ROWS()](https://trumpexcel.com/excel-rows-function/)
 formula to do this.![Dynamic Excel Filter - Helper Column 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20377%20448'%3E%3C/svg%3E)

**Helper Column 2:** In helper column 2, we check whether the text entered in the search box matches the text in the cells in the country column.

This can be done using a combination of [IF](https://trumpexcel.com/excel-if-function/)
, [ISNUMBER](https://trumpexcel.com/excel-is-function/)
 and [SEARCH](https://trumpexcel.com/excel-search-function/)
 functions.

Here is the formula:

\=IF(ISNUMBER(SEARCH($K$2,D4)),E4,"")

This formula will search for the content in the search box (which is linked to cell K2) in the cell that has the country name.

If there is a match, this formula returns the row number, else it returns a blank. _For example, if the Combo Box has the value ‘US’, all the records with country as ‘US’ would have the row number, and rest all would be blank (“”)![Dynamic Excel Filter - Helper Column 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20445'%3E%3C/svg%3E)_

**Helper Column 3:** In helper column 3, we need to get all the row numbers from Helper Column 2 stacked together. To do this, we can use a combination if [IFERROR](https://trumpexcel.com/excel-iferror-function/)
 and [SMALL](https://trumpexcel.com/excel-small-function/)
 formulas. Here is the formula:

\=IFERROR(SMALL($F$4:$F$23,E4),"")

This formula stacks all the matching row numbers together. _For example, if the Combo Box has the value US, all the row numbers with ‘US’ in it get stacked together.![Dynamic Excel Filter - Helper Column 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20507%20442'%3E%3C/svg%3E)_

Now when we have the row numbers stacked together, we just need to extract the data in these row number. This can be done easily using the index formula (insert this formula in where you want to extract the data. Copy it in the top-left cell where you want the data extracted, and then drag it down and to the right).

\=IFERROR(INDEX($B$4:$D$23,$G4,COLUMNS($I$3:I3)),"")

_This formula has 2 parts:_  
**[INDEX](https://trumpexcel.com/excel-index-function/)
** – This extracts the data based on the row number.  
**IFERROR** – This returns blank when there is no data.

Here is a snapshot of what you finally get:![Dynamic Excel Filter - Final Output](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20690%20399'%3E%3C/svg%3E)

The Combo Box is a drop down as well as a search box. You can hide the original data and helper columns to show only the filtered records. You can also have the raw data and helper columns in some other sheet and create this dynamic excel filter in another worksheet. ![Dynamic Excel Filter - Demo of the Search Box](https://trumpexcel.com/wp-content/uploads/2015/01/Dynamic-Filter.gif)

_**Download the Dynamic Excel Filter Example File[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2015/01/Dynamic-Excel-Filter.xlsx)
**_

**Get Creative! Try Some Variations**

You can try and customize it to your requirements. You may want to create multiple excel filters instead of one. For example, you may want to filter records where Sales Rep is Mike and Country is Japan. This can be done exactly following the same steps with some modification in the formula in helper columns.

Another variation could be to filter data that starts with the characters that you enter in the combo Box. For example, when you enter ‘I’, you may want to extract countries starting with I (as compared with the current construct where it would also give you Singapore and Philippines as it contains the alphabet I).

_As always, most of my articles are inspired by the questions/responses of my readers. I would love to get your feedback and learn from you. Leave your thoughts in the comments section._

Note: In case you’re using Office 365, you can use the [FILTER function](https://trumpexcel.com/filter-function/)
 to quickly filter the data as you type. It’s easier than the method shown in this tutorial.

**You May Also Like the Following Excel Tutorials:**

*   [Highlight Matching Data Using Conditional Formatting – Dynamic Search](https://trumpexcel.com/search-highlight-using-conditional-formatting/)
    .
*   [Create a Search Suggestion Drop Down List in Excel](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/)
    .
*   [Using Advanced Filter in Excel](https://trumpexcel.com/excel-advanced-filter/)
    .
*   [How to Extract a Substring in Excel (Using TEXT Formulas)](https://trumpexcel.com/extract-a-substring-in-excel/)
    .
*   [Creating a Drop Down Filter to Extract Data Based on Selection](https://trumpexcel.com/extract-data-from-drop-down-list/)
    .
*   [How to Filter Cells with Bold Font Formatting in Excel.](https://trumpexcel.com/filter-bold-font-formatting-in-excel/)
    
*   [Highlight Rows Based on a Cell Value in Excel.](https://trumpexcel.com/highlight-rows-based-on-cell-value/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

187 thoughts on “Dynamic Excel Filter Search Box – Extract Data as you Type”
----------------------------------------------------------------------------

1.  Hi, how do i get the helper columns to automatically update when i add to my MasterData list when the helper columns are hidden?  
    Thanks
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-14523)
    
2.  Hey Hi There, this does not work in large data it takes too long to find the result is there any other way to do it?  
    My data is of 5lks
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-13850)
    
3.  Hi,
    
    what if i want to filter only unique record only? lets say in my data against the country japan “Product 7” is coming for 7 times but i want to filter it only one time . is it possible?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-13567)
    
4.  What is the workaround to the ActiveX to reproduce this result? I’m working in a Mac environment and AX is problematic.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-13414)
    
5.  Brilliant Idea, It helped me a lot, I was looking for a similar solution  
    Thank you
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-13289)
    
6.  Hi Sumit  
    Thank you for this excellent post.  
    I have a question regarding sub-query within the attribute.
    
    For example if you want to see product category from both India AND China how do you change the equation?
    
    In this case we are trying to separate group of country and applying filter on them.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-13140)
    
7.  Great article that I have immediately put to use! How would I have the cursor default to being inside the combo box when the workbook is opened? Thanks
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-12907)
    
8.  This is a brilliant tutorial with a very effective final result. Thanks for laying this out. I’ll be using this over and over again, I’m sure. FANTASTIC!
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-12887)
    
9.  Excellent Video.  
    I was thinking how it would be possible to apply this advance filter and then have the option to input data into the filtered products.
    
    Example I filter for India, it bring up 4 result and then I want to input data to the results. More like i’m filtering the actual entire row of the result?
    
    You response will be greatly appreciated.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-12867)
    
10.  hi, I have been using this dynamic filter system for years and it works brilliantly!!!.  
    One thing that was not needed was the drop down choice to be filtered, but  
    recently I have re-used this idea and again it works perfectly but….. this time the drop down filter to choose just a letter and it filter the results would be wonderful, but it just doesn’t work. I have downloaded the excel file and have copied everything to the letter but it just chooses the full name of the selection. Can anyone help.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-12808)
    
11.  Hi Sumit,
    
    I’ve found your video extremely useful, but like a lot of others I’m struggling to apply your formula to multiple searches/filters/conditions. I’ve seen you’ve shared a dropbox link for this solution but they have expired. Is it possible to please create another link or to comment in an example of this formula – this would be much appriciated.
    
    Many thanks,
    
    Jack
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-12806)
    
12.  Hi There,
    
    It really helped me do the search bar and it works fine,  
    however, my data is huge and it takes lot of time to get the output and it keeps calculating.  
    Kindly suggest on the concern.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-12771)
    
13.  You are really good
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-12743)
    
14.  How do I create this for multiple excel filters? Let’s say, I want to put in a second filter.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-12566)
    
    *   Hey Bradley – did you figure this out? I am trying to do the same
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-12577)
        
        *   Hey, no I didn’t figure it out; hoping someone would lend a hand
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-12579)
            
            *   It says above it can be done ‘exactly following the same steps with some modification in the formula in helper columns.’
                
                Can anyone help??
                
                [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-12588)
                
    *   I did get this to work with multiple filters. Use the search for multiple selections (Column Helper 2 – apply for each sort field) to come up with the data columns, and then use a separate column to call out where the various columns all have the same data. I did three helper columns with a sort of “if Helper 1 = Helper 2 = Helper 3 then show value in Helper 1”. Then I did the sort in Helper 3 off of the new column and it worked.
        
        I hope that makes sense…
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-12888)
        
15.  how if searching in multiple sheets  
    \=IFERROR(INDEX(‘DAY1′!$B$6:$O$55,’DAY1’!$S6,COLUMNS($B$10:B10)),””)  
    day 1 = 1 sheet up to 31 sheet
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-12522)
    
16.  I like your post it is very informational. Kindly also make post to use this search filter in vba form
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-12432)
    
17.  Another variation could be to filter data that starts with the characters that you enter in the combo Box. For example, when you enter ‘I’, you may want to extract countries starting with I (as compared with the current construct where it would also give you Singapore and Philippines as it contains the alphabet I).
    
    I would love to know will I do the above statement. and btw thankyou for the video it really helo me a lot. the only thing that i need to do is the statment above.
    
    I hope you will answer this
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-12268)
    
18.  So effective… Thank you so much !  
    One improvement would by to allow us to search for multiple words.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-11997)
    
19.  What if i would like to have the entire spreadsheet to be filtered to only extract data with everything that contains “la” or “east”. This formula only allows for data from a specific column. How can this be accomplished?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-11259)
    
20.  hi
    
    please I have different sheet each one of them have the same think just different company name. i want to have as in this exemple but result in an other sheet and also the data coming from different sheet  
    thanks
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-11238)
    
21.  I know this is old, but I know too that a lot of people still uses this topic. It’s so useful! But I’d like to know if there is any way to make the search box better, I mean, searching Products, Sales Rep and Countries. Not ONLY contries. Thanks!
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-11152)
    
22.  hi  
    first, thank you for this excellent work :
    
    I need, please your help if you can.
    
    I want to know I want to create this filter first with more than 15 worksheets and each one having the same column and rows information.
    
    I want to create a comparison tool, as if, I enter for example item number or name will give me a grill with what I need in a unique worksheet as an output.
    
    Here is what I have :
    
    1- 15 worksheets: each worksheet, it’s for a specific company, each sheet has the same thing: ex:  
    item name, prices, capacity, our prices, margin, etc..
    
    2- I want to make a search ( as you did in the box you create ) when I search for example by name:
    
    \*\*\* My result expected: will give a table with the less price first and which company is associated with.
    
    3- is it possible to do with excel, if not can you guide me please, which program I can need to use is it a database +VB or what exactly, please.
    
    Thanks a lot.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-11146)
    
23.  sorry,its doesn’t work over 313 rows,what i should do?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-10938)
    
24.  Can I make it show no result until/unless I type something in the search box?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-10856)
    
25.  Can a search box be created in a second sheet using the data from sheet1?  
    I have about 2500 line items (Inventory) and 7 header columns. I currently use Conditional formatting but the problem is scrolling down the page to see what is highlighted.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-10849)
    
    *   Yes, you can.  
        Make these “helpers” in the sheet where all the data is.  
        Then, in the secondary sheet, make a table with Filtered Data.  
        \=IFERROR(INDEX((dataSheet!$B$4:$D$23000);(dataSheet!$G4);COLUMNS(showSheet!$A$4:A4));””)
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-10862)
        
26.  Is there a way to then be able to sort through this list? When I sort, some blank rows appear
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-10816)
    
    *   Sort Z>A not A>Z
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-11295)
        
27.  I need to use a dynamic filter text for online usage, with a shared website in my company. How can I use ActiveX Dynamic filter this way?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-10785)
    
28.  How can I do this if I don’t have a designer license?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-10580)
    
29.  Would it be possible to set up 2 columns, where the first column has multiple looks for “this” AND “that”, and the second column has fields that looks for “this” OR “that”, and return the results in the same column?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-10447)
    
30.  Very nice
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-10376)
    
31.  Extremly super admin.. i appreciate it a lot. thank you so much.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-10253)
    
32.  can you do the filter without using helper columns? i mean, filtering the data table?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-10095)
    
33.  How do you make it so that hyperlink would stay intact in your search results?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-10073)
    
34.  how can i provide security for this file.i mean we have a cleint list.the flle shall be available for everyone in office.i can protect workbook with a password. but search bar also getting password protection. what can i do
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9976)
    
35.  hi, could we make this filter but with additional conditions instead of just 1 condition?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9974)
    
36.  Hello,
    
    I have successfully completed this; however, one of my columns with information the populates contains hyperlinks to documents on the computer. Right now these hyperlinks are only showing up as text. I would like the link to be retained when it appears in the search results, can you help with this?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9930)
    
37.  Hi Sumit, can you tell me how can I customize the text search to show only the specific text I am looking for? Current formulas return any text that contains what was entered in the text box.  
    Thank you for your help,  
    Enna
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9918)
    
    *   I’m also having this problem. Any help would be appreciated!
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-10866)
        
38.  hi…  
    if there are multiple rows then what should be done in helper coloumns…. do i setup the helper 4 row and which formula i have to enter…  
    please do needful help
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9825)
    
39.  This works great for my needs! I would like to hide the dynamic list while the search box is empty and only show the results. Is there a way to do this?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9717)
    
40.  I like the idea (and I’m guessing this is pretty old) but this is the most round about way I’ve ever seen to accomplish this. What you really want is to simply work the autofilters via the combobox’s change event. if you need to view your filtered data on a separate sheet then simply copy the filtered range to it. No need for helper columns or vlookup/index formula’s either. You could also use a dynamic range in VBA and forget about the static named range altogether.  
    Just my 2cents…
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9661)
    
    *   Hi SM177y  
        can you please elaborate on this?  
        I think you are referring to manage large number of data rows  
        I have around 10K rows and the original equation in this post is little slow.
        
        how can i improve this?
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-13141)
        
41.  Hello. This is a great tutorial and is just what I was looking for. However, I’m stuck on Helper 3. In the YouTube video you mention something about adding ROWS. I can’t see the formula because the video is a little blurry. In the instructions above, there is no mention of rows. When I follow the instructions above, I’m not getting my numbers stacked in Helper 3.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9651)
    
    *   Hello.. The ROWS function is used in Helper Column 1. The formula used in cell E4 is =ROWS($B$4:B4) and then copied for all the remaining cells in the column. You can also download the example file and see the exact formula in it.
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9681)
        
42.  Hi Sumit, just to check can we select two filters like maybe one box for both country and name or two boxes , one for country and one for name. How would the excel sheet formula be like? Thanks in advance
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9600)
    
43.  I am still a relative novice with excel, so forgive me if my question seems silly. I was fine until I got to creating the index. When I try to drag the formula down and to the right, it changes the formula in the other boxes in such a way that the search doesn’t bring up the proper information. Basically the formula changes by shifting the area of information either down a row or one column to the right. Is there a way to prevent it from changing anything other than what is necessary for accuracy so I don’t have to manually go in and fix it?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9531)
    
44.  Straight forward with clear explanations! Sambit you are an excellent trainer 🙂
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9528)
    
45.  This is brilliant, thanks a lot for posting it!
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9478)
    
46.  too good, but this formula only on 20 cell i need it on 2k cell please help me!
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9441)
    
47.  i need this formula, but its work only with 20 cell in need it till 2k cells. please help me?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9439)
    
    *   Following this guide, to use it on a larger data set, you would only need to redefine the named range to include however many rows you need….But if you read my other comment and do a little Googling, you’ll find much easier, faster, and more efficient ways to accomplish this that aren’t bound to any static range.
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9662)
        
48.  Is there a way how I could add more than 1 dynamic filter in a sheet? Let’s say first I sorted all which were for India, and then via second one I need to sort only Sales Rep John within India. Thanks in advance. Emil
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9333)
    
49.  Many thanks for this. I was able to follow your very clear explanations. Works remarkably well. I’d like to add a button to clear the search field. I wonder if you would mind sharing any suggestions?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-8978)
    
50.  Thanks a lot
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-8843)
    
51.  Hi Sumit,  
    I would like to make dynamic books title list with the help of this formula, can you suggest further options to me e.g. – once a user will get the data after applying drop down option after this can he directly email the outcome to clients or save the outcome in PDF
    
    email – [varunsharma16@gmail.com](mailto:varunsharma16@gmail.com)
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-8703)
    
52.  Hi, Plz give me the two filters in same excel file and its not working in office 2007.
    
    Plz help me with sample file
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-8656)
    
53.  Hello. How can insert more filters for different columns?[https://uploads.disquscdn.com/images/5bf7497f303c2c95f33b160f2df5f94f550af55627fa776df4f806e6f5f84d4c.png](https://uploads.disquscdn.com/images/5bf7497f303c2c95f33b160f2df5f94f550af55627fa776df4f806e6f5f84d4c.png)
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-8471)
    
    *   Have a look at this file: [https://www.dropbox.com/s/junqiduvcu929im/Dynamic-Excel-Filter%20-%202%20conditions.xlsx?dl=0](https://www.dropbox.com/s/junqiduvcu929im/Dynamic-Excel-Filter%20-%202%20conditions.xlsx?dl=0)
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-8499)
        
        *   Thanks it works!
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-8570)
            
54.  Hi Sumit – I am building an excel dynamic filter with three combo filters and used the sheet you provided. I updated your data with mine and the table will not populate with the data in J,K,L,M Columns. It also brings up results that include partial spelling of the word I filtered by. Any tips?
    
    [https://uploads.disquscdn.com/images/19ca56064e7652e5ae9209a5241c817f0644dc910843e1b1839187be278cae47.jpg](https://uploads.disquscdn.com/images/19ca56064e7652e5ae9209a5241c817f0644dc910843e1b1839187be278cae47.jpg)
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-7907)
    
    *   Hi Summit – I fixed the issue with the table populating when using the combo boxes. I do have two other questions. When I use the Combo boxes for filter it includes any results that has similar spelling, but I just want it to show the “Brand” I have selected.  
        How do I update Helper 2 formula: =IF(AND(ISNUMBER(SEARCH($M$2,B4)),ISNUMBER(SEARCH($L$2,C4)),ISNUMBER(SEARCH($K$2,D4))),F4,””)  
        My other question is how can I show no results when no combo filter box has nothing selected?  
        Thank You! Great tutorial.
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-7909)
        
        *   Use the exact formula instead of search. Use the following formula in helper column 2: =IF(EXACT($K$2,D4),E4,””)
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-8531)
            
        *   Your above finding was really helpful for my report with multiple filters. This is what I was looking for. Appreciate your contribution 🙂
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-11120)
            
        *   I’m having issues with the Helper Column 3 with this formula, where nothing is displayed / organised despite the filters being met. Any ideas?
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-13989)
            
55.  Hi Sumit, would you please share the formula to include up to 30 conditions again please? I can’t seem to be able to access the file via the dropbox link above. It would help very much!  
    Thank you!!
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-7032)
    
56.  Great idea. My list fill range does not seem to work. When I type in the Name of my unique list, it disappears when I hit enter. Any ideas? Thanks!
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-4752)
    
    *   I was able to replicate the issue using your demo file. It seems to fail if you turn the unique list into a table and use the =Tablex\[ColumnY\] function. Pretty frustrating that Excel does that. I prefer to use the table functions as my arrays/lists rather than a range, since the unique list may change over time. Any ideas of a workaround? Thanks!
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-4754)
        
        *   This is a known issue with Excel 2013 being unable to directly refer to a table name. Instead we have create another surrogate name that simply refers to the first. Then ListFillRange will accept it. source [http://www.contextures.com/excelworksheetcomboboxes.html](http://www.contextures.com/excelworksheetcomboboxes.html)
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-4759)
            
57.  Hello Sumit, thank you for your wonderful and very helpful tutorial. Question, I have certain questions that are highlighted but when they are extracted they’re no longer highlighted, how can I keep the questions in the same style?  
    thank you for your amazing knowledge.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-4206)
    
58.  हिन्दी में बताइए
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3918)
    
59.  This is brilliant! Thanks for the sharing! Very useful!
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3881)
    
60.  This was great Sumit! Very helpful. I ran into one problem and was wondering if you knew a quick fix. If it was mentioned already in the comments, please let me know and I’ll go find it. In my list, I have terms such as NBC, MSNBC, CNBC, etc. When I do the drop down selection for MSNBC, I only get results for MSNBC (which is good!) However when I do the drop down selection for NBC, I get results for anything related to NBC (NBC, MSNBC, CNBC, NBCSN, etc). Is there a way for me to isolate just NBC? Thanks  
    ~Brian
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3859)
    
61.  Hi there, can I embed this feature on my website?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3712)
    
62.  Great article Sumit. Thanks for sharing 🙂
    
    I’ve just discovered a pretty good video where the search filter works dynamicaly by hiding the rows. Looks very nice and useful. Moreover, there is a download link below the video, so you can try it immediately.
    
    [https://www.youtube.com/watch?v=iZ933-tU6Yw](https://www.youtube.com/watch?v=iZ933-tU6Yw)
    
    Maybe you will find there some new ideas..
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3697)
    
    *   thanks yu, you are really helping me a lot.. keep up your good work. god of excel 🙂
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9854)
        
63.  Hi… Thanx for the great post…it was really helpful !!!  
    I want to do something similar, but rather than filtering on the column i want to filter by row.  
    i.e. You are showing a row if it the cell has the particular value, I want to show the columns if the cell in it has the particular value. I am able to write formulas for populating the helper columns.  
    But am stuck with the last one to populate the final set.  
    Can you please help with this?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3607)
    
64.  Thank you for the video. What if I want to extract any data that I type in the combo box, what would the formula be? Thanks.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3498)
    
65.  Is there a way to auto fill repetitive data like name and address?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3401)
    
    *   Hello Robert.. have a look at this tutorial: [http://trumpexcel.com/2014/05/let-excel-complete-abbreviations-for-you/](http://trumpexcel.com/2014/05/let-excel-complete-abbreviations-for-you/)
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3439)
        
        *   Thanks Sumit for the reply and pointing me to the right topic. I will check out the link.
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3455)
            
        *   I did check the link but it does not suit what I was looking for. This is the actual scenario what I am looking for maybe you can point me to the right topic. We have to input name of companies to Excel based on the Invoice issued, the name would occur several times. Together with the name there is assigned Tax Identification Number that would be inputted beside the company name. I would appreciate any help.
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3456)
            
66.  Fantastic demo, well written. I’m a little confused why you need to create a unique table, why not dump all your raw data on one sheet (in my case, priority, alarm, information, support team) and have another sheet do the search and display the relevant rows below ? This would (I think) be more universal and help more people. Just a thought, not by any means a criticism.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3344)
    
    *   Thanks for sharing Miles.. Unique list is created for the drop down, so that there are no repetitions in that. If that’s not needed, that you can do away with the unique list step
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3438)
        
67.  Hello,
    
    If I have dates in mm/dd/year (or some equivalent) how can I use the dynamic filter to search by month or year whilst keeping the date format?
    
    Unfortunately even if the dates are formated to say the respective month it only searches in based off of what is in the formula box.
    
    I look forward to your response.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3262)
    
68.  Hi Sumit, thanks for this. It’s a great tutorial. I have a couple of further issues I’m hoping you can help me with. In my filtered results any cells that were left blank in the raw data now have a 0 (zero) in them. Is there a way to show the cells as blank in the filtered results? Also, some of the filtered cells contain hyperlinks. These are “live” in the raw data (if you click them they open the relevant page in your browser), but they are not live in the filtered data. Is there a way to make them live in the filtered data? Thanks for any help you can give!
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3196)
    
69.  hello, thanks for your post. but i noticed the first formula doesn’t work for me
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3168)
    
70.  HOW DO I SELECT ONLY ITEMS THAT START WITH THE CHARACTER I WANT. IF I ENTER “PH” I WANT TO RETRIEVE PHILLIP NOT ALPHOSO…YOU MENTION TWEEKING THE HELP BUT I’M NOT SURE HOW..
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3148)
    
71.  Hello. Thank you for the superb post. You saved me big time. But there’s a problem. The search box also filter the words that contain the words I search. For example, I search for “AN” and the rows with “CHANH” also appear. How can I set it so that only the exact word is filtered?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3121)
    
    *   Hello Minh. You can do that by replacing the formula in Helper 2 with the following: =IF(AND(ISNUMBER(SEARCH($K$2,D4)),LEN(D4)=LEN($K$2)),E4,””)
        
        Simply put this formula in F4 and copy for all the cells in that column.
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3137)
        
72.  Hi Sumit, Can you show how to add two filters, Country and Product? How can that be done?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2949)
    
    *   Hello.. Have a look at this file: [https://www.dropbox.com/s/junqiduvcu929im/Dynamic-Excel-Filter%20-%202%20conditions.xlsx?dl=0](https://www.dropbox.com/s/junqiduvcu929im/Dynamic-Excel-Filter%20-%202%20conditions.xlsx?dl=0)
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2964)
        
73.  Hello, Is it possible to take the range of the ‘Filtered Data’ section from one sheet to another?
    
    If I copy the formula over and add the sheet name before the cell I can see all the current values, but it doesn’t appear to be dynamic and update like the information does on the original sheet.
    
    any help is appreciated.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2824)
    
    *   Hello JP.. You can get the filtered data in another sheet as well. Instead to adding the sheet name manually, I would suggest you reconstruct it from scratch (as shown in the tutorial). That way Excel will take care of the cell referencing and naming itself
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2873)
        
74.  Hi Sumit
    
    This is a brilliant method for making a searchable staff telephone list. However, some of my cells in the range are blank, where there is either no extension or mobile, and they are showing in the search result table as 0. I have tried, without success, to add an if statement to weed these out and show them as blank cells. Is there a way to do this without causing the formula =IFERROR(INDEX($B$4:$D$23,$G4,COLUMNS($I$3:I3)),””) to throw up an error?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2823)
    
    *   Hello Dawn.. Would be great if you could paste a screen shot of the data, or send me the data via email. I just want to make sure I give you the formula that suits your data. It can be done by tweaking existing formulas used in the template
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2874)
        
75.  Hi Sumit,
    
    Thanks for sharing!
    
    I am currently putting the dynamic filter and its data on a different worksheet. May I know if it is possible to also have a filter option to display “All the data”.
    
    If I would like to have the option to choose “All Countries” from your example, how would I be able to do it?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2817)
    
    *   Hello Jo. You can do that by changing the formula in Helper Column2. Here is a template that gives the option to select all countries – [https://www.dropbox.com/s/sczdl872t74say2/Dynamic-Excel-Filter\_All%20Countries.xlsx?dl=0](https://www.dropbox.com/s/sczdl872t74say2/Dynamic-Excel-Filter_All%20Countries.xlsx?dl=0)
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2875)
        
76.  When the combo box is empty it shows the entire result(s). Is there a way when the combo box is empty the results are blank?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2815)
    
    *   Hello Rob.. change the formula in Helper Column 2 with the following formula: =IF(AND($K$2″”,ISNUMBER(SEARCH($K$2,D4))),E4,””)
        
        Now when the combo box is empty, it will show no results
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2876)
        
77.  Hi Sumit, is it possible to search 2 items at the same time for example: all the US and the Canada ?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2745)
    
    *   Hello Elyse..Yes you can have filter on multiple conditions. The formula needs to be changed to make it OR instead of AND. Have a look at this file where you can filter based on two countries [https://www.dropbox.com/s/q49v1qhuozxnrq9/Dynamic-Excel-Filter%20-%202%20conditions%20Same%20Country.xlsx?dl=0](https://www.dropbox.com/s/q49v1qhuozxnrq9/Dynamic-Excel-Filter%20-%202%20conditions%20Same%20Country.xlsx?dl=0)
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2760)
        
78.  Hi Sumit – this is awesome! Just wondering if you’re able to help me out a little bit more?
    
    I’m trying to do a version of this where the data is output to a second sheet (saves me from hiding & unhiding cells all the time).
    
    I’ve managed to output the data to a sheet named UI (user interface) but now the search filter isn’t working. It’s probably something to do with how I’ve written the Formula’s, but I can’t figure it out.
    
    I’ve attached screenshots showing the sheets and the formula’s being used. Any help would be much appreciated!
    
    Cheers,  
    Jen
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2728)
    
    *   Hello Jen.. Can you share the file (may be a dropbox or onedrive link). I can’t see snapshots here
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2761)
        
79.  This is super awesome ! One quick question: can we highlight the keywords in some color in the database as we type and it hits the match. Please let me know
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2633)
    
    *   Thanks for commenting Shameek.. Here is a tutorial to highlight the matching rows as you type in a search box – [http://trumpexcel.com/2013/07/search-in-excel-conditional-formatting/](http://trumpexcel.com/2013/07/search-in-excel-conditional-formatting/)
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2634)
        
        *   I checked this one before, not working for me. I already have a dynamic filter using the formula what’s it’s shown here, now i want to color code only texts while typing using the same dynamic filter .. I have used 3 helper and the formula is the same what’s shown in this. Also I have created a front end where showing the search results but the color coding is not working. Don’t know why.
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2637)
            
80.  Sir, Thank you so much for the tutorial, you save my family’s business.  
    I do have a bit of question. Instead of country name like Japan, India, Singapore, I have a “group id” like 001, 01, 240, 24, 924. And I did >Define Name and all. But once I start using the combo box, “24”, the items of other group like 240 and 924 would come along.
    
    I guess it has something to do with The helper 2 column “=IF(ISNUMBER(SEARCH($K$2,D4)),E4,””)”  
    Could you please help me to search the result of the exact value? Thank you so much !
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2621)
    
    *   Hello Seebear.. You can do that by changing the formula in Helper Column 2 to =IF($K$2=D4,E4,””)
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2762)
        
81.  hi i m sumeet , sir i want to know that can i edit the data selected from the drop down list on real time , for eg. i have selected sumeet as my name from the drop down list & i want to add singh as my surname after my name on real time basis
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2538)
    
82.  This was so helpful. Thank you. I had been banging my head all week trying to do this on my own.
    
    Only issue I encountered is after selecting the item from the Combo list, sometimes the selection just disappears – i.e. the combolist seems to just clear itself. Not sure what is going on there. Do you have any idea what could be causing this please?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2533)
    
83.  can we add 3 or 4 columns in data and shown in filtered data
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2520)
    
84.  Hello Sumit, thanks a lot very helpful site!! I have been trying for days now without getting any solution. Is there a way to edit the filtered values? for example I type Japan. Then once I have the filtered results I go and change/update the Sales Rep name?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2479)
    
85.  hi. if I have 6 columns, then i will be having 6 helper?? pls answer. thanks
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2469)
    
86.  hi Sir,  
    i have tried it on my datasheet using the same formulas but it seen like i cant filter the information what i want.  
    can you able to see what wrongs with my formula?
    
    thank you in adance
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2421)
    
87.  Hi,  
    As i mentioned in the comments below. I’ve got a pretty large dataset for which this solution really struggles. and takes good few seconds to filter through data. I’ve just read about INDEX MATCH formula – so was wondering if this type of dynamic search could be achieved using INDEX MATCH formula, which should be most probably quicker than the INDEX you have used here. Please advise.  
    Thank you
    
    p.s. more about INDEX MATCH benefits: [http://www.mbaexcel.com/excel/why-index-match-is-better-than-vlookup/](http://www.mbaexcel.com/excel/why-index-match-is-better-than-vlookup/)
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2284)
    
88.  Hello Sumit,
    
    Thank you so much for uploading this video. Is there any way to show the search result blank if there is no data in the combobox ?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2242)
    
    *   Hello Siddhartha.. Thanks for dropping by and commenting. You can do this by changing the formula in 2nd helper column to: =IF(LEN($K$2)=0,””,IF(ISNUMBER(SEARCH($K$2,D4)),E4,””))
        
        Paste this formula in F4 and drag it down.
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2248)
        
        *   Hi Sumit,  
            Thanks for your sharing, if the data table have a blank in somewhere cell, it doesn’t count this row, any formula can solve it?
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2323)
            
89.  Keep going, i am a fan of this website.. Gaurav Negi
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2138)
    
    *   Thanks for commenting Gaurav,, Glad you like the tutorials here 🙂
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2140)
        
90.  Hi Sambit,
    
    Regarding the variations: I’m wondering if it’s possible to have more than two conditions/filters? I can’t seem to figure out the correct formula.
    
    Thanks!
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2120)
    
    *   Hello Anna, Have a look at this file. I have created the filter for 2 conditions – [https://www.dropbox.com/s/junqiduvcu929im/Dynamic-Excel-Filter%20-%202%20conditions.xlsx?dl=0](https://www.dropbox.com/s/junqiduvcu929im/Dynamic-Excel-Filter%20-%202%20conditions.xlsx?dl=0)
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2121)
        
        *   Hi again Sumit,
            
            I’ve downloaded that version and applied the formula to my spreadsheet. It works perfectly for two conditions, but I can’t figure it out for more than two. Is this possible? Sorry if this isn’t clear!
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2122)
            
            *   have a look at this – I have used 3 conditions here – [https://www.dropbox.com/s/sumo1l3b37nc1jm/Dynamic-Excel-Filter%20-%203%20conditions.xlsx?dl=0](https://www.dropbox.com/s/sumo1l3b37nc1jm/Dynamic-Excel-Filter%20-%203%20conditions.xlsx?dl=0)
                
                You need to modify the formula in second helper column to check for all 3 conditions
                
                [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2123)
                
                *   AMAZING! Thank you so much for your quick response. Is there a maximum condition limit, or can you use as many conditions as you like? Thank you again!
                    
                *   Glad it helped.. The number of conditions depends on the data, In this case, we have 4 columns of data, so there could be 4 conditions. AND formula can handle a maximum of up to 30 conditions
                    
                *   I added another condition and it worked. Thank you so much again for your help, it’s much appreciated!
                    
                *   Hi Sumit, would you please share the formula to include up to 30 conditions again please? I can’t seem to be able to access the file via the dropbox link above. It would help very much!  
                    Thank you!!
                    
                *   Gr8, but Combo Box 2 is drop down list is carrying sales rep data, though in case I type any name of product category, it’s ok.
                    
91.  Nice,works well, but unusable with big tables, takes 5 min to filter a 12k row table on a Quad Core i5 with 4G RAM. I am aware this is not the intended use, just want to inform others who want to give it a try 🙂
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2119)
    
    *   Hi.  
        I’m in the same situation as posted above. I’ve got a file of 15 000 rows and the list is constantly growing. I’ve tried the formula with helper columns and all works great, apart that it takes around 1-3 seconds to generate a list from my query. Also the way i made a formula is to output the data to another sheet as a summary instead of seeing all raw data, so it looks really need. I’ve also tried the same solution with the 1 000 entries and that returns data as i type. I’ve got i5 6 GB laptop and it really struggles with the large database (15k rows). Is there another way of making the same dynamic search that wouldn’t put so much pressure on processor and would return data as i type?  
        Also big thanks for trumpexel for such a great solution.
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2282)
        
92.  Hi there 🙂 Suppose I have hyperlinks instead of text data in the specific columns, how do I retain the hyperlink and not extract the data as text after the search
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2110)
    
    *   Have a look at this technique – [http://trumpexcel.com/2014/03/create-dynamic-hyperlinks-in-excel/](http://trumpexcel.com/2014/03/create-dynamic-hyperlinks-in-excel/)
        
        You would need to club the 2 to get dynamic filter that retain hyperlinks
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2111)
        
        *   ahh ok thanks for the prompt reply!
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2112)
            
        *   Club the two? I have web links in the “Sales Rep” Column. How do I get it to retain the hyperlink after it has been searched? This has been very helpful so far. Thanks!
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2663)
            
93.  I have a huge data approx. 50,000 rows and i want to filter it with search box as i start typing in the search box the data starts to filtering but i am failed to do it.
    
    Your example is too good but I don’t want to use “INDEX” formula.  
    Please help me out.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2108)
    
    *   Hi.  
        I’m in the same situation. I’ve got a file of 15 000 rows and the list is constantly growing. I’ve tried the formula with helper columns and all works great, apart that it takes around 1-3 seconds to generate a list from my query. Also the way i made a formula is to output the data to another sheet as a summary instead of seeing all raw data, so it looks really need. I’ve also tried the same solution with the 1 000 entries and that returns data as i type. I’ve got i5 6 GB laptop and it really struggles with the large database (15k rows). Is there another way of making the same dynamic search that wouldn’t put so much pressure on processor and would return data as i type?  
        Also big thanks for trumpexel for such a great solution.
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2281)
        
94.  Hi Sumit,
    
    You wrote this “You can try and customize it to your requirements. You may want to create 2 filter instead of one. For example, you may want to filter records where Sales Rep is Mike and Country is Japan. This can be done exactly following the same steps with some modification in the formula in helper columns.”
    
    Could you please tell me what changes to make in helper columns to make 2 filters work?
    
    Thanks a lot!
    
    Kindly let me know.  
    Best Regards,  
    Karthik
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2093)
    
    *   Have a look at this – [https://www.dropbox.com/s/junqiduvcu929im/Dynamic-Excel-Filter%20-%202%20conditions.xlsx?dl=0](https://www.dropbox.com/s/junqiduvcu929im/Dynamic-Excel-Filter%20-%202%20conditions.xlsx?dl=0)
        
        I have added another filter and changed the formula in the helper columns
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2095)
        
        *   Thanks Sumit, i tried that, but it gives me a message “we found one or more circular references that might cause your formulas to calculate incorrectly”. is there something I can look out for to resolve this problem?
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2097)
            
            *   Hey Karthik.. Are you talking about the file I shared, or something you created? The file I have shared works fine on my system. I checked and there are no circular reference errors. If it’s a file you have created, kindly share with me and I can have a look
                
                [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2098)
                
95.  You can try and customize it to your requirements. You may want to create 2 filter instead of one. For example, you may want to filter records where Sales Rep is Mike and Country is Japan. This can be done exactly following the same steps with some modification in the formula in helper columns.
    
    Sumit, Could you please tell me how to use 2 filters, i.e. what changes to make in the helper columns?  
    Thanks
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2092)
    
96.  hi, this is very useful for my task. But I need one that can hyperlink also. Does this dynamic filter can be linked to other file such as pdf file? For example, if I click product 1 in the filtered table, I expect that it will open another file consists of product 1 data. Is it possible? Thanks
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2058)
    
    *   It can be done if you are looking to hyperlink within the same workbook. Have a look at this – [http://trumpexcel.com/2014/03/create-dynamic-hyperlinks-in-excel/](http://trumpexcel.com/2014/03/create-dynamic-hyperlinks-in-excel/)
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2059)
        
        *   I guess I can’t link it to other file like .doc? only to data in the same workbook
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2060)
            
        *   What if I want to Hyperlink to a website?
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2662)
            
97.  Yes . I have a database where there are 50 columns and each column has  
    10000 rows , with new entries being added each day . I want 50 dynamic  
    filters on each column so that i dont have to scroll the page for  
    applying filters on each column . As i want to filter data with  
    combination of any number of columns , i was looking for multiple  
    dynamic filter . Basically i want to use normal filters to filter data ,  
    with the exception that i can place the combobox as per my convenience  
    . Also if you can tell any technique wherein when I type the data in  
    dynamic filter it gives a google type search dropdown also , it will be most  
    helpful . Thanks
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2047)
    
98.  this was really helpful .. can anyone tell how to make more than one dynamic filter in this
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2044)
    
    *   Glad you liked it.. What do you mean by more than one filter. Are you looking for more than one criteria?
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2046)
        
99.  Great Bansal sahab
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-1977)
    
    *   Thanks for commenting.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2045)
        
100.  hi Sumit,  
    two days back only I came across your site and just looking through..it makes me wonder!!  
    Keep on keeping On.
    
    Amal
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-1886)
    
    *   Hello Amal.. Welcome to Trump Excel and Thanks for commenting.. I am really glad you found the website useful 🙂
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-1887)
        
101.  Hey, great idea and implementation. I might use it at school to teach the kids a few tricks. Can all of this be done with a text field instead of drop-box?
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-1806)
    
    *   Thanks for commenting and glad you liked it 🙂 I am afraid I not aware of any way to do this without combo-box. The benefit for combo-box is that it makes the data entry dynamic, which instantly gives you results.
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-1807)
        
102.  This is worked perfect! I have a table with 830 rows that displays totals at the bottom of each column; and each filter option will result in about 200 rows. The problem that I have now is that I have to scroll all the way down to row 831 in order to see the totals. This document will also be printed by end users and I would like to avoid the extra blank papers. Any suggestions will be highly appreciated.
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-1773)
    
    *   Hi Michelle.. you can try this formula:
        
        \=IF(AND(G3″”,G4=””),SUM($G$4:G4),IFERROR(INDEX($B$4:$D$23,$G4,COLUMNS($I$3:J3)),””))
        
        I have made it based on the data set I have provided in the download file (assuming Column C has numbers)
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-1774)
        
103.  Very cool
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-1692)
    
    *   Thanks Buddy.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-1697)
        
104.  It is really helpful
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-1691)
    
    *   Thanks for the comment Uday.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-1698)
        
    *   Thanks for commenting Uday..Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2636)
        
        *   Thanks alot for this great video , it helped me alot , God bless you
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-14207)
            
105.  Hey, I did it without Helper and Array. For intermediate level, it’s bit complex 🙂
    
    {=IFERROR(INDEX($B$2:$D$21,SMALL(IF(ISNUMBER(SEARCH($U$1,$D$2:$D$21)),ROW($D$2:$D$21)-1,””),ROW()-4),COLUMNS($L$4:L4)),””)}
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-1679)
    
    *   Hello Deepak.. Thanks for commenting and sharing the formula 🙂
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-1682)
        
    *   Hi Deepak, can you maybe brake your formula down into smaller segments so i can understand what and how you did it. Also i’m trying to find a way to work with 15k lines of dataset which Trumpexel is not really coping well with as it takes 3-4 seconds to give the results on i5 6GB RAM processor. So i wonder if your formula would be any quicker as it wouldn’t need helper colums. please advise.  
        Thank you
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2296)
        
        *   dragging the array formula till 15k row will make the excel sheet slow..
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3935)
            
    *   Hello Deepak, i’m really interested in seeing the rest of your formula here, for some reason it’s cutting it off after ROW($D$2:$D$21)-1,””),
        
        I know it was a long time ago, but if you could possibly reply with the rest of the formula i would really appreciate it!
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3930)
        
        *   Nevermind, it appeared when I opened in a different browser, thank you!
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3931)
            
            *   Thanks Randy, you know it takes time to understand my own complex formula 🙂 lol …
                
                [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3934)
                
    *   Hey Deepak Could u share your excel sheet. Your formula is little bir confusing
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9080)
        
        *   Its difficult to find the excel file, what i have done is – i have incorporated all the helper formula in one formula..so it became big.
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9082)
            
        *   Sure but i can’t upload the excel file here, can you please share your Email Id so that i can send it to you.
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9083)
            
            *   [b.alperkaya@gmail.com](mailto:b.alperkaya@gmail.com)
                
                [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9089)
                
                *   Sent
                    
    *   Hi Deepak, would you be able to send me a copy of the corresponding excel file please to help understand your formula a bit better? Thanks in advance!
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9145)
        
        *   Pls share your email so that I can send you the file.
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9149)
            
    *   Do you know how can I multiple excel filters with your formula?  
        Thank you,
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-9913)
        
106.  Really it’s great…….
    
    [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-1678)
    
    *   Thanks for commenting Sambit.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-2635)
        
        *   Hello Bansal,  
            i’m new on the forum. i looking for a way to do exactly what you describ in this topic.  
            from the bebening, it works well. but when it come to apply the formulla, it became confused for me. the formula doesn’t work on my side.  
            it come with mistake from the helper column 2 :=IF(ISNUMBER(SEARCH($K$2,D4)),E4,””)  
            can you help me please.  
            will be gratfull
            
            Isaac
            
            [Reply](https://trumpexcel.com/dynamic-excel-filter/#comment-3169)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/dynamic-excel-filter/#respond)

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