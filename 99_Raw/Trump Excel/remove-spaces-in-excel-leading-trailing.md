# Remove Spaces in Excel - Leading, Trailing and Double

**Source:** https://trumpexcel.com/remove-spaces-in-excel-leading-trailing

---

[Skip to content](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/#below-title)

**Watch Video – Remove Spaces in Excel**

Leading and trailing spaces in Excel often leads to a lot of frustration. I can’t think of a situation where you may need these extra spaces, but it often finds its way into the excel spreadsheets.

There are many ways you can end up with these extra spaces – for example, as a part of the data download from a database, while copying data from a text document, or entered manually by mistake.

Leading, trailing, or double space between text could lead to a lot of serious issues.

For example, suppose you have a data set as shown below:

![How to Remove Spaces in Excel - Leading, Trailing and Double - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20253%20155'%3E%3C/svg%3E)

Now have a look at what happens when I use a [VLOOKUP](https://trumpexcel.com/excel-vlookup-function/)
 function to get the last name using the first name.

![How to Remove Spaces in Excel - Leading, Trailing and Double - Vlookup Error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20748%20164'%3E%3C/svg%3E)

You might not be able to spot the difference with the naked eye that there is an extra trailing space in the name that is causing this error.

![How to Remove Spaces in Excel - Leading, Trailing and Double - Trailing space](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20430%20160'%3E%3C/svg%3E)

In this example, it was easy to spot the issue in such a small data set, but imagine having to check this for thousands of records.

To be on the safe side, it is always a good idea to [clean your data](https://trumpexcel.com/clean-data-in-excel/)
 and remove spaces in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/#)

How to Remove Spaces in Excel
-----------------------------

In this tutorial, I will show you two ways to remove spaces in Excel.

*   Using TRIM function.
*   Using Find and Replace.

### Using the TRIM Function

[Excel TRIM function](https://trumpexcel.com/excel-trim-function/)
 removes the leading and trailing spaces, and double spaces between text strings.

For example, in the above example, to remove spaces from the entire list if first names (in A2:A7), use the following formula in cell C1 and drag it down for all the first names:

\=TRIM(A2)

Excel TRIM function would instantly remove all the leading and trailing spaces in the cell.

Once you have the cleaned data, copy it paste it as values in place of the original data.

![How to Remove Spaces in Excel - Leading, Trailing and Double - Paste as Vaues](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20300'%3E%3C/svg%3E)

This function is also helpful if you have more than one space character between words. It would remove the extra spaces such that the result always have one space character between words.

![How to Remove Spaces in Excel - Leading, Trailing and Double - space in between](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20332%20168'%3E%3C/svg%3E)

Excel TRIM function does a good job in removing spaces in Excel, however, it fails when you have non-printing characters (such as line breaks) in your data set. To remove non-printing characters, you can use a combination of TRIM and CLEAN functions.

If you have some text in cell A1 from which you want to remove spaces, use the below formula:

\=TRIM(CLEAN(A1))

Non-printing characters can also result from =CHAR(160), which can not be removed by the CLEAN formula. So, if you want to be absolutely sure that you have all the extra spaces and non-printing characters, use the below formula:

\=TRIM(CLEAN([SUBSTITUTE](https://trumpexcel.com/excel-substitute-function/)
(A1,CHAR(160)," ")))

### Remove Extra Spaces in Excel using FIND and REPLACE  

You can remove spaces in Excel using the Find and Replace functionality.

This is a faster technique and can be useful in the given situations:

*   When you want to remove double spaces.
*   When you want to remove all the space characters.

#### Removing Double Spaces

Note that this technique cannot be used to remove leading or trailing spaces. It will find and replace double spaces irrespective of its position.

Here are the steps to do this:

*   Select the cells from which you want to remove double spaces.
*   Go to Home –> Find & Select –> Replace. (You can also use the keyboard shortcut – Control + H).![How to Remove Spaces in Excel - Leading, Trailing and Double - find & replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20222%20220'%3E%3C/svg%3E)
*   In the Find and Replace dialogue box, enter:
    *   Find what: Double Space.
    *   Replace with: Single Space.![How to Remove Spaces in Excel - Leading, Trailing and Double - remove double space](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20203'%3E%3C/svg%3E)
*   Click on Replace All.![How to Remove Spaces in Excel - Leading, Trailing and Double - replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20454%20204'%3E%3C/svg%3E)

This will replace all the double spaces with a single space character.

![How to Remove Spaces in Excel - Leading, Trailing and Double - Remove double](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20496%20404'%3E%3C/svg%3E)

Note that this will only remove double spaces. If you have three space characters in between 2 words, it would result in 2 space characters (would remove one). In such cases, you can do this again to remove and any double spaces that might have been left.

#### Removing Single Spaces

To remove all the space characters in a data set, follow the below steps:

*   Select the cells from which you want to remove the space character.
*   Go to Home –> Find & Select –> Replace. (You can also use the keyboard shortcut – Control + H).![How to Remove Spaces in Excel - Leading, Trailing and Double - find & replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20222%20220'%3E%3C/svg%3E)
*   In the Find and Replace dialogue box, enter:
    *   Find what: Single Space.
    *   Replace with: Leave this blank.![How to Remove Spaces in Excel - Leading, Trailing and Double - Single space](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20451%20202'%3E%3C/svg%3E)
*   Click on Replace All.![How to Remove Spaces in Excel - Leading, Trailing and Double - replace single](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20453%20204'%3E%3C/svg%3E)

This will remove all the space characters in the selected data set.

![How to Remove Spaces in Excel - Leading, Trailing and Double - Remove Single Space](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20504%20344'%3E%3C/svg%3E)

Note that in this case, even if there are more than one space characters between two text strings or numbers, all of it would be removed.

#### Remove Line Breaks

You can also use Find and Replace to quickly [remove line breaks](https://trumpexcel.com/remove-line-break-excel/)
.

Here are the steps to do this:

*   Select the data.
*   Go to Home –> Find and Select –> Replace (Keyboard Shortcut – _Control + H_).
*   In the Find and Replace Dialogue Box:
    *   Find What: Press Control + J (you may not see anything except for a blinking dot).
    *   Replace With: Leave it empty.![How to Remove Spaces in Excel - Leading, Trailing and Double - Control J](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20451%20204'%3E%3C/svg%3E)
*   Replace All.

This will instantly remove all the line breaks from the data set that you selected.

Based on your situation, you can choose either method (formula or [find and replace](https://trumpexcel.com/find-and-replace-in-excel/)
) to remove spaces in Excel.

**You may also like the following Excel tutorials:**

*   [Find and Remove Duplicates in Excel](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
    .
*   [Separate First And Last Name In Excel](https://trumpexcel.com/separate-first-and-last-name-excel/)
    
*   [10 Super Neat Ways to Clean Data in Excel](https://trumpexcel.com/clean-data-in-excel/)
    .
*   [MS Help – Remove Space and Non-printing characters](https://support.office.com/en-us/article/Remove-spaces-and-nonprinting-characters-from-text-023f3a08-3d56-49e4-bf0c-fe5303222c9d)
    .
*   [How to Remove the First Character from a String in Excel](https://trumpexcel.com/remove-first-character-from-string/)
    
*   [How to Remove Time from Date in Excel](https://trumpexcel.com/remove-time-from-date-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

6 thoughts on “Remove Extra Spaces in Excel (Leading, Trailing, Double Spaces)”
-------------------------------------------------------------------------------

1.  Hi,  
    May you help me to trim (removal) all excess spaces in row specially if have I have data with alt+enter function (more than 1 rows) becausem if converted to word it would be have additonal paragraph including before and after word. example  
    \===================================  
    haha (2 space in last character)  
    hehe (1 space befor character)  
    (1 space blank to be remove due to no character)  
    and excess alt + enter  
    \================  
    result shall be like below:  
    \===========  
    haha  
    hehe  
    \==============
    
    [Reply](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/#comment-13255)
    
2.  how to remove space from last word  
    like 12345Space
    
    [Reply](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/#comment-12497)
    
3.  your formula ” =TRIM(CLEAN(SUBSTITUTE(A1,CHAR(160),” “)))” is WRONG!!!
    
    [Reply](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/#comment-11977)
    
4.  I want to control space (line space, in the old days-“leading”) between two lines of type within a cell. Is it possible and how to do it?
    
    [Reply](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/#comment-11450)
    
5.  Hi Sumit, thank you for your post, quick observation bro, forgive me if I have misunderstood the image. I noticed in you \*.gif explanation of VLOOKUP not being able to find “Bob”, due to the leading space.
    
    \=VLOOKUP(D2,$A$2:$B$7,2,0)
    
    Perfect example; however in your formula you refer to the 2nd column. Even if there were no leading spaces, the formula would still result in the #N/A error as “Bob” is in the 1st column. You might consider re-filming the gif to show your formula again i.e. =VLOOKUP(D2,$A$2:$B$7,1,0). Please forgive my assertion; I’m not trying to teach you to suck eggs, as I know you are a top Excel guru, just a typo. Best Josh
    
    [Reply](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/#comment-11004)
    
    *   Sumit’s formula is correct, Josh: he is wanting “to get \[Bob’s\] last name using the first name.”  
        The reason he is getting an error is because there is a \_trailing\_ space after “Bob” in A5, but not in D2.  
        He explains this.
        
        [Reply](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/#comment-11023)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/#respond)

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