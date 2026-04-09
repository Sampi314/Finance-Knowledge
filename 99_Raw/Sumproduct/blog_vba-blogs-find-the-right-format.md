# VBA Blogs: Find The Right Format

**Source:** https://sumproduct.com/blog/vba-blogs-find-the-right-format/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Find The Right Format

*   June 14, 2018

VBA Blogs: Find The Right Format
================================

VBA Blogs: Find The Right Format
================================

15 June 2018

It’s easy enough to get on a cell’s case as we explored last week, but what if we wanted to find a cell that is formatted in a particular way? Like cells that have been bolded or have a specific background colour?

This is where the **SearchFormat** parameter comes in. This is a Boolean parameter that tells the **Find** method to search a particular format. But how do we set the format?

This is where we have declare the **FindFormat** object. **FindFormat** is a special object property of the **Application** where one can set particular formatting details to search in the **Range.Find** method. All we need to do, is set the **FindFormat** properties as if we were setting the properties of any given Range.

For example, if we wanted to set the text to be bold, we would use:

Application.FindFormat.Font.Bold = **True**

Let’s review the search range we’ve been using the last few weeks:

![](https://sumproduct.com/wp-content/uploads/2025/05/e7f274419d11bbedec5710fdb887b5f4.jpg)

In our range that we’ve been using, some of the cells have been highlighted yellow. The RGB code for that colour is R = 255, G = 255 and B= 0 (note this information can be found by going into the “Custom” colours and it will show the RGB code for the chosen cell). To search for that particular format, we would use:

Application.FindFormat.Interior.Color = RGB(255, 255, 0)

So how would this apply in our Macro?

**Sub** FindFormat()

**Dim** searchRange **As** Range

**Set** searchRange = Range(“A1:E10”)   

    Application.FindFormat.Interior.Color = RGB(255, 255, 0)

**Dim** foundrange **As** Range

**Set** foundrange = searchRange.Find(“upon”, Lookat:=xlPart, MatchCase:=False, searchformat:=True)

**If** foundrange **Is Nothing Then**

**Debug.Print** “not found!”

**Else**

**Debug.Print** foundrange

**Debug.Print** foundrange.Address

**End If**

**End Sub**

![](<Base64-Image-Removed>)

Easy!

Now we can add multiple formatting details to a cell. We could do this:

**Sub** FindFormat()

**Dim** searchRange **As** Range

**Set** searchRange = Range(“A1:E10”)

    Application.FindFormat.Interior.Color = RGB(255, 255, 0)

    Application.FindFormat.Font.Color = RGB(255, 0, 0)

**Dim** foundrange **As** Range

**Set** foundrange = searchRange.Find(“upon”, Lookat:=xlPart, MatchCase:=False, searchformat:=True)

**If** foundrange **Is Nothing Then**

**Debug.Print** “not found!”

    **Else**

**Debug.Print** foundrange

**Debug.Print** foundrange.Address

    **End If**

**End Sub**

![](<Base64-Image-Removed>)

There is a cell in that is formatted in that particular way despite there is no cell with the word “upon” in the search range. We can easily find just the format by giving it an empty string i.e. “” to search for.

**Sub** FindFormat()

**Dim** searchRange As Range

**Set** searchRange = Range(“A1:E10”)

    Application.FindFormat.Interior.Color = RGB(255, 255, 0)

    Application.FindFormat.Font.Color = RGB(255, 0, 0)

**Dim** foundrange As Range

**Set** foundrange = searchRange.Find(“”, Lookat:=xlPart, MatchCase:=False, searchformat:=True)

    **If** foundrange **Is Nothing Then**

**Debug.Print** “not found!”

    **Else**

        **Debug.Print** foundrange

        **Debug.Print** foundrange.Address

    **End If**

**End Sub**

![](<Base64-Image-Removed>)

There’s a lot of different ways we could format a cell, but the one thing the **FindFormat** object will not allow us to set is a particular _Style_.

Because we can assign multiple properties in the **Application.FindFormat** it is easy to reset in order to search a different format later on with the simple line:

Application.FindFormat.Clear

That’s it for the **Find** method. Check out a new topic next week!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-find-the-right-format/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-find-the-right-format/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-find-the-right-format/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-find-the-right-format/#0)

[](https://sumproduct.com/blog/vba-blogs-find-the-right-format/#0 "close")

top