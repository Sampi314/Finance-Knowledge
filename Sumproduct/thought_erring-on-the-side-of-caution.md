# Erring on the Side of #CAUTION!

**Source:** https://sumproduct.com/thought/erring-on-the-side-of-caution/

---

[Home](https://sumproduct.com/)

\> Erring on the Side of #CAUTION!

*   May 14, 2025

Erring on the Side of #CAUTION!
===============================

How to understand and fix the various errors that can occur in Excel.

Erring on the Side of #CAUTION!
===============================

_We look at something you would have thought we would have discussed years ago – explaining errors. Better late than never, we suppose! By Liam Bastick, director (and Excel MVP) with SumProduct Pty Ltd._

Query
-----

Further to your recent Error Checks article (please see June 2016 Insight Article for more details), I am still learning Excel and I keep getting error messages which aren’t always helpful. Can you provide any guidance please?

Advice
------

If I had a dollar for every time we encounter an error in an Excel spreadsheet, wow, I’d have _#REF!_ by now… Error messages are never welcome in modelling, but they can be career-threatening when scattered like confetti over a key dashboard or output summary. But do you know what all of them mean? We think most users understand the common messages, but we thought we would take this opportunity to summarise them:

*   **#VALUE!** is a very common error. It occurs whenever the data type a function is given doesn’t match what it is expecting. A simple example arises when using text as a number, _e.g.  
    _**\=”Dog”/4**  
    We all know the correct answer is “kebab”.
*   **#REF!**errors occur when a cell reference is deleted or moved. Excel tries to automatically update all references, but when it can’t do so, it replaces the actual cell reference with this error. For example, if I added the contents of cells **A1** and **A2**, the summation formula would be  
    **\=A1+A2  
    **but if I then deleted row 2, I would be left with the formula  
    **\=A1+#REF!  
    **which would give rise to the result _#REF!_ too.
*   **#DIV/0!** happens when a mathematical operation attempts to divide by zero (this value is mathematically indeterminate). This is common in division formulae and may be avoided by using the error trap  
    **\=IF(Denominator=0,0,Numerator/Denominator)**
*   **#NAME?** appears when Excel cannot find an implied named range. Excel assumes that any text not in inverted commas or missing parentheses is a range name. You will most likely encounter this when you forget to quote a string, mis-type a cell reference or forget the brackets on an Excel function, _e.g._  
    \=Guest+1
*   **#NULL!** Refers to the empty set (i.e. nothing to be found). It usually arises from inadvertent intersect operations, most commonly involving an accidental space in a formula (space is not just the final frontier, it is also the intersect operator in Excel; to find out more simply Google “ “…). An example might be:  
    **\=SUM(A1:A4 B1:B4)** (_e.g._ comma has been omitted)
*   **#N/A** happens when Excel cannot locate what is sought. This tends to occur in lookup-type functions such as  
    **\=MATCH(“Monsters”,{“Charlies”,”Angels”},0)**  
    These types of errors are often found in the cell **U2**
*   **#NUM!** occurs when a formula or function contains numerical values that are not valid. For example, you can’t enter the value **$1,000,000** in currency format as dollar signs are absolute reference indicators and commas are argument separators. This would give rise to an _#NUM!_ error.
*   **#GETTING\_DATA** is a message that can appear in Excel when a large or complex worksheet is being calculated. In Excel 2007 and later versions, operations are grouped so more complicated cells may finish after earlier ones do. While the calculations are still processing, the unfinished cells may display #GETTING\_DATA. However, this message is essentially temporary and should vanish once all calculations are complete. In essence, this isn’t really an error, more a status report.

Error types can also be determined with the, er, **ERROR.TYPE** function. Using the formula

\=ERROR.TYPE(Cell\_Reference)

Excel will return the error type as a number:

### Error Table

![](<Base64-Image-Removed>)

Like **#GETTING\_DATA** described above, not all errors are errors. One very common error is  
########  
which sometimes expands to ################################################## as the column is widened. There are two reasons you could see a string of hash / pound symbols (#) in a cell:

1.  The first is that the cell column is too narrow to display the value. This is easy to fix: widen the column!
2.  The second is if a date-formatted cell becomes negative. Usually this happens when dates are subtracted from each other.

In both instances, the data is still available in the cell, it is simply a formatting issue. Since other formulae referencing the affected cells can still read and incorporate these values, neither of these instances are true errors.

### Word to the Wise

Always deal with these prima facie errors in a model. If you do not, it reflects badly on you when models are circulated and they are so easy to locate (simply Find using **CTRL + F** and seek out ‘_#_’ in both ‘Values’ and ‘Formulas’).

If you have a query for the Spreadsheet Skills section, please feel free to drop Liam a line at [liam.bastick@sumproduct.com](mailto:liam.bastick@sumproduct.com)
.

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/erring-on-the-side-of-caution/#0)
    
*   [Register](https://sumproduct.com/thought/erring-on-the-side-of-caution/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/erring-on-the-side-of-caution/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/erring-on-the-side-of-caution/#0)

[](https://sumproduct.com/thought/erring-on-the-side-of-caution/#0 "close")

top