# VBA Blogs: Going Through the Visual Basics – Part 15

**Source:** https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-15/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Going Through the Visual Basics – Part 15

*   December 6, 2018

VBA Blogs: Going Through the Visual Basics – Part 15
====================================================

VBA Blogs: Going Through the Visual Basics – Part 15
====================================================

7 December 2018

_We thought we’d run an elementary series going through the rudiments of Visual Basic for Applications (VBA) as a springboard for newer users. This blog takes a WHILE to get going…_

In a programming, a control structure determines the order in which statements are executed. The iteration control structure is used for repetitively executing a block of code multiple times.

![](<Base64-Image-Removed>)

The iteration structure executes a sequence of statements repeatedly if a condition holds true. One such type is **WHILE**.

The **WHILE…WEND** loop executes a series of statements as long as a given condition is True. The syntax is very simple:

While condition

    \[statements\]

Wend 

The condition must result in a Boolean value of **True** or **False**. **WHILE** tests the condition and if it is **True** then proceeds to execute the statements inside the loop.

**Sub** While**Wend**()

**Dim** counter **As Integer**

    counter = 0

**While** counter < 5

        counter = counter + 1

**Debug.Print** counter

**Wend**

**End Sub**

![](<Base64-Image-Removed>)

While loops are preferred when the number of iterations is unknown. For example, modelling how many days it takes to reach sales a target, or running through a worksheet column until it reaches an empty cell.

Notice how the condition is tested first – this means that the code will not run at all if the condition is not met. **WHILE…WEND** is a remnant from BASIC where VBA originated from. These are not as powerful as **DO…LOOP** (covered soon).

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-15/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-15/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-15/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-15/#0)

[](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-15/#0 "close")

top