# Power Query: Project Population – Part 3

**Source:** https://sumproduct.com/blog/power-query-project-population-part-3/

---

[Home](https://sumproduct.com/)

\> Power Query: Project Population – Part 3

*   May 2, 2023

Power Query: Project Population – Part 3
========================================

Power Query: Project Population – Part 3
========================================

3 May 2023

_Welcome to our Power Query blog. This week, I keep on keeping on the transformation of selected data from a public source._

I have found some information on population growth provided by The World Bank, which I am using as an example of how to transform real-life data.

![](https://sumproduct.com/wp-content/uploads/2025/05/c8f4d74d3dd91801f4fc065ed038dd13.jpg)

I have downloaded the Excel file, and in [Part 1](https://sumproduct.com/blog/power-query-project-population-part-1/)
, I extracted the queries I needed:

![](https://sumproduct.com/wp-content/uploads/2025/05/47928a4c9b79320d95781b1f9c205fb5.jpg)

I reduced the data by selecting only the columns I wanted to keep:

![](https://sumproduct.com/wp-content/uploads/2025/05/ade79e1b5856658e7b1cdfcd417f44d0.jpg)

[Last time](https://sumproduct.com/blog/power-query-project-population-part-2/)
, I identified and removed any unnecessary rows:

![](https://sumproduct.com/wp-content/uploads/2025/05/7b4358c8088524f82761c48f3d4608de.jpg)

I also transformed the **System of National Accounts** column:

![](https://sumproduct.com/wp-content/uploads/2025/05/93070386a844e1b1c9fe61f30e0d59a4.jpg)

I renamed these steps to make it easier to follow the transformations:

![](https://sumproduct.com/wp-content/uploads/2025/05/98b3e3d740f89e6a6ae559513e3558c8.jpg)

This time, I am going to look at the column **Latest Population Census**:

![](https://sumproduct.com/wp-content/uploads/2025/05/6e8c6c0679468a640e6553f306d03fed.jpg)

This column currently contains mixed data types, which is why Power Query has given it a type of ‘Any’. I would like to transform this column into two \[2\] columns, one with the year, and one with any additional notes. On the Transform tab, I choose to split the column ‘By Positions’:

![](https://sumproduct.com/wp-content/uploads/2025/05/a02d6ca8d8cc3568da09861022abd1ea.jpg)

This prompts me for where to split the column, remembering that Power Query counts from zero \[0\]:

![](https://sumproduct.com/wp-content/uploads/2025/05/d1284e9b1ae5a413cca736139734f3dc.jpg)

Clicking on ‘Advanced options’ also indicates how to enter multiple positions to split the data. For this example, I just need to split at position 4, however, if I only enter 4, then the column after position 4 would be retained. In order to preserve the year and have two \[2\] columns, I need to enter ‘0,4’ in the Positions box. I take the default to ‘Split into Columns’.

![](<Base64-Image-Removed>)

This gives me two \[2\] new columns.

![](<Base64-Image-Removed>)

Note that I did not have an option to name my split columns. I can add a step to rename them, but instead I will change the **M** code in the ‘Split Column by Positions’ step:

![](<Base64-Image-Removed>)

I change the code from:

**\= Table.SplitColumn(Table.TransformColumnTypes(#”Changed SNA  
to Number”, {{“Latest population census”, type text}},  
“en-GB”), “Latest population census”,  
Splitter.SplitTextByPositions({0, 4}), {“Latest population census.1”,  
“Latest population census.2”})**

to:

**\= Table.SplitColumn(Table.TransformColumnTypes(#”Changed SNA  
to Number”, {{“Latest population census”, type text}},  
“en-GB”), “Latest population census”,  
Splitter.SplitTextByPositions({0, 4}), {“Latest population census”,  
“Population census notes”})**

![](<Base64-Image-Removed>)

I rename the step, and delete ‘Changed Type1’. It no longer uses the correct column names, and it left **Latest population census** with data type ‘Text’.

![](<Base64-Image-Removed>)

Next time, I will look at why the column **Latest population census** was not assigned a numerical data type.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-project-population-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-project-population-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-project-population-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-project-population-part-3/#0)

[](https://sumproduct.com/blog/power-query-project-population-part-3/#0 "close")

top