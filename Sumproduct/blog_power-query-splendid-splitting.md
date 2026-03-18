# Power Query: Splendid Splitting

**Source:** https://sumproduct.com/blog/power-query-splendid-splitting/

---

[Home](https://sumproduct.com/)

\> Power Query: Splendid Splitting

*   May 22, 2018

Power Query: Splendid Splitting
===============================

Power Query: Splendid Splitting
===============================

23 May 2018

_Welcome to our Power Query blog. This week, I look at splitting data using a variety of delimiters._

I have some data for my ever-reliable fictional salespeople. As usual, the data is not in a format I would like!

![](https://sumproduct.com/wp-content/uploads/2025/05/2a82f80345863514269add809d4e49e5.jpg)

Basically, I have a list of which salespeople are attending sales conferences and who is in charge at each one. Naturally, I’d like to put this data into a more useful table. What I would prefer is a list of pairings. I need to make sure I have a way of identifying which data is my sales conference location, which I why I have put ‘Location:’ before each city. I start by creating a query ‘From Table’ in the ‘Get and Transform’ section on the ‘Data’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/4a98901f9b8c71431eb24e4c73dcd15f.jpg)

I want to convert this data into a list of pairings, and the best way for me to do this is to tell Power Query what the delimiter is. However, I don’t want to actually split the column up at this point, so I won’t be using the ‘Split Column’ on the UI (user interface). Instead, I will be using some **M** code. The function I am using is

**Table.TransformColumns(table** **as** **table, transformOperations** **as** **list,** **optional** **defaultTransformation** **as** **nullable** **function****,** **optional** **missingField** **as** **nullable number)** **as** **table**

I have a similar step already created for me to change the type (shown on the previous screenshot), so I can work out what my function needs to be.

**\= Table.TransformColumns(#”Changed Type”, {{“Sales Conferences”, Splitter.SplitTextBy Delimiter(“, “), type text}})**

This converts each of my column entries into a list as shown below:

![](<Base64-Image-Removed>)

Now I need to extend this so that I have a long list, with all my lists contained within. In order to do this, I convert my table to a list in the ‘Transform’ tab.

![](<Base64-Image-Removed>)

My data is now a list of lists, and I need to convert it back to a table so that I can have one long list. This is made possible by the ability to expand the data, as I will show shortly.

![](<Base64-Image-Removed>)

I don’t need a delimiter for this part, so I take the defaults.

![](<Base64-Image-Removed>)

Now I have my table again, but I have the option to expand my columns, allowing me to view my separated data in one long column.

![](<Base64-Image-Removed>)

Once I ‘Expand to New Rows’ I can see all of my data.

![](<Base64-Image-Removed>)

I need to pull out the sales conference locations and to do this I create a ‘Conditional Column’ from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

This new column will be populated with my location if the text contains ‘Location:’

![](<Base64-Image-Removed>)

I can right click on my new column and ‘Fill Down’.

![](<Base64-Image-Removed>)

This is starting to look like my goal. Now I may swap my columns around and remove anything where **_Column1_** contains ‘Location:’. I then rename **_Column1_**.

![](<Base64-Image-Removed>)

I decide that the ‘Location:’ has been useful to identify the cities, but now it has to go! I split the column by delimiter (right click or use the transform menu).

![](<Base64-Image-Removed>)

I can now get rid of the **Location.1** column and rename the other location column. I ‘Close & Load’ to Excel.

![](<Base64-Image-Removed>)

Now to test my query. In my original Excel data, I try adding a new location (Leeds) and a new salesperson ‘Sam’, who will attend the conferences in Leeds and London.

![](<Base64-Image-Removed>)

After refreshing my query, the new salesperson Sam appears in both locations:

![](<Base64-Image-Removed>)

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-splendid-splitting/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-splendid-splitting/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-splendid-splitting/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-splendid-splitting/#0)

[](https://sumproduct.com/blog/power-query-splendid-splitting/#0 "close")

top