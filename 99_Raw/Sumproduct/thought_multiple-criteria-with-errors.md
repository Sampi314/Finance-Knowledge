# Multiple Criteria with Errors

**Source:** https://sumproduct.com/thought/multiple-criteria-with-errors/

---

[Home](https://sumproduct.com/)

\> Multiple Criteria with Errors

*   May 14, 2025

Multiple Criteria with Errors
=============================

How to deal with errors in data when summing up subject to multiple criteria.

Multiple Criteria with Errors
=============================

_This month, in our series of articles providing solutions to common issues encountered by finance professionals, we look at how to deal with errors when using formulae considering multiple criteria. By Liam Bastick, director (and Excel MVP) with SumProduct Pty Ltd._

Query
-----

How do I deal with errors in data that I am trying to sum up subject to multiple criteria?

Advice
------

It’s easy to write a formula that will work when everything else is working perfectly. It’s much more challenging to write a formula that will work when our data doesn’t work the way we want it to. To start this new year, we’re going to talk about adding up values when we have text and other nasties.

We’ve covered how to do sums with multiple criteria using the **SUMPRODUCT** function before. However, this doesn’t work if we have text or errors in our data. Consider the following example:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

This is reasonably straightforward. Here, I compare the Business Unit to the input, the Product type to the input, and then multiply the results by the values to get:

**\=SUMPRODUCT(($F$12:$F$21=$G$26)\*($G$12:$G$21=$G$27)\*$H$12:$H$21)**

If you’re a regular reader of the Spreadsheet Skills section, this will have been easy so far; if not feel free to consult my past article [here](https://www.sumproduct.com/thought/sumproduct-squared)
. However, not all data behaves nicely:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

With text in a cell, our function is attempting to multiply “?????” with 1s and 0s, which leaves us with _#VALUE!_, which is not the desired result. If only there were a way to ignore text or errors..?

Enter **SUMIFS**. **SUMIFS** has the nifty feature that it will ignore text values in the vector that we are summing, just like the **SUM** function. It behaves like **SUMIF** (see [this article](https://www.sumproduct.com/thought/sumproduct-squared)
 for further details) just for multiple criteria rather than a single criterion. I can replace the **SUMPRODUCT** function with **SUMIFS** like so:

![](<Base64-Image-Removed>)

Here, the formula is:

\=**SUMIFS($H$12:$H$21,$F$12:$F$21,$G$33,$G$12:$G$21,$G$34)**

This solution ignores the text whether it forms part of the answer or not. Since **SUMIFS** will use the conditions to isolate only matching values that should be summed, it also has the benefit of ignoring items like _#N/A_ in unused data that may cause errors.

Do note that if the _#N/A_ result occurs in the data, there are other ways to get around this issue. Did you know that you can incorporate error results into your conditions? You could try the following for example:

**\=SUMIFS($H$12:$H$21,$F$12:$F$21,$G$33,$G$12:$G$21,$G$34,$H$12:$H$21,”<>#N/A”)**

The last argument ensures that the _#N/A_ results will be ignored, regardless of whether they form part of your target data. You could repeat this with any other error results as well, though this may result in a very long formula if you don’t consider shortcuts!

![](<Base64-Image-Removed>)

### Suggested Solution

This image is a screenshot from the [attached Excel file](https://sumproduct.com/assets/thought-files/multiple-criteria-with-errors/sp-multiple-criteria-with-errors---suggested-solution-2017.xlsm)
, which contains my suggested solution. This file has had some issues with data and some of our inputs have become garbled (no change there then).

![](<Base64-Image-Removed>)

A very “basic” solution would be the following wonder:

**\=($I$15\*IFERROR(N($J$15),)\*$J$22\*($H$15=J$38))+($I$15\*IFERROR(N($K$15),)\*$K$22\*($H$15=J$38))+($I$15\*IFERROR(N($L$15),)\*$L$22\*($H$15=J$38))+($I$15\*IFERROR(N($M$15),)\*$M$22\*($H$15=J$38))+($I$15\*IFERROR(N($N$15),)\*$N$22\*($H$15=J$38))+($I$15\*IFERROR(N($O$15),)\*$O$22\*($H$15=J$38))  
****+($I$16\*IFERROR(N($J$16),)\*$J$22\*($H$16=J$38))+($I$16\*IFERROR(N($K$16),)\*$K$22\*($H$16=J$38))+($I$16\*IFERROR(N($L$16),)\*$L$22\*($H$16=J$38))+($I$16\*IFERROR(N($M$16),)\*$M$22\*($H$16=J$38))+($I$16\*IFERROR(N($N$16),)\*$N$22\*($H$16=J$38))+($I$16\*IFERROR(N($O$16),)\*$O$22\*($H$16=J$38))  
****+($I$17\*IFERROR(N($J$17),)\*$J$22\*($H$17=J$38))+($I$17\*IFERROR(N($K$17),)\*$K$22\*($H$17=J$38))+($I$17\*IFERROR(N($L$17),)\*$L$22\*($H$17=J$38))+($I$17\*IFERROR(N($M$17),)\*$M$22\*($H$17=J$38))+($I$17\*IFERROR(N($N$17),)\*$N$22\*($H$17=J$38))+($I$17\*IFERROR(N($O$17),)\*$O$22\*($H$17=J$38))  
****+($I$18\*IFERROR(N($J$18),)\*$J$22\*($H$18=J$38))+($I$18\*IFERROR(N($K$18),)\*$K$22\*($H$18=J$38))+($I$18\*IFERROR(N($L$18),)\*$L$22\*($H$18=J$38))+($I$18\*IFERROR(N($M$18),)\*$M$22\*($H$18=J$38))+($I$18\*IFERROR(N($N$18),)\*$N$22\*($H$18=J$38))+($I$18\*IFERROR(N($O$18),)\*$O$22\*($H$18=J$38))**

Lovely. It works, but it’s far from pretty. Sounds like me.

The **N** function returns the value of any contents that appear to be numbers and treats text as zeros and errors as errors. It’s a “brute force and ignorance” approach but it does appear to get the job done. The problem is, what if (a) I add more rows and / or columns and / or conditions and (b) I don’t have a spare six hours to understand how the formula works? It’s very simple to miss a cross-multiplication too.

No, I suggest the following – much shorter – solution instead:

**{=SUMPRODUCT($I$30:$I$33\*IF(NOT(ISNUMBER($J$30:$O$33)),,$J$30:$O$33)\*$J$22:$O$22\*($H$30:$H$33=J$38))}**

It’s a short, “simple” array formula (one that requires entering using **CTRL + SHIFT + ENTER**, please see [this article](https://www.sumproduct.com/thought/array-of-light)
 for more details) – don’t try typing in the brace brackets (**{** and **}**) yourself.

Last time I explained how errors / text could be ignored when data is in a row or a column (“**vectors**”) using **SUMIF** or **SUMIFS**. However, my question deliberately used multiple rows and columns (an “**array**” of data) because these useful functions will not work in this instance.

Our old friend **SUMPRODUCT** comes to the rescue in this instance. For a refresher on **SUMPRODUCT**, please see [this article](https://www.sumproduct.com/thought/sumproduct-squared)
. Essentially, the use of the multiplication delimiter is deliberate (the formula will not work if the delimiters were to become commas instead). It should be noted that this last formula is essentially

**\=SUMPRODUCT(Column\_Vector\*Array\*Row\_Vector\*Condition)**

where the number of rows in the **Column\_Vector** must equal the number of rows in the **Array**, and also the number of columns in the **Array** must equal the number of columns in the **Row\_Vector**. The **Condition** dimensions are slightly more relaxed, but typically are similar to either the **Column\_Vector** or the **Row\_Vector**.

The key trick concerns **Array**: I must check if the relevant element of the **Array** contains a number or not. To be honest, blank cells, text or errors could all create issues in my cross multiplication, so I really want to identify when the cell value is not a number. This is what

**IF(NOT(ISNUMBER($J$30:$O$33)),,$J$30:$O$33)**

does. It returns the value in the cell only if it is a number. After that, it is simply a case of cross-multiplying and adding the array syntax (this is necessary for Excel to consider errors in an array). If you require more conditions, rows or columns, simply add them. Easy!

The solution:

**{=SUMPRODUCT($I$30:$I$33\*IF(NOT(ISNUMBER($J$30:$O$33)),,$J$30:$O$33)\*$J$22:$O$22\*($H$30:$H$33=J$38))}**

is pretty easy to understand once it has been explained to you.

**_Word to the Wise_**

Some readers may have noted that the expression **IF(NOT(ISNUMBER(Array)),,Array)** appears a little convoluted and could be readily replaced by **IF(ISNUMBER(Array),Array,)** – which simply swaps the order of the TRUE and FALSE conditions. That’s true (pun intended), but **NOT(ISNUMBER())** is a powerful combination that comes up time and time again in Excel error testing (_e.g._ to highlight cells that do not contain numbers using conditional formatting). Therefore, my use of **NOT()** to negate TRUE and FALSE was deliberate so that you know how to report by exception.

If you have a query for the Spreadsheet Skills section, please feel free to drop Liam a line at [liam.bastick@sumproduct.com](mailto:liam.bastick@sumproduct.com)
 or visit the [SumProduct website](https://www.sumproduct.com/)
.

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/multiple-criteria-with-errors/#0)
    
*   [Register](https://sumproduct.com/thought/multiple-criteria-with-errors/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/multiple-criteria-with-errors/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/multiple-criteria-with-errors/#0)

[](https://sumproduct.com/thought/multiple-criteria-with-errors/#0 "close")

top