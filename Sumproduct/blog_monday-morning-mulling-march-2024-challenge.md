# Monday Morning Mulling: March 2024 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-march-2024-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: March 2024 Challenge

*   March 31, 2024

Monday Morning Mulling: March 2024 Challenge
============================================

Monday Morning Mulling: March 2024 Challenge
============================================

1 April 2024

_On the final Friday of each month, set an Excel for you to puzzle over for the weekend. On the Monday, we publish one suggested solution. No-one is stating this is the best approach, it’s just the one we selected. If you don’t like it, lump it – or contact us with your preferred solution._

**_The Challenge_**

On Friday, we raised a challenge that some of you may have already come across. Consider the following example:

![](<Base64-Image-Removed>)

You can download the original question file [here](https://www.sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/Mar/sp-formulae-will-not-calculate-example.xlsx)
. As you will see, in cell **F12**_(pictured)_ we have the formula

**\=5\*7**

Similarly, the two formulae in cells **F13** and **F14** were not calculating either. All you had to do was force a calculation as simply as possible without recreating the formula elsewhere.

**_Suggested Solution_**

The second formula, in cell **F13**, perhaps gives the game away:

**\=sqrt(pi())**

This expression should be taking the square root (**SQRT()**) of the number pi (**π**) (**PI()**). However, functions in Excel capitalise automatically. This expression hasn’t. It is not being recognised as a formula.

The formulae

**\=5\*7**

**\=sqrt(pi())**

**\=CHOOSE(2,F12,F13)**

will not calculate. They merely display as above. But hang on a minute: why don’t these calculations compute when I write them here? Well, aside from the fact I am not in Excel, these are **text** expressions. The ‘equals’ sign (**\=**) is meaningless here. And that’s the problem in Excel. Take a closer look at the Home tab for these cells:

![](<Base64-Image-Removed>)

Do you see the cells **F12:F14** are formatted as Text? If you were to multiply each cell by one \[1\], you would get _#VALUE!_ Text doesn’t calculate. It’s as simple as that.

Well, not quite. First, let’s change the formatting to something other than Text, say, General:

![](<Base64-Image-Removed>)

This does not have an immediate effect:

![](<Base64-Image-Removed>)

However, if you now edit each cell (_e.g._press **F2**) and then hit **ENTER**, the formulae will calculate as intended:

![](<Base64-Image-Removed>)

Problem solved. The solution file can be inspected [here](https://www.sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/Mar/sp-formulae-will-not-calculate-resolved.xlsx)
.

**_Word to the Wise_**

Not all of our problems need PhDs in Astrophysics and the patience of Dr Garcia. This one was incredibly simple _if you knew what to do_. You might think this month’s challenge was a “cop out” but we decided to include this one as it is amazing how often this problem occurs in practice and stumps fairly experienced modellers. Until next month.

_The Final Friday Fix will return on Friday 26 April 2024 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-march-2024-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-march-2024-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-march-2024-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-march-2024-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-march-2024-challenge/#0 "close")

top