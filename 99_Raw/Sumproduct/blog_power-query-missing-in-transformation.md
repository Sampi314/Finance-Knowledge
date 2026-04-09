# Power Query: Missing in Transformation

**Source:** https://sumproduct.com/blog/power-query-missing-in-transformation/

---

[Home](https://sumproduct.com/)

\> Power Query: Missing in Transformation

*   June 9, 2020

Power Query: Missing in Transformation
======================================

Power Query: Missing in Transformation
======================================

10 June 2020

_Welcome to our Power Query blog. This week, I look at a method to make column transformations more dynamic._

John, one of my imaginary salespeople, has been busy submitting his expenses. I used this same data in [Dynamic Removals](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-dynamic-removals)
, but this time, I am using another method to dynamically transform my columns.

![](<Base64-Image-Removed>)

I extract my data to Power Query using ‘From Table’ in the ‘Get & Transform’ section of the Data tab.

_![](<Base64-Image-Removed>)_

I change the data type on **Amount**, **Card**, **Cash**, **Mike** and **Cheque** to ‘Currency’.

![](<Base64-Image-Removed>)

I do this by selecting my columns and setting the Datatype on the Transform tab.

![](<Base64-Image-Removed>)

I rename this step ‘Change to Currency’, as I am going to show what happens if John doesn’t have a column for **Mike**. I close and load this query and go back to my original worksheet:

![](<Base64-Image-Removed>)

I remove the **Mike** column and return to my query.

![](<Base64-Image-Removed>)

As expected, I get an error. This is because the **M** code in the ‘Change to Currency’ step refers to **Mike**:

**\= Table.TransformColumnTypes(#”Source”,{{“Amount”, Currency.Type}, {“Card”, Currency.Type}, {“Cash”, Currency.Type}, {“Mike”, Currency.Type}, {“Cheque”, Currency.Type}})**

I am going to create a function that will only transform columns if they exist. To do this, I create a new blank query. I can do this from the Excel workbook by choosing ‘Blank Query’ in the ‘From Other Sources’ section of ‘New Query’ in the ‘Get & Transform’ grouping of the Data tab.

![](<Base64-Image-Removed>)

In the Advance Editor, I add the following **M** code:

**(table as table,**

 **typeTransformations as list,**

 **optional culture as nullable text) as table =>**

**List.Accumulate(**

    **typeTransformations,**

    **{},**

    **(x, y) => try Table.TransformColumnTypes(table, y, culture)**

              **otherwise x**

**)**

This means that I only try and transform the column **_if_** it exists. This will work for any column transformation I wish to apply.

![](<Base64-Image-Removed>)

I call the function **DynamicTransform**.

I go back to the query which gave an error for the missing **Mike** column and adjust the **M** code in the ‘Change to Currency’ step:

![](<Base64-Image-Removed>)

Instead of using **Table.TransformColumnTypes**, I use my new function:

**\= DynamicTransform(#”Source”,{{“Amount”, Currency.Type}, {“Card”, Currency.Type}, {“Cash”, Currency.Type}, {“Mike”, Currency.Type}, {“Cheque”, Currency.Type}})**

And now, the error does not occur:

![](<Base64-Image-Removed>)

I now have a dynamic way to apply changes to John’s columns even if some of them are missing.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-missing-in-transformation/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-missing-in-transformation/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-missing-in-transformation/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-missing-in-transformation/#0)

[](https://sumproduct.com/blog/power-query-missing-in-transformation/#0 "close")

top