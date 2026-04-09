# Power Pivot Principles: Concatenating Filters

**Source:** https://sumproduct.com/blog/power-pivot-principles-concatenating-filters/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Concatenating Filters

*   December 3, 2018

Power Pivot Principles: Concatenating Filters
=============================================

Power Pivot Principles: Concatenating Filters
=============================================

4 December 2018

_Welcome back to our Power Pivot blog. Today, we look at using concatenation with the **FILTER** function to combine filter criteria._

Say we wanted to create a measure that calculates the total sales amount for April 2015 and May 2016 from our data set. How would we do that?

One simple solution would combine two **CALCULATE** functions together:

![](<Base64-Image-Removed>)

That would yield the following:

![](<Base64-Image-Removed>)

A more delicate solution would involve a combination of the **CALCULATE**, **FILTER**, **ALL** and **OR** functions to create the measure.

![](<Base64-Image-Removed>)

Note that we can concatenate two criteria into one by using the ‘&&’ syntax:

‘Calendar'\[Year\]=2015&& ‘Calendar'\[Month Name (Short)\] = **“Apr”****,**

‘Calendar'\[Year\]=2016&&’Calendar'\[Month Name (Short)\]= **“May”**

This allows us to combine the two criteria into one **CALCULATE** function.

![](<Base64-Image-Removed>)

The type of criteria that can be used in this manner is not limited to dates. We can also use **Product Category Keys** and **Standard Costs** criteria in the same manner to build a similar measure.

![](<Base64-Image-Removed>)

This measure yields:

![](<Base64-Image-Removed>)

That’s it for this week, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-concatenating-filters/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-concatenating-filters/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-concatenating-filters/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-concatenating-filters/#0)

[](https://sumproduct.com/blog/power-pivot-principles-concatenating-filters/#0 "close")

top