# Power Query: Riveting Results Part 7

**Source:** https://sumproduct.com/blog/power-query-riveting-results-part-7/

---

[Home](https://sumproduct.com/)

\> Power Query: Riveting Results Part 7

*   January 25, 2022

Power Query: Riveting Results Part 7
====================================

Power Query: Riveting Results Part 7
====================================

26 January 2022

_Welcome to our Power Query blog. This week, I insert parameters from Excel cells into my query._

My salespeople are in self-isolation. This week, I continue looking at the exam results I created in [Power Query: Riveting Results Part 1](https://sumproduct.com/blog/power-query-riveting-results-part-1/)
:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-74.jpg)

I will be grading the results, and I will be using this example to explore parameters. [Last week](https://sumproduct.com/blog/power-query-riveting-results-part-6/)
, I defined named cells for the other grading bands and created queries for each band:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-102.jpg)

I will now apply these parameters to the **Exam Results** query and check that any changes to the Excel cells affect the outcome of the query.

I return to the **Exam Results** query.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-78.jpg)

The easiest way to change the query to use the Excel controlled parameters is by editing in the Advanced Editor, which I can access from the Home tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-72.jpg)

The ‘Assigned Grade’ step is changed from:

**#”Assigned Grade” =**

    **Table.AddColumn(#”Changed Type”, “Grade”, each**

        **if      \[Result\] > P\_Grade\_9 then 9**

        **else if \[Result\] > P\_Grade\_8 then 8**

        **else if \[Result\] > P\_Grade\_7 then 7**

        **else if \[Result\] > P\_Grade\_6 then 6**

        **else if \[Result\] > P\_Grade\_5 then 5**

        **else if \[Result\] > P\_Grade\_4 then 4**

        **else if \[Result\] > P\_Grade\_3 then 3**

        **else “Ungraded”)**

to

**#”Assigned Grade” =**

    **Table.AddColumn(#”Changed Type”, “Grade”, each**

        **if      \[Result\] > DP\_Grade\_9 then 9**

        **else if \[Result\] > DP\_Grade\_8 then 8**

        **else if \[Result\] > DP\_Grade\_7 then 7**

        **else if \[Result\] > DP\_Grade\_6 then 6**

        **else if \[Result\] > DP\_Grade\_5 then 5**

        **else if \[Result\] > DP\_Grade\_4 then 4**

        **else if \[Result\] > DP\_Grade\_3 then 3**

        **else “Ungraded”)**

This works because each ‘**DP\_**‘ query represents one value:

![](<Base64-Image-Removed>)

This currently has no effect on the results of the query, since the values are the same:

![](<Base64-Image-Removed>)

However, it does have an effect on the screen accessed by clicking on the cog (gear icon) next to the ‘Assigned Grade’ step:

![](<Base64-Image-Removed>)

Note that I cannot view the **Value** column now. Any changes must be made directly to the **M** code, either from the Advanced Editor or the Formula Bar:

![](<Base64-Image-Removed>)

Back in Excel, if I change the Named cell **Grade\_3** from 30 to 20 percent, the outcome will change when I refresh the **Exam Results** query:

![](<Base64-Image-Removed>)

If I go back to **Exam Results** and view all the data, I can see that everyone has passed now!

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-riveting-results-part-7/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-riveting-results-part-7/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-riveting-results-part-7/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-riveting-results-part-7/#0)

[](https://sumproduct.com/blog/power-query-riveting-results-part-7/#0 "close")

top