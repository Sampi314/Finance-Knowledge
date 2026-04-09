# Matching the Case

**Source:** https://sumproduct.com/thought/matching-the-case/

---

[Home](https://sumproduct.com/)

\> Matching the Case

*   June 8, 2018

Matching the Case
=================

VBA Blogs: Matching the Case
============================

8 June 2018

Last week we used the **LookAt** parameter with the **Find** method to match the complete word.

Of the three methods of matching words listed last week, today we tackle the second method, matching the case of the word.

1.  Matching the complete word
2.  **Matching the case of the word (i.e. the capitalisation)**
3.  Matching a specific cell formatting

Similar to last week we are going to be matching words found in this field.

![](https://sumproduct.com/wp-content/uploads/2025/06/e774d10cbbb9450fc45efbe51abdf434-686.jpg)

**Matching the capitalized word**

We want it to return with the cell **C9** “chance UPON”. Let’s search for “UPON” from cell **A1**.

**Sub** FindMatchCase()

**Dim** searchRange **As** Range

    **Set** searchRange = Range(“A1:E10”)

**Dim** foundrange **As** Range

    **Set** foundrange = searchRange.Find(“UPON”, LookAt:=xlPart)

 **If** foundrange **Is Nothing Then**

**Debug.Print** “not found!”

    **Else**

        **Debug.Print** foundrange

        **Debug.Print** foundrange.Address

    **End If**

**End Sub**

![](<Base64-Image-Removed>)

It found ‘stumble upon’ from cell **E3**. This suggests that we have to add another parameter: _MatchCase_. The _MatchCase_ parameter will force VBA to match the case of the word. Let’s search of “UPON” again from cell **A1**:

**Sub** FindMatchCase()

**Dim** searchRange **As** Range

 **Set** searchRange = Range(“A1:E10”)

 **Dim** foundrange **As** Range

**Set** foundrange = searchRange.Find(“UPON”, LookAt:=xlPart, MatchCase:=True)

**If** foundrange **Is Nothing Then**

**Debug.Print** “not found!”

   **Else**

        **Debug.Print** foundrange

**Debug.Print** foundrange.Address

    **End If**

**End Sub**

![](<Base64-Image-Removed>)

This change in the code will give us the expected result of ‘chance UPON’ in cell **C9**.

A noteworthy part of the code to point out is that we setting the ‘LookAt’ parameter to ‘xlPart’ and not ‘xlWhole’. So if we wish to find the entire word we would have to change ‘xlPart’ to ‘xlWhole’.

Come back next week where we discuss how to match specific cell formatting.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/matching-the-case/#0)
    
*   [Register](https://sumproduct.com/thought/matching-the-case/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/matching-the-case/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/matching-the-case/#0)

[](https://sumproduct.com/thought/matching-the-case/#0 "close")

top