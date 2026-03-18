# Power Query: Project Population – Part 5

**Source:** https://sumproduct.com/blog/power-query-project-population-part-5/

---

[Home](https://sumproduct.com/)

\> Power Query: Project Population – Part 5

*   May 16, 2023

Power Query: Project Population – Part 5
========================================

Power Query: Project Population – Part 5
========================================

17 May 2023

_Welcome to our Power Query blog. This week, I complete the first query that I downloaded from a public source._

I have found some information on population growth provided by The World Bank, which I am using as an example of how to transform real-life data.

![](<Base64-Image-Removed>)

I have been transforming the data, and [last week](https://sumproduct.com/blog/power-query-project-population-part-4/)
, I created and tidied the **Latest population census** column.

![](<Base64-Image-Removed>)

I also kept the **Population census notes**, which I need to tidy up. To begin, I move the column after **Latest population census**. I can do this by selecting the column and dragging it to the end, or by right-clicking and choosing to Move ‘To End’:

![](<Base64-Image-Removed>)

I examine the contents of the column by looking at the values on the Filter dialog:

![](<Base64-Image-Removed>)

I need to remove the full stops (**.**) from the beginning of the some of the values. I can do this by using ‘Replace Values’ from the right-click menu:

![](<Base64-Image-Removed>)

When I click OK, my data looks better, but I need to remove the leading spaces:

![](<Base64-Image-Removed>)

I can do this by using ‘Trim’ from the Format dropdown on the Transform tab:

![](<Base64-Image-Removed>)

My data looks better. However, the recent steps are a little ambiguous:

![](<Base64-Image-Removed>)

Renaming them will make it easier to see what I have done:

![](<Base64-Image-Removed>)

Moving on to the **National accounts base year** column, a quick look at the data might suggest that I use the same approach that I used for **Latest population census**, where I converted the column to a number to easily identify any values that are not years in order to remove them.

![](<Base64-Image-Removed>)

However, if I view the values on the Filter dialog, I see that there are combined year values, which cannot be expressed as a number:

![](<Base64-Image-Removed>)

In order to preserve this data, I am going to use a different approach. If the first four \[4\] characters are not numeric, then I want to replace the current value with _null_. I go to the ‘Add Column’ tab, where I choose to Extract ‘First Characters’:

![](<Base64-Image-Removed>)

This takes me to a dialog where I can select the first four \[4\] characters. Note I cannot choose the name of the new column, but as it will be temporary, this doesn’t matter here.

![](<Base64-Image-Removed>)

This gives me a new column **First Characters** containing the first year, which I can change to data type ‘Whole number’:

![](<Base64-Image-Removed>)

This has identified the values that did not contain a year as errors. I can right-click and choose to ‘Replace Errors’. I shall replace them with _null_:

![](<Base64-Image-Removed>)

Now I can add a ‘Conditional Column’ from the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

In the new column name, I have capitalised ‘Accounts’ so that I am not trying to use the same name as the existing column. If the temporary column **First Characters** is _null_ (meaning that **National accounts base year** did not have a year in the value), then the new column is set to _null_, otherwise it will have the same value as **National accounts base year**.

This gives me a new column, and I can delete **National accounts base year** and **First Characters**.

![](<Base64-Image-Removed>)

I tidy up by changing the new column to data type Text, and rename the steps.

![](<Base64-Image-Removed>)

Now that all the columns in this query have consistent data, next time, I will look at the data that I can add from the other queries I imported.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-project-population-part-5/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-project-population-part-5/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-project-population-part-5/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-project-population-part-5/#0)

[](https://sumproduct.com/blog/power-query-project-population-part-5/#0 "close")

top