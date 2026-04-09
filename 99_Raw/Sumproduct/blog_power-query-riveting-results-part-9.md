# Power Query: Riveting Results Part 9

**Source:** https://sumproduct.com/blog/power-query-riveting-results-part-9/

---

[Home](https://sumproduct.com/)

\> Power Query: Riveting Results Part 9

*   February 8, 2022

Power Query: Riveting Results Part 9
====================================

Power Query: Riveting Results Part 9
====================================

9 February 2022

_Welcome to our Power Query blog. This week, I create parameters from another Excel file._

My salespeople are retraining. This week, I continue looking at the exam results I created in [Power Query: Riveting Results Part 1](https://sumproduct.com/blog/power-query-riveting-results-part-1/)
:

![](<Base64-Image-Removed>)

I will be grading the results, and I will be using this example to explore parameters. [Last week](https://sumproduct.com/blog/power-query-riveting-results-part-8/)
, I created a query as a building block for parameters extracted from another workbook, which I called ‘**Base Query**‘.

![](<Base64-Image-Removed>)

I also created a **FilePath** parameter to store the location of the other workbook:

![](<Base64-Image-Removed>)

Having created the **FilePath** parameter, I return **Base Query**. For me, the **M** code for the Source step is:

**\= Excel.Workbook(File.Contents(“C:UserskathrOneDriveDocumentsSUMPRODUCTPQ BlogBlog 270 Exam Grade Bands.xlsm”), null, true)**

I am going to replace the path with the **FilePath** parameter:

**\= Excel.Workbook(File.Contents(FilePath), null, true)**

This is easier to read, and now I can change the path by changing the **FilePath** parameter.

![](<Base64-Image-Removed>)

I can now select **Base Query** in the Queries panel and right-click to create reference queries which will become the new grade band **Parameters**:

![](<Base64-Image-Removed>)

I rename the first new query **EDP\_Grade\_9**. The Source step points to **Base Query**. I can click on the ‘Table’ text next to **Grade\_9** to expand the data for that row:

![](<Base64-Image-Removed>)

This gives me the data for **Grade\_9** from the workbook, and I can right-click and drill down to the value:

![](<Base64-Image-Removed>)

This gives me the first parameter:

![](<Base64-Image-Removed>)

I can then make more references of **Base Query** and repeat this process to get the other ‘**EDP\_Grade\_**‘ parameters.

![](<Base64-Image-Removed>)

Next time, I will go back to the **Exam Results** query and use these parameters.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-riveting-results-part-9/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-riveting-results-part-9/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-riveting-results-part-9/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-riveting-results-part-9/#0)

[](https://sumproduct.com/blog/power-query-riveting-results-part-9/#0 "close")

top