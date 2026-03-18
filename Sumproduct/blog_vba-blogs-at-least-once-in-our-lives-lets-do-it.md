# VBA Blogs: At Least Once in Our Lives, Let’s ‘Do’ It!

**Source:** https://sumproduct.com/blog/vba-blogs-at-least-once-in-our-lives-lets-do-it/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: At Least Once in Our Lives, Let’s ‘Do’ It!

*   April 5, 2018

VBA Blogs: At Least Once in Our Lives, Let’s ‘Do’ It!
=====================================================

VBA Blogs: At Least Once in Our Lives, Let’s ‘Do’ It!
=====================================================

6 April 2018

![](<Base64-Image-Removed>)

Last week this blog looked at using **Do…Loop** loops and experimented with the **Exit** statement making them better than **While Wend**.

The second reason that **Do…Loop** is superior is that **While Wend** loops check for the condition prior to running – but with **Do…Loop** the condition can be checked at the end.

Now why would you want to test the condition at the end?

For an example, Jack & Jill will always take at least one step onto the hill before falling. They won’t fall if they haven’t moved!

How this is done in code is by simply moving the **“While** condition” part of the **Do** statement next to **Loop**.

The syntax changes to:

**Do**

\[ statements \]

\[ **Exit Do** \]

\[ statements\]

**Loop** \[{ **While** |**Until** } condition \]

![](<Base64-Image-Removed>)

This will execute the statements within the loop to run at least once, before checking the condition and exiting if applicable.

Last week left Jack and Jill sitting pretty on the top of the hill having already taken 5 steps. Let’s set them on a loop walking, despite having reached the top.

**Sub** DoItAtLeastOnce()

**Dim** CurrentStepsTaken **As Integer**

CurrentStepsTaken = 5

**Do**

    CurrentStepsTaken = CurrentStepsTaken + 1

**Loop While** CurrentStepsTaken < 5

**Debug.Print** CurrentStepsTaken & ” steps were taken.”

**End Sub**

This results in:

![](<Base64-Image-Removed>)

Loop back next week to find out the final attribute making **Do…Loop** superior to **While Wend**.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-at-least-once-in-our-lives-lets-do-it/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-at-least-once-in-our-lives-lets-do-it/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-at-least-once-in-our-lives-lets-do-it/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-at-least-once-in-our-lives-lets-do-it/#0)

[](https://sumproduct.com/blog/vba-blogs-at-least-once-in-our-lives-lets-do-it/#0 "close")

top