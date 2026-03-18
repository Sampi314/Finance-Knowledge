# How to Get the Word Count in Excel (Using Simple Formulas)

**Source:** https://trumpexcel.com/word-count-in-excel

---

[Skip to content](https://trumpexcel.com/word-count-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/word-count-in-excel/#below-title)

Want to get the word count in Excel? Believe it or not, Excel does not have an inbuilt word counter.

But don’t worry.

A cool bunch of [excel functions](https://trumpexcel.com/excel-functions/)
 (or a little bit of VBA if you’re feeling fancy) can easily do this for you.

In this tutorial, I will show a couple of ways to count words in Excel using simple formulas. And at the end, will also cover a technique to create a custom formula using VBA that will quickly give you the word count of any text in any cell.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/word-count-in-excel/#)

Formula to Get Word Count in Excel
----------------------------------

Before I give you the exact formula, let’s quickly cover the logic to get the word count.

Suppose I have a sentence as shown below for which I want to get the word count.

![Word Count in Excel - formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20358%2070'%3E%3C/svg%3E)

While Excel cannot count the number of words, it can count the number of spaces in a sentence.

So to get the word count, we can count these spaces instead of words and add 1 to the total (as the number of space would be one less the number of words).

Now there can be two possibilities:

1.  There is a single space between each word
2.  There are multiple spaces between words.

So let’s see how to count the total number of words in each case.

### Example 1 – When there is a single space between words

Let’s say I have the following text in cell A1: Let the cat out of the bag

![Word Count in Excel - formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20358%2070'%3E%3C/svg%3E)

To count the number of words, here is the formula I would use:

\=LEN(A1)-LEN(SUBSTITUTE(A1," ",""))+1

This would return ‘7’ as a result.

Here is how this formula works:

*   _LEN(A1)_ – This part of the formula returns 26, which is the total number of characters in the text in cell A1. It includes the text characters as well as the space characters.
*   SUBSTITUTE(A1,” “,””) – This part of the formula removes all the spaces from the text. So the result, in this case, would be **Letthecatoutofthebag**.
*   _LEN(SUBSTITUTE(A1,” “,_“”_)_ – This part of the formula [counts the total number of characters](https://trumpexcel.com/count-characters-in-excel/)
     in the text that has no spaces. So the result of this would be 20.
*   _LEN(A1)-LEN(SUBSTITUTE(A1,” “,_“”_))_ – This would subtract the text length without spaces from the text length with spaces. In the above example, it would be 26-20 which is 6.
*   _\=LEN(A1)-LEN(SUBSTITUTE(A1,” “,_“”_))+1_ – We add 1 to the overall result as the total number of spaces is one less than the total number of words. For example, there is one space in two words and two spaces in three words.

![Get Word Count in Excel - Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20730%20293'%3E%3C/svg%3E)

Now, this works well if you have only one space character between words. But it wouldn’t work if you have more than one space in between words.

In that case, use the formula in the next example.

### Example 2: When there are multiple spaces between words

Let’s say you have the following text: Let the cat   out of    the bag

![Word Count in Excel - multiple spaces](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20364%2074'%3E%3C/svg%3E)

In this case, there are multiple space characters between words.

To get the word count, we first need to remove all the extra spaces (such that there is only one space character between two words) and then count the total number of spaces.

Here is the formula that will give us the right number of words:

\=LEN(TRIM(A1))-LEN(SUBSTITUTE(A1," ",""))+1

This is a similar formula used in the above example, with a slight change – we have also used the [TRIM function](https://trumpexcel.com/excel-trim-function/)
 here.

Excel TRIM function removes any [leading, trailing, and extra spaces](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
 (except single spaces between words).

The rest of the formula works the same (as explained in Example 1).

![Get Word Count in Excel - Example 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20730%20298'%3E%3C/svg%3E)

_Note: If there are no spaces between words, it is considered as one word._

Using VBA Custom Function to Count Words in Excel
-------------------------------------------------

While the above formulas work great, if you have a need to calculate the word count often, you can use VBA to create a custom function (also called a [User Defined Function](https://trumpexcel.com/user-defined-function-vba/)
).

The benefit of using a custom function is that you can create it once and then use it like any other regular Excel function. So instead of creating a long complex formula as we did in the two examples above, you have a simple formula that takes the cell reference and instantly gives you the word count.

Here is the code that will create this custom function to get the word count in Excel.

Function WordCount(CellRef As Range)
Dim TextStrng As String
Dim Result() As String
Result = Split(WorksheetFunction.Trim(CellRef.Text), " ")
WordCount = UBound(Result()) + 1
End Function

Once created, you can use the WordCount function just like any other regular Excel function.

![Custom Function Created with VBA to get the word count in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20461%20198'%3E%3C/svg%3E)

In the above code for the custom function, I have used the worksheet TRIM function to remove any leading, trailing, and double spaces in between words. This ensures that all the three cells give the same result, as only the words are counted and not the double spaces.

**How this formula works:**

The above VBA code first uses the TRIM function to remove all the leading, trailing and double spaces from the text string in the referenced cell.

Once it has the cleaned string, it uses the SPLIT function in VBA to split the text string based on the delimiter, which we have specified to be the space character. So each word is separated as stored as a separate item in the Result variable.

We then use the UBOUND function to count the total number of items that got stored in the Result variables. Since VBA has a base of 0, we need to add 1 to get the total number of words.

This means that Result(0) stores the first word, Result(1) stores the second word, and so on. Since this counting starts from 0, we need to add 1 to get the real word count.

**Where to Put this Code?**

When creating a custom function, you need to put the code in the [VB Editor](https://trumpexcel.com/visual-basic-editor/)
 of the workbook (which is the back end of the workbook where you can write code to automate tasks and create custom functions).

Below are the steps to put the code for the ‘GetNumeric’ function in the workbook.

1.  Go to the Developer tab.![Word Count in Excel - Ribbon for Developer Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20708%20162'%3E%3C/svg%3E)
2.  Click on Visual Basic option. This will open the VB editor in the backend.![Click on Visual Basic button in the Excel ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20708%20162'%3E%3C/svg%3E)
3.  In the Project Explorer pane in the VB Editor, right-click on any object for the workbook in which you want to insert the code. If you don’t see the Project Explorer go to the View tab and click on Project Explorer.
4.  Go to Insert and click on Module. This will insert a module object for your workbook.![Saving a Custom Function code in the module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20497%20420'%3E%3C/svg%3E)
5.  Copy and paste the code in the module window.

Once you have copied the code in the code window, you can go back to your worksheet and use this function just like any other regular Excel function.

Just type **\=Word** and it will show you the formula in the list.

![VBA Custom Formula shows up in Worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20198'%3E%3C/svg%3E)

It takes one argument, which is the cell reference and instantly gives you the word count in it.

**You May Also Like the Following Excel Tutorials:**

*   [How to Count Cells that Contain Text Strings](https://trumpexcel.com/count-cells-that-contain-text/)
    .
*   [Using Multiple Criteria in Excel COUNTIF and COUNTIFS Function](https://trumpexcel.com/multiple-criteria-in-excel-countif/)
    .
*   [How to Add Leading Zeroes in Excel](https://trumpexcel.com/add-leading-zeroes-excel/)
    .
*   [Remove Spaces in Excel – Leading, Trailing, and Double](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
    .
*   [How to Extract the First Word from a Text String in Excel](https://trumpexcel.com/extract-first-word-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

9 thoughts on “How to Get the Word Count in Excel (Using Simple Formulas)”
--------------------------------------------------------------------------

1.  thank you finally my problem is resolved
    
    [Reply](https://trumpexcel.com/word-count-in-excel/#comment-31211)
    
2.  Thanks very much. If you use this across a range that includes blank cells you can use this =IF(ISBLANK(A1),0,LEN(TRIM(A1))-LEN(SUBSTITUTE(A1,” “,””))+1)
    
    [Reply](https://trumpexcel.com/word-count-in-excel/#comment-14405)
    
3.  nice and very usefull
    
    [Reply](https://trumpexcel.com/word-count-in-excel/#comment-13564)
    
4.  thanks for nicely explained for word count .  
    please can you make clear your ref.38 in count by colour .
    
    [Reply](https://trumpexcel.com/word-count-in-excel/#comment-13463)
    
5.  Let the cat out of the bag  
    after applied  
    output is 1  
    this is not correct
    
    [Reply](https://trumpexcel.com/word-count-in-excel/#comment-13085)
    
    *   I just checked all the formulas and the code. Working fine at my end. Which formula did you use and what was the text in the cell?
        
        [Reply](https://trumpexcel.com/word-count-in-excel/#comment-13086)
        
6.  I don’t get it – “Let the cat out of the bag” is 7 words… how do you get a result of 9?
    
    [Reply](https://trumpexcel.com/word-count-in-excel/#comment-10955)
    
    *   I guess he actually got this count with “The quick…lazy dog” sentence but somehow made a mistake while making the screen shot or something like that
        
        [Reply](https://trumpexcel.com/word-count-in-excel/#comment-11922)
        
        *   Horrible miss on my part. I have corrected the code and it should work fine.
            
            [Reply](https://trumpexcel.com/word-count-in-excel/#comment-11923)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/word-count-in-excel/#respond)

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