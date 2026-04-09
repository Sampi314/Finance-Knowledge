# Going Through the Visual Basics – Part 17

**Source:** https://sumproduct.com/thought/going-through-the-visual-basics-part-17/

---

[Home](https://sumproduct.com/)

\> Going Through the Visual Basics – Part 17

*   December 21, 2018

Going Through the Visual Basics – Part 17
=========================================

VBA Blogs: Going Through the Visual Basics – Part 17
====================================================

21 December 2018

_We thought we’d run an elementary series going through the rudiments of Visual Basic for Applications (VBA) as a springboard for newer users. This blog has a lot to DO this time._

In a programming, a control structure determines the order in which statements are executed. The iteration control structure is used for repetitively executing a block of code multiple times.

![](<Base64-Image-Removed>)

The final loops belong to the **DO** family. There are several members and examples are presented below.

**DO…LOOP**

**DO…LOOP** loops are considered the upgraded alternative to **WHILE WEND**. Let’s have a look at how they work:

Do \[{ While |Until } condition \]

\[ statements \]

\[ Exit Do \]

\[ statements\]

Loop

How does the code change from **WHILE WEND** to **DO…LOOP**? Simply replace the **WHILE** with **DO WHILE** and **WEND** with **LOOP**. It’s as easy as that!

![](<Base64-Image-Removed>)

**DO…LOOP** is superior to While Wend for several reasons:

*   **WHILE WEND** has no ability to have an **EXIT**
*   **WHILE WEND** loops check for the condition prior to running – but with **DO…LOOP** the condition can be checked at the end. This is useful if the code needs to be run at least once.
    
    This is done by simply moving the “**WHILE** \[condition\]” part of the **DO** statement next to **LOOP**. The syntax changes to:
    

Do

\[ statements \]

\[ Exit Do \]

\[ statements\]

Loop \[{ While |Until } condition \]

![](<Base64-Image-Removed>)

*   The ability to replace **WHILE** with **UNTIL**: what effect does this achieve? This essentially reverses the value of the condition to be tested.  
    **  
    WHILE** executes the block of code when the condition is True and keeps executing that till the condition becomes False. Once the condition becomes False, the loop is terminated. However, if the condition tested is initially False, the condition must be tested as:
    
    DO WHILE condition = FALSE  
    **  
    UNTIL** does the opposite. It executes the block of code when the condition is False and keep executing that till the condition becomes True. Once the condition becomes True, the **UNTIL** loop is terminated.
    
    It should be noted that the \[condition\] is a Boolean value, the loop can then be adjusted with the starting statement:
    
    DO UNTIL condition
    

![](<Base64-Image-Removed>)

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/going-through-the-visual-basics-part-17/#0)
    
*   [Register](https://sumproduct.com/thought/going-through-the-visual-basics-part-17/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/going-through-the-visual-basics-part-17/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/going-through-the-visual-basics-part-17/#0)

[](https://sumproduct.com/thought/going-through-the-visual-basics-part-17/#0 "close")

top