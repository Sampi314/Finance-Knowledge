# Charts and Dashboards: Conditional Chart Labelling – Part 4

**Source:** https://sumproduct.com/blog/charts-and-dashboards-conditional-chart-labelling-part-4/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Conditional Chart Labelling – Part 4

*   March 31, 2022

Charts and Dashboards: Conditional Chart Labelling – Part 4
===========================================================

Charts and Dashboards: Conditional Chart Labelling – Part 4
===========================================================

1 April 2022

_Welcome back to our Charts and Dashboards blog series._ _This week, I take the final step and ensure my solution is sufficiently robust. Anything else would be (April) foolish!_

I have the following chart data:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-47-1.jpg)

“All” I have to do is create the associated Excel chart with replicated label formatting:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-64.jpg)

Do you see the need for _supposed_ conditional formatting in the chart? I require positive values to be blue, zeros to be yellow and negative values to be in red – both labels and fill colours. It is possible, but I need to break the task down into various steps.

Essentially, there are several steps:

1.  Understand how I can create multiple number formats in Excel, never mind in a chart data label
2.  Create the basic chart
3.  Create the formatting in the data labels, realising custom number formatting will not work and conditional formatting may not be applied
4.  Make the solution robust enough to cope with saving the file and re-opening.

[Last week](https://sumproduct.com/blog/charts-and-dashboards-conditional-chart-labelling-part-3/)
, I looked at step 3, where I almost solved everything . This week I move onto step 4, where I ensure my solution is robust. It looks good so far, but there is a problem…

 

**_Step 4: Make the Solution Robust_**

I try closing and saving the file, then re-open. If I make all of the input values (50.00%), I see the following chart:

![](<Base64-Image-Removed>)

Some of my labels have gone missing! Similarly, if I type ‘123’ into all the inputs I get:

![](<Base64-Image-Removed>)

Now I have the missing labels, but the rest have gone instead. Not good!

This is **_soooo_** frustrating! This is a **bug** in Excel. It is still prevalent in Excel 2019 and Excel 2021, plus the latest versions of Microsoft 365. A quick consultation with my favourite search engine tends to lead me to ideas such as saving the chart as a chart template, and creating a macro on opening that will re-apply the chart. Thank you very much; that’s not for me.

It’s not often on these challenges that I cheat quite like I will be doing this time. For this problem, there is a common free, third party add-in that appears to come to the rescue, namely past Excel MVP Rob Bovey’s **XY Chart Labeler** _(sic)_ located at

[http://www.appspro.com/Utilities/ChartLabeler.htm](http://www.appspro.com/Utilities/ChartLabeler.htm)

If your IT administrator will allow you, downloading this add-in allows you to add ‘XY chart labels’ – and these seem to stick. It’s easy to use – all you have to do is add the chart labels and reference the text values using the add-in rather than Excel’s tools.

With no disrespect, maybe eventually Excel will get its own data labelling house in order though:

![](<Base64-Image-Removed>)

I look forward to writing a blog announcing that this is fixed!

That’s it for this week. Come back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-conditional-chart-labelling-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-conditional-chart-labelling-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-conditional-chart-labelling-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-conditional-chart-labelling-part-4/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-conditional-chart-labelling-part-4/#0 "close")

top