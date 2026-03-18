# Weird Little Traps: Excel Going Wrong from Day 1…

**Source:** https://sumproduct.com/blog/weird-little-traps-excel-going-wrong-from-day-1/

---

[Home](https://sumproduct.com/)

\> Weird Little Traps: Excel Going Wrong from Day 1…

*   September 7, 2017

Weird Little Traps: Excel Going Wrong from Day 1…
=================================================

Weird Little Traps: Excel Going Wrong from Day 1…
=================================================

8 September 2017

While our _VBA blog_ series takes a little hiatus (it’s coming back soon, we promise!), we thought we’d share with you a problem that raises its ugly little head from time to time. Don’t fall foul of it!

As many of you are aware, range names are created by selecting your range of cells and then either typing directly into the Name Box (circled, below),

![](<Base64-Image-Removed>)

or else by using the keyboard shortcut **CTRL + F3**, and then clicking on the ‘New’ button in the ‘Name Manager’ dialog box), _viz._

![](<Base64-Image-Removed>)

Since Excel 2007 came about, many users have fallen into a trap that previously harmless range names seemed to invoke the wrath of Excel:

![](<Base64-Image-Removed>)

Believe it or not, **Day1** is a common range name used in spreadsheets. While **Day\_1**, **Day01** and **Days1** all seem fine, Excel proclaimed that Day1 was a reserved name. And guess what? Indeed, it is!

Since Excel 2007, the spreadsheet has grown to 16,384 columns (**A** to **XFD**) and 1,048,576 rows. Since range names cannot be called potential cell references (can you imagine how much fun that would be – we’d call cell **A1** ‘**F5**‘ and so on), this means many three-letter range names are not available. **DAY1** is in fact a cell reference:

![](<Base64-Image-Removed>)

So be careful! At least we now have the answer to the age-old question, **CAR54** where are you?

_The VBA blog series returns soon. We’ve just got stick in an iterative loop!_

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/blog/weird-little-traps-excel-going-wrong-from-day-1/#0)
    
*   [Register](https://sumproduct.com/blog/weird-little-traps-excel-going-wrong-from-day-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/weird-little-traps-excel-going-wrong-from-day-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/weird-little-traps-excel-going-wrong-from-day-1/#0)

[](https://sumproduct.com/blog/weird-little-traps-excel-going-wrong-from-day-1/#0 "close")

top