# Monday Morning Mulling: December 2018 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-december-2018-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: December 2018 Challenge

*   December 30, 2018

Monday Morning Mulling: December 2018 Challenge
===============================================

Monday Morning Mulling: December 2018 Challenge
===============================================

31 December 2018

It’s the last day of 2018! A perfect time to take a look at the answer to a question that seems quite easy, but is difficult to do elegantly.

To recap the question, given a series of numbers, and a target sum, can you get Excel to tell you which combination of numbers will result in the sum being achieved?

For example, with a target of 10 and the numbers:

![](<Base64-Image-Removed>)

… we should expect to see the results of 9 + 1, 7 + 3, 7 + 2 + 1 and 5 + 2 + 3 (in no particular order).

A couple of rules that we set:

*   No macros / VBA
*   No array (Ctrl + Shift + Enter) functions
*   No Solver or other iterative tools (_i.e._ no circular references)
*   Feel free to use Power Query if you think it will help.

How did you go with the task? We’ve come up with a [solution](https://sumproduct.com/assets/blog-pictures/2018/challenges/12-dec/mmm/december-2018-solution-file.xlsx)
 that is 100% formula-based, that didn’t even delve into Power Query (which has been our go-to tool for solving problems like these in recent times).

The first task was to create a table with every combination of numbers that could be used. Given that we have 6 numbers to choose from, there are 6 + 15 + 20 + 15 + 6 + 1 = 63 possible results. Our results go down the page, so given the row limitation, this approach can work for a maximum of 20 numbers (with up to 20 choices), as that requires exactly 1,048,575 rows (conveniently one less than the number of rows in a spreadsheet, giving us room for the table header!).

If we have more input numbers than that, we can restrict the number of items in our combination. For example, looking at a list of 40 numbers but restricting the possible combinations of items to add to a maximum of five unique numbers would require 760,098 combinations to check – a lot, but well within the maximum capacity of Excel. Restricting the search to four number combinations would allow us to look through a list of up to 71 items before we run out of space.

![](<Base64-Image-Removed>)

So the first step is to create a list of all the combinations. Once this is done, we can use an **INDEX** function to pick up the numbers that correspond to those combinations:

![](<Base64-Image-Removed>)

Totalling the values, we compare this back to our target number and set up a \[1,0\] flag to highlight any correct results. We also create a simple little rank using the **COUNTIF** function to see how many times the correct result was achieved prior to that combination:

![](<Base64-Image-Removed>)

From here, we can create a new index – starting from one, and looking up the corresponding values based on the Rank column:

![](<Base64-Image-Removed>)

This result shows us that, for the numbers we provided, there are four possible answers. However, if I change the target to 21, there are only two possible answers:

![](<Base64-Image-Removed>)

If we change the number of options to choose from, we can simply expand out the Index#, Unique# and Value# columns to include additional results, up to a maximum of 20 (since there are 2^20 rows in a spreadsheet). In the solution, we’ve included another example at 11 to demonstrate how it might work. With the new Dynamic Arrays in Office 365, you could actually set it up so that the columns would expand sideways dynamically, adapting automatically to your input table.

What did you think of our approach? How did it compare to your approaches? Let us know at [contact@sumproduct.com](mailto:contact@sumproduct.com)
. See you with a new challenge next month!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-december-2018-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-december-2018-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-december-2018-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-december-2018-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-december-2018-challenge/#0 "close")

top