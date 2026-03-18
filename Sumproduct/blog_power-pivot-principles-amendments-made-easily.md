# Power Pivot Principles: Amendments Made Easily

**Source:** https://sumproduct.com/blog/power-pivot-principles-amendments-made-easily/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Amendments Made Easily

*   February 15, 2021

Power Pivot Principles: Amendments Made Easily
==============================================

Power Pivot Principles: Amendments Made Easily
==============================================

16 February 2021

_Welcome back to the Power Pivot Principles blog. This week, we’ll continue last week’s example, which we are going to turn into a large case study over the next few weeks._

From small acorns, large oak trees grow…

Let me remind you we that we calculated a **Sales** measure [last week](https://www.sumproduct.com/blog/article/power-pivot-principles/power-pivot-principle-calculating-measures)
.

![](<Base64-Image-Removed>)

Silly me, I almost forgot that the **sales transactions** included in our budget were inclusive of **GST** of 10%. Let’s put that right.

I know you are still wondering about the recalculating the **Sales** measure. But hey, do not forget how easy it is to edit measures in Power Pivot. I have already highlighted my amendment of the measure below and it should make sense to you.

**\=CALCULATE(-SUM(Budget\[Amount\])****/1.1****, COA\[Group\] = “P”)**

![](<Base64-Image-Removed>)

On pressing OK, we now have the correct sales figure:

![](<Base64-Image-Removed>)

It was not that hard to make this small yet important amendment. Additionally, we might as well calculate the **Gross Profit** now that we have the correct **Sales** figure and is shown below.

**\=\[Total Sales\] – \[Cost of Goods Sold (COGS)\]**

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

It is clear to see that the numbers flow through.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-amendments-made-easily/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-amendments-made-easily/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-amendments-made-easily/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-amendments-made-easily/#0)

[](https://sumproduct.com/blog/power-pivot-principles-amendments-made-easily/#0 "close")

top