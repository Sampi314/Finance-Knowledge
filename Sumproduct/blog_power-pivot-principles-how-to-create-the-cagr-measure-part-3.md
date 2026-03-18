# Power Pivot Principles: How to Create the CAGR Measure, Part 3

**Source:** https://sumproduct.com/blog/power-pivot-principles-how-to-create-the-cagr-measure-part-3/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: How to Create the CAGR Measure, Part 3

*   March 25, 2019

Power Pivot Principles: How to Create the CAGR Measure, Part 3
==============================================================

Power Pivot Principles: How to Create the CAGR Measure, Part 3
==============================================================

26 March 2019

_Welcome back to our Power Pivot blog. We continue on our CAGR series. Today, we shall look into making our CAGR measure more dynamic and discuss additional improvements to the measures._

Last week we left off at a functioning CAGRmeasure (you can read last week’s blog [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-how-to-create-the-cagr-measure-part-2)
). However, it only calculated the CAGR value for the final year in our data. What if we wanted the CAGR measure to be dynamic and calculate the CAGR value for each year we have on our PivotTable?

The reason why our CAGR formula is not calculating dynamically is because we are using the **\[Last Year\]** measure, which is currently set to retrieve the last year in our data set. To avoid confusion, we are going to create a measure that retrieves the current year called **\[Current Year\]**:

\=MAX(‘Calendar'\[Year\])

![](<Base64-Image-Removed>)

Now we modify our **\[CAGR\]** measure to use the **\[Current Year\]** measure:

\=(\[Sales in Current Year\]/\[Sales in First Year\])^(1/\[Number of Years\])-1

![](<Base64-Image-Removed>)

However, attempting to put our CAGR measure in the Pivot Table will result in this error:

![](<Base64-Image-Removed>)

This is because the number of years for the 2018 period is zero, and we can’t divide by zero. In this scenario, we should use the **DIVIDE** function to create our **\[CAGR Dynamic\]** new-and-improved measure. You can read more about the **DIVIDE** function [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-divide-function)
:

\=DIVIDE(

\[Sales in Current Year\],\[Sales in First Year\]

)

^DIVIDE(

1,\[Number of Years\]

)-1

![](<Base64-Image-Removed>)

The **DIVIDE** function manages our division by zero problem by returning with **BLANK()** when the denominator is zero. Therefore, this gives us the dynamic CAGR calculation we require:

![](<Base64-Image-Removed>)

That’s it for this week, happy Pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-how-to-create-the-cagr-measure-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-how-to-create-the-cagr-measure-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-how-to-create-the-cagr-measure-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-how-to-create-the-cagr-measure-part-3/#0)

[](https://sumproduct.com/blog/power-pivot-principles-how-to-create-the-cagr-measure-part-3/#0 "close")

top