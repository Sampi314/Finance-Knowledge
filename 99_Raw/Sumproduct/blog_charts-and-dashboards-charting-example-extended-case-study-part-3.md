# Charts and Dashboards: Charting Example – Extended Case Study Part 3

**Source:** https://sumproduct.com/blog/charts-and-dashboards-charting-example-extended-case-study-part-3/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Charting Example – Extended Case Study Part 3

*   September 22, 2022

Charts and Dashboards: Charting Example – Extended Case Study Part 3
====================================================================

Charts and Dashboards: Charting Example – Extended Case Study Part 3
====================================================================

23 September 2022

_Welcome back to our Charts and Dashboards blog series._ _This week, we continue to take a look at an example of a chart, covering some of the intricacies behind the scenes with its workings. This week, we consider custom number formatting further._

[Last week](https://sumproduct.com/blog/charts-and-dashboards-charting-example-extended-case-study-part-2/)
, we looked at the formatting of the assumptions and calculations driving our chart:

![](https://sumproduct.com/wp-content/uploads/2025/05/0853fc8f07b89b559723b7f14de3fbf5.jpg)

But there’s another number formatting trick used in the workings.

![](https://sumproduct.com/wp-content/uploads/2025/05/e194c9c623811b6e8f15b76e126c424f.jpg)

Here, with ‘Gross Margin’ selected, the figures display as percentages – but what if we were to change this to a Metric that we don’t expect to display as a percentage? Let’s use ‘Gross Profit’.

![](https://sumproduct.com/wp-content/uploads/2025/05/26d251e24dbb78aaac179d8ba7a84ea1.jpg)

As you can see, (most of) the numbers aren’t displaying as percentages and that’s not because I’ve changed the formatting between screenshots. We’ve used _conditional_ custom number formatting.

This may be seen by **Home -> Format -> Format Cells…**(**CTRL + 1**):

![](https://sumproduct.com/wp-content/uploads/2025/05/118403698e082e5a457c6afb79b46398.jpg)

If you recall the tables from last week, we can see the code for conditional formatting within the ‘Miscellaneous’ section.

![](https://sumproduct.com/wp-content/uploads/2025/05/72fa71e6639a1cc6f98736eb4ec24e55.jpg)

Here we’ve used the following conditional formatting:

**\[<1\]0.00%;#,##0**

This means that if the number is less than one \[1\], then display it as a percentage to two decimal places, else display it as a whole number with a thousand separator if necessary. However, this does have its limitations. If any Metrics besides our Gross Margin contained a figure less than 1 (including negative values), it would display as a percentage. This is why it’s important to know your data, so that you can understand if this is a viable solution. In this case, Gross Margin is the only graphable variable that will generate values less than 1 in this line. For those of you concerned about COGS, know that we have included the [**ABS** function](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-abs-function)
 in this line to display COGS as a positive number, but more on that later.

That’s it for this week. Come back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-charting-example-extended-case-study-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-charting-example-extended-case-study-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-charting-example-extended-case-study-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-charting-example-extended-case-study-part-3/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-charting-example-extended-case-study-part-3/#0 "close")

top