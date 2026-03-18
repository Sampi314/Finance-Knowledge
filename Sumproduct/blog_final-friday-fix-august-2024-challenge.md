# Final Friday Fix: August 2024 Challenge

**Source:** https://sumproduct.com/blog/final-friday-fix-august-2024-challenge/

---

[Home](https://sumproduct.com/)

\> Final Friday Fix: August 2024 Challenge

*   August 29, 2024

Final Friday Fix: August 2024 Challenge
=======================================

Final Friday Fix: August 2024 Challenge
=======================================

30 August 2024

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

**_The Challenge_**

Suppose we are forecasting our company’s sales 10 years in advance. We have specific sales estimates out to Year 5, but after that, we are simply provided with a growth rate. We want a formula that will simply calculate the sales for any particular period.

However, there’s a twist. For any period, we can apply a sales discount, which will discount the sales by a set value. Additionally, it’s important to note that the first period will always just take the value in the **Sales** row less the sales discount. Finally, in the scenario where we are given both a sales value and a growth rate, the growth rate will override the value whilst in the scenario where neither are given, sales growth is assumed to be zero \[0\].

We challenge you to find the most efficient formula to calculate the sales for a given period. You can download the question file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/August/sp-sales-forecast---challenge.xlsx)
.

![](<Base64-Image-Removed>)

As always, we have some requirements:

*   the sales discount cannot make the net sales lower than zero \[0\], and is only applied to the period it is specified in, it does not accumulate
*   you must do this with a single Excel formula, although it may be copied across for different periods
*   no **LAMBDA** or **LAMBDA** helper functions (_e.g_. **LET**, **BYROW** or **MAP**) are allowed
*   no Power Query or VBA allowed; this is a formula challenge.

_Sounds easy? Then give it a go. There are various ways you could approach this, see if you can find the most efficient solution. We’ll publish our solution in Monday’s blog. In the meantime, have a great weekend._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/final-friday-fix-august-2024-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/final-friday-fix-august-2024-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/final-friday-fix-august-2024-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/final-friday-fix-august-2024-challenge/#0)

[](https://sumproduct.com/blog/final-friday-fix-august-2024-challenge/#0 "close")

top