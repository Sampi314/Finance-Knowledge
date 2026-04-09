# Power Query: Riveting Results Part 3

**Source:** https://sumproduct.com/blog/power-query-riveting-results-part-3/

---

[Home](https://sumproduct.com/)

\> Power Query: Riveting Results Part 3

*   December 28, 2021

Power Query: Riveting Results Part 3
====================================

Power Query: Riveting Results Part 3
====================================

29 December 2021

_Welcome to our Power Query blog. This week, I add the parameters I created last week to the query from the week before._

My salespeople are having a big break. This week, I continue looking at the exam results I created in [Power Query: Riveting Results Part 1](https://sumproduct.com/blog/power-query-riveting-results-part-1/)
:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-86.jpg)

I will be grading the results, and I will be using this example to explore parameters. [Last week](https://sumproduct.com/blog/power-query-riveting-results-part-2/)
, I created the parameters:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-120.jpg)

I can now edit the original query using the Advanced Editor, which I access from the Home tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-88.jpg)

I change the **M** code in the ‘Added Conditional Column’ step from:

**Table.AddColumn(#”Changed Type”, “Grade”, each**

        **if      \[Result\] > 90 then 9**

        **else if \[Result\] > 80 then 8**

        **else if \[Result\] > 70 then 7**

        **else if \[Result\] > 60 then 6**

        **else if \[Result\] > 50 then 5**

        **else if \[Result\] > 40 then 4**

        **else if \[Result\] > 30 then 3**

        **else “Ungraded”)**

to

**Table.AddColumn(#”Changed Type”, “Grade”, each**

        **if      \[Result\] > P\_Grade\_9 then 9**

        **else if \[Result\] > P\_Grade\_8 then 8**

        **else if \[Result\] > P\_Grade\_7 then 7**

        **else if \[Result\] > P\_Grade\_6 then 6**

        **else if \[Result\] > P\_Grade\_5 then 5**

        **else if \[Result\] > P\_Grade\_4 then 4**

        **else if \[Result\] > P\_Grade\_3 then 3**

        **else “Ungraded”)**

I can use the Intellisense to make sure I enter the correct name for each parameter:

![](<Base64-Image-Removed>)

I also rename the step to ‘Assigned Grade’:

![](<Base64-Image-Removed>)

I click ‘Done’ to make sure that the query still works as I expect:

![](<Base64-Image-Removed>)

Next time, I will look at how to create parameters I can control from Excel.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-riveting-results-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-riveting-results-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-riveting-results-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-riveting-results-part-3/#0)

[](https://sumproduct.com/blog/power-query-riveting-results-part-3/#0 "close")

top