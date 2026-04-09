# Digging Up

**Source:** https://sumproduct.com/thought/digging-up/

---

[Home](https://sumproduct.com/)

\> Digging Up

*   May 18, 2018

Digging Up
==========

VBA Blogs: Digging Up
=====================

18 May 2018

Last week we ran into the **SearchOrder** parameter of the **Find** function. We knew that we could go right across the row or down the column. But what if we wanted to manipulate the _direction_ of which we searched? Instead of going down the columns using _xlByColumns_ what if we wanted to go up? We can change that direction by using the **SearchDirection** parameter.

The **SearchDirection** parameter accepts the values of _xlNext_ which means it’s looking forwards (i.e. down columns and to the right of rows) or its opposite _xlPrevious_.

Let’s see how it works in our amended subroutine.

**Sub** FindAfterByGoingUpColumns()

**Dim** searchRange **As** Range

**Set** searchRange = Range(“A1:E10”)   

**Dim** foundrange **As** Range

**Set** foundrange = searchRange.Find(“up”, After:=Range(“C5”), SearchOrder:=xlByColumns, SearchDirection:=xlPrevious)

**If** foundrange **Is Nothing Then**

**Debug.Print** “not found!”

**Else**

**Debug.Print** foundrange

**Debug.Print** foundrange.Address

    **End If**

**End Sub**

Results in:

![](<Base64-Image-Removed>)

Changing the **SearchOrder** to _xlByRows_ will force the **Find** method to go left across the rows first before going up.

It’s simple to go after what you are looking for in any direction. Next week we’re going to be experimenting with more parameters of the **Find** function.

Ferret out more right here next week!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/digging-up/#0)
    
*   [Register](https://sumproduct.com/thought/digging-up/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/digging-up/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/digging-up/#0)

[](https://sumproduct.com/thought/digging-up/#0 "close")

top