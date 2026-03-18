# Power Query: Simply Conditional

**Source:** https://sumproduct.com/blog/power-query-simply-conditional/

---

[Home](https://sumproduct.com/)

\> Power Query: Simply Conditional

*   August 18, 2020

Power Query: Simply Conditional
===============================

Power Query: Simply Conditional
===============================

19 August 2020

_Welcome to our Power Query blog. This week I look at a method to conditionally replace values efficiently._

I have the following tent data:

![](<Base64-Image-Removed>)

I want to add a prefix to the data in my Awning column, which is dependent on the value in that column, viz.

*   Blank: N/A
*   Standard or Dining: Fixed
*   Budget: (No prefix)
*   Package or Kids: Variable.

I begin by extracting my data to Power Query using ‘From Table’ on the ‘New Query’ section of the ‘Get & Transform’ section on the Data tab.

![](<Base64-Image-Removed>)

I accept the defaults.

![](<Base64-Image-Removed>)

I could use a custom column to achieve my required result:

![](<Base64-Image-Removed>)

The **M** code I have used is:

**if \[Awning\] is null then “N/A ”**

**else if \[Awning\] = “Package” or \[Awning\]= “Kids” then “Variable ” & \[Awning\]**

**else  if \[Awning\] = “Standard” or \[Awning\] = “Dining” then “Fixed ” & \[Awning\]**

**else \[Awning\]**

When I click ‘OK’, I get my new column:

![](<Base64-Image-Removed>)

Taking the ‘**if**‘ statement I used, I can do this another way, by using ‘Replace values’.

![](<Base64-Image-Removed>)

I am going to start by creating a simple ‘Replace values’ statement by replacing _null_ with ‘N/A’:

![](<Base64-Image-Removed>)

When I click ‘OK’, the _null_ values are replaced.

![](<Base64-Image-Removed>)

More importantly, the **M** code for this step has been generated:

**\= Table.ReplaceValue(#”Changed Type”,null,”N/A”,Replacer.ReplaceValue,{“Awning”})**

I need to change this so that I can apply a change to every row, so instead of _null_, I am going to use **‘each \[Awning\]’**:

**\= Table.ReplaceValue(#”Changed Type”,each \[Awning\], “N/A”,Replacer.ReplaceValue,{“Awning”})**

I am now going to replace ‘N/A’ with the ‘**if**‘ statement I used earlier, prefixed by ‘**each**‘ as I am applying it to each row.

**\= Table.ReplaceValue(#”Changed Type”,each \[Awning\], each if \[Awning\] is null then “N/A ”**

**else if \[Awning\] = “Package” or \[Awning\]= “Kids” then “Variable ” & \[Awning\]**

**else  if \[Awning\] = “Standard” or \[Awning\] = “Dining” then “Fixed ” & \[Awning\]**

**else \[Awning\]**

**,Replacer.ReplaceValue,{“Awning”})**

![](<Base64-Image-Removed>)

When I click the tick next to my amended step, I can see the results.

![](<Base64-Image-Removed>)

I have applied a conditional change in my column without the need for an extra column.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-simply-conditional/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-simply-conditional/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-simply-conditional/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-simply-conditional/#0)

[](https://sumproduct.com/blog/power-query-simply-conditional/#0 "close")

top