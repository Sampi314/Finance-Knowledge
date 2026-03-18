# Power Query: Totals by Type

**Source:** https://sumproduct.com/blog/power-query-totals-by-type/

---

[Home](https://sumproduct.com/)

\> Power Query: Totals by Type

*   July 13, 2021

Power Query: Totals by Type
===========================

Power Query: Totals by Type
===========================

14 July 2021

_Welcome to our Power Query blog. This week I look at selective running totals._

I have some tent data (yet again).

![](<Base64-Image-Removed>)

I am going to create some running totals. I start by loading my data to Power Query using ‘From Table/Range’ from the ‘Get & Transform Data’ section of the Data tab.

![](<Base64-Image-Removed>)

I take the defaults and load my data.

![](<Base64-Image-Removed>)

I will start by creating a running total using **List()** functionality, as I did in [Power Query: Keep On Running](https://sumproduct.com/blog/power-query-keep-on-running/)
. To achieve this, I start by adding an Index column from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

I’ll start from one \[1\].

![](<Base64-Image-Removed>)

Now, I can create a Custom Column to calculate the running total.

![](<Base64-Image-Removed>)

This gives me the running total.

![](<Base64-Image-Removed>)

I can then add list buffering to stop it from reading the list of amounts every time it calculates a running total field.

![](<Base64-Image-Removed>)

However, now I want to see the running total for each **Tent Type**. The method I will use this week is _specific_ to this dataset. I will look at a more generic method next week.

I start from the **Added Index** step. I need to sort my data by **Tent Type** and then by **Index**.

![](<Base64-Image-Removed>)

Having done both sorts, my data is ready for the next step.

![](<Base64-Image-Removed>)

I am going to use similar **M** code to the overall running total, which was:

_**\= List.Sum(List.Range(#”Buffered List”,0, \[Index\])))**_

However, this time I want the values in **\[Index\]** to only increment within each **Tent Type**, and instead of using an offset of zero, I will offset to read the values for each **Tent Type**.

I start by creating a new Index column from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

Next, I set up the column I will be using as the offset in my calculation. From the ‘Add Column’ tab, I insert a column which is **Index.1** divided by seven \[7\].

![](<Base64-Image-Removed>)

I just need to tidy up these columns now. Using the Transform tab, I apply modulo seven \[7\] to **Index.1**, and add one \[1\] to it. I also round down **Division**.

![](<Base64-Image-Removed>)

Now I am ready to apply the list functions to get my running totals.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= List.Sum(List.Range(#”Added to Column”\[Amount\],\[Division\]\*7,\[Index.1\]))**

I am summing up the amounts for my data in groups of seven \[7\].

![](<Base64-Image-Removed>)

The amounts are correct. I can sort by the original **Index** to restore the order and remove the columns I used to work towards the result.

![](<Base64-Image-Removed>)

Next time I will look at another method, which doesn’t rely on the data being in groups of seven \[7\].

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-totals-by-type/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-totals-by-type/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-totals-by-type/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-totals-by-type/#0)

[](https://sumproduct.com/blog/power-query-totals-by-type/#0 "close")

top