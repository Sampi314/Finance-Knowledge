# Stop Reticulating Splines – Part 2

**Source:** https://sumproduct.com/thought/stop-reticulating-splines-part-2/

---

[Home](https://sumproduct.com/)

\> Stop Reticulating Splines – Part 2

*   July 13, 2018

Stop Reticulating Splines – Part 2
==================================

VBA Blogs: Stop Reticulating Splines – Part 2
=============================================

13 July 2018

[Last week](https://www.sumproduct.com/blog/article/vba-blogs/vba-blog-stop-reticulating-splines-part-1)
 we discussed how our macro is “[Reticulating Splines](https://www.urbandictionary.com/define.php?term=reticulating+splines)
” on run-time. Let’s discuss another tip we could use to mitigate it.

**_Stop Screen Flickering_**

You might be “Calibrating Fame Indicant” which may require a lot of movements between sheets whether in one work book or many.

Each time Excel copies data from another worksheet in VBA, it snaps to the worksheet to copy the selection on the screen and snaps to the destination worksheet to paste it. A macro with a lot of copying around despite no scroll movement on the screen appear to “flicker” a lot as it jumps around. It flashes as it moves to different parts as the macro runs and can be very distracting.

But even updating the screen to show this movement requires memory! Not only is Excel using memory to calculate the procedure, it’s also reserving part of it to update the changes on the screen as it progresses through.

We can turn this off in order for Excel to concentrate purely on the calculations. This is done with the **Application.ScreenUpdating** property.

It’s pretty simple – at the start of the routine, just set this to **False** and at the end set it back to **True** and we’re golden!

**Sub** StopReticulatingSplines()

    Application.ScreenUpdating = **False**

**Call** DoStuff

    Application.ScreenUpdating = **True**

**End Sub**

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/stop-reticulating-splines-part-2/#0)
    
*   [Register](https://sumproduct.com/thought/stop-reticulating-splines-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/stop-reticulating-splines-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/stop-reticulating-splines-part-2/#0)

[](https://sumproduct.com/thought/stop-reticulating-splines-part-2/#0 "close")

top