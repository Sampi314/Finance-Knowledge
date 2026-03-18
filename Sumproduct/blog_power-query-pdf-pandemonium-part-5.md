# Power Query: PDF Pandemonium – Part 5

**Source:** https://sumproduct.com/blog/power-query-pdf-pandemonium-part-5/

---

[Home](https://sumproduct.com/)

\> Power Query: PDF Pandemonium – Part 5

*   October 12, 2021

Power Query: PDF Pandemonium – Part 5
=====================================

Power Query: PDF Pandemonium – Part 5
=====================================

13 October 2021

_Welcome to our Power Query blog. This week, I continue transforming some data that is coming in from a PDF file, turning my attention this week to function development._

You are possibly over the tent business, but it continues to do well, and the UK division maintain their plans to expand the workforce. I have a PDF file, and it contains tables for 10 stores. [Last week](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-4/)
, I created a query which I am planning to convert to a function to transform the **Stores** data.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-122.jpg)

I am ready to create the transformations required and convert this query. I start by getting rid of any empty rows. I can do this by using ‘Remove Blank Rows’ from the Home tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-164.jpg)

This simplifies my table: for this store it is one row, but for other stores there may be more.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-128.jpg)

I need the store information to be a separate column. I can do this by employing the ‘Unpivot Column’ feature from the Transform tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-127.jpg)

I now have a column with the store data, and one for the pay scales and percentage increase of workforce. I will rename these columns later.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-104.jpg)

I need to keep in mind that this function needs to cope with the data for all the stores. This means I need to carry out some replacements:

*   ‘All’ needs to be replaced by ‘A,B,C’
*   ‘ and ‘ needs to be replaced by ‘,’

I can then use comma (,) as my delimiter to split up the pay scales. I begin with ‘Replace Values’ on the ‘Transform’ tab, or else by right-clicking:

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-92.jpg)

First I replace ‘All’:

![](<Base64-Image-Removed>)

Then I replace ‘ and ‘:

![](<Base64-Image-Removed>)

My data is now ready to be split:

![](<Base64-Image-Removed>)

I am going to split the column into pay scales and increase percentage. I can do this by right-clicking, and choosing to ‘Split Column’ ‘By Non-Digit to Digit’:

![](<Base64-Image-Removed>)

This gives me an extra column.

![](<Base64-Image-Removed>)

Now I can split up the pay scales: I will do this using Comma as a Delimiter, and I will choose to ‘Split into Rows’ in the advanced options.

![](<Base64-Image-Removed>)

This gives me more rows:

![](<Base64-Image-Removed>)

I keep the automated ‘Changed Type’ step and rename the columns.

![](<Base64-Image-Removed>)

My query is ready to be converted to a function. I need to parameterise, so I view the **M** code in the Advanced Editor, available from the Home tab.

![](<Base64-Image-Removed>)

The only line I need to change is the Source step. I am going to introduce a parameter **p\_store**, which will receive any of the store columns as a list. The **M** code before the ‘let’ statement will be:

**(p\_store as list) =>**

and the Source step will change from:

**Source = #”Store 1″,**

to:

**Source = p\_store,**

![](<Base64-Image-Removed>)

As soon as I click ‘Done’, Power Query recognises that my query is now a function.

![](<Base64-Image-Removed>)

It is prompting me for a column (field). This means that this function will now create a table from any of the store columns in the **Stores** query.

![](<Base64-Image-Removed>)

I can test the function on **Column1**:

![](<Base64-Image-Removed>)

Invoking this query will give me a table:

![](<Base64-Image-Removed>)

This looks good – next time I will apply this to all the columns with store data in the **Stores** query.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-5/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-5/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-5/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-5/#0)

[](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-5/#0 "close")

top