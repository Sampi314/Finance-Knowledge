# Finding the Part of a Whole

**Source:** https://sumproduct.com/thought/finding-the-part-of-a-whole/

---

[Home](https://sumproduct.com/)

\> Finding the Part of a Whole

*   June 1, 2018

Finding the Part of a Whole
===========================

VBA Blogs: Finding the Part of a Whole
======================================

1 June 2018

Last week we looked at using the **After**, **SearchDirection** and **SearchOrder** parameters of the **Find** method.

What if we needed an exact match? There’s a few things we could match.

1.  Matching the complete word
2.  Matching the case of the word (i.e. the capitalisation)
3.  Matching a specific cell formatting

Luckily, the **Find** method has parameters that can help us with that! Today’s article will look at the first option. Not to worry, we will cover the other options in later weeks!

The word field has been adjusted slightly to give us more interesting things to search (the changed squares are highlighted in yellow):

![](<Base64-Image-Removed>)

**Matching the complete word**

If we were to search “encounter” from **C5** what would the result be? Let’s give it a go:

**Sub** EncounterOfTheFirstKind()

**Dim** searchRange **As** Range

**Set** searchRange = Range(“A1:E10”)

**Dim** foundrange **As** Range

**Set** foundrange = searchRange.Find(“encounter”, After:=Range(“C5”))

**If** foundrange **Is Nothing Then**

**Debug.Print** “not found!”

    **Else**

        **Debug.Print** foundrange

**Debug.Print** foundrange.Address

    **End If**

**End Sub**

![](<Base64-Image-Removed>)

It technically found ‘encounter’ but within ‘rencounter’. To force it to match the complete word, we would need to trigger the **LookAt** parameter. By defining it to be _xlWhole,_ that will force it to look at the entire contents of the cell.

**Sub** FindWholeWord()

**Dim** searchRange **As** Range

**Set** searchRange = Range(“A1:E10”)

**Dim** foundrange **As** Range

**Set** foundrange = searchRange.Find(“encounter”, After:=Range(“C5”), LookAt:=xlWhole)

**If** foundrange **Is Nothing Then**

        **Debug.Print** “not found!”

**Else**

**Debug.Print** foundrange

**Debug.Print** foundrange.Address

    **End If**

**End Sub**

This change will land on the expected answer of cell **A3.**

![](<Base64-Image-Removed>)

Now, this is where things get interesting. If we were to run another search immediately after without the LookAt:=xlWhole portion, it would still maintain the parameter setting. This is because Excel saves this setting in the **Find** dialogue**.** Opening the dialogue up, view the advanced settings by clicking the “Options > >” button:

![](<Base64-Image-Removed>)

There it is! So whenever doing a search using the **Find** method in VBA, ensure that you always set the parameters for each Find because otherwise it will lead to unexpected results.

Come back next week where we will keep finding things on a Case-by-Case basis!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/finding-the-part-of-a-whole/#0)
    
*   [Register](https://sumproduct.com/thought/finding-the-part-of-a-whole/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/finding-the-part-of-a-whole/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/finding-the-part-of-a-whole/#0)

[](https://sumproduct.com/thought/finding-the-part-of-a-whole/#0 "close")

top