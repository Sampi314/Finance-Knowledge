# Power Query: Example Grading

**Source:** https://sumproduct.com/blog/power-query-example-grading/

---

[Home](https://sumproduct.com/)

\> Power Query: Example Grading

*   September 3, 2019

Power Query: Example Grading
============================

Power Query: Example Grading
============================

4 September 2019

_Welcome to our Power Query blog. Today, I use Column From Examples to help me put my data into grade boundaries._

I have some data for components used in my fictional tent hire business:

![](<Base64-Image-Removed>)

I want to check what category each component falls into. There are several ways of doing this, but today, I want to see how Column From Examples may help me.

![](<Base64-Image-Removed>)

I have created a query for my data using ‘From Table’ on the ‘Get & Transform’ section of the Data tab. On the ‘Add Column’ tab, I have the option to create a ‘Column from Examples’:

![](<Base64-Image-Removed>)

Since I am only interested in grading the deviation, I want to create my column using data from **_Deviation_** only.

![](<Base64-Image-Removed>)

I fill in at least one from each category, and then Power Query provides the **M** code to calculate the grade.

![](<Base64-Image-Removed>)

I can then edit the **M** code to use the correct boundaries:

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Table.AddColumn(#”Renamed Columns”, “Custom”, each if \[Deviation\] >= 0.8 then “Too Big” else if \[Deviation\] >= 0.5 then “Caution” else if \[Deviation\] >= -0.5 then “Pass” else if \[Deviation\] >= -0.8 then “Caution” else “Too Small”, type text)**

This has saved me the job of working out the logic! I may now save this change which will apply the correct boundaries to all of my data.

![](<Base64-Image-Removed>)

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-example-grading/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-example-grading/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-example-grading/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-example-grading/#0)

[](https://sumproduct.com/blog/power-query-example-grading/#0 "close")

top