# Power Query: Power Query Tables Do Not Have to be Green

**Source:** https://sumproduct.com/blog/power-query-power-query-tables-do-not-have-to-be-green/

---

[Home](https://sumproduct.com/)

\> Power Query: Power Query Tables Do Not Have to be Green

*   March 14, 2023

Power Query: Power Query Tables Do Not Have to be Green
=======================================================

Power Query: Power Query Tables Do Not Have to be Green
=======================================================

15 March 2023

_Welcome to our Power Query blog. This week, we change the format of the Table loaded from Power Query._

**Please Note**: Power Query has moved on since this blog was written, and if you would like your Power Query table to have the same default style as a normal table please read [this](https://sumproduct.com/blog/power-query-power-query-tables-dont-have-to-be-green-update/)
.

I have some data for the manager for the upcoming sales conference:

![](<Base64-Image-Removed>)

The manager is happy with the data, but they want to know why some of the Tables are green. You may realise that the default colour for input Tables is blue / white, whereas the default colour scheme for Power Query output Tables is green / white.

I can select each Table by clicking somewhere in it, and then choose the ‘Table styles’ option that matches the other tables (here, I have **Table\_Contains** selected):

![](<Base64-Image-Removed>)

I do this for all the Tables, and choose ‘Refresh All’ from the Data tab to ensure that the formatting is preserved:

![](<Base64-Image-Removed>)

Some of the column widths have changed, but the formatting is fine. We receive the news that Paul is sick, so we have to remove him from the **Selection** table:

![](<Base64-Image-Removed>)

I ‘Refresh All’ twice, once to update the Power Query Tables and again to update the PivotTable.

![](<Base64-Image-Removed>)

Everything is fine, so we’ve solved the problem.

Well, not quite.

The manager wants to add some location data, so I load the query to the same sheet:

![](<Base64-Image-Removed>)

When I click OK, the new Table appears:

![](<Base64-Image-Removed>)

The new Table is green. This means I will need to alter the ‘Table style’ for every new query. Power Query is supposed to save me from repetitive tasks!

There is another way. I return to the original version of the sheet, and go to the ‘Page Layout’ tab:

![](<Base64-Image-Removed>)

The leftmost section is Themes. The Themes icon shows that my current theme is Office. If I click on the ‘Colors’ dropdown, I can see all the Themes I can choose.

![](<Base64-Image-Removed>)

The last colour in the Office palette looks familiar. I choose ‘Customize Colors…’

![](<Base64-Image-Removed>)

‘Accent 6’ is the colour used for Power Query Tables. I change this colour to blue and save my new theme as ‘Power Query’:

![](<Base64-Image-Removed>)

This updates the Power Query Tables.

![](<Base64-Image-Removed>)

Now if I add the Locations Table again:

![](<Base64-Image-Removed>)

The new theme is used. Currently, the theme will only be used for this workbook, but I can select it from the ‘Colors’ dropdown when I am in other workbooks.

![](<Base64-Image-Removed>)

I can also share the saved THMX file with others, and even set it as the default for all new workbooks if I wish.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-power-query-tables-do-not-have-to-be-green/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-power-query-tables-do-not-have-to-be-green/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-power-query-tables-do-not-have-to-be-green/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-power-query-tables-do-not-have-to-be-green/#0)

[](https://sumproduct.com/blog/power-query-power-query-tables-do-not-have-to-be-green/#0 "close")

top