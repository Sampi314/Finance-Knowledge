# Declaring Variables

**Source:** https://sumproduct.com/thought/declaring-variables/

---

[Home](https://sumproduct.com/)

\> Declaring Variables

*   April 7, 2017

Declaring Variables
===================

VBA Blogs: Declaring Variables
==============================

7 April 2017

To see the start of our VBA blog series, click [here](https://www.sumproduct.com/blog/article/vba-blogs/introduction-to-vba)
.

One of the most useful things you can do in VBA is to store values in the program’s memory, so that you can use it in the future. In Excel, we would normally do this in cells – put a value in a cell, then refer back to that cell when you want to use it. In VBA, we do this with variables.

Variables can be used to store any type of object or value. For example, you could create a variable to store a particular sheet or workbook. You can create a variable to hold a number, or even an array of numbers. You can use variables to store text. However, you generally want to define what each variable will store in advance. We can do this by _dimensioning_ (which is really a fancy way for telling the computer to allocate space for) variables:

Dim <VariableName> as <VariableType>

For example, we can use the following to create a variable for our message box:

Dim MessageBoxText as String

A String is the variable type – this tells Excel that the value being stored in this variable is text, rather than numeric or some other form of variable.

We can then add a value to this variable, using the code:

<VariableName> = <Value>

So again, in the case of our message box, we can use:

MessageBoxText = “Hello World!”

This effectively tells Excel that we want to find the variable called “MessageBoxText” and set it to represent the value “Hello World!”. We need to note that the type of variable is important in defining how the variable will take values. If we set the variable to be equal to “3”, then it will take on the value, but it will treat it as a String type, meaning that it can’t be used in some types of mathematical operations that don’t automatically convert text to numbers.

In some cases (in particular, the Workbook example below), we might need to use:

Set StartingWorkbook = ActiveWorkbook

Let’s take a look at some other examples of variables:

Dim StoredValue as Integer

(set up a variable that contains integers, i.e. whole numbers)

Dim DetailedValue as Double

(set up a variable that contains decimal numbers)

Dim FlagValue as Boolean

(set up a variable that contains True and False values)

Dim StartingWorkBook as Workbook

(set up a variable that contains a reference to the workbook, so that you can use that in other code elements, e.g. StartingWorkbook.Sheets(“Sheet1”))

Hope this all makes sense, next week we will start using our declared variables in some interesting ways!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/declaring-variables/#0)
    
*   [Register](https://sumproduct.com/thought/declaring-variables/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/declaring-variables/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/declaring-variables/#0)

[](https://sumproduct.com/thought/declaring-variables/#0 "close")

top