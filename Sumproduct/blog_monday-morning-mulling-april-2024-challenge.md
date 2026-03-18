# Monday Morning Mulling: April 2024 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-april-2024-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: April 2024 Challenge

*   April 28, 2024

Monday Morning Mulling: April 2024 Challenge
============================================

Monday Morning Mulling: April 2024 Challenge
============================================

29 April 2024

_On the final Friday of each month, set an Excel for you to puzzle over for the weekend. On the Monday, we publish one suggested solution. No-one is stating this is the best approach, it’s just the one we selected. If you don’t like it, lump it – or contact us with your preferred solution._

**_The Challenge_**

On Friday, we raised a challenge with an all too familiar example:

![](https://sumproduct.com/wp-content/uploads/2025/05/5a78991d84c0d34d049717b7a4ec0115-1.jpg)

You can download the original question file [here](https://www.sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/Apr/sp-removing-apostrophes.xlsx)
. As you will see, in cell **F12**_(pictured)_ we had the “pseudo-formula”:

**‘=5\*7**

Indeed, the cells **F12:F14** are notformatted as Text. They do not calculate as they are deemed text since they all begin with an apostrophe (**‘**). This month’s challenge was to remove all the apostrophes **at the same time** (without using Power Query, VBA or other similar code). How did you get on?

**_Suggested Solution_**

Your first thought might be to use ‘Replace…’ (**CTRL + H**) and replace **‘=** with **\=**. Unfortunately, this does not work in all versions of Excel as ‘Replace…’ does not seem to recognise apostrophes in certain instances.

However, there is a very simple trick to circumvent this problem. With this data still selected, click on the ‘Text to Columns’ button in the ‘Data Tools’ group of the ‘Data’ tab on the Ribbon (**ALT + D + E**):

![](https://sumproduct.com/wp-content/uploads/2025/05/68152c6d2dcb65ec1009593902c7e395-1.jpg)

This launches the ‘Text to Columns Wizard’ dialog box. In the first step, ensure that the ‘…file type that best describes your data…’ is set to ‘Delimited’:

![](<Base64-Image-Removed>)

Then, believe it or not, simply depress the ‘Finish’ button. The spreadsheet will then reinstate the formulae, _viz_.

![](<Base64-Image-Removed>)

Simple!

The solution file can be inspected [here](https://www.sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/Apr/sp-removing-apostrophes-solved.xlsx)
.

**_Word to the Wise_**

For the second month running, this challenge was incredibly simple _if you knew what to do_. Again, we offer no apology because this is a trick you should add to your repertoire, if you’re not already aware of it.

Don’t worry; normal service will be resumed next month.

_The Final Friday Fix will return on Friday 31 May 2024 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-april-2024-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-april-2024-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-april-2024-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-april-2024-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-april-2024-challenge/#0 "close")

top