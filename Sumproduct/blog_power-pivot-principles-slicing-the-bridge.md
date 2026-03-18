# Power Pivot Principles: Slicing the Bridge

**Source:** https://sumproduct.com/blog/power-pivot-principles-slicing-the-bridge/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Slicing the Bridge

*   April 12, 2021

Power Pivot Principles: Slicing the Bridge
==========================================

Power Pivot Principles: Slicing the Bridge
==========================================

13 April 2021

_Welcome back to the Power Pivot Principles blog. This week, we will create a slicer to filter out the summary table._

[Last week](https://www.sumproduct.com/blog/article/power-pivot-principles/power-pivot-principles-how-did-i-bridge-the-gaps)
, I showed you the creation of a bridging table to join two queries with non-unique values. The result from last week is shown below:

![](<Base64-Image-Removed>)

This week, I will [create a slicer](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-slicers)
 for the ‘Account\_Number’ column, to filter selected **Budget** and **Actuals** data. The summary table currently looks like this:

![](<Base64-Image-Removed>)

I thought it best to show you first what NOT to do. Here, I have inserted a slicer using the **Budget** table and then chose an ‘**Account\_Number**‘:

![](<Base64-Image-Removed>)

When I select one of the fields from the slicer, my table looks like the following:

![](<Base64-Image-Removed>)

Notice how only the **Budget** columns are filtered! If I use the **Actuals** query to create my slicer, my summary table would look like this instead:

![](<Base64-Image-Removed>)

Again! But this time only the **Actuals** columns have been filtered. I know this seems confusing, but the solution is straightforward. In order, to filter both **Budget** and **Actuals**, my slicer needs to use the ‘**Account\_Number**‘ field only from the **Bridge** table created. This will then cascade filters into both dependent tables:

![](<Base64-Image-Removed>)

There it is problem solved! Notice how the **Bridge** has multiple uses and advantages. In a nutshell, to filter fields with non-unique values in more than one table, one must link the slicer to the bridging table only. This ensures data filtering works perfectly!

That’s it for this week!

Come back next week to see how we use the disconnected table for performing a sensitivity analysis by staying tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-slicing-the-bridge/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-slicing-the-bridge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-slicing-the-bridge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-slicing-the-bridge/#0)

[](https://sumproduct.com/blog/power-pivot-principles-slicing-the-bridge/#0 "close")

top