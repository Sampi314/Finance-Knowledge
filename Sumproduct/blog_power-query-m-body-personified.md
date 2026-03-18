# Power Query: M-Body Personified

**Source:** https://sumproduct.com/blog/power-query-m-body-personified/

---

[Home](https://sumproduct.com/)

\> Power Query: M-Body Personified

*   March 14, 2017

Power Query: M-Body Personified
===============================

Power Query: M-Body Personified
===============================

15 March 2017

_Welcome to our latest Power Query blog. Last time we introduced M and some basic Power Query functions. This time I look at M language syntax._

In order to see some **M** language in action, I return once again to the query I created in [Two (Queries) Become One](https://sumproduct.com/blog/power-query-two-queries-become-one/)
.

Having opened the Query Editor for **_ACCT\_Order\_Charges\_with\_Group,_** this time I choose the ‘Advanced Editor’ from the ‘Home’ tab:

![](<Base64-Image-Removed>)

This allows me to view a short section of **M** language, which demonstrates some of the **M** language syntax rules:

*   Since this is a query and not a function, the first line of every query must begin with ‘let’
    *   ‘let
        *   Source = Table.NestedJoin( …
        *   #”Expanded NewColumn” = Table…
        *   #”Renamed Columns” = Table…
        *   #”Sorted Rows” = Table…’
    *   In this case I have four lines which refer to steps defining the source of the query and data manipulation (some of which are preceded by a ‘#’ – more on this in a minute). The lines are separated by a comma (‘,’)
*   The end of the query is indicated by ‘in’ and a further step
    *   ‘in
        *   #”Sorted Rows”

This tells Power Query which step to return to once the query has been executed, in this case ‘Sorted Rows’.

*   The ‘#’ at the beginning of some of the lines is a message to Power Query to ignore the spaces in the names (_e.g._ in ‘Sorted Rows’). This is useful to know when creating steps manually.
*   The steps are sequential, and need to be linked to the previous step. Hence, the ‘Sorted Rows’ step refers to the ‘Renamed Columns’ step and the ‘Renamed Columns’ step refers to the ‘Expanded NewColumn’ and so on. When inserting lines, I must adjust the surrounding lines to make sure the sequence is intact, otherwise I will get an error.
*   The lines are quite long and can get quite convoluted, so I can edit the format to make it easier to read:

![](<Base64-Image-Removed>)

I have split the lines up to make them less of a long list of code – this can be useful when trying to keep track of whether all brackets have been closed (and closed in the right place). I have also inserted a single comment by preceding the line with ‘//’, and a section of comments by preceding with ‘/\*’ and ending with ‘\*/’. There is a check at the bottom of the screen which will warn me if the syntax is wrong and allow me to jump to the error.

![](<Base64-Image-Removed>)

Users of earlier versions of Power Query may notice that the ‘token comma’ is now not needed after a comment section – be guided by the syntax checker.

Next time I will make more changes to my query in order to show how **M** language can be configured to operate on each row in a table.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-m-body-personified/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-m-body-personified/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-m-body-personified/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-m-body-personified/#0)

[](https://sumproduct.com/blog/power-query-m-body-personified/#0 "close")

top