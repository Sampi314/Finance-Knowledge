# ‘Do’ You Want To ‘Exit’?

**Source:** https://sumproduct.com/thought/do-you-want-to-exit/

---

[Home](https://sumproduct.com/)

\> ‘Do’ You Want To ‘Exit’?

*   March 23, 2018

‘Do’ You Want To ‘Exit’?
========================

VBA Blogs: ‘Do’ You Want To ‘Exit’?
===================================

23 March 2018

[Last week](https://www.sumproduct.com/blog/article/vba-blogs/vba-blog-wending-down-the-hill-until-you-do)
 this blog **While****Wend**\-ed down a loopy path, but now it is time to find better things to **Do**.

**Do…Loop** loops are considered the upgraded alternative to **While Wend.** Let’s have a look at how they work:

**Do** \[{ **While** |**Until** } condition \]

\[ statements \]

\[ **Exit Do** \]

\[ statements\]

**Loop**

So how would the code change from a **While Wend** to a **Do…Loop** ?

Simple replace the **While** with **Do While** and **Wend** with **Loop**.

![](https://sumproduct.com/wp-content/uploads/2025/06/60e2eb188d28f8c0504972a90238e355.jpg)

**Do**…**Loop** is superior to **While Wend** for a multitude of reasons. Why is **Do…Loop** preferred?

Firstly, **While Wend** has no ability to have an **Exit**. Let’s return to our Jack and Jill example. What if the hill has 5 steps? The condition for the loop could be altered to check **CurrentStepsTaken** before entering, but **Do…****Loop** has the flexibility to break out with an **Exit** statement. Here, the subroutine can check if Jack & Jill fall down after they take a step. If they don’t fall down when they reach the top of the hill, then the print statements need to be changed accordingly:

**Sub** JackAndJillExit()

**Dim** CurrentStepsTaken **As Integer**

CurrentStepsTaken = 0

**Dim** FallenDown **As Boolean**

FallenDown = **False**

**Do While** FallenDown = **False**

    CurrentStepsTaken = CurrentStepsTaken + 1

**If** Rnd() <= 0.3 **Then**

        FallenDown = **True**

    **End If**

**If** CurrentStepsTaken = 5 **Then**

        **Exit Do**

    **End If**

**Loop**

**Debug.Print** CurrentStepsTaken & ” step(s) up the hill were taken.”

**If** FallenDown **Then**

**Debug.Print** “Jack fell down the hill!”

**Debug.Print** “Jill came tumbling after…”

**Else**

**Debug.Print** “Jack & Jill reached the top of the hill!”

**End If**

**End Sub**

Which results in:

![](<Base64-Image-Removed>)

They didn’t fall down when they reached the top, but because they had reached the top we asked the program to exit as reaching the top was not part of our loop conditional expression.

Circle back week to find out the second reason why **Do Loop**’s are on top of **While Wend** on the loopy hill.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/do-you-want-to-exit/#0)
    
*   [Register](https://sumproduct.com/thought/do-you-want-to-exit/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/do-you-want-to-exit/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/do-you-want-to-exit/#0)

[](https://sumproduct.com/thought/do-you-want-to-exit/#0 "close")

top