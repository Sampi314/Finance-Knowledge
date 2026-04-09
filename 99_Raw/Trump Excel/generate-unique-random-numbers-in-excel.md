# How to Generate Unique Random Numbers in Excel

**Source:** https://trumpexcel.com/generate-unique-random-numbers-in-excel

---

[Skip to content](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#below-title)

I was going through the questions on the [Microsoft Excel Community](http://answers.microsoft.com/en-us/office/forum/excel?tab=Threads)
, and one of the questions was on generating random numbers in Excel between 1 to 10, where none of the numbers repeat (i.e., there are no duplicates).

My first instinct was to use the [RANDBETWEEN](https://trumpexcel.com/excel-randbetween-function/)
 function.

I did a quick check with some random data in Excel, and it failed me – there were repetitions in the results.

Here is what I got when I used the RANDBETWEEN function:

![Generate Unique Random Numbers in Excel - Using Randbetween](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20279'%3E%3C/svg%3E)

So, I had to resort to the [RAND](https://trumpexcel.com/excel-rand-function/)
 function.

It works well with a negligible probability of the numbers repeating (I tested it multiple times on more than 100,000 cells, and there were no repetitions.

If you are generating a lot of random numbers, you can test it once).

Generating a Set of Unique Random Numbers in Excel
--------------------------------------------------

Here is how you can use the RAND function to generate a set of unique random numbers in Excel:

1.  In a column, use =RAND() formula to generate a set of random numbers between 0 and 1.
2.  Once you have generated the random numbers, [convert it into values](https://trumpexcel.com/convert-formulas-to-values-excel/)
    , so that it won’t recalculate again and again to make your workbook slow.![Unique Random Numbers in Excel - RAND function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20313%20221'%3E%3C/svg%3E)
3.  In the adjacent column, use the following [RANK](https://trumpexcel.com/excel-rank-function/)
     formula and copy/drag for other cells (here I have used it for 10 numbers only, hence A2:A11. You can adjust the range accordingly).  
    \=RANK(A2,$A$2:$A$11)![Unique Random Numbers in Excel - RANK function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20320%20224'%3E%3C/svg%3E)
4.  That’s it. You would have a list of random numbers from 1 to 10, and none of the numbers would repeat.

_**NOTE:** Remember to convert cells with RAND function from formula to values, else it will recalculate and change the list of Random Numbers every time you change anything in the workbook._

**Caution:** While I checked and didn’t find repetitions in the result of the RAND function, I still recommend you check once you have generated these numbers. You can use [Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
 to highlight duplicates or use the [Remove Duplicate](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
 option to get rid of it.

Do you use any other technique to generate random numbers with no duplicates?

Let me know in the comments section.

**You May Also Like the Following Excel Tutorials:**

*   [Automatically Sort Data in Alphabetical Order using Formula](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/)
    .
*   [Random Group Generator Template](https://trumpexcel.com/random-group-generator-template/)
    .
*   [Change Negative Number to Positive in Excel \[Remove Negative Sign\]](https://trumpexcel.com/change-negative-to-positive-in-excel/)
    
*   [How to Stop Excel from Changing Numbers to Dates Automatically](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/)
    
*   [How to Shuffle a List of Items/Names in Excel? 2 Easy Formulas!](https://trumpexcel.com/shuffle-list-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

17 thoughts on “How to Generate Unique Random Numbers in Excel (No Duplicates)”
-------------------------------------------------------------------------------

1.  Another approach: =SORTBY(SEQUENCE(Count,1,FirstNumber,Increment),RANDARRAY(Count,1,0,1,FALSE))
    
    Note: replace “Count” with your upper limit, “FirstNumber” with our lower limit and “Increment” with your increment.
    
    [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-38068)
    
2.  I think RANK now contains a tiebreaker argument so you can guarantee a perfect set of unique numbers with your method.
    
    [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-14102)
    
3.  Only way I found out to do this with zero chance of it repeating was with VBA…your solution probably will work if you’re only doing 10 or something like that.
    
    If it doesn’t, you need to generate a random number, fill it in to the array, and for each next random figure you generate, check to see if it matches any figure in the array; if it does, generate a new number, if it doesn’t, store it and go to the next in the array.
    
    [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-10379)
    
    *   I tested with 50,000 numbers and there is no repetition
        
        [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-11031)
        
4.  To me, this is a very elegant solution that should work well more than 99% of the time. Thanks!
    
    [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-8775)
    
5.  Hello, I need to know, how I can pick random unique no. in my excel. e.g. I have 2000 account and I need 100 account randomly. When I click one button. Highly appreciate your prompt response.
    
    [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-8482)
    
    *   You want to select random records with a click. That would need VBA. Another way could be use randbetween function in a column and then sort the data based on it. Then you can select first 100 records and those would be random.
        
        [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-8494)
        
6.  Another way to do this is join the result of 2/3 of function’s result using “&” sign. This will give more probability of getting unique numbers.
    
    [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-3900)
    
7.  Sir, i have 1 to 10 numbers in column “A” as A1:A10. Then i want 1 number in B1 in one click, then 2 number in B1 in next click, then 3, then 4,…..then 10. But after 10 i want 1 numer in next click.  
    Is it possible in excel please reply me.
    
    [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-2848)
    
    *   Hi Bhimrao,
        
        try this macro (leave first cell blank (means take A2:A11 rather A1:10) and select B2 cell and run the macro)
        
        Sub SerNum3()
        
        If ActiveCell.Offset(-1, 0).Value < 10 Then
        
        ActiveCell.Value = ActiveCell.Offset(-1, 0).Value + 1
        
        ActiveCell.Offset(1, 0).Select
        
        Else
        
        ActiveCell.Value = 1
        
        ActiveCell.Offset(1, 0).Select
        
        End If
        
        End Sub
        
        Regards  
        Hareesh
        
        [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-3298)
        
        *   Dear Sir, you give me answer but when we run macro then only in B2 cell  
            I have 1, then 2, then 3,…..then 10  
            and after 10 i have reapet from 1, then 2, then 3,…..then 10  
            again 1 to 10  
            again 1 to 10 only in B2 cell
            
            [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-3304)
            
            *   Hi Bhimrao,
                
                what i understood is “for every click excel has to display 1 to 10 numbers and after 10 it is again 1,2,3……..10.
                
                when i checked with same macro it is running as said above.
                
                please send a excel sheet (explaining u r requirement) to my mail “hareesh.nalubolu@gmail.com  
                i will try to get the answer
                
                regards  
                Hareesh
                
                [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-3309)
                
8.  This is how I do it (same principle)
    
    1\. Fill a range of cells with ascending numbers (unique for example: 1,2,3,4…)
    
    2.The fill an adjacent range of cells with randomly generated numbers using RANDBETWEEN
    
    3\. Sort the entire range by the second column of random numbers. You will now have unique random numbers.
    
    [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-1654)
    
9.  There is a chance that the RAND numbers will contain a repetition. Thus their RANK would repeat.  
    Regards  
    Brian
    
    [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-1626)
    
    *   Hi Brian.. It should work fine on small data sets. I did some testing on large data sets as well and it came clean. But yes, as I mentioned in the article, there is still a chance, and it is good to check it once
        
        [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-1627)
        
        *   My trick is to put the numbers you want to randomize in column A put the rand function beside them in column B then sort by column B.. Even if there might be a duplicate inColumn b column a will have none.
            
            [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-1629)
            
            *   Good trick.. Thanks for sharing. It is a fine approach when you want the random numbers once. If you need to randomize again, you will have to sort it again.
                
                [Reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#comment-1630)
                

### Leave a Comment [Cancel reply](https://trumpexcel.com/generate-unique-random-numbers-in-excel/#respond)

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