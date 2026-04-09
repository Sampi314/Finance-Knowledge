# Going Through the Visual Basics – Part 16

**Source:** https://sumproduct.com/thought/going-through-the-visual-basics-part-16/

---

[Home](https://sumproduct.com/)

\> Going Through the Visual Basics – Part 16

*   December 14, 2018

Going Through the Visual Basics – Part 16
=========================================

VBA Blogs: Going Through the Visual Basics – Part 16
====================================================

14 December 2018

_We thought we’d run an elementary series going through the rudiments of Visual Basic for Applications (VBA) as a springboard for newer users. This blog has a lot going FOR it._

In a programming, a control structure determines the order in which statements are executed. The iteration control structure is used for repetitively executing a block of code multiple times.

![](https://sumproduct.com/wp-content/uploads/2025/06/c72dffa960010e866e9df32d2cdbd9db.jpg)

One group of powerful loops is the **FOR** family. There are several members and examples are presented below.

**FOR…NEXT**

The **FOR…NEXT** loop uses a variable, which cycles through a series of values within a specified range and the statements inside the loop is then executed for each value.

**For** counter = start To end \[ Step step \]

\[ statements \]

Exit **For**

\[ statements \]

**Next** \[ counter \]        

Here’s a simple example:

**Sub**ForNext()

**Dim** counter **As Integer**

**For** counter = 1 To 5

**Debug.Print** counter

**Next** counter

**End Sub**

![](<Base64-Image-Removed>)

The **STEP** keyword allows the specification of how the counter changes. It defaults to an increment of 1, but it can be used for jumps and decrements.

**Sub** ForNextStep()

**Dim** counter **As Integer**

**For** counter = 10 To 0 Step -2

**Debug.Print** counter

**Next** counter

**End Sub**

![](<Base64-Image-Removed>)

**EXIT FOR**

**EXIT FOR** statements may be placed anywhere in the loop as an alternate way to exit. This is often used after evaluating of some condition, for example **[IF…THEN](https://www.sumproduct.com/blog/article/vba-blogs/vba-blog-going-through-the-visual-basics-part-12)
**, and then skips to the statements after the loop.

**Sub**ForNextExit()

**Dim** counter **As Integer**

**For** counter = 10 To 0 Step -2

**Debug.Print** counter

**If** counter = 6 **Then**

**Exit** For

**End** If

**Next** counter

**End Sub**

![](<Base64-Image-Removed>)

**FOR EACH…NEXT**

What if an action is needed to be performed to every object in a set?

**FOR EACH…NEXT** loops are a great way to cycle through sets – like an array or a range. Sometimes the number of rows or columns is uncertain. It is relatively easy to count the number of objects and set the upper bound of the **FOR…NEXT** loop appropriately. However, using **FOR EACH…NEXT** more clearly illustrates that the instructions are happening to every object.

Example:

**Sub**ForEach()

**Dim** myNumbers() **As** Variant

    myNumbers = Array(1, 5, 10, 15)

**Dim** aNumber **As** Variant

**For Each** aNumber **In** myNumbers

**Debug.Print** aNumber \* 5

**Next**

**End Sub**

![](<Base64-Image-Removed>)

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/going-through-the-visual-basics-part-16/#0)
    
*   [Register](https://sumproduct.com/thought/going-through-the-visual-basics-part-16/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/going-through-the-visual-basics-part-16/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/going-through-the-visual-basics-part-16/#0)

[](https://sumproduct.com/thought/going-through-the-visual-basics-part-16/#0 "close")

top