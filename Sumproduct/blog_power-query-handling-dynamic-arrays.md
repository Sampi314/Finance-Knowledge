# Power Query: Handling Dynamic Arrays

**Source:** https://sumproduct.com/blog/power-query-handling-dynamic-arrays/

---

[Home](https://sumproduct.com/)

\> Power Query: Handling Dynamic Arrays

*   March 7, 2023

Power Query: Handling Dynamic Arrays
====================================

Power Query: Handling Dynamic Arrays
====================================

8 March 2023

_Welcome to our Power Query blog. This week, I extract data from a Dynamic Array._

**Please Note**: Since this blog was written, Power Query has moved on and can now handle dynamic arrays.  Instead of creating a Table, a Named Range is created and called “FromArray\_**n”**, where **n** is the next available integer.  Whilst the error at the beginning of this blog will no longer occur, I still recommend creating your own Named Range instead so that meaningful titles are used.

I have a list of trainee salespeople that I need to extract to Power Query, so that I can merge their details with another query:

![](<Base64-Image-Removed>)

Seems simple enough; I select the data and use ‘From Table/Range’ on the ‘Get & Transform’ section of the data tab:

![](<Base64-Image-Removed>)

I don’t have any headers, so I take the defaults.

![](<Base64-Image-Removed>)

The results are not good. If I click on the Error value, I see this:

![](<Base64-Image-Removed>)

If I discard the query and go back to the sheet, I can see what has happened:

![](<Base64-Image-Removed>)

To get a **#SPILL!** error, I must be dealing with a Dynamic Array. I use **CTRL**\+ **Z** to undo the Table creation.

![](<Base64-Image-Removed>)

The list has been created using **FILTER()** which means that the output is a Dynamic Array. Obviously in this example, I can just use the original table, but let’s assume that I don’t have access to that.

I used ‘From Table/Range’ to extract the data, and so Power Query converted the data to a Table, which doesn’t currently work with Dynamic Arrays. I could however create a range.

In the ‘Name Manager’ on the Formulas tab, I can create a new range. If I just select the cells currently populated, this will be incorrect when I have more trainees. I need to create a dynamic range. This is the range I create:

![](<Base64-Image-Removed>)

The Excel formula is:

**\=Sheet1!$F$2#**

This links to the data in the Dynamic Array created by the formula in cell **$F$2**. Now, I can create a blank query to access this range:

![](<Base64-Image-Removed>)

I create the Source step:

![](<Base64-Image-Removed>)

The **M** code is:

**\= Excel.CurrentWorkbook(){\[Name=”DR\_Trainees”\]}\[Content\]**

This extracts the content from the range **DR\_Trainees** in the current workbook.

Power Query generates a ‘Changed Type’ step, which I keep.

![](<Base64-Image-Removed>)

I don’t rename the columns yet, as I want to check that this query will refresh as expected. I use ‘Close & Load’ from the Home tab and create the output on a new sheet:

![](<Base64-Image-Removed>)

Now I can add some new trainees to the original table:

![](<Base64-Image-Removed>)

The Dynamic Array updates immediately. I refresh the**Trainee\_list** query:

![](<Base64-Image-Removed>)

The new trainees appear, and my list is complete. I _can_ use Power Query to extract data from a Dynamic Array.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-handling-dynamic-arrays/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-handling-dynamic-arrays/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-handling-dynamic-arrays/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-handling-dynamic-arrays/#0)

[](https://sumproduct.com/blog/power-query-handling-dynamic-arrays/#0 "close")

top