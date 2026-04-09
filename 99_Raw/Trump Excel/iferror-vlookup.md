# Use IFERROR with VLOOKUP to Get Rid of #N/A Errors

**Source:** https://trumpexcel.com/iferror-vlookup

---

[Skip to content](https://trumpexcel.com/iferror-vlookup/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/iferror-vlookup/#below-title)

When using the [VLOOKUP formula](https://trumpexcel.com/excel-vlookup-function/)
 in Excel, sometimes you may end up with the ugly #N/A error. This happens when your formula can not find the lookup value.

In this tutorial, I will show you different ways to use IFERROR with VLOOKUP to handle these #N/A errors cropping up in your worksheet.

Using the combination of IFERROR with VLOOKUP allows you to show something meaningful in place of the #N/A error (or any other error for that matter).

Before getting into details on using this combination, let’s first quickly go through the [IFERROR function](https://trumpexcel.com/excel-iferror-function/)
 and see how it works.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/iferror-vlookup/#)

### IFERROR Function Explained

With IFERROR function, you can specify what should happen in case a formula or a cell reference returns an error.

Here is the syntax of the IFERROR function.

**\=IFERROR(value, value\_if\_error)**

*   **value –** this is the argument that is checked for the error. In most cases, it is either a formula or a cell reference. When using VLOOKUP with IFERROR, the VLOOKUP formula would be this argument.
*   **value\_if\_error** – this is the value that is returned if there is an error. The following error types evaluated: #N/A, [#REF!](https://trumpexcel.com/ref-error-in-excel/)
    , #DIV/0!, #VALUE!, #NUM!, #NAME?, and #NULL!.

### Possible Causes Of VLOOKUP Returning a #N/A Error

VLOOKUP function may return a #N/A error due to any of the following reasons:

1.  The lookup value is not found in the lookup array.
2.  There is a leading, trailing, or double space in the lookup value (or in the table array).
3.  There is a spelling error in the lookup value or the values in the lookup array.

You can handle all these causes of error with the combination of IFERROR and VLOOKUP. However, you should keep an eye out for cause #2 and #3, and correct these in the source data instead of letting IFERROR handle these.

Note: IFERROR would treat an error irrespective of what caused it. If you only want to treat the errors caused by VLOOKUP not being able to find the lookup value, use IFNA instead. That will make sure that errors other than #N/A are not treated and you can investigate these other errors.

You can [treat leading, trailing, and double spaces](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
 using the [TRIM function](https://trumpexcel.com/excel-trim-function/)
.

### Replacing VLOOKUP #N/A Error with Meaningful Text

Suppose you have a dataset as shown below:

![Error with VLOOKUP when lookup value not found](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20564%20366'%3E%3C/svg%3E)

As you can see that the VLOOKUP formula returns an error as the lookup value is not in the list. We are looking to get the score for Glen, which is not in the table of scores.

While this is a very small dataset, you may get huge datasets where you have to check the occurrence of many items. For every case when the value is not found, you will get a #N/A error.

Here is the formula you can use to get something meaningful instead of the #N/A error.

**\=IFERROR(VLOOKUP(D2,$A$2:$B$10,2,0),"Not Found")**

![Using IFERROR with VLOOKUP to get Not Found](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20603%20369'%3E%3C/svg%3E)

The above formula returns the text “Not Found” instead of the #N/A error. You can also use the same formula to return blank, zero, or any other meaningful text.

### Nesting VLOOKUP With IFERROR Function

In case you are using VLOOKUP and your lookup table is fragmented on the same worksheet or different worksheets, you need to check the VLOOKUP value through all of these tables.

For example, in the dataset shown below, there are two separate tables of student names and the scores.

![Nested IFERROR with VLOOKUP dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20635%20179'%3E%3C/svg%3E)

If I have to find the score of Grace in this dataset, I need to use the VLOOKUP function to check the first table, and if the value is not found in it, then check the second table.

Here is the nested IFERROR formula I can use to look for the value:

**\=IFERROR(VLOOKUP(G3,$A$2:$B$5,2,0),IFERROR(VLOOKUP(G3,$D$2:$E$5,2,0),"Not Found"))**

![Nested IFERROR with VLOOKUP](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20633%20246'%3E%3C/svg%3E)

### Using VLOOKUP with IF and ISERROR (Versions prior to Excel 2007)

IFERROR function was introduced in Excel 2007 for Windows and Excel 2016 in Mac.

If you’re using the prior versions, then IFERROR function will not work in your system.

You can replicate the functionality of IFERROR function by using the combination of the [IF function](https://trumpexcel.com/excel-if-function/)
 and the ISERROR function.

Let me quickly show you how to use the combination of IF and ISERROR instead of IFERROR.

![using IF and ISERROR - Example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20632%20107'%3E%3C/svg%3E)

In the above example, instead of using IFERROR, you can also use the formula shown in cell B3:

\=IF(ISERROR(A3),”Not Found”,A3)

The ISERROR part of the formula checks for the errors (including the #N/A error) and returns TRUE if an error is found and FALSE if not.

*   If it’s TRUE (which means that there is an error), the IF function returns the specified value (“Not Found” in this case).
*   If it’s FALSE (which means that there is no error), the IF function returns that value (A3 in the above example).

### IFERROR Vs IFNA

IFERROR treats all kinds of errors while IFNA treats only the #N/A error.

When handling errors caused by VLOOKUP, you need to make sure you’re using the right formula.

**Use IFERROR** when you want to treat all kinds of errors. Now an error can be caused by various factors (such as the wrong formula, misspelled named range, not finding the lookup value, and returning error value from the lookup table). It wouldn’t matter to IFERROR and it would replace all these errors with the specified value.

**Use IFNA** when you want to treat only #N/A errors, which are more likely to be caused by VLOOKUP formula not being able to find the lookup value.

**You May Also Find the Following Excel Tutorials Useful:**

*   [How to make VLOOKUP Case Sensitive](https://trumpexcel.com/vlookup-case-sensitive/)
    .
*   [VLOOKUP Vs. INDEX/MATCH – The Debate Ends Here!](https://trumpexcel.com/vlookup-vs-index-match/)
    
*   [Use VLookup to Get the Last Number in a List in Excel](https://trumpexcel.com/get-the-last-number-in-excel-vlookup/)
    .
*   [How to Use VLOOKUP with Multiple Criteria](https://trumpexcel.com/vlookup-with-multiple-criteria/)
    
*   [#NAME Error in Excel – What Causes it and How to Fix it!](https://trumpexcel.com/name-error-excel/)
    
*   [Using VLOOKUP From Another Sheet in VBA](https://trumpexcel.com/excel-vba/vlookup/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

17 thoughts on “Use IFERROR with VLOOKUP to Get Rid of #N/A Errors”
-------------------------------------------------------------------

1.  \=IFERROR(VLOOKUP(E3,'\[Customer Mapping.xlsx\]main’!$A$1:$C$822,3,0)),IFERROR(VLOOKUP,(E3,'\[Customer Mapping.xlsx\]main’!$A$1:$C$822,3,0)),”L1/N5″))
    
    Can you let me know the error in this message
    
    [Reply](https://trumpexcel.com/iferror-vlookup/#comment-40917)
    
2.  Very Useful
    
    [Reply](https://trumpexcel.com/iferror-vlookup/#comment-12679)
    
3.  What is the result returned by VLOOKUP when both the columns has same value (i.e., blank)?
    
    I received “#N/A” when both the source cell and target cell has no values. Can someone help me here please?
    
    thanks in advance.
    
    [Reply](https://trumpexcel.com/iferror-vlookup/#comment-11616)
    
4.  Kudos! This has been really helpful.
    
    [Reply](https://trumpexcel.com/iferror-vlookup/#comment-11476)
    
5.  \=+IFERROR(Vlookup(B2,’Customer Details’!B:C,2,0),””) why this formula not showing the result ?
    
    [Reply](https://trumpexcel.com/iferror-vlookup/#comment-11082)
    
    *   I am using excel 2010, while using the formula it is showing the correct selection in the formula but it is not displaying the area we want but it is showing the entire formula again. can you help me?
        
        [Reply](https://trumpexcel.com/iferror-vlookup/#comment-11083)
        
6.  i am using =IFNA(vlookup,0) in code but its reflected in excel as =ifna(vlookup,0) as i want value 0 where #N/A comes. because of that it gives me value as #NAME
    
    [Reply](https://trumpexcel.com/iferror-vlookup/#comment-10363)
    
7.  Thanks
    
    [Reply](https://trumpexcel.com/iferror-vlookup/#comment-9525)
    
    *   I think IFNA will be a better option rather than ISERROR
        
        [Reply](https://trumpexcel.com/iferror-vlookup/#comment-9529)
        
8.  I think it’s much better to use the IFNA function that works more or less like IFERROR, but with the really important difference that IFNA only get rid of the #N/A errors…
    
    [Reply](https://trumpexcel.com/iferror-vlookup/#comment-9522)
    
    *   Yeah, if your lookup data table doesn’t have errors, IFNA is the better choice
        
        [Reply](https://trumpexcel.com/iferror-vlookup/#comment-9523)
        
        *   No, IFNA is always the best solution with VLOOKUP, because only the #N/A are hidden, so it’s possible to detect all other errors: wrong range, wrong formula, misspelled name range and so on… With IFERROR you hide all this stuff and you cannot correct the errors…
            
            [Reply](https://trumpexcel.com/iferror-vlookup/#comment-9526)
            
            *   not always dear
                
                [Reply](https://trumpexcel.com/iferror-vlookup/#comment-9530)
                
                *   So, what do you mean? Why not always?
                    
                *   Hello Franz.. While I agree that IFNA is the better choice with VLOOKUP, it’s also dependent on the data structure and the output that decides what function should be used.
                    
                    As far as I know, IFNA is not available in 2007 and 2010 versions of Excel Windows. Instead of going the longer IF + ISNA, route, it’s easier to check the formula and make sure there are no errors in the formula or named range and go with IFERROR instead. Another example is of a recent dashboard i worked on, where the data I got itself had errors such as DIV and NA. Instead of going a 2-step process of checking with IFNA and then treating the DIV errors with IFERROR, it’s better to make sure the formula/named range is correct and then use IFERROR.
                    
                    Also, wrong range anyway returns NA error, so even IFNA wouldn’t help in that case.
                    
                    My point is, IFNA is better, but it’s not the only way to go.
                    
9.  Good post but I do have an issue with IFERROR
    
    You may also be getting an error if the range looked up is too short narrow, or if the cell value returned (legitimately) is itself an error, or if the index is negative, or if the lookup range is unsorted and the last element in the VLOOKUP is omitted, or if the lookup value is an error, or maybe mistyped a range name or …  
    What I’m getting at is that errors can occur for many reasons and defaulting the error response to “not found” may mean you’re going to overlook an incorrect formula
    
    Much better to anticipate the error (with a COUNTIF in this case) and deal with it properly
    
    IFERROR is a very dangerous thing to use in such a cavalier manner – beware
    
    jim
    
    [Reply](https://trumpexcel.com/iferror-vlookup/#comment-9520)
    
    *   Hey Jim.. I mentioned in the tutorial that there can be various reasons for errors and first it must be sorted at the data level instead of letting IFERROR handle it (covered in the ‘possible causes or error’ section).
        
        Also, the next step would always be to make sure the formula is created properly. There wouldn’t be any other way to handle misspelled named range or not having the proper data structure or not having the right lookup range, than to make sure it’s sorted in the first place.
        
        In case of approximate match, having the data sorted in an ascending order is a pre-requisite to use the VLOOKUP formula. That would anyway lead to wrong results (even in cases when the result is not an error).
        
        In case the formula returns a result that is an error, IFERROR would still be valuable in making the result more meaningful.
        
        The cases where this combination works well is when you get data download from a data set that have fixed formats and you need to perform lookup on such data.
        
        When used properly, IFERROR can be a really useful function.
        
        [Reply](https://trumpexcel.com/iferror-vlookup/#comment-9521)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/iferror-vlookup/#respond)

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