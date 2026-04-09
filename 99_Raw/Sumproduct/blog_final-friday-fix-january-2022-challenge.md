# Final Friday Fix: January 2022 Challenge

**Source:** https://sumproduct.com/blog/final-friday-fix-january-2022-challenge/

---

[Home](https://sumproduct.com/)

\> Final Friday Fix: January 2022 Challenge

*   January 27, 2022

Final Friday Fix: January 2022 Challenge
========================================

Final Friday Fix: January 2022 Challenge
========================================

28 January 2022

_On the final Friday of each month, we are going to set an Excel / Power BI challenge for you to puzzle over so that you can get your “Excel fix”. Challenge your office colleagues to see who can solve the puzzle quickest. There are no prizes at this stage: you are playing for bragging rights only!_

**_The Challenge_**

![](https://sumproduct.com/wp-content/uploads/2025/05/431a66884c0bacb02361d2d439b22511.jpg)

If you host prize draws on your website, social media, or live meetings, you may need to demonstrate a fair way to select random winner(s).

It is easy to randomly select just one winner as a suggested solution is simple as follows:

**\=INDEX(List\[Name\], RANDBETWEEN(1, ROWS(List\[Name\])))**

**ROWS** counts number of names in the list. **RANDBETWEEN** will generate a random integer (_i.e_. position number) between one \[1\] and the number of names. Then, [**INDEX**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-index-function)
 will help us pick the name at that position.

In this challenge, the objective is to create a random selector in Excel to choose three winners for a prize draw from a list of 10 people. The tricky part here is that a person cannot win the game more than once. Hence, the winners list must not contain any duplicates.

You can download the question file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/jan/sp-random-picks---challenge.xlsx)
.

As always, there are some requirements:

*   this is a formula challenge; no Power Query / Get & Transform or VBA!
*   there must be no duplicate in the result list
*   if we change the number of winners, the formula should still work.

_Sounds easy? Then why not have a go? We’ll publish one solution in Monday’s blog. Have a great weekend in the meantime!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/final-friday-fix-january-2022-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/final-friday-fix-january-2022-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/final-friday-fix-january-2022-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/final-friday-fix-january-2022-challenge/#0)

[](https://sumproduct.com/blog/final-friday-fix-january-2022-challenge/#0 "close")

top