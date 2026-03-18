# Power Query: Keep on Running

**Source:** https://sumproduct.com/blog/power-query-keep-on-running/

---

[Home](https://sumproduct.com/)

\> Power Query: Keep on Running

*   February 2, 2021

Power Query: Keep on Running
============================

Power Query: Keep on Running
============================

3 February 2021

_Welcome to our Power Query blog. This week, I revisit running totals._

I looked at running totals some time ago, [Power Query: One Route to a Running Total](https://sumproduct.com/blog/power-query-one-route-to-a-running-total/)
. I used a combination of **List() M** functions, namely the **List.Range()** and **List.Sum()** functions. I did this so that I could get a list of all the amounts to the current point to be totalled and then simply add them up.

My example used some accounting data, so I will return to it once more:

![](<Base64-Image-Removed>)

I have extracted data from **ACCT\_Order\_Charges\_with\_Group**, a table on my MS Access database. I picked this data because there are more than 30,000 rows, which will be useful as I plan to look at how efficiently running totals can be calculated.

In order to use the **List.Range****()** function, I needed a way to sequentially identify the rows containing the amounts so that they form a list. To assign a number to each row, I added an index column from the ‘Add Column’ tab, starting from 1 and not 0 (the default).

![](<Base64-Image-Removed>)

I needed to tell the **List.Range()** function to look at this list, and where to start reading from and (in this case) where to stop. I created a new custom column from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

The **M** code I used was:

**\= List.Range(#”Added Index”\[Amount\],0,\[Index\])**

This looked at the amounts sequentially by row number, starting at the first row and ending with the index for the current row. The column created looks a little odd, as it just contains the word ‘List’ for each row _(see below)_. However, if I clicked in the column next to (not on) the word ‘List’, then the contents appeared at the bottom left of the screen under the title ‘List’:

![](<Base64-Image-Removed>)

The next step was to add them all up. This is where **List.Sum()** came into play. The only parameter that **List.Sum()** requires is a list. Therefore, I created another custom column, with the following **M** code:

**\= List.Sum(List.Range(#”Added Index”\[Amount\],0,\[Index\]))**

![](<Base64-Image-Removed>)

I loaded this data back into my workbook, but as I noted in the original blog, the load is not instantaneous. This is because for each running total calculation, **List.Range()** creates a list of all the amounts to that point and then **List.Sum()** sums them. I can add another list function which will speed up the process (subject to constraints which I will expand on later).

**List.Buffer(list** as list**)** as list

This buffers the **list** in memory. The result of this call is a _stable list_. This basically means that the list does not need to be recalculated, and in this case, can be added to.

I look at the **M** code I have in the Advanced Editor (I removed the custom column **Running Total List** as it was just to show how **List.Range()** worked).

![](<Base64-Image-Removed>)

The **M** code for the lines associated with the running total is:

    **#”Added Index” = Table.AddIndexColumn(#”Inserted Multiplication”, “Index”, 1, 1),**

    **#”Added Custom” = Table.AddColumn(#”Added Index”, “Running Total”, each List.Sum(List.Range(#”Added Index”\[Amount\],0,\[Index\])))**

**in**

    **#”Added Custom”**

I add a **List.Buffer()** step after the “Added Index” step:

**BufferedValues = List.Buffer(#”Added Index”\[Amount\]),**

Then, I change the “Added Custom” step to use **BufferedValues** instead of **“Added Index”\[Amount\]**

    **#”Added Custom” = Table.AddColumn(#”Added Index”, “Running Total”, each List.Sum(List.Range(BufferedValues,0,\[Index\])))**

I make these changes in the Advanced Editor:

![](<Base64-Image-Removed>)

I click ‘Done’ and check my data.

![](<Base64-Image-Removed>)

The totals still look good, so I load the data to the workbook. I had issues with the time taken for this in the original blog – but no more!

![](<Base64-Image-Removed>)

There is an improvement, but this is not an ideal solution. If I had a query which used query folding for efficiency, then folding would be prevented because I have used a buffer function. Next week I will look at another, more complex way of creating a running total…

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-keep-on-running/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-keep-on-running/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-keep-on-running/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-keep-on-running/#0)

[](https://sumproduct.com/blog/power-query-keep-on-running/#0 "close")

top