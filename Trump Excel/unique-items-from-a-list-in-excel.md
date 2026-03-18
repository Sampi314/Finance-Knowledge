# How to Get Unique Items from a List in Excel Using Formulas

**Source:** https://trumpexcel.com/unique-items-from-a-list-in-excel

---

[Skip to content](https://trumpexcel.com/unique-items-from-a-list-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/unique-items-from-a-list-in-excel/#below-title)

In this blog post, I will show you a formula to get a list unique items from a list in excel that has repetitions. While this can be done using [Advanced Filter](https://trumpexcel.com/excel-advanced-filter/)
 or [Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
, the benefit of using a formula is that it makes your unique list dynamic. This means that you continue to get a unique list even when you add more data to the original list.

![Get Unique Items from a List in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20295%20235'%3E%3C/svg%3E)

##### Get Unique Items from a List in Excel Using Formulas

Suppose you have a list as shown above (which has repetitions) and you want to get unique items as shown on the right.

Here is a combination of [INDEX](https://trumpexcel.com/excel-index-function/)
, [MATCH](https://trumpexcel.com/excel-match-function/)
 and [COUNTIF](https://trumpexcel.com/excel-countif-function/)
 formulas that can get this done:

\=IFERROR(INDEX($A$2:$A$11,MATCH(0,COUNTIF($C$1:C1,$A$2:$A$11),0)),"")

##### **How it works**

![Get Unique Items from a List in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201319%20394'%3E%3C/svg%3E)

When there are no more unique items, the formula displays an error. To handle it, I have used the [Excel IFERROR function](https://trumpexcel.com/excel-iferror-function/)
 to replace the error message with a blank.

Since this is an array formula, **use Control + Shift + Enter** instead of Enter.

This is a smart way to exploit the fact that MATCH() will always return the first matching value from a range of values. For example, in this case, MATCH returns the position of the first 0, which represents the first non-matching item.

I also came up with another formula that can do the same thing (its longer but uses a smart MATCH formula trick)

\=IFERROR(INDEX($A$2:$A$11,SMALL(MATCH($A$2:$A$11,$A$2:$A$11,0), SUM((COUNTIF($A$2:$A$11,$C$1:C1)))+1)),"")

I will leave it for you to decode. This is again an array formula, so use Control + Shift + Enter instead of Enter.

In case you come up with a better formula or a smart trick, do share it with me.

##### Related Tutorials:

*   [The Ultimate Guide to Find and Remove Duplicates in Excel.](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

24 thoughts on “How to Get Unique Items from a List in Excel Using Formulas”
----------------------------------------------------------------------------

1.  How can I do this without using Array Formulas? It is now slowing down my data sheet with only over 180 rows
    
    [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-14855)
    
2.  This Formular returns always 0. What do I do wrong? Where do I use CTRL+Shift+Enter? Why?
    
    [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-12483)
    
3.  Great post. How would the formula look if you were wanting to do the same thing (Return a list of unique values) but with the data sourced from across 2 or more columns????
    
    [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-11907)
    
4.  This formula is not working for me, I always get ‘0’, I have dragged the formula to columns by double clicking the + sign
    
    [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-11532)
    
5.  Hai sumit, This formula is ok for small data sets but if we need to work with a huge data set i want to know how to use the unique values generated from a pivot table in excel forumlas and functions.
    
    [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-10299)
    
6.  But isn’t Pivot Table can do the same job easier
    
    [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-8459)
    
    *   It can, but Pivot table is not dynamic so you need to refresh it every time there is a change in the back-end data.
        
        [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-8508)
        
7.  In which cell this formula will go?
    
    [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-3675)
    
    *   In this example, the formula is in C2:C11
        
        [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-8509)
        
8.  In which cell this formula will go?
    
    [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-3674)
    
9.  Hi Sumit i’M looking for this formula quite a long time.Great work!!. Also Created a table version of this formula using structured references and working fine and would like to share this
    
    {=IFERROR(INDEX(\[Orginal List\],MATCH(0,COUNTIF(OFFSET(Unique\[\[#Headers\],\[Unique Value\]\],ROW()-1-ROW(Unique\[\[#Headers\],\[Unique Value\]\]),0,ROW(Unique\[\[#Headers\],\[Unique Value\]\])-ROW()),\[Orginal List\]),0)),””)}  
    Where Unique is the Table name and Original List ,Unique Value are its column.
    
    [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-1793)
    
    *   Hi Karthik.. Thanks for sharing the formula. It is almost always a good idea to convert data range into a table.
        
        [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-1794)
        
        *   May i Get the example excel file link for this.
            
            [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-9169)
            
10.  Hi! I have fixed the error and now the formula works well. Thanks a lot! It’s a very useful formula. But now I have two columns of data, do you know how can I combine multiple columns of data and remove the duplicates?
    
    [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-1327)
    
    *   Hi Wang.. Glad it was helpful. In your query, do you have numbers in the 2 columns, or there is a mix of numbers and alphabets.
        
        Also, can you create a helper (additional) column, copy paste this data to get it in one column and use this formula, or you looking for a dynamic formula?
        
        [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-1328)
        
        *   Hi! Thanks for your reply! Yes I have numbers in 2 columns. Right now I’m doing with a helper (additional) column, but is there a dynamic formula that can do this without copy and paste?
            
            [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-1329)
            
            *   Try this: (Assuming you have data in A2:B18)
                
                \=IFERROR(IF(ROWS($C$2:C2)<=COUNT($A$2:$B$18),INDEX($A$2:$B$18,IF(ROWS($C$2:C2)<=COUNT($A$2:$A$18),ROWS($C$2:C2),ROWS($C$2:C2)-COUNT($A$2:$A$18)),IF(ROWS($C$2:C2)<=COUNT($A$2:$A$18),1,2)),""),"")
                
                This would give you a single column list with data from both the columns (and this is dynamic)
                
                I am sure there could be a shorter way, but if this works for you, nothing like that.
                
                [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-1330)
                
                *   Thanks! I think your formula would work. But actually the data are not in two adjacent columns, meaning they are in $A$1:$A$10 and $E$1:$E$10. How should I change your formula to make it work with these two column?
                    
                *   Try this:
                    
                    \=IFERROR(IF(ROWS($C$2:C2)<=COUNT($A$2:$A$18,$E$2:$E$18),INDEX($A$2:$E$18,IF(ROWS($C$2:C2)<=COUNT($A$2:$A$18),ROWS($C$2:C2),ROWS($C$2:C2)-COUNT($A$2:$A$18)),IF(ROWS($C$2:C2)<=COUNT($A$2:$A$18),1,5)),""),"")
                    
                *   Thanks! I’ll try it out.
                    
11.  Hi! This formula is exactly what I’m looking for, but I got an error with it. I attach the screenshot here. Sorry that I’m kind of new to excel..hope you can help me solve this problem..
    
    [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-1326)
    
    *   Hello, I got the same exception. How can I fix it?
        
        [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-2505)
        
12.  Very usefull……….
    
    [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-1318)
    
    *   Thanks Ankur. Glad you found this useful
        
        [Reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#comment-1319)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/unique-items-from-a-list-in-excel/#respond)

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