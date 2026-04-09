# Power Query: Words are Key

**Source:** https://sumproduct.com/blog/power-query-words-are-key/

---

[Home](https://sumproduct.com/)

\> Power Query: Words are Key

*   August 28, 2018

Power Query: Words are Key
==========================

Power Query: Words are Key
==========================

29 August 2018

_Welcome to our Power Query blog. Last week’s blog looked at how to use list functionality to translate numerical grades into their letter equivalents. This week, I use another List() function to look for multiple keywords in columns of data._

I have a series of comments recorded by my salespeople after attending sales conferences. I would like to analyse the comments to see where there needs to be some follow-up.

![](<Base64-Image-Removed>)

I plan to use the **M** function **List.ContainsAny()**:

**List****.ContainsAny(****list****as****list****, values** **as****list****,optional equationCriteria** **as** **any)** **as** **logical**

This returns true if any item in **values** is found in a **list**.

The first step is to create a list of keywords. I can either do this by creating a manual list from a blank query or I can convert a table. In this case, I will create a table in Excel and then convert it in Power Query.

![](<Base64-Image-Removed>)

I choose ‘From Table’ in the ‘Get & Transform’ section on the ‘Data’ tab.

![](<Base64-Image-Removed>)

Having defined my table, I can now convert it to a list by using the ‘Convert to List’ option in the ‘Any Column’ section on the ‘Transform’ tab.

![](<Base64-Image-Removed>)

I save my list as ‘Connection Only’ from the ‘Close & Load’ dropdown on the ‘Home’ (or ‘File’) tab.

![](<Base64-Image-Removed>)

I can now create a query for my main table.

![](<Base64-Image-Removed>)

As I plan to use a list function, I need to convert the **_Comments_** column to a list. However, if I use the GUI functionality for this, the other columns will disappear:

![](<Base64-Image-Removed>)

Instead, I need to create some functionality in **M** that will treat the **_Comments_** column as a list. Last week, I looked at a function called **Text.Split()**:

**Text****.Split(****string****as****text****, separator** **as****text****)** **as** **list**

This returns a list containing parts of a **string** that are delimited by a **separator** text value.

Before I convert **_Comments_** to a list, I make sure everything is lowercase, so that my comparison will work. I can do this by right-clicking my column and picking the appropriate ‘Transform’ option.

![](<Base64-Image-Removed>)

I can now create a custom column from the ‘Add Column’ section.

![](<Base64-Image-Removed>)

The **M** functionality I have used is

**\= Text.Split(\[Comments\],” “)**

This creates a list of words by splitting at the space.

![](<Base64-Image-Removed>)

I can now create another custom column to compare values.

![](<Base64-Image-Removed>)

The **M** functionality I have used is

**\= List.ContainsAny(\[Comments\_List\], Keywords)**

![](<Base64-Image-Removed>)

I now have a **_Follow-Up_** column that tells me which contact needs further attention.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-words-are-key/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-words-are-key/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-words-are-key/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-words-are-key/#0)

[](https://sumproduct.com/blog/power-query-words-are-key/#0 "close")

top