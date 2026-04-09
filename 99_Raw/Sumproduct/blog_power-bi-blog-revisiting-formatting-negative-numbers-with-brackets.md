# Power BI Blog: Revisiting Formatting Negative Numbers with Brackets

**Source:** https://sumproduct.com/blog/power-bi-blog-revisiting-formatting-negative-numbers-with-brackets/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Revisiting Formatting Negative Numbers with Brackets

*   October 21, 2020

Power BI Blog: Revisiting Formatting Negative Numbers with Brackets
===================================================================

Power BI Blog: Revisiting Formatting Negative Numbers with Brackets
===================================================================

22 October 2020

_Welcome back to this week’s edition of the Power BI blog series. This week, we look how to format negative currency values, including those infernal brackets._

We are finally going to take a break from my card example; let’s give that a rest for the time being. This week, we are going to revisit a blog we wrote about a while back, how to format negative values with brackets.

The previous blog about how to format negative values can be found [here](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-conditionally-formatting-brackets-with-negatives)
. As a quick recap, we had to use a separate measure that uses the **FORMAT** function to achieve the brackets around negative number format. As reference, here is a snippet of the code used in the measure:

**(Total Profit) Formatted =**

**FORMAT(**

        **\[Total Profit\],**

        **“##,###  ; (##,###) ; -“**

    **)**

If you recognise the formatting code style, it is because it is the same code we would use in Excel (please see [Number Formatting](https://www.sumproduct.com/thought/number-formatting)
 for more information).

For example, we have the ‘Total Profit’ measure here, which is currently formatted as a ‘Whole Number’:

![](<Base64-Image-Removed>)

To change its format, we click on the measure in the Fields list on the right pane:

![](<Base64-Image-Removed>)

With the ‘Total Profit’ measure selected, navigate to the ‘Measure Tools’ tab on the Ribbon. Then, in the Formatting group, click on the Format dropdown, but instead of choosing an option, we can type the following:

**##,###  ; (##,###)**

![](<Base64-Image-Removed>)

The resulting formatting change should look like this:

![](<Base64-Image-Removed>)

No need for any fancy **FORMAT** function here, just a change in the formatting options!

That’s it for this week! Come back next week for more on Power BI!

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-revisiting-formatting-negative-numbers-with-brackets/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-revisiting-formatting-negative-numbers-with-brackets/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-revisiting-formatting-negative-numbers-with-brackets/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-revisiting-formatting-negative-numbers-with-brackets/#0)

[](https://sumproduct.com/blog/power-bi-blog-revisiting-formatting-negative-numbers-with-brackets/#0 "close")

top