# Power Query: Riveting Results Part 10

**Source:** https://sumproduct.com/blog/power-query-riveting-results-part-10/

---

[Home](https://sumproduct.com/)

\> Power Query: Riveting Results Part 10

*   February 15, 2022

Power Query: Riveting Results Part 10
=====================================

Power Query: Riveting Results Part 10
=====================================

16 February 2022

_Welcome to our Power Query blog. This week, I show how the **FilePath** Parameter allows me to change the workbook I extract data from._

My salespeople will be back soon. This week, I continue looking at the exam results I created in [Power Query: Riveting Results Part 1](https://sumproduct.com/blog/power-query-riveting-results-part-1/)
:

![](<Base64-Image-Removed>)

I will be grading the results, and I will be using this example to explore parameters. [Last week](https://sumproduct.com/blog/power-query-riveting-results-part-9/)
, I created ‘**EDP\_Grade\_**‘ parameters, which were extracted from another workbook.

![](<Base64-Image-Removed>)

I can go back to the **Exam Results** query and use these parameters.

![](<Base64-Image-Removed>)

I showed in [Power Query: Riveting Results Part 7](https://sumproduct.com/blog/power-query-riveting-results-part-7/)
 that it is not possible to edit using the cog next to the ‘Assigned Grade’ step to change the parameters, as they are not shown in the dialog unless they are true Power Query parameters. I looked at the difference between Power Query parameters and other queries that can be used as parameters in [Power Query: Riveting Results Part 5](https://sumproduct.com/blog/power-query-riveting-results-part-5/)
.

I use the Advanced Editor, available on the Home tab, to change the **M** code:

![](<Base64-Image-Removed>)

I change the ‘Assigned Grade’ step from this:

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

to this:

**#”Assigned Grade” =**

    **Table.AddColumn(#”Changed Type”, “Grade”, each**

        **if      \[Result\] > EDP\_Grade\_9 then 9**

        **else if \[Result\] > EDP\_Grade\_8 then 8**

        **else if \[Result\] > EDP\_Grade\_7 then 7**

        **else if \[Result\] > EDP\_Grade\_6 then 6**

        **else if \[Result\] > EDP\_Grade\_5 then 5**

        **else if \[Result\] > EDP\_Grade\_4 then 4**

        **else if \[Result\] > EDP\_Grade\_3 then 3**

        **else “Ungraded”)**

This has no immediate effect on the results of the query:

![](<Base64-Image-Removed>)

To show how **FilePath** allows me to point to another workbook, I have another workbook where I have the same Named Cells for grading bands set up. You should note that I must _close_ the Power Query Editor in the workbook containing **Exam Results** before I can edit another workbook, so I ‘Close & Load To’ and choose ‘Connection Only’ for the new ‘**EDP\_Grade\_’** queries and **Base Query**:

![](<Base64-Image-Removed>)

The new workbook I have created has different values for the grading bands:

![](<Base64-Image-Removed>)

The workbook also has a different name and is located in a different folder.

I close the new workbook, and go back to the workbook containing the **Exam Results** query, where I select the **FilePath** parameter in the Queries pane, and use the ‘Manage Parameter’ button to access the dialog:

![](<Base64-Image-Removed>)

I change the ‘Current Value’ to the new workbook name and location:

![](<Base64-Image-Removed>)

When I go back to the **Exam Results** query, the results have changed:

![](<Base64-Image-Removed>)

The results have changed, and it’s not looking good for the class!

Note that if users of the workbook containing **Exam Results** needed to maintain the **FilePath** parameter without editing in Power Query, I could link **FilePath** to a Named Excel Cell in the workbook as I have done for the ‘**DP\_Grade\_**‘ and ‘**EDP\_Grade\_**‘ parameters.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-riveting-results-part-10/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-riveting-results-part-10/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-riveting-results-part-10/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-riveting-results-part-10/#0)

[](https://sumproduct.com/blog/power-query-riveting-results-part-10/#0 "close")

top