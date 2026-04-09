# Power Query: True Texting

**Source:** https://sumproduct.com/blog/power-query-true-texting/

---

[Home](https://sumproduct.com/)

\> Power Query: True Texting

*   June 5, 2018

Power Query: True Texting
=========================

Power Query: True Texting
=========================

6 June 2018

_Welcome to our Power Query blog. This week, I look at some useful Boolean Text() functions in M._

Cleaning data often involves transforming text strings to ensure they contain consistently formatted information. There are a few **Text()** functions in **M** which are particularly useful. I start this week with some true / false functions, and I will give an example for each one.

**_Text.Contains_**

**Text****.Contains(****string****as** **nullable** **text****, substring** **as****text****,** **optional** **comparer** **as** **nullable** **function****)** **as** **nullable logical**

Returns true if a text value **substring** was found within a text value **string**; otherwise, false.

This function is either true or false, so if a particular word or series of letters exists in a column, the function will be true, otherwise it will be false. This function can be useful in conditional statements where I need to decide how to populate a new column. I give a simple example below, where I want to create a column containing the country:

![](<Base64-Image-Removed>)

I choose to create a new custom column so that I have complete control over the formula that populates my column. I choose ‘Custom Column’ from the ‘Add Column’ tab (I will use this feature for all of my examples).

![](<Base64-Image-Removed>)

The formula I have used is:

 **= if Text.Contains(\[Address\],”US”) then “US” else if Text.Contains(\[Address\], “UK”) then “UK” else “Other”**                                                         

The resulting column extracts the country to make my data more useful and easier to combine with other tables.

![](<Base64-Image-Removed>)

**_Text.Endswith_**

This is also a Boolean (true or false) function.

**Text****.EndsWith(****string****as** **nullable** **text****, substring** **as****text****,** **optional** **comparer** **as** **nullable** **function****)** **as** **nullable logical**

Returns a logical value indicating whether a text value **substring** was found at the end of a **string**.

I have added a new column to my data and I want to know which client subscribed to marketing communication. Note that I can’t just look for the substring ‘subscribed’ as one of my targets changed their mind!

![](<Base64-Image-Removed>)

I add a new custom column from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

This time, the formula is:

**\= if Text.EndsWith(\[Contact\], “subscribed”) then “Yes” else “No”**

![](<Base64-Image-Removed>)

The two clients who are currently subscribing are identified by the new column.

**_Text.StartsWith_**

This is clearly related to the previous function, but this time I am looking for a substring at the beginning of the column.

**Text****.StartsWith(****string****as** **nullable** **text****, substring** **as****text****,** **optional** **comparer** **as** **nullable** **function****)** **as** **nullable logical**

Returns a logical value indicating whether a text value **substring** was found at the beginning of a **string**.

On the query below, I want a column to indicate whether the contact is the manager at their company.

![](<Base64-Image-Removed>)

I create a custom column from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

The formula I have used is:

**\= if Text.StartsWith(\[Position\], “Manager”) then “Yes” else “No”**

![](<Base64-Image-Removed>)

I can now see which managers have been contacted.

**_Text.Length_**

This is not actually a Boolean function, since it returns a length, but it is often used within a Boolean statement, as I show in the following example.

**Text****.Length(****text****as** **nullable** **text****)** **as** **nullable number**

Returns the number of characters in a text value.

On the next screen, I have some (UK) phone numbers, but not all of them include the location code. The easiest way to tell that the full number has not been given is to look at the length of the number.

![](<Base64-Image-Removed>)

I create a custom column from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

The formula I have used is:

**\= if Text.Length(\[Phone\]) < 11 then “No – Check Number” else “Yes”**

![](<Base64-Image-Removed>)

I can now see the numbers that may need further investigation.

Next time I will look at some useful **M** **Text()** functions that can be used to edit the text in a column.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found here. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-true-texting/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-true-texting/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-true-texting/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-true-texting/#0)

[](https://sumproduct.com/blog/power-query-true-texting/#0 "close")

top