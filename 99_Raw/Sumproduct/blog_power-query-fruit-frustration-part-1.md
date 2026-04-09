# Power Query: Fruit Frustration – Part 1

**Source:** https://sumproduct.com/blog/power-query-fruit-frustration-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Fruit Frustration – Part 1

*   August 24, 2021

Power Query: Fruit Frustration – Part 1
=======================================

Power Query: Fruit Frustration – Part 1
=======================================

25 August 2021

_Welcome to our Power Query blog. This week, I look at how changing steps can lose data._

This week, I am loading some juicy data into a Query. I have specified an Excel Workbook as the source:

![](<Base64-Image-Removed>)

The **M** code I have used is:

**Source = Excel.Workbook(File.Contents(“C:UserskathrOneDriveDocumentsSUMPRODUCTPQ BlogBlog 247 Fruit Source.xlsm”), null, true)**

(where the file path is personal to me). I want to extract some data out of the **Apples** table, so I filter on ‘Name’:

![](<Base64-Image-Removed>)

This gives me one row. I only want the **Data** column, so I select this, and right click to ‘Remove Other Columns’.

![](<Base64-Image-Removed>)

I can then expand the data:

![](<Base64-Image-Removed>)

I choose all the columns and I don’t need to ‘Use original column name as prefix’:

![](<Base64-Image-Removed>)

Well, that’s all done, I have my apples, so I’ll see you next week. Wait! I changed my mind: I want to squeeze some data out of my **Oranges** table. I need to go back to the ‘Filtered Rows’ step.

![](<Base64-Image-Removed>)

If I click on the cog icon for this step, I can change it.

![](<Base64-Image-Removed>)

I change the dropdown to ‘Oranges’ and click ‘OK’.

![](<Base64-Image-Removed>)

This all looks fine, so I look at the ‘Expanded Data’:

![](<Base64-Image-Removed>)

I have oranges. Well, this is all working nicely, I’ll just check out the bananas next.

![](<Base64-Image-Removed>)

I’ve changed ‘Filtered Rows’ to select **Bananas**, so now I can check the ‘Expanded Data’:

![](<Base64-Image-Removed>)

This is not how to spell banana. Where has the middle column gone? If I click on the gear icon next to ‘Expanded Data’, I can see what has happened:

![](<Base64-Image-Removed>)

One of these columns does not actually exist for **Bananas**. The second column is called **two**, not **2**. If I select **two** and deselect **2**, the data looks correct:

![](<Base64-Image-Removed>)

If I go back to the expand options, there is no longer an option to select **2**.

![](<Base64-Image-Removed>)

So, what happened? A little knowledge is a dangerous thing! Power Query will try to adapt if steps are changed, added or deleted. Since nothing triggered an error, it appears that everything is okay until the user notices the missing column. This can be difficult to spot. This is the **Oranges** table in the source file:

![](<Base64-Image-Removed>)

Although the table looked fine, there was a missing column. Next time I’ll look at what went wrong.

I’ll leave with one final challenge – I haven’t changed anything in the query, but now I have a fetching red line under the columns? Why? The answer is in this blog!

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-fruit-frustration-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-fruit-frustration-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-fruit-frustration-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-fruit-frustration-part-1/#0)

[](https://sumproduct.com/blog/power-query-fruit-frustration-part-1/#0 "close")

top