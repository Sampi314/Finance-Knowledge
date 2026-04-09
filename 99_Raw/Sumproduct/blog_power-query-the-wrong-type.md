# Power Query: The Wrong Type

**Source:** https://sumproduct.com/blog/power-query-the-wrong-type/

---

[Home](https://sumproduct.com/)

\> Power Query: The Wrong Type

*   December 3, 2019

Power Query: The Wrong Type
===========================

Power Query: The Wrong Type
===========================

4 December 2019

_Welcome to our Power Query blog. This week, I look at a problem when assigning data types to columns._

[Last time](https://sumproduct.com/blog/power-query-not-your-type/)
, I looked at several methods for setting the data type when creating a table. I used **Table.FromRecords**, **Table.FromColumns** and **#table**.

To recap, the **Table.FromRecords** method had three steps (which I could combine to two).

![](<Base64-Image-Removed>)

The **M** code I used was:

**\= Table.FromRecords({ \[Name = “Mary”, Employee\_Number = 1\], \[Name = “Paul”, Employee\_Number = 18\], \[Name = “John”, Employee\_Number = 18\], \[Name = “Newbie”, Employee\_Number = 150\]} )**

![](<Base64-Image-Removed>)

The **M** code I used to define the data types was:

**\= type table\[Name = text, Employee\_Number = number\]**

![](<Base64-Image-Removed>)

I created another step to assign this type to my table.

![](<Base64-Image-Removed>)

The **M** code I used was:

**\= Value.ReplaceType(Source, Custom1)**

![](<Base64-Image-Removed>)

Using **#table**, I could refine the table creation to one step:

![](<Base64-Image-Removed>)

The **M** code I used was:

**\= #table(type table\[Name = text, Employee\_Num = number\],{{“Mary”,1},{“Paul”,18},{“John”,15},{“Newbie”,150}})**

I also used **Table.FromColumns**, which accepts the table types as the second parameter.

![](<Base64-Image-Removed>)

The **M** code I used was:

**\= Table.FromColumns({{“Mary”, “Paul”, “John”, “Newbie”},{1,18,15,150}},type table \[Name = text, Employee\_Number = number\])**

![](<Base64-Image-Removed>)

There are some disadvantages to declaring data types in this way. For example, in the next screen, I have entered a step to create a new table.

![](<Base64-Image-Removed>)

There is a deliberate mistake, but when I upload my step, everything looks fine:

![](<Base64-Image-Removed>)

I ‘Close & Load To’ so that I can load my query.

![](<Base64-Image-Removed>)

I decide to ‘Add this data to the Data Model’.

![](<Base64-Image-Removed>)

I can view the error in Excel, and correct it using the dropdown.

![](<Base64-Image-Removed>)

But that does not solve the issue with the data model.

![](<Base64-Image-Removed>)

I have four rows loaded and one error. I try clicking on ‘1 error’ to see what has happened.

![](<Base64-Image-Removed>)

Not very useful!

In my simple example, I know that one row has failed to load because I put “15” instead of 15 as John’s employee number. However, in a long list of data, this would be hard to spot. The error doesn’t appear because the query doesn’t have an error flagged. This is the problem when I manually define the column types in the table.

When I go to look at the Data Model (from the ‘Power Pivot’ tab) there is no data loaded!

![](<Base64-Image-Removed>)

If I am defining datatypes for columns manually, I need to bear in mind that I am bypassing the checks that Power Query uses. This functionality should be used with caution.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-the-wrong-type/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-the-wrong-type/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-the-wrong-type/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-the-wrong-type/#0)

[](https://sumproduct.com/blog/power-query-the-wrong-type/#0 "close")

top