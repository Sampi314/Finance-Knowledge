# Power Query: Power Query Tables Don’t Have to be Green UPDATE

**Source:** https://sumproduct.com/blog/power-query-power-query-tables-dont-have-to-be-green-update/

---

[Home](https://sumproduct.com/)

\> Power Query: Power Query Tables Don’t Have to be Green UPDATE

*   May 23, 2023

Power Query: Power Query Tables Don’t Have to be Green UPDATE
=============================================================

Power Query: Power Query Tables Don’t Have to be Green UPDATE
=============================================================

24 May 2023

_Welcome to our Power Query blog. This week, I am interrupting our series on Project Population to being you a newsflash – sorry, I mean an update to a previous blog._

Regular readers will recall I described how the default colours of Power Query tables can be changed from the familiar green colour in [Power Query Tables Don’t Have to be Green](https://sumproduct.com/blog/power-query-power-query-tables-do-not-have-to-be-green/)
. I started with a typical selection of Excel Tables, together with Tables created from Power Query:

![](https://sumproduct.com/wp-content/uploads/2025/05/3c8974bf6b4f1dd6986423ce9afec281.jpg)

I changed their appearance by changing the Theme on the ‘Page Layout’ tab. The green tables came from the Office Theme:

![](https://sumproduct.com/wp-content/uploads/2025/05/0af29724f1fb470bced0be31ba479cdd.jpg)

‘Accent 6’ is the default colour used for Power Query Tables:

![](https://sumproduct.com/wp-content/uploads/2025/05/3b2f48d9b9ef4dd198c8a357e46e871c.jpg)

I was able to change this colour to blue and save my new theme as ‘Power Query’:

![](https://sumproduct.com/wp-content/uploads/2025/05/ed11cffe5c99b60d46f2edc1e7c58f39.jpg)

This updated the Power Query Tables.

![](https://sumproduct.com/wp-content/uploads/2025/05/a9e654be8855a1bb97557ad3df1bb735.jpg)

The theme would only be used for the current workbook, but I was able to select it from the ‘Colors’ dropdown in other workbooks.

![](https://sumproduct.com/wp-content/uploads/2025/05/187e4362a744cdb592c1bdb5d52fced1.jpg)

I could also share the saved THMX file with others, and set it as the default for all new workbooks if I wished.

However, there is now an easier way to ensure that Power Query Tables are created with the same colour as Tables created in Excel. I can go back to my data, and set the Theme back to Office:

![](https://sumproduct.com/wp-content/uploads/2025/05/48053c26f8efdf131322d044b80369f2.jpg)

I edit any of my queries by accessing the ‘Queries & Connections’ from the Data tab, and double-clicking on a query:

![](<Base64-Image-Removed>)

In the File tab, I choose ‘Query Options’ from the ‘Options and settings’ dropdown:

![](<Base64-Image-Removed>)

In the dialog, on the General tab under GLOBAL, I can see a new setting:

![](<Base64-Image-Removed>)

‘Query table style’ can now be set to ‘Use default table style for query tables’! I tick this box and click ‘OK’. To test it, I create a new query by right-clicking on the current query, and choosing to create a reference query:

![](<Base64-Image-Removed>)

I call my new query **Test\_Colour**, and choose to ‘Close & Load To..’ so that I can put it on the same sheet:

![](<Base64-Image-Removed>)

The new query Table starting in cell **H3** is a reference of the query Table starting in cell **A12**, but it is clearly the same colour as the Excel Table starting in cell **A3**. This setting will apply to any query Tables I create whilst the setting is on. Changing the setting will not change existing Tables; you will need my original method for that.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-power-query-tables-dont-have-to-be-green-update/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-power-query-tables-dont-have-to-be-green-update/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-power-query-tables-dont-have-to-be-green-update/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-power-query-tables-dont-have-to-be-green-update/#0)

[](https://sumproduct.com/blog/power-query-power-query-tables-dont-have-to-be-green-update/#0 "close")

top