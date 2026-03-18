# Power Query: ToolTip

**Source:** https://sumproduct.com/blog/power-query-tooltip/

---

[Home](https://sumproduct.com/)

\> Power Query: ToolTip

*   September 15, 2020

Power Query: ToolTip
====================

Power Query: ToolTip
====================

16 September 2020

_Welcome to our Power Query blog. This week, I look at how to use M metadata functions to create a ToolTip for columns._

I looked at some uses for metadata nearly three years ago in [Customising Custom-Built Functions](https://sumproduct.com/blog/power-query-customising-custom-built-functions/)
_._ One of the metadata functions I looked at was:

**Documentation.FieldDescription** as text

_Description to show next to the display name._

As I described in that blog, these functions can be found at [https://msdn.microsoft.com/library/mt807488.aspx](https://msdn.microsoft.com/library/mt807488.aspx)
.

Back then, when I looked at how **Documentation.FieldDescription** could be used, I was making a function I had created more user-friendly; this time, I will use it as I create a table.

I start by creating a new blank query. In Excel on the ‘Data’ tab, I choose ‘New Query’ and select ‘Blank Query’ from the dropdown next to ‘From Other Sources’:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-143-1.jpg)

I can then access the ‘Advanced Editor’ from the Home tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-132-1.jpg)

The **M** code I am going to use will create a simple table of employees.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-123-1.jpg)

The **M** code I have created is:

**let source =**

**#table({“Name”, “Secret”}, {{“Mary Smith”, “67”}}),**

**tableType =**

**type table\[Name = Text.Type, Secret = Number.Type\]**

**meta \[**\
\
**Documentation.FieldDescription =**\
\
**\[Name = “Full Name”, Secret = “Age!”\]**\
\
**\],**

**replaceType = Value.ReplaceType(source, tableType)**

**in**

**replaceType**

In this **M** code, I first create a table by defining my source as an **#table** – for more on this, see [Bring it to the Table](https://sumproduct.com/blog/power-query-bring-it-to-the-table/)
. I then create a **tableType**, where I define the column properties of a table and include the **Documentation.FieldDescription()** function. Finally, I ensure my table uses that **tableType** (using **Value.ReplaceType**).

When I click ‘Done’, I get my table:

![](<Base64-Image-Removed>)

If I hover over the title of **Secret**, I get a ToolTip:

![](<Base64-Image-Removed>)

I can see that the secret column holds Mary’s age (shhh).

There are some limitations to this. For example, if I remove **Name**:

![](<Base64-Image-Removed>)

I find I can no longer see the ToolTip for **Secret**.

![](<Base64-Image-Removed>)

This is because the table type has changed, so the link to the metadata is lost. If I delete this step, I can see the ToolTips again:

![](<Base64-Image-Removed>)

I can also lose the Tooltips on the table if I change the type of one of the columns:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

I should therefore ensure that my **tableType** with metadata functionality is assigned to my table at a point where I am not planning to change anything that affects the **tableType**.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-tooltip/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-tooltip/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-tooltip/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-tooltip/#0)

[](https://sumproduct.com/blog/power-query-tooltip/#0 "close")

top