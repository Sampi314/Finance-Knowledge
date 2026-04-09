# Lost and Found

**Source:** https://sumproduct.com/thought/lost-and-found/

---

[Home](https://sumproduct.com/)

\> Lost and Found

*   April 20, 2018

Lost and Found
==============

VBA Blogs: Lost and Found
=========================

20 April 2018

It’s easy to get lost in a sea of data, but at times we want to find something in particular, be it a word, number or formula. Autofilters can help us do that. In Excel, the Find & Select (CTRL + F) function helps us do specific value/formula searches. But how can we automate this in VBA?

Enter the **Find** method.

**Find** finds a specific information in a range, so it can only be used on _Range_ objects. Let’s have a look at its parameters.

| Parameter | Type | Description | Values |
| --- | --- | --- | --- |
| **What** | Required | What we are looking for | Any VBA data type, can be a string “find me”, or integer 42 |
| **After** | Optional | A single cell after which you want the search to begin – will not be searched until the search loops around and returns to it. Defaults to the cell in the upper-left corner of the range. | Range(“A1”) |
| **LookIn** | Optional | What type of thing we want to look in – defaults to _xlValues_ | _xlValues_ for searching values e.g. “51”<br><br>_xlFormulas_ for searching formulae “=A5<br><br>_xlComments_ for searching within the Review Comments |
| **LookAt** | Optional | Defines a complete or partial search – defaults to _xlPart_ | _xlWhole_ matches the entire contents of the field<br><br>_xlPart_ matches part of the field |
| **SearchOrder** | Optional | The search order – defaults to _xlByRows_ | _xlByRows_ to go across the rows first<br><br>_xlByColumns_ to go down the columns first |
| **SearchDirection** | Optional | The search direction – the default is _xlNext_ | _xlNext_ going forwards in direction<br><br>_xlPrevious_ going backwards in direction |
| **MatchCase** | Optional | True to make the search case sensitive – default value is _False_ | Variant |
| **MatchByte** | Optional | Used in double-byte language searches and irrelevant if the language in Excel is single-byte. Double-byte languages include Korean, Japanese etc., Defaults | _True_ to have double-byte characters match only double-byte characters.<br><br>_False_ to have double-byte characters match their single-byte equivalents. |
| **SearchFormat** | Optional | Searching by format which must be set first using **Application.FindFormat** | True or False |

Let’s start with some data:

![](<Base64-Image-Removed>)

Today we are going to start with the most basic search. Let’s ignore all the other parameters and use their default settings for the time being.

**Sub** TestFind()

    **Dim** searchRange **As** Range

    **Set** searchRange = Range(“A1:E10”)

    **Debug.Print** searchRange.Find(“observe”)

**End Sub**

We get the result:

![](<Base64-Image-Removed>)

It gives us the _value_ of the cell that has the first match. But what if we wanted to know the address of the cell? As the **Find** method returns a **Range** result, we can simply use the **Address** property.

**Sub** TestFindAddress()

     **Dim** searchRange **As** Range

     **Set** searchRange = Range(“A1:E10”)

     **Debug.Print** searchRange.Find(“observe”).Address

**End Sub**

![](<Base64-Image-Removed>)

But what happens we try to search for something that isn’t in our range?

**Sub** CantFind()

     **Dim** searchRange **As** Range

     **Set** searchRange = Range(“A1:E10”)

     **Debug.Print** searchRange.Find(“lost”).Address

**End Sub**

We will get an error.

![](<Base64-Image-Removed>)

This is because there was no _Range_ returned. To prepare for that contingency, a little checking is required to determine if there was a result. This where the **Nothing** keyword would be utilised. **Nothing** represents the default value of a data type. For example, a **Nothing**_String_ would be “”.

As a result, if the **Find** method can not return a result, it will return a default value which is **Nothing** and our code can be adjusted as follows

**Sub** CantFindNothing()

**Dim** searchRange **As** Range

**Set** searchRange = Range(“A1:E10”)

**If** searchRange.Find(“lost”) **Is Nothing Then**

        **Debug.Print** “lost is not found!”

**Else**

        **Debug.Print** searchRange.Find(“lost”).Address

    **End If**

**End Sub**

![](<Base64-Image-Removed>)

It doesn’t seem to be difficult to **Find** things using VBA!

Next week we will go over some of the parameters on the **Find** function and see how they fine tune your searches to pinpoint accuracy.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/lost-and-found/#0)
    
*   [Register](https://sumproduct.com/thought/lost-and-found/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/lost-and-found/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/lost-and-found/#0)

[](https://sumproduct.com/thought/lost-and-found/#0 "close")

top