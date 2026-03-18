# Power Query: Not Your Type

**Source:** https://sumproduct.com/blog/power-query-not-your-type/

---

[Home](https://sumproduct.com/)

\> Power Query: Not Your Type

*   November 26, 2019

Power Query: Not Your Type
==========================

Power Query: Not Your Type
==========================

27 November 2019

_Welcome to our Power Query blog. This week, I look at assigning types to columns._

Setting the data types when transforming data in Power Query is important. Data type specific functions, such as **M** date functions, will not work correctly if the data does not have the expected data type.

![](<Base64-Image-Removed>)

When I extract data into Power Query, algorithms are used to determine the most appropriate data type. On the previous screen, this step is called ‘Changed Type’. The **M** code used is

**\= Table.TransformColumnTypes(Source,{{“Name “, type text}, {“Employee Number”, Int64.Type}})**

This sets my **_Name_** column to data type text and my **_Employee Number_** column to data type whole number.

I can change the data type from the ‘Home’ tab or ‘Transform’ tab:

![](<Base64-Image-Removed>)

If I decide to change the type, I have the option of changing the ‘Changed Type’ step or by creating a new step, _viz._

![](<Base64-Image-Removed>)

If I create a new step, I can see the **M** code that Power Query uses to change the type.

![](<Base64-Image-Removed>)

The **M** code is

**\= Table.TransformColumnTypes(#”Changed Type”,{{“Employee Number”, type text}})**

I can also use **M** code to set the data types myself. I start by creating the table.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Table.FromRecords({ \[Name = “Mary”, Employee\_Number = 1\], \[Name = “Paul”, Employee\_Number = 18\], \[Name = “John”, Employee\_Number = 18\], \[Name = “Newbie”, Employee\_Number = 150\]} )**

I have not defined data types, so both columns have type ‘Any’. I can add a step to change this.

![](<Base64-Image-Removed>)

The **M** code I have used is

**\= type table\[Name = text, Employee\_Number = number\]**

![](<Base64-Image-Removed>)

This has created a table type. I need another step to assign this type to my table:

![](<Base64-Image-Removed>)

The **M** code I have used is

**\= Value.ReplaceType(Source, Custom1)**

![](<Base64-Image-Removed>)

My **_Name_** column is now text and the **_Employee\_Number_** column is a number.

I have achieved my goal in three steps, but I can do it in two. For that, I need to be able to specify the types when creating my table.

![](<Base64-Image-Removed>)

I have entered a step to create the types for my table (before I specify the data). The **M** code is

**\= type table\[Name = text, Employee\_Number = number\]**

![](<Base64-Image-Removed>)

Next, I need to provide the data to populate the table.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= #table(Source,{{“Mary”,1},{“Paul”,18},{“John”,15},{“Newbie”,150}})**

![](<Base64-Image-Removed>)

My table has the correct column data types. I can combine these steps and achieve this in one more complicated step.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= #table(type table\[Name = text, Employee\_Num = number\],{{“Mary”,1},{“Paul”,18},{“John”,15},{“Newbie”,150}})**

I can also use **Table.FromColumns**, which accepts the table types as the second parameter.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Table.FromColumns({{“Mary”, “Paul”, “John”, “Newbie”},{1,18,15,150}},type table \[Name = text, Employee\_Number = number\])**

![](<Base64-Image-Removed>)

My columns have the correct data type.

There are some disadvantages to declaring data types in this way which I will look at next time.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-not-your-type/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-not-your-type/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-not-your-type/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-not-your-type/#0)

[](https://sumproduct.com/blog/power-query-not-your-type/#0 "close")

top