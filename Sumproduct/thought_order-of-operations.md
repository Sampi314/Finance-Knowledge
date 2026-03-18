# Order of Operations

**Source:** https://sumproduct.com/thought/order-of-operations/

---

[Home](https://sumproduct.com/)

\> Order of Operations

*   May 14, 2025

Order of Operations
===================

Understanding the order of operations in Excel to avoid potential errors.

Order of Operations
===================

_Liam Bastick_ _highlights some of the common mistakes prevalent in financial modelling / Excel spreadsheeting. This article actually considers the oft-neglected area of operating operators. Don’t feel drowsy…_

**_So What is an Operator?_**

Operators specify the type of calculation that you want to perform on the elements of a formula. They are essentially the smallest building blocks of a calculation – even most functions are based upon these humble specifiers.

There are four types of operator altogether: Comparison, Arithmetic, Reference and Text – think **CART**. Let me go through each type now.

**_Comparison Operators_**

These operators are used to compare one expression with another, as long as these expressions evaluate to values. When two values are compared by these operators, the result is a logical value, _i.e._ either TRUE or FALSE.

![](<Base64-Image-Removed>)

As mentioned in the table above, the equals operator is used to denote a formula in Excel. It essentially communicates to Excel what the value of the cell should equal.

There are two common mistakes made by less experienced Excel users:

1.  Some modellers write ‘greater than or equal to’ as ‘=>’ rather than ‘>=’ (and similarly with ‘less than or equal to’). Be sure Excel will advise you of such an error with the ‘We found a typo’ dialog box or similar.
2.  The opposite of ‘>’ (greater than) is not ‘<’ (less than). It is in fact ‘<=’ (less than or equal to). Be careful any logic you employ in a model allows for the two values to be identical.

**_Arithmetic Operators_**

I once saw a brilliant typo on a website describing these type of operators as ‘arthritic operators’. AutoCorrect is such a wonderful tool. It’s a good job my spelling is sew grate or I may have create similar errors. Whilst it is true these operators probably represent the oldest and most readily recognisable operators, they don’t need pensioning off just yet!

![](<Base64-Image-Removed>)

These are the operators everyone considers to be operators. However, familiarity may breed contempt and there are potential pitfalls / tips to watch out for:

1.  It has been proved by greater minds than mine that using a double minus (e.g. =–A1) is the quickest way to convert a number stored as text into a number. This beats multiplying by 1 or using the VALUE function apparently.
2.  Some modellers add a zero before negating a value or cell reference. For example, they may use the formula =0-A1 rather than =-A1 as they argue it is easier to see that the value has been negated (tired eyes may easily miss the minus sign).
3.  Take care with the forward slash (‘/’) for dividing. Some users accidentally use backslashes. Not only may this result in an attempted murder, the backslash (‘’) is used to refer to file locations or even act as the ALT button in certain versions of Excel depending upon user settings.
4.  I recommend avoiding the per cent sign (‘%’) altogether and simply divide by 100 instead. Whilst having hard coded values in a formula should be avoided, there are greater perils risked here. The ‘%’ symbol can cause problems in certain formulae and DAX (Power Pivot) expressions when shared on the internet or SharePoint as % is often used to refer to a space in a URL for example.

**_Reference Operators_**

These operators are used to combine values and / or ranges for calculations in Excel.

![](<Base64-Image-Removed>)

Most users are unaware of the space operator. Space may be the final frontier, but hitting the spacebar may inadvertently cause Excel to try and intersect ranges. Be careful as many Microsoft Help examples are blighted by the proliferation of these pesky spaces in formulae.

**_Text Operator_**

Like Highlander, there can be only one.

![](<Base64-Image-Removed>)

Similar to the **CONCATENATE** function, ‘&’ is useful for connecting segments together. Each segment must make sense on its own: an open bracket must be followed by a close bracket, open quotation marks require closed quotation marks later and so on.

**_Order of Operations_**

But it’s not as simple as just picking out an operator. Sometimes we need to combine them – and unfortunately, they do not mix in the order we might think.

At school, many of us are taught a variant of **BoDMAS**, which stipulates the order of calculations in a mathematical expression. The order is:

1.  **Brackets**: items in brackets are calculated first
2.  **Powers**: values are raised exponentially second
3.  **Division**: values are divided third
4.  **Multiplication**: values are multiplied fourth
5.  **Addition**: values are added fifth
6.  **Subtraction**: values are deducted from each other last.

Therefore, an expression such as

\=3+8^2×5+(4/7+8)-5+9

evaluates to 335.57, when several other values may be calculated otherwise without this rule. The problem is, this may be the way we have been brought up to calculate, but Excel was taught a subtly different order which sometimes leads to formulaic errors as a consequence.

Finding the correct order of operations in Excel is tricky but I reproduce the order here:

![](<Base64-Image-Removed>)

Do you see the slight differences? Negating in general (essentially multiplying by -1) and dividing by 100 (per cent) will both be computed ahead of exponentiation. This may not be what you expect.

I strongly recommend that you take a look at some of your more complex formulae. Stepping out calculations not only makes logic easier to follow but also ensures that computations are executed in the desired order. If all else fails, inserting brackets, like Star Wars, will “use the Force”.

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/order-of-operations/#0)
    
*   [Register](https://sumproduct.com/thought/order-of-operations/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/order-of-operations/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/order-of-operations/#0)

[](https://sumproduct.com/thought/order-of-operations/#0 "close")

top