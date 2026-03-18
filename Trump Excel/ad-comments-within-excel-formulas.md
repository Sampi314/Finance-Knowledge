# Add Comments Within Excel Formulas (3 Easy Ways)

**Source:** https://trumpexcel.com/ad-comments-within-excel-formulas

---

[Skip to content](https://trumpexcel.com/ad-comments-within-excel-formulas/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/ad-comments-within-excel-formulas/#below-title)

Excel formulas can get complicated, especially when you’re working with [advanced functions](https://trumpexcel.com/advanced-excel-functions-formulas/)
 or creating solutions for others to use.

Adding comments directly within your formulas can make them more understandable and easier to maintain in the future.

It’s like leaving helpful notes for yourself or anyone else who might need to work with your spreadsheets later.

While Excel formulas do not natively support adding comments, in this article I am going to show you three simple tricks you can use to add comments to any Excel formula you are working with.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/ad-comments-within-excel-formulas/#)

Example Formula Used for Demonstration
--------------------------------------

Imagine we have names in column A, their corresponding scores in column B, and we’re using an [XLOOKUP formula](https://trumpexcel.com/xlookup-function/)
 to fetch a specific person’s score.

![Dataset to fetch score from name using lookup](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201362%20822'%3E%3C/svg%3E)

Below is the XLOOKUP formula I have used to fetch the score based on the name in cell D2.

\=XLOOKUP(D2,A2:A11,B2:B11,"NA")

![XLOOKUP formula for adding comments in formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201453%20943'%3E%3C/svg%3E)

Now, within this formula, I want to add a comment.

Let me show you three ways to do this.

While this example is straightforward, the techniques I cover in this article work equally well for any complex formulas where comments would be more valuable.

Method 1: Using LET Function
----------------------------

The [LET function](https://trumpexcel.com/excel-functions/let-function/)
 is the most elegant solution for adding comments to your [Excel formulas](https://trumpexcel.com/excel-functions/)
.

_This function is available in Excel with Microsoft 365 subscriptions only. So if you are using an older version of excel you can use the next method._

The LET function allows you to assign numbers, text, or calculations to variables that you can then use throughout your formula. The clever trick here is that we can create variables that hold our comments but aren’t actually used in the calculation.

Below is the LET formula that returns the same result as our original XLOOKUP formula, and also has two sample comments.

\=LET(  
fx, XLOOKUP(D2,A2:A11,B2:B11,"NA"),  
comment1, "This is an example comment explaining the XLOOKUP.",  
comment2, "This formula finds the score for the name in cell D2.",  
fx  
)

When you press Enter, this formula will return the same result as your original XLOOKUP, but now it contains helpful explanatory comments.

Note: Each comment can be a maximum of 255 characters long. If it is more than 255 characters long, it would give an error.

**Pros of this method**:

*   You can add multiple comments throughout your formula (by assigning them to different variables)
*   Very readable format with clear separation between formula and comments
*   Comments can be placed anywhere within the LET function

**Cons of this method**:

*   Only available in Excel with Microsoft 365
*   Each comment is limited to 255 characters (though you can use multiple comment variables to overcome this)

Method 2: Using IF Function
---------------------------

If you don’t have access to the LET function, you can use the [IF function](https://trumpexcel.com/excel-if-function/)
 instead, which works in all [versions of Excel](https://trumpexcel.com/excel-version/)
.

The IF function takes three arguments:

*   A logical test that returns TRUE or FALSE
*   The value to return if the test is TRUE
*   The value to return if the test is FALSE

The trick is to set the logical test to always return TRUE, put your actual formula in the second argument, and use the third argument (which will never be executed) for your comment.

Below is the formula that will give us the same result as the XLOOKUP formula, and also has a comment as the last arguemnt

\=IF(TRUE,XLOOKUP(D2,A2:A11,B2:B11,"NA"),"This is an example comment explaining what this formula does.")

Since the first argument is always TRUE, the formula will always return the result of the XLOOKUP, but the comment is still there in the formula for reference.

**Pros of this method**:

*   Works in all versions of Excel
*   Simple to use

**Cons of this method**:

*   Limited to one comment per IF statement (though you could nest IF statements)
*   Less readable than the LET function approach
*   Comment is at the end of the formula, which might be less convenient for long formulas
*   Comment can be upto 255 character long only

Method 3: Using the N Function
------------------------------

The third method uses the N function, which is the simplest approach but has an important limitation: it only works when your formula returns a numeric result.

The N function converts non-numeric values to numbers. Text values are converted to 0.

By adding +N(“your comment”) to the end of a formula that returns a number, you effectively add 0 to your result (not changing it) while incorporating a comment.

Below is the formula that will give us the same result as the XLOOKUP formula, and also has a comment within the N function in double quotes.

\=XLOOKUP(D2,A2:A11,B2:B11,"NA")+N("This XLOOKUP finds the score for the name in cell D2")

The N function converts the text comment to 0, so adding it to your numeric result doesn’t change the outcome.

**Pros of this method**:

*   The simplest and easiest method to implement
*   Works in all Excel versions
*   Very concise syntax

**Cons of this method**:

*   Only works with formulas that return numeric values
*   Limited to one comment per formula (though you could chain multiple N functions)
*   Each comment is limited to 255 characters

So to sum it all up
-------------------

Of the three methods we’ve covered:

The LET function is the best overall approach if you have Excel with Microsoft 365, offering multiple comments and better readability.

The IF function is a solid alternative that works in any version of Excel.

The N function is the simplest method but only works with formulas that return numeric values.

Choose the method that works best for your specific situation and Excel version. Your future self (and colleagues) will thank you for the added clarity in your formulas!

Do you know of any other methods for adding comments to Excel formulas? Have you found these techniques helpful in your work? Let me know in the comments!

**Other Excel articles you may also like:**

*   [How to Insert a Picture in Excel Comment](https://trumpexcel.com/insert-picture-in-excel-comment/)
    
*   [How to Insert / Delete Comments in Excel (including Shortcuts)](https://trumpexcel.com/insert-delete-comments-excel/)
    
*   [Comments in Excel VBA (Add, Remove, Block Commenting)](https://trumpexcel.com/comments-excel-vba/)
    
*   [Identify Errors Using Excel Formula Debugging](https://trumpexcel.com/excel-formula-debugging/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “Add Comments Within Excel Formulas”
-------------------------------------------------

1.  Good work Sir Ji
    
    [Reply](https://trumpexcel.com/ad-comments-within-excel-formulas/#comment-45094)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/ad-comments-within-excel-formulas/#respond)

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