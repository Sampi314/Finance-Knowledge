# Power Query: Riveting Results Part 6

**Source:** https://sumproduct.com/blog/power-query-riveting-results-part-6/

---

[Home](https://sumproduct.com/)

\> Power Query: Riveting Results Part 6

*   January 18, 2022

Power Query: Riveting Results Part 6
====================================

Power Query: Riveting Results Part 6
====================================

19 January 2022

_Welcome to our Power Query blog. This week, I complete the creation of the parameters from Excel cells._

My salespeople are furloughed. This week, I continue looking at the exam results I created in [Power Query: Riveting Results Part 1](https://sumproduct.com/blog/power-query-riveting-results-part-1/)
:

![](<Base64-Image-Removed>)

I will be grading the results and I will be using this example to explore parameters. [Last week](https://sumproduct.com/blog/power-query-riveting-results-part-5/)
, I created a query from an Excel cell, which I will use as a parameter.

![](<Base64-Image-Removed>)

I now define names for all the cells that I want to use as parameters:

![](<Base64-Image-Removed>)

If I go to the **DP\_Grade\_9** query in the Power Query Editor, I can view the Source step:

![](<Base64-Image-Removed>)

I ‘Refresh Preview’, using the option on the Home tab:

![](<Base64-Image-Removed>)

I notice that the other named cells now appear:

![](<Base64-Image-Removed>)

I can create a duplicate of **DP\_Grade\_9**:

![](<Base64-Image-Removed>)

I can use this as a template to create the other queries:

![](<Base64-Image-Removed>)

I have renamed the duplicate query, and I click on the cog next to ‘Filtered Rows’ to amend the value of **Name** selected to ‘Grade\_8’. Note that the step ‘Grade\_9’ will also need to be edited, as I will see as soon as I click OK and move to that step.

![](<Base64-Image-Removed>)

This step is trying to expand the **Content** column which corresponds to the **Name** ‘Grade\_9’. The **M** code is:

**\= #”Filtered Rows”{\[Name=”Grade\_9″\]}\[Content\]**

I can change this to:

**\= #”Filtered Rows”{\[Name=”Grade\_8″\]}\[Content\]**

![](<Base64-Image-Removed>)

I have the correct result, but I should also right-click on the step and change the name to avoid confusion:

![](<Base64-Image-Removed>)

I have completed this query:

![](<Base64-Image-Removed>)

I repeat this process for the other named cells:

![](<Base64-Image-Removed>)

Next time, I will apply these parameters to the **Exam Results** query and check that any changes to the Excel cells affect the outcome of the query.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-riveting-results-part-6/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-riveting-results-part-6/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-riveting-results-part-6/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-riveting-results-part-6/#0)

[](https://sumproduct.com/blog/power-query-riveting-results-part-6/#0 "close")

top