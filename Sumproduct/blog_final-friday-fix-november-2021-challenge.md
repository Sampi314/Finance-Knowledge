# Final Friday Fix: November 2021 Challenge

**Source:** https://sumproduct.com/blog/final-friday-fix-november-2021-challenge/

---

[Home](https://sumproduct.com/)

\> Final Friday Fix: November 2021 Challenge

*   November 25, 2021

Final Friday Fix: November 2021 Challenge
=========================================

Final Friday Fix: November 2021 Challenge
=========================================

26 November 2021

_On the final Friday of each month, we are going to set an Excel / Power BI challenge for you to puzzle over so that you can get your “Excel fix”. Challenge your office colleagues to see who can solve the puzzle quickest. There are no prizes at this stage: you are playing for bragging rights only!_

This is based upon a real-life problem, which was not as easy to solve as we thought it would be.

**_The Challenge_**

Numbers with leading zeroes may sometimes cause problems. In order to find duplicates from a list, you might think of using [**FILTER**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-filter-function)
 with [**COUNTIF**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-countif-function)
 for example. However, **COUNTIF** cannot distinguish between numbers with and without leading zeroes, or “real” numbers and numbers which have been stored as text. Surprised? Try it and see!

As you can see below, the number of occurrences of each number is calculated incorrectly by **COUNTIF**:

![](<Base64-Image-Removed>)

Therefore, this challenge is trickier than it might at first seem. You can download the number list [here](https://sumproduct.com/assets/blog-pictures/2021/fff-mmm/nov/fff/sp-list-of-duplicates---question.xlsm)
.

This month’s challenge is to write a **formula in one cell** using [Dynamic Arrays](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
 that will spill down to generate a list of duplicates (_i.e_. all numbers that show up more than once) from the number list in the file above. The result should be similar to the list generated on the right _(below)_:

![](<Base64-Image-Removed>)

As always, there are some requirements:

*   the formula needs to be in just one cell (no “helper” cells)
*   it should treat these kinds of numbers differently:
    *   with and without leading zeroes
    *   “real” numbers as opposed to numbers stored or formatted as text
*   this is a formula challenge – no Power Query / Get & Transform or VBA!

_Sounds easy? Then why not have a go? We’ll publish one solution in Monday’s blog. Have a great weekend in the meantime!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/final-friday-fix-november-2021-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/final-friday-fix-november-2021-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/final-friday-fix-november-2021-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/final-friday-fix-november-2021-challenge/#0)

[](https://sumproduct.com/blog/final-friday-fix-november-2021-challenge/#0 "close")

top