# Power Pivot Principles: Caution when Negating Formulae

**Source:** https://sumproduct.com/blog/power-pivot-principles-caution-when-negating-formulae/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Caution when Negating Formulae

*   June 4, 2018

Power Pivot Principles: Caution when Negating Formulae
======================================================

Power Pivot Principles: Caution when Negating Formulae
======================================================

5 June 2018

_Welcome back to our Power Pivot blog. Today we discuss negating formulas in Power Pivot._

In our previous blog here, you may recall that we were creating a measure that calculated refunds. Let’s now consider that we want to have that measure be negated. To do this, go to the ‘Power Pivot’ tab on the Ribbon and then click on the ‘Measures’ drop-down menu:

![](<Base64-Image-Removed>)

The ‘Manage Measures’ dialog box will appear, allowing us to select the ‘Refunds’ measure. Next, select the ‘Edit’ button:

![](<Base64-Image-Removed>)

The ‘Refund’ measure will appear, where we can add a negative operator in-front of the formula _viz._

![](<Base64-Image-Removed>)

On some occasions, negating the formula via this method does not seem to work DAX. Further the minus sign – straight after the equals sign – can easily be missed by the unwary. There is a simple, safer option: multiply the entire formula by negative 1 instead:

![](<Base64-Image-Removed>)

That’s it for this week, stay tuned to our [blog](https://www.sumproduct.com/blog)
 for more on Power Pivot. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-caution-when-negating-formulae/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-caution-when-negating-formulae/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-caution-when-negating-formulae/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-caution-when-negating-formulae/#0)

[](https://sumproduct.com/blog/power-pivot-principles-caution-when-negating-formulae/#0 "close")

top