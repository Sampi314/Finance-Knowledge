# Select Case Flexibility

**Source:** https://sumproduct.com/thought/select-case-flexibility/

---

[Home](https://sumproduct.com/)

\> Select Case Flexibility

*   February 8, 2019

Select Case Flexibility
=======================

VBA Blogs: Select Case Flexibility
==================================

8 February 2019

_This month, we’re talking about the Select Case statement. This week, we’re going to introduce tips to make the case statements more flexible._

Last week, we introduced the case statement. We noted that it is like a VLOOKUP – it searches through a list to find the value that matches, then it reports back on it.

However, let’s consider two cases:

*   What if you want a numeric value to meet a particular condition?
*   What if none of the statements match?

Let’s consider these one at a time.

**Numeric conditions**

If you want the value to be, say, greater than X, you can adapt the Case expression to provide a test for it to be correct. In addition to checking if the value is exactly equal to the expression, there are two additional options:

*   Case X To Y
*   Case Is >= X

In the case of X To Y, it will search for values that will fall between (and including) the values X and Y. In the case of Is >=X, other comparison operators (e.g. =, <>, <, <=, > and >=) can be used to provide that restriction.

So, we can use an example like the following:

![](<Base64-Image-Removed>)

**No statements match**

Last week, our leap year example had a single case to check if the value was 0, rather than 365 or 366 days. However, if a value of 200 was entered, it would not provide a correct answer. This is where we need to use Case Else.

Case Else allows us to specify what happens if none of the other cases are true. Going back to the VLOOKUP analogy, this would normally result in an #N/A! error. However, with Select Case, we can provide a default result if nothing else matches. So, we could amend the code as follows:

![](<Base64-Image-Removed>)

This means that anything that doesn’t match 365 or 366 will prompt us with a message box telling us that our value is invalid.

We have an interesting query from a client coming up, so check back next week for more!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/select-case-flexibility/#0)
    
*   [Register](https://sumproduct.com/thought/select-case-flexibility/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/select-case-flexibility/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/select-case-flexibility/#0)

[](https://sumproduct.com/thought/select-case-flexibility/#0 "close")

top