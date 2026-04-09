# Monday Morning Mulling: July 2017 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-july-2017-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: July 2017 Challenge

*   July 30, 2017

Monday Morning Mulling: July 2017 Challenge
===========================================

Monday Morning Mulling: July 2017 Challenge
===========================================

31 July 2017

_On the final Friday of each month, set an Excel for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

**_Final Friday Fix: July Challenge Recap_**

On Friday, I provided an [attached Excel file](https://sumproduct.com/assets/blog-pictures/2017/final-friday/july-17/sp-example-of-autofilter-error.xlsm)
. This file had data in the following format:

![](<Base64-Image-Removed>)

Highlighting the entire selection, I went to the ‘Data’ tab on the Ribbon and clicked on ‘Filter’ in the ‘Sort & Filter’ grouping (**ALT + A + T**) to create a filtered list. I then filtered on ‘Country’ for Australia and obtained the following subset:

![](<Base64-Image-Removed>)

The problem was that when I did this ‘USA’ became part of the filtered ‘Australia’ subset. The questions were, why did this happen and how do you fix it?

**_The Solution_**

The problem here resides with the formula in cells **F13:F42**, namely

**\=SUBTOTAL(103,$G$13:$G13)**

Yes, it will auto-number visible data, but there is an inherent problem in this formula too. Let me explain by first recapping on the **SUBTOTAL** function. On the face of it, it seems like many other Excel functions:

**\=SUBTOTAL(Function\_Number, Ref1, Ref2, …)**

The **Function\_Number** is an integer between 1 and 11 inclusive or 101 and 111 inclusive as follows:

![](<Base64-Image-Removed>)

For the **Function\_Number** constants from 1 to 11, the **SUBTOTAL** function includes the values of rows hidden by the ‘Hide Rows’ command under the ‘Hide & Unhide’ submenu of the ‘Format’ command in the ‘Cells’ group on the ‘Home’ tab. These constants should be used when you want to subtotal hidden and unhidden (visible) numbers in a list. For the **Function\_Number** constants from 101 to 111, the **SUBTOTAL** function ignores values of rows hidden by the ‘Hide Rows’ command. These constants should be used when you want to subtotal the visible numbers in a list only.

If there are other subtotals within **Ref1, Ref2, …** (or nested subtotals), these nested subtotals are ignored. This is an important feature as it allows you to consider complete ranges without any risk of double-counting.

**SUBTOTAL(103, Range)** acts like **COUNTA** excluding any hidden cells, _i.e._ it counts the number of non-empty visible cells in **Range**. That’s how the auto-numbering works.

There’s just one problem.

**SUBTOTAL** also works with the built-in subtotal functionality of Excel, which totals numbers excluding – essentially, ignoring – the **SUBTOTAL** function. Therefore, Excel is trained to ignore what it thinks are subtotal rows.

Look again at the USA row included. It’s the final row of the data selection and it begins with a **SUBTOTAL** function. Excel thinks it’s a subtotal calculation. Therefore, it has excluded it quite deliberately from the filtering believing it to be a subtotal of the data. Since the **Function\_Number** lies between 101 and 111, Excel realises this function is designed to include filtered items only, so programmatically it makes sense to retain this row. Excel thinks it’s the sum of the above!

There are several ways that this logic can be defeated. This [attached Excel file](https://sumproduct.com/assets/blog-pictures/2017/monday-morning-mulling/july/sp-example-of-autofilter-error-solutions.xlsm)
 contains the following alternative ‘fixes’:

1.  **Double Unary:** possibly first discovered by Excel guru Dick Kusleika, putting two minus signs straight after the equals sign (_e.g._**\=–SUBTOTAL(103,$G$13:$G13)** ) fools Excel into thinking it’s a different formula. The first minus sign negates the calculation; the second makes it positive again
2.  **Multiplying by 1:** this one I am taking credit for! Who in their right mind would multiply a total by 1? Excel therefore thinks it isn’t a total and hence it becomes part of the filter set
3.  **Add a column before the Item Number:** In most instances (but sadly, not all), adding a column of data before the column containing **SUBTOTAL** will make the dataset work as intended. Suddenly Excel doesn’t believe the bottom row is a total anymore
4.  **Add a blank row at the bottom:** put a (sub)total at the bottom of the data? That’s just what Excel expected you to do! So don’t. Make it the penultimate row of the data by making a blank row part of the dataset. This is often quoted on the internet, but I think this is a terrible solution. If you need to add data, you’ll need to insert it before the blank row. What end user would appreciate the first blank row is part of the dataset? Further, blanks will be included in the list of options for the ‘Country’ filter. This is not an ideal fix
5.  **Convert the data range to a Table:** by highlighting the data and then converting the range to a Table (**CTRL + T**), filtering will work as expected – and you will get built in filtering as a bonus! Table totals work in a different way, so Excel is not confused by the **SUBTOTAL** formula. I quite like this solution as it requires no modification to the formula or need to add a row or column.

![](<Base64-Image-Removed>)

Other than adding a blank row (not sold on that at all), the others all have their strengths and weaknesses. I don’t want to advocate one solution over another. Hopefully, you came up with one of the above. If not – and it works – do let us know…

You can find out more about **SUBTOTAL** and Excel’s subtotal functionality [here](https://www.sumproduct.com/thought/subtotal-function-and-functionality)
. For more tricks and tips, check out our many examples at [www.sumproduct.com/thought](https://www.sumproduct.com/thought)
.

_The Final Friday Fix will return on Friday 25 August with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our [home page](https://www.sumproduct.com/)
 and watch out for a new blog every other business workday._

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-july-2017-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-july-2017-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-july-2017-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-july-2017-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-july-2017-challenge/#0 "close")

top