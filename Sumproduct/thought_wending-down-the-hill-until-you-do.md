# Wending down the hill Until you Do

**Source:** https://sumproduct.com/thought/wending-down-the-hill-until-you-do/

---

[Home](https://sumproduct.com/)

\> Wending down the hill Until you Do

*   March 16, 2018

Wending down the hill Until you Do
==================================

VBA Blogs: Wending down the hill Until you Do
=============================================

16 March 2018

![](<Base64-Image-Removed>)

[Last week](https://www.sumproduct.com/blog/article/vba-blogs/vba-blog-getting-loopy-each-time)
 we looked at **For Each…Next** loops – but this time let’s have a look at **While Wend** loops.

The syntax is very simple:

**While** condition

    \[statements\]

**Wend**

The condition must result in a Boolean value of **True** or **False**.

**While** tests the condition and if it is **True** then proceeds to execute the statements inside the loop. **While** loops are preferred over **For** loops when the number of iterations is unknown. For example, modelling how many days it takes to reach sales a target, or running through a worksheet column until it reaches an empty cell.

An example: Jack and Jill go up a hill, but they might go tumbling down at any point. Assume the probability of falling down with any step is 30% and independent of any steps previously taken. Let’s model how many steps it takes for them to fall down. What needs to be done?

*   Take a step
*   Assess the probability if they have fallen down or not
*   Repeat if they haven’t.

![](<Base64-Image-Removed>)

Notice how our condition is tested first – this means that the code will not run at all if the condition is not met. **FallenDown** is a Boolean value, the **While** statement can be used as the condition.

**While** FallenDown

…

**Wend**

This is equivalent to saying:

**While** FallenDown = **True**

…

**Wend**

**FallenDown** was initially set to be False. Using **FallenDown** as the condition for the loop would mean that Jack & Jill would never set foot on the hill.

**While Wend** loops are a remnant from the BASIC programming language and remains as a form of backwards compatibility. Using a **Do…Loop** statement is preferred.

Loop back next week explore why these are superior to **While Wend**.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/wending-down-the-hill-until-you-do/#0)
    
*   [Register](https://sumproduct.com/thought/wending-down-the-hill-until-you-do/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/wending-down-the-hill-until-you-do/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/wending-down-the-hill-until-you-do/#0)

[](https://sumproduct.com/thought/wending-down-the-hill-until-you-do/#0 "close")

top