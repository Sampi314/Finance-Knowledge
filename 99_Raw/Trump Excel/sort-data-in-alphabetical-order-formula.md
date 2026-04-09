# Automatically Sort Data in Alphabetical Order using Formula

**Source:** https://trumpexcel.com/sort-data-in-alphabetical-order-formula

---

[Skip to content](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#below-title)

Excel built-in [data sorting](https://trumpexcel.com/sort-excel/)
 is amazing, but it isn’t dynamic. If you sort data and then add data to it, you would need to sort it again.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#)

**Sort Data** in **Alphabetical Order**
---------------------------------------

In this post, I will show you various ways to sort data in alphabetical order using formulas. This means you can add data, and it will automatically sort it for you.

### When the Data is all Text with No Duplicates

Suppose you have a data as shown below:![Sort data in alphabetical order - text dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20265%20187'%3E%3C/svg%3E)

In this example, all the data is in text format (no numbers, blanks or duplicates). To sort this, I will use a helper column. In the column next to the data, use the following [COUNTIF](https://trumpexcel.com/excel-countif-function/)
 formula:

\=COUNTIF($A$2:$A$9,"<="&A2)

![sort data in alphabetical order - Helper column with countif](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20524%20243'%3E%3C/svg%3E)

This formula compares a text value with all the other text values and returns its relative rank. For example, in cell B2, it returns 8, as there are 8 text values that are lower than or equal to the text ‘US’ (alphabetical order).

Now to sort the values, use the following combination of [INDEX](https://trumpexcel.com/excel-index-function/)
, [MATCH](https://trumpexcel.com/excel-match-function/)
 and [ROWS](https://trumpexcel.com/excel-rows-function/)
 functions:

\=INDEX($A$2:$A$9,MATCH(ROWS($B$2:B2),$B$2:$B$9,0))

![sort data in alphabetical order - Formula Index to get sorted data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20646%20241'%3E%3C/svg%3E)This formula simply extracts the names in the alphabetical order. In the first cell (C2), it looks for the country name that has the lowest number (Australia has 1). In the second cell, it returns Canada (which has the number 2) and so on..

**Allergic to Helper Columns??**

Here is a formula that will do the same without the helper column.

\=INDEX($A$2:$A$9,MATCH(ROWS($A$2:A2),COUNTIF($A$2:$A$9,"<="&$A$2:$A$9),0))

This is an array formula, so use _Control + Shift + Enter_ instead of Enter.

I will leave it for you to de-code.

_**Try it Yourself.. Download Example File**_[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2015/02/Sort-Data-in-Alphabetical-Order-using-Formula.xlsx)

This formula works well if you have text or alphanumeric values.

But it fails miserably if:

*   You have duplicates in the data (try putting US twice).
*   There are blanks in the data.
*   You have a mix of numbers and text (try putting 123 in one of the cells).

Also read: [Separate First and Last Name in Excel](https://trumpexcel.com/separate-first-and-last-name-excel/)

### When Data is a Mix of Numbers, Text, Duplicates, & Blanks

Now this one is a bit tricky. I will use 4 helper columns to show you how it works (and then give you a huge formula that will do it without the helper columns). Suppose you have a data as shown below:![sort data in alphabetical order - blank duplicate 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20243%20217'%3E%3C/svg%3E)

You can see there are duplicate values, blank and numbers. So I will use helper columns to address each of these issues.

**Helper Column 1**

Enter the following COUNTIF formula in Helper Column 1

\=COUNTIF($A$2:$A$9,"<="&A2)

![sort data in alphabetical order - blank duplicate 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20244'%3E%3C/svg%3E)

This formula does the following:

*   It returns 0 for blanks.
*   In the case of duplicates, it returns the same number.
*   Text and numbers are processed parallelly and this formula returns the same number for text and number (for example 123 and India both get 1).

**Helper Column 2** 

Enter the following [IS Function](https://trumpexcel.com/excel-is-function/)
 in Helper Column 2:

\=--ISNUMBER(A2)

![sort data in alphabetical order - blank duplicate 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20471%20269'%3E%3C/svg%3E)

**Helper Column 3**

Enter the following formula in Helper Column 3:

\=--ISBLANK(A2)

![sort data in alphabetical order - blank duplicate 4](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20441%20268'%3E%3C/svg%3E)

**Helper Column 4**

Enter the following formula in Helper Column 4

\=IF(ISNUMBER(A2),B2,IF(ISBLANK(A2),B2,B2+$C$10))+$D$10

![sort data in alphabetical order - blank duplicate 5](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20658%20264'%3E%3C/svg%3E)

The idea for this formula is to segregate blanks, numbers and text values.

*   If the cell is blank, it returns the value in cell B2 (which would always be 0) and adds the value in cell D10. In a nutshell, it will return the total number of blank cells in the data
*   If the cell is a numerical value, it will return the comparative rank and add the total number of blanks. For example, for 123 it returns 2 (1 is the rank of 123 in the data, and there is 1 blank cell)
*   If it is text, it returns the comparative rank and add the total number of numerical values and blanks. For example, for India, it add the text’s comparative rank in text (which is 1) and adds the number of blank cells and the number of numerical values.

**Final Result – Sorted Data**

Now we will use these helper columns to get the sorted list. Here is the formula:

\=IFERROR(INDEX($A$2:$A$9,MATCH(SMALL($E$2:$E$9,ROWS($F$2:F2)+$D$10),$E$2:$E$9,0)),"")

![sort data in alphabetical order - blank duplicate 6](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20887%20265'%3E%3C/svg%3E)

This method of sorting now becomes fool-proof. I have shown you the method for 8 items, but you can extend it to as many items as you want.

_**Try it Yourself.. Download Example File[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2015/02/Sort-Data-in-Alphabetical-Order-using-Formula.xlsx)
**_

### One Formula to Sort it All (without Helper Columns)

If you can handle extreme formulas, here is an all-in-one formula that will sort data in alphabetical order (without any helper column).

Here is the formula:

\=IFERROR(INDEX($A$2:$A$9,MATCH(SMALL(NOT($A$2:$A$9="")\*IF(ISNUMBER($A$2:$A$9),COUNTIF($A$2:$A$9,"<="&$A$2:$A$9),COUNTIF($A$2:$A$9,"<="&$A$2:$A$9)+SUM(--ISNUMBER($A$2:$A$9))),ROWS($A$2:A2)+SUM(--ISBLANK($A$2:$A$9))),NOT($A$2:$A$9="")\*IF(ISNUMBER($A$2:$A$9),COUNTIF($A$2:$A$9,"<="&$A$2:$A$9),COUNTIF($A$2:$A$9,"<="&$A$2:$A$9)+SUM(--ISNUMBER($A$2:$A$9))),0)),"")

Enter this formula in a cell and drag it down to get the sorted list. Also, since this is an array formula, use _Control + Shift + Enter_ instead of Enter.

This formula has real-world utility. What do you think? I would love to learn from you. Leave your footprints in the comments section!

**You May Also Like the Following Excel Tutorials:**

*   [Multi-level Sorting in Excel](https://trumpexcel.com/multiple-level-sorting-excel/)
    
*   [How to Sort by Length in Excel? Easy Formulas!](https://trumpexcel.com/sort-by-length-excel/)
    
*   [Step-by-step Guide to Use Sorting in Excel](https://trumpexcel.com/sort-excel/)
    .
*   [Concatenate Excel Ranges (with and without separator)](https://trumpexcel.com/concatenate-excel-ranges/)
    .
*   [How to Sort Data in Excel using VBA (A Step-by-Step Guide)](https://trumpexcel.com/sort-data-vba/)
    .
*   [How to Sort By Color in Excel](https://trumpexcel.com/sort-by-color/)
    
*   [How to Sort by the Last Name in Excel](https://trumpexcel.com/sort-by-last-name-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

82 thoughts on “Automatically Sort Data in Alphabetical Order using Formula”
----------------------------------------------------------------------------

1.  Smart Guy!  
    🙂
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-42309)
    
2.  If you want to extract unique values with ignoring blank cells use this formula:
    
    {=IFERROR(INDEX($A$2:$A$9,MATCH(SMALL(IF(($A$2:$A$9″”)\*(MATCH($A$2:$A$9&””,$A$2:$A$9&””,0)=ROW($A$2:$A$9)-ROW($A$2)+1),IF(ISNUMBER($A$2:$A$9),COUNTIF($A$2:$A$9,”<="&$A$2:$A$9),COUNTIF($A$2:$A$9,"<="&$A$2:$A$9)+SUM(–ISNUMBER($A$2:$A$9)))),ROWS($A$2:A2)),IF(($A$2:$A$9″”)\*(MATCH($A$2:$A$9&””,$A$2:$A$9&””,0)=ROW($A$2:$A$9)-ROW($A$2)+1),IF(ISNUMBER($A$2:$A$9),COUNTIF($A$2:$A$9,”<="&$A$2:$A$9),COUNTIF($A$2:$A$9,"<="&$A$2:$A$9)+SUM(–ISNUMBER($A$2:$A$9)))),0)),"")}
    
    For reverse sorting data from ascending to descending replace SMALL( to LARGE(
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-13407)
    
3.  Excellent, love it, thanks. Mike H.
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-13313)
    
4.  Love your ingenuity with this. 🙂
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-12973)
    
5.  and this is why libre office is far better than excel
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-11984)
    
6.  Formula works great if the originating data list is not the result of formulas that may contain blanks. I dont mean empty cells. I mean the result of a formula that returns a blank (“”). Even the downloaded version puts the blanks on the top of the list (when changing the Column A to show a few =””. Simply put – the formula doesnt work unless the originating data does not contain “”. Shame too, it was a nice formula….until it didnt work. (If anyone figures this out, let me know) (jason@simconconcrete.com)
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-11961)
    
7.  Method with helper columns also fails when I have duplicates… Will have to sort out a solution…
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-11577)
    
    *   Solution was:  
        i) add a preliminary Helper 0 in column B, and shift rightward the rest of Helpers (ie. Helper 1 in col.C, etc).  
        ii) in Helper 0, add the formula in cell B2  
        \=COUNTIF($A$2:$A$9;”=”&A2) – COUNTIF($A$2:A2;”=”&A2)  
        … and extend to the end of the column range.  
        iii) adjust Helper 1 column with the formula in cell C2  
        \=COUNTIF($A$2:$A$9;”<="&A2)-B2
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-11587)
        
        *   This indeed fixes the duplication problem! thank you.
            
            [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-14601)
            
8.  Great work, thanks! Would have taken me a stupid amount of time to dope this out on my own (and I LOVE helper columns)
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-11521)
    
    *   Sorry, meant to mention.  
        In my case, I was actually needing to sort column A by the alpha order of Column B. Meaning that for all the duplicates in Column B, I actually had a unique value in Column A, each of which I need to list.  
        SO….  
        I simply added two more helper columns, helper 4: counted the occurrences of value of column B in range column B, helper 5: added helper 4 and 5 together, and voila!
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-11522)
        
9.  Above sort without helper column will fail with dupes. Use this following variation as the lazy person solution to dupes. If column to be sorted has varying number of rows of data, this one handles it…
    
    \=If(a2=””,””,INDEX($A$2:$A$9,IFERROR(MATCH(ROWS($A$2:A2),COUNTIF($A$2:$A$9,”<="&$A$2:$A$9),0),MATCH(ROWS($A$2:A2),COUNTIF($A$2:$A$9,"<="&$A$2:$A$9),-1))
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-11330)
    
10.  Very good for me ! I adjusted it and it works. But ….  
    How and what must it be changed in formula to have number sorted descendig and the text unchanged, at the end ?
    
    \=IFERROR(INDEX($A$2:$A$9,MATCH(SMALL(NOT($A$2:$A$9=””)\*IF(ISNUMBER($A$2:$A$9),COUNTIF($A$2:$A$9,”<="&$A$2:$A$9),COUNTIF($A$2:$A$9,"<="&$A$2:$A$9)+SUM(–ISNUMBER($A$2:$A$9))),ROWS($A$2:A2)+SUM(–ISBLANK($A$2:$A$9))),NOT($A$2:$A$9="")\*IF(ISNUMBER($A$2:$A$9),COUNTIF($A$2:$A$9,"<="&$A$2:$A$9),COUNTIF($A$2:$A$9,"<="&$A$2:$A$9)+SUM(–ISNUMBER($A$2:$A$9))),0)),"")
    
    Thank you in the event of a reply!
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-11324)
    
11.  Wonderfully helpful — thank you. The way you’ve structured your explanation is excellent; you’ve communicated the information with great clarity.
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-11299)
    
12.  This only appears to work if the range is a text range rather than text returned from a formula. If the range is cells with formulas it appears to sort the blank or zeros at the top rather than the bottom. Is there a way to sort this?
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-11187)
    
13.  I used your final formula (no helpers) but my data comes out at the bottom of my column and not at top. HELP
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-11018)
    
14.  Hi,
    
    How would you work the above solution if there were names (first name and Surname of a person)?  
    For example:  
    David Li  
    Matthew McLennan  
    Darren Findlay  
    Ben Maddahi  
    David Currie
    
    None of the above methods seem to work (I am getting the rank formula value as 0)
    
    Could you help me with this?
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-10818)
    
15.  to handle duplicates, I just add the row number divided by a huge number to the rank. So, something like =A4+row()/1000000000. This will make every rank unique.
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-10817)
    
16.  I need to sort a names list alphabetically, primarily by the last name, together with the first name and a student number. I obviously want the first name and student number to match up to the last name after sorting. Is there are a way to set this up automatically so that as I paste raw data into 3 columns – LAST NAME, FIRST NAME, STUDENT NUMBER, 3 formula columns will fill-up automatically with the sorted data?
    
    I have 100’s of students to sort this way each term and repeatedly using the “sort” function is tedious.
    
    Thank you
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-10390)
    
17.  Thank You!!
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-10382)
    
18.  How can I get the following formula to ignore cells which has a formula in, but appear blank?
    
    \=INDEX($A$2:$A$9,MATCH(ROWS($A$2:A2),COUNTIF($A$2:$A$9,”<="&$A$2:$A$9),0))
    
    Even better would be a formula that removes duplicates and sort the data alphabetically. This source data is text only.
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-10294)
    
19.  Two things:  
    1 – The “One formula to sort if all” did not work for me as written. I had to make an edit:  
    “–ISBLANK” I had to change to “COUNTBLANK” and then it worked fine.
    
    2 – Duplicates still appear in the result column. How can I have it remove duplicates in the result column?
    
    Thank you!
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-9997)
    
    *   Thanks Paul this worked a treat
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-10811)
        
    *   Changing -ISBLANK to “COUNTBLANK” worked perfectly for me as my table had formulas resulting in some cells =””, which are not true blank values, Thanks!
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-13480)
        
20.  Hi Sumit. The forumala doesnt seem to work for me :/ When i click enter it become N/A. At the bottom it says ciruclar reference 🙁 can you please help?
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-9844)
    
21.  Hi i have the below formula, but it appear 0 in the cell, how can i make the cell in blank in adjusting formula.  
    Thank you for your help.
    
    \=IF(ISERROR(INDEX(‘Oct-Dec2017’!$B$3:$V$350,SMALL(IF(‘Oct-Dec2017’!$B$3:$B$392=MID(CELL(“filename”,X1),FIND(“\]”,CELL(“filename”,X1))+1,256),ROW(INDIRECT(“$1:$”&COUNTA(‘Oct-Dec2017′!$B$3:$B$392)))),ROW(1:1)),MATCH(C$3,’Oct-Dec2017’!$B$3:$V$3,0))),””,INDEX(‘Oct-Dec2017’!$B$3:$V$392,SMALL(IF(‘Oct-Dec2017’!$B$3:$B$392=MID(CELL(“filename”,X1),FIND(“\]”,CELL(“filename”,X1))+1,256),ROW(INDIRECT(“$1:$”&COUNTA(‘Oct-Dec2017′!$B$3:$B$392)))),ROW(1:1)),MATCH(C$3,’Oct-Dec2017’!$B$3:$V$3,0)))
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-9829)
    
22.  Beautiful
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-9589)
    
23.  So helpful Sumit! This works great. I am using this to alphabetize a dynamic personnel list. But when two people have the same last name, the first person shows up twice and the second person is lost. Of course it takes another level of checking (first name will do). Any advice?
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-9502)
    
    *   Never mind Sumit, I got it! Thanks anyway.
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-9503)
        
24.  trying to get a range of cells to change AUTOMATICALLY together by the last date and arranging from oldest to newest date. (i.g. pallet total – row number – product date.)
    
    50 A5 15/02/2017 stating something like this  
    10 B3 15/01/2017  
    178 A10 1/01/2017
    
    178 A10 1/01/2017 and ending like so  
    10 B3 15/01/2017  
    50 A5 15/02/2017
    
    I would think some sort of an array but any help would be most appreciated.
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-9415)
    
25.  Well done, Sumit! Until I consulted your well-written article the only way I had thought of to sort a table column without using the Sort command was to use a pivot table (which still requires a refresh if the contents of the source column change). I had also tried using conditional formatting to warn the user that the column was no longer sorted, but conditional formatting rules break easily when you move the contents around. I assume your solution works with Excel tables and will find out shortly. Also glad to see someone else uses the =index(match(…)) combination, which I find more reliable than vlookup and lookup.
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-9141)
    
    *   Actually, I needed to sort a two-column list, and borrowing your approach I couldn’t find a way to do it without using a helper column. Have you figured out a way? Here’s an example:  
        Letter Number  
        B 3  
        A 7  
        A 5  
        B 8  
        A 4  
        B 7
        
        Sort the above list in order of Letter and Number so that it looks like this:  
        Letter Number  
        A 4  
        A 5  
        A 7  
        B 3  
        B 7  
        B 8
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-9154)
        
26.  Hi Sumit, Thank you for posting such a fantastic tutorial. I needed an array like this to sort data from one source into another, and the “One Formula to Sort it All (without Helper Columns)” solution was perfect once adapted.
    
    One thing though, could you show me how to add a conditional filter to the match?
    
    I have a sorting array (thank you ) in “Sheet 2” that works perfectly to grab unsorted data from column “E” in the sheet “Level 4”, and then it sorts the data, drops any blanks and returns a list sorted by “Last Name”. What I need to add to this array formula is the filtering of data based on the “City” in column “G”.
    
    Here is my amended version of your formula:
    
    \=IFERROR(INDEX(‘Level 4’!$C$2:$G$110,MATCH(SMALL(NOT(‘Level 4’!$E$2:$E$110=””)\*IF(ISNUMBER(‘Level 4’!$E$2:$E$110),COUNTIF(‘Level 4’!$E$2:$E$110,”<="&'Level 4'!$E$2:$E$110),COUNTIF('Level 4'!$E$2:$E$110,"<="&'Level 4'!$E$2:$E$110)+SUM(–ISNUMBER('Level 4'!$E$2:$E$110))),ROWS('Level 4'!$E$2:$E2)+SUM(–ISBLANK('Level 4'!$E$2:$E$110))),NOT('Level 4'!$E$2:$E$110="")\*IF(ISNUMBER('Level 4'!$E$2:$E$110),COUNTIF('Level 4'!$E$2:$E$110,"<="&'Level 4'!$E$2:$E$110),COUNTIF('Level 4'!$E$2:$E$110,"<="&'Level 4'!$E$2:$E$110)+SUM(–ISNUMBER('Level 4'!$E$2:$E$110))),0),3),"")
    
    This is what the unsorted data looks like on the "Level 4" sheet:
    
                C          |          D           |           E           |    F    |   G  
    ——————————————————————-  
    1|   id number   |  First Name    |   Last Name   |  N/A  |  City
    
    Where do I start?
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-4000)
    
    *   I’ve tried to carry on, but I am thoroughly stuck. I have changed the formula as follows, and although it picks up the first match correctly, it doesn’t parse through the data to give any other matches, just the same one over and over again.
        
        \=IFERROR(INDEX(‘Level 4’!$C$2:$G$110,MATCH(SMALL(–NOT(‘Level 4’!$G$2:$G$110=”Rome”)\*NOT(‘Level 4’!$E$2:$E$110=””)\*IF(ISNUMBER(‘Level 4’!$E$2:$E$110),COUNTIF(‘Level 4’!$E$2:$E$110,”<="&'Level 4'!$E$2:$E$110),COUNTIF('Level 4'!$E$2:$E$110,"<="&'Level 4'!$E$2:$E$110)+SUM(–ISNUMBER('Level 4'!$E$2:$E$110))),ROWS('Level 4'!$E$2:$G2)+SUM(–ISBLANK('Level 4'!$E$2:$E$110))),–NOT('Level 4'!$G$2:$G$110=Key!$G$6)\*NOT('Level 4'!$E$2:$E$110="")\*IF(ISNUMBER('Level 4'!$E$2:$E$110),COUNTIF('Level 4'!$E$2:$E$110,"<="&'Level 4'!$E$2:$E$110),COUNTIF('Level 4'!$E$2:$E$110,"<="&'Level 4'!$E$2:$E$110)+SUM(–ISNUMBER('Level 4'!$E$2:$E$110))),0),3),"")
        
        Help! I'm spiraling into excel hell!
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-4020)
        
        *   Sumit, please help. You wrote this formula. If anyone can solve this, it’s you!
            
            [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-4025)
            
            *   Sorry for a late response. Can you please share the example file (email at [sumitbansal@trumpexcel.com](mailto:sumitbansal@trumpexcel.com)
                )
                
                [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-8534)
                
27.  Sumit even i am facing same problem as prachi. can you share the sheet you have shared with prachi. Prob by prachi was:  
    Hi..I am trying to use this formula but am facing a problem. My datasheet is different as i have a list of names and the scores against it ( which obviously will have duplicates). I have arranged that using helper 1 in a new column. If I use this formula, the same name gets repeated for the same score. Please help with this problem. Am stuck at this since 4 days now. Thanks in advance.
    
    Please help
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-3916)
    
    *   Hey Abhishek.. Here is the file shared with prachi – [https://www.dropbox.com/s/3vgxpqpowi00q2m/Sort%20Scores\_For%20Prachi.xlsx?dl=0](https://www.dropbox.com/s/3vgxpqpowi00q2m/Sort%20Scores_For%20Prachi.xlsx?dl=0)
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-4009)
        
28.  Hi- first, you are brilliant- and this formula saved me! But, I have a question…I need the associated data in the other columns to sort WITH my “Client Name” column which I want auto-sorted in Alphabetic order so that I can add Clients without having to manually sort each time. So, for example, I have “Client Originator” and “Client Owner” that is associated with each client. When they auto sort, the Originator and Owner info needs to sort too. Help! Many thx in advance.
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-3785)
    
    *   The better way would be to sort one column only, and based on the sorted data, use VLOOKUP to fetch all the remaining records.
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-8533)
        
29.  Hi Sumit, can you help me to have a formula for the automatic removal of the duplicate in one colum, appreciate your help. thanks
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-3510)
    
30.  Hi can someone help me, is there a formula for automatic remove duplicates
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-3509)
    
    *   Hello Jeh.. Have a look at this: [https://trumpexcel.com/unique-items-from-a-list-in-excel/](https://trumpexcel.com/unique-items-from-a-list-in-excel/)
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-8532)
        
31.  Really a great contribution. Helps a lot. Many thanks indeed.
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-3496)
    
32.  Hello,
    
    What if I want to sort cells with on Column A which greater than zero on Column C?
    
    Apple 1  
    Orange 1  
    Pear 0  
    Watermelon 2  
    Result:  
    Apple 1  
    Orange 1  
    Watermelon 2
    
    Is it possible to sort it with a simple formula but not array?  
    Many thank!
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-3480)
    
33.  This works great in the first 30-40 columns, but if I try to use it in column AW for example, it doesn’t work. Any reason for that?
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-3299)
    
34.  Hey Sumith . Can u just help me in arranging from descending order? I kinda modified the formula but dint work!
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-3199)
    
35.  Hi, great formula but I am having some difficulties. The blanks in my data set appear after the last number in the data set therefore when I apply the formula the blanks appear at the top of my sorted list. Is there a method to make these appear below the numbers in the sorted list? Much appareciated!
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-2551)
    
    *   Hello Arlen, I tried replicating what you mentioned here and the blanks were at ṭhe bottom. Have a look at image below
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-2553)
        
        *   Yes! that’s exactly what I need. Thanks … could you provide a solution please?
            
            [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-2560)
            
            *   Use the download file in the tutorial. You’ll get this in the second tab of the workbook.
                
                [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-8535)
                
        *   This formula is awesome! Can you share how you get the spaces to appear at the bottom?
            
            [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-7905)
            
            *   Have a look at the download file (second tab)
                
                [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-8536)
                
36.  I am trying to sort my data that has been pasted into a spread sheet that will transpose to another sheet and place the names in alphabetic order.
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-2187)
    
    *   Hello James, you can use the TRANSPOSE function to do this.
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-2554)
        
37.  Hi..I am trying to use this formula but am facing a problem. My datasheet is different as i have a list of names and the scores against it ( which obviously will have duplicates). I have arranged that using helper 1 in a new column. If I use this formula, the same name gets repeated for the same score. Please help with this problem. Am stuck at this since 4 days now. Thanks in advance.
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-2137)
    
    *   Hello Prachi, have a look at this file – [https://www.dropbox.com/s/3vgxpqpowi00q2m/Sort%20Scores\_For%20Prachi.xlsx?dl=0](https://www.dropbox.com/s/3vgxpqpowi00q2m/Sort%20Scores_For%20Prachi.xlsx?dl=0)
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-2139)
        
        *   This is really awesome. Worked perfectly. Can you please explain what was the first row about? Thanks a ton
            
            [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-2142)
            
        *   SUMIT EVEN I AM FACING SAME PROBLEM LIKE PRACHI. CAN YOU SHARE THE DATA
            
            [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-3914)
            
38.  Hey Sumit bhai you did a awesome job…. i have also made a formula …..
    
    \=IFERROR(INDEX($A$1:$A$15,MATCH(SMALL(IF(ISTEXT($A$1:$A$15),COUNTIF($A$1:$A$15,”<="&$A$1:$A$15)\*15^2,IF(ISNUMBER($A$1:$A$15),COUNTIF($A$1:$A$15,"<="&$A$1:$A$15))),ROW(1:1)),IF(ISTEXT($A$1:$A$15),COUNTIF($A$1:$A$15,"<="&$A$1:$A$15)\*15^2,IF(ISNUMBER($A$1:$A$15),COUNTIF($A$1:$A$15,"<="&$A$1:$A$15))),0)),"")
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1997)
    
39.  NICE.
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1969)
    
    *   Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1970)
        
        *   Shortcut for Referencing Ranges  
            A shortcut is available when referencing ranges. The shortcut uses square brackets, as shown in Table .  
            Shortcuts for Referencing Ranges  
            Standard Method ShortcutRange  
            (“D5”) \[D5\]  
            Range(“A1:D5”) \[A1:D5\]  
            Range(“A1:D5, G6:I17”) \[A1:D5, G6:I17\]  
            Range(“MyRange”) \[MyRange\]
            
            [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1971)
            
40.  Thanks so much
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1900)
    
41.  Thats a great tip indeed.. it really works for me, although I had to put lot of mind to understand it.
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1899)
    
    *   Thanks Sukarno.. Glad it worked for you 🙂
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1902)
        
42.  Its very helpful tip , Thanks Sumit
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1761)
    
    *   Thanks Raghu.. Glad you found it helpful 🙂
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1901)
        
43.  Real world utility? I would guess it is good for feeding in a NamedRange for Data Validation, so that you validating list always come in sorted order. What you say?
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1758)
    
    *   Thanks for commenting. Named range + Data validation would make an amazing use of it. It can also be used to get the sorted data in another location/worksheet (in case of employee names or any types of Ids). I got this query from a friend who wanted to sort id names and numbers using a formula.
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1759)
        
44.  very clear and helpful… thank you Sumit!
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1753)
    
    *   Thanks for commenting Hubert.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1757)
        
45.  Wow, thanks for this amaizing exemple!!! I have had really needed it.
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1752)
    
    *   Thanks for commenting Oana.. This type of dynamic sorting helps save a lot of time. Glad you find it useful
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1756)
        
46.  Great tip, thanks
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1751)
    
    *   Thanks for commenting Pierre.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1755)
        
47.  Nice
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1750)
    
    *   Thanks for commenting Dhiraj.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1754)
        
48.  A bit complicated but the formulas help – Thanks
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1748)
    
    *   Thanks for commenting Rose. I know the final formula is a bit too much to handle. But I have tried making it robust to handle all situations (numbers, text, duplicates and blanks).
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1749)
        
49.  Great tip! I don’t understand the big formula in the end, but it seems to do the trick! I am using it going forward. Thanks for sharing
    
    [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1745)
    
    *   Thanks for commenting Ryan! Glad it works for you.
        
        [Reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#comment-1746)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/#respond)

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