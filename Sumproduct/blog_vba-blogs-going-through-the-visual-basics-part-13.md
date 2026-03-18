# VBA Blogs: Going Through the Visual Basics – Part 13

**Source:** https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-13/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Going Through the Visual Basics – Part 13

*   November 15, 2018

VBA Blogs: Going Through the Visual Basics – Part 13
====================================================

VBA Blogs: Going Through the Visual Basics – Part 13
====================================================

16 November 2018

_We thought we’d run an elementary series going through the rudiments of Visual Basic for Applications (VBA) as a springboard for newer users. This blog takes a look at selection control structures._

In a programming, a control structure determines the order in which statements are executed. The selection control structure is used for making decisions and branching statements.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Here are several examples.

**SELECT CASE**

**SELECT CASE** is the VBA equivalent to a switch control structure. A switch statement allows a variable to be tested for equality against a list of values. Each value is called a case, and the variable being “switched” on is checked for each case:

The **SWITCH** statement is used as follows:

Select \[ Case \] testexpression 

    \[ Case expressionlist \
\
        \[ statements \] \] 

    \[ Case Else \
\
        \[ elsestatements \] \] 

End Select 

Let’s look at a coding example:

**Sub**SWITCHStatement()

**Dim** myNumber **As Integer**

    myNumber = 1

**Select Case** myNumber

**Case** 0

**Debug.Print** “Zero the hero!”

**Case** 1

**Debug.Print** “Number one!”

**Case** 2

**Debug.Print** “Number two!”

**Case** 3

**Debug.Print** “Number three!”

**Case Else**

**Debug.Print** “Not a podium finish”

    End Select

**End Sub**

**IS**

**SELECT CASE** allows the use of the **IS** keyword to compare values. If the variable can use comparison operators, then **IS** is used before the operator. For example:

**Sub**SwitchISStatement()

**Dim** myNumber **As Integer**

    myNumber = 1

**Select Case** myNumber

        Case Is < 0

**Debug.Print** “Negative”

        Case Is < 10

**Debug.Print** “Single Digit Positive Integer”

**Case Is** < 100

**Debug.Print** “Double Digit Positive Integer”

        Case Else

            Debug.Print “Large number!”

    End Select

**End Sub**

Note: upon typing an operator (>, < or =) after the keyword **CASE**, the VBA editor will automatically correct the statement and place the **IS** keyword after **CASE**.

**TO**

If the variable assessed can lie within a range, the **TO** keyword is called upon to denote the range. For example:

**Sub**SwitchTOStatement()

**Dim** myNumber **As Integer**

    myNumber = 1

**Select Case** myNumber

        Case Is < 0

**Debug.Print** “Negative”

**Case** 0 **To** 9

**Debug.Print** “Single Digit Positive Integer”

        Case 10 **To** 99

**Debug.Print** “Double Digit Positive Integer”

**Case Else**

**Debug.Print** “Large number!”

    End Select

**End Sub**

**Combination**

Multiple expressions can be used in a single **CASE** statement for optimum efficiency. Another example:

**Sub**SwitchCombinationStatement()

**Dim** myNumber **As Integer**

    myNumber = 1

**Select Case** myNumber

**Case Is** < 0

**Debug.Print** “Negative”

**Case** 1, 2, 3, 4, 5 **To** 9

**Debug.Print** “Single Digit Positive Integer”

**Case** 10 **To** 50, 51, 52, 53, 54, 55 **To** 99

**Debug.Print** “Double Digit Positive Integer”

        Case Else

            Debug.Print “Large number!”

    End Select

**End Sub**

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-13/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-13/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-13/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-13/#0)

[](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-13/#0 "close")

top