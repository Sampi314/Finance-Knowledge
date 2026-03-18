# Scoping Variables

**Source:** https://sumproduct.com/thought/scoping-variables/

---

[Home](https://sumproduct.com/)

\> Scoping Variables

*   October 20, 2017

Scoping Variables
=================

VBA Blogs: Scoping Variables
============================

20 October 2017

Last weeks’ blog examined the value of declaring variables. But variables can also be used in different subroutines and functions. If there are items that are known to have constant values throughout the entire workbook, they can be declared explicitly in one place for easy reference.

**Explicit Variable Declaration**

Today let’s examine how variables can be scoped according to the needs of the project.

Let’s start with a simple function

![](<Base64-Image-Removed>)

This shows that the variable is IMPLICITLY declared. However to ensure that all variables are declared, at the beginning of the code the keywords “Option Explicit” are used

![](<Base64-Image-Removed>)

When the routine is activated the VBA compiler spits an error message saying it is not defined. It must be defined by at least the Dim statement before it is run.

**Module level sharing**

Let’s make a new subroutine referencing myTestString:

![](<Base64-Image-Removed>)

The declaration for the variable is in ScopeTest but the subroutine calling it is not the one that defined it.

![](<Base64-Image-Removed>)

The “Variable not defined” message pops up again. Let’s move the declaration OUTSIDE the subroutine, under the “Option Explicit” statement as follows

![](<Base64-Image-Removed>)

When NextScopeTest is run the following happens:

![](<Base64-Image-Removed>)

However if ScopeTest is run prior to NextScopeTest then:

![](<Base64-Image-Removed>)

These shows that the variable is accessible to the entire module and is changed as required.

The Dim statement outside any subroutines means the variable is accessible within the module that it is declared in.

**The Private Statement**

One may notice that sometimes the “Private” statement in declaration can be used. This is for module level sharing and identical to the “Dim” statement. Using the two is interchangeable and is more for more good coding practice. Using “Private” is makes the code much more reasonable and draws to the eye immediately the scope of the variable.

**Project level sharing**

What if another module wants to reuse the same variable?

![](<Base64-Image-Removed>)

Module2 wants to use myTestString but it is declared in Module1.

![](<Base64-Image-Removed>)

But upon running, it again says the “Variable not defined”. In order to force a variable to be accessible to the entire workbook the statement, the “Public” statement can be used

![](<Base64-Image-Removed>)

And now this will be accessible from Module2 so when the following code is called

![](<Base64-Image-Removed>)

The variable is used as necessary and the expected response happens

![](<Base64-Image-Removed>)

**Why NOT to use Public variables**

It’s not actually a good idea to maintain public variables between function calls. It is much better coding practice for variables to be stored in Subs and Functions and passed as parameters. There shouldn’t be any expectation that the VBA Project to maintains any values of variables. This is because that there are lots of things that can cause a VBA project to reset whilst using the workbook. All public variables will get reset.

Another reason is that if multiple projects are open, other projects can call upon the variable as well which could lead to very interesting results. Save the heartache, avoid public variables.

There are more options for declarations that you might see including “Friend” and “Protected”. However this is done at the Class level which are essentially the “Objects” of VBA which is out of the scope of today’s blog.

[To Top](https://www.sumproduct.com/blog/article/vba-blogs/vba-blog-scoping-variables)

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/scoping-variables/#0)
    
*   [Register](https://sumproduct.com/thought/scoping-variables/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/scoping-variables/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/scoping-variables/#0)

[](https://sumproduct.com/thought/scoping-variables/#0 "close")

top