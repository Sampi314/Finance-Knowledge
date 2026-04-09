# Power Pivot Principles: Drawing a BLANK on Error Traps

**Source:** https://sumproduct.com/blog/power-pivot-principles-drawing-a-blank-on-error-traps/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Drawing a BLANK on Error Traps

*   May 7, 2018

Power Pivot Principles: Drawing a BLANK on Error Traps
======================================================

Power Pivot Principles: Drawing a BLANK on Error Traps
======================================================

8 May 2018

_Welcome back to our Power Pivot blog series. Today we discuss how to include error traps in our measure formulae._

This blog continues from our previous blog on [Measure Creation Practice](https://www.sumproduct.com/)
. Another common measure that we might want to create is a ‘Profit Margin’ measure:

![](https://sumproduct.com/wp-content/uploads/2025/05/4459e64f967c0335588ed6153df626c5.jpg)

Nothing seems to be wrong with this formula, even Power Pivot thinks so. But what if there were no sales in one period? We would get a division by zero error. To avoid the potential error, we can use the **IF** function to provide us with an error trap:

![](https://sumproduct.com/wp-content/uploads/2025/05/b73af42107a26d3e5e622fddaf6d57aa.jpg)

This will return a zero value when the sales are nil. But why report it anyway? We can use the **BLANK** function to further streamline this measure _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/c8883c18b5ecb8d1fadf288fdd4519c5.jpg)

Now the value will be suppressed in the Pivot Table if sales are blank, leading to clearer, more concise reports.

That’s it for this week, stay tuned to our blog page for more on Power Pivot. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-drawing-a-blank-on-error-traps/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-drawing-a-blank-on-error-traps/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-drawing-a-blank-on-error-traps/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-drawing-a-blank-on-error-traps/#0)

[](https://sumproduct.com/blog/power-pivot-principles-drawing-a-blank-on-error-traps/#0 "close")

top