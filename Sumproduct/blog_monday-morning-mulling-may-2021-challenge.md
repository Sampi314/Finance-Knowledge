# Monday Morning Mulling: May 2021 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-may-2021-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: May 2021 Challenge

*   May 30, 2021

Monday Morning Mulling: May 2021 Challenge
==========================================

Monday Morning Mulling: May 2021 Challenge
==========================================

31 May 2021

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

This month, we just wanted you to change the font colour of a cell. Easy, yes?

**_The Challenge_**

All you had to do was change the font colour of this text to blue – with no VBA help.

![](<Base64-Image-Removed>)

Our [starter file](https://sumproduct.com/assets/blog-pictures/2021/fff-mmm/may/fff/font-change-example.xlsx)
 was all yours.

**_Suggested Solution_**

As you probably suspected, all was not as it seemed and it wasn’t quite the trivial exercise it might have appeared on first glance. Changing the font to blue in the usual way did nothing. It _appeared_ to go blue…

![](<Base64-Image-Removed>)

…but once the operation had completed…

![](<Base64-Image-Removed>)

Drat.

You might recall from our article on [custom number formatting](https://www.sumproduct.com/thought/number-formatting)
 that number formatting is prioritised over text formatting and decide to take a look at the number formatting in the cell (**CTRL + 1**):

![](<Base64-Image-Removed>)

That didn’t yield the answer either.

Since the file is an Excel workbook (**.xlsx**) rather than a macro-enabled Excel workbook (_e.g._ **.xlsm**), then macros were not behind this devious behaviour either. So what the heck is causing the issue..?

Clearly, the problem must be number formatting is text formatting is not changing the font colour. But this can be defined somewhere else too – [**_conditional formatting_**](https://www.sumproduct.com/thought/conditional-formatting)
.

If you checked conditional formatting (**ALT + O + D**),

![](<Base64-Image-Removed>)

you would note that conditional formatting had been applied to all cells. Format “38718” is not very descriptive (!), but if you click on ‘Edit Rule…’ it leads you to realise all non-blank cells have been mandated to have this formatting:

![](<Base64-Image-Removed>)

If you click on the ‘Format…’ button, the Number tab of the resulting ‘Format Cells’ dialog explains everything:

![](<Base64-Image-Removed>)

Clearing this custom number format type will allow you to change the font colour.

If you fell for this example, you might be seeing ‘Red’ in more ways than one _(Groan – Ed.)_.

Until next month!

_The Final Friday Fix will return on Friday 25 June 2021 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business workday._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-may-2021-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-may-2021-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-may-2021-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-may-2021-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-may-2021-challenge/#0 "close")

top