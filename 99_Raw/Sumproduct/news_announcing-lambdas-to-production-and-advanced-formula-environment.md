# Announcing LAMBDAs to Production and Advanced Formula Environment

**Source:** https://sumproduct.com/news/announcing-lambdas-to-production-and-advanced-formula-environment/

---

[Home](https://sumproduct.com/)

\> Announcing LAMBDAs to Production and Advanced Formula Environment

*   February 10, 2022

Announcing LAMBDAs to Production and Advanced Formula Environment
=================================================================

Announcing LAMBDAs to Production and Advanced Formula Environment
=================================================================

10 February 2022

At last! **LAMBDA** and the **LAMBDA** helper functions are now Generally Available to anyone using Production: Current Channel builds of Excel. In conjunction with **LAMBDA** going to production, Microsoft has also announced the release of a new add-in, the Advanced Formula Environment, which allows simpler importing, exporting and authoring of named **LAMBDA**s.

As a reminder, [**LAMBDA**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-lambda-function)
 allows you to define a custom function in Excel’s very own formula language.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-7.jpg)

To show how **LAMBDA** and the Advanced Formula Environment might work together, let’s look at an example that Microsoft use for simplicity: **IFBLANK**.

Now, no such function exists in Excel – but now, it _can_. Many regularly encounter issues replacing certain values in a dataset, such as errors or blanks cells. Excel provides **IFERROR** to replace error values, but there is no function to replace blank cells. However, with **LAMBDA**, you may now build your own **IFBLANK** function.

Now you may author this in a worksheet and then import it into the Name Manager, but you may also create this in the new formula environment and then synchronise it with the Excel workbook to make use of it therein.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-5.jpg)

Without **IFBLANK**, Excel, by default returns a blank which gets coerced to zero \[0\] when placed in the cell. Not any more.

Furthermore, Microsoft has added support for function ToolTips for named **LAMBDA**s in addition to auto-completing the open parentheses character when calling these functions, _i.e._ calling a function defined using a **LAMBDA** is now exactly the same as calling a native function.

Also, Microsoft has increased the limit of recursion by 16 times its original limit, _i.e._ Microsoft has increased the limit of recursion by 16 times its original limit, _i.e._ Microsoft has increased the limit of recursion by 16 times its original limit…

The way the **LAMBDA** helper functions handle arrays of references differently now too. Previously when **a LAMBDA** helper function returned an array and the associated **LAMBDA** returns a single cell, an _#CALC!_ error would be returned. This has now been modified to automatically return the cell value as the output of the **LAMBDA** function.

**_Advanced Formula Environment_**

To facilitate the new, improved **LAMBDA** in a Current Channel production environment, a new tool to aid in the authoring of more complex named formulae has been created. The Advanced Formula Environment (AFE) is a space where you may explore new and different methods for authoring formulae with special functionality designed with **LAMBDA**s and **LET** in mind.

This new tool includes the following features:

*   advanced formula authoring capabilities:
    *   Intellisense
    *   commenting
    *   in-line errors
    *   auto tabulation
    *   code collapse
*   undo / redo of formula edits within the manager
*   namespaces to allow for groups of named functions
*   import and export functionality
*   text and GitHub Gist import
*   different views to filter your names and edit in a single location.

The environment is available on all platforms where Office Add-ins are available (_i.e._ Mac, Windows and the Web).

There are two views presently in this tool: Manager and Editor views.

Think of the Manager view as similar to Excel’s Name Manager, but with more functionality. This is where you will see all of your names with their own individual cards and associated quick actions. There are four key actions:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

On the other hand, the Editor is where you can go to edit all entries within the workbook or create new namespaces for collections of formulae. This is where you will most likely go to create more complex functions, since you get the full version of the Editor in this view and may create multiple names sequentially.

The workbook section contains all names which are not attached to a given sheet but instead are saved globally in the workbook.

![](<Base64-Image-Removed>)

The Advanced Formula Environment can import definitions into the manager. You can important individual definitions as well as libraries of definitions via text or through GitHub Gists. The main entry point for importing can be found by selecting the action in the actions bar. The main entry point defaults to “From URL” but the dropdown reveals the “From text” option.

![](<Base64-Image-Removed>)

**_Accessibility_**

To get access to **LAMBDA** functions, please make sure you have updated to the latest version of Excel. **LAMBDA** is now available to Office 365 Subscribers in Production: Current Channel. Versions must be greater than or equal to:

*   Windows: 16.0.14729.20260
*   Mac: 16.56 (Build 21121100)
*   iOS: 2.56 (Build 21120700)
*   Android: 16.0.14729.20176.

To access the Advanced Formula Environment (AFE), you may use this link or manually install if from the app:

[https://aka.ms/get-afe](https://aka.ms/get-afe)

To access the AFE, simply search for the “advanced formula environment” within the built-in add-ins store of Excel and install it like any other Office add-in:

*   go the Insert Tab
*   select the ‘Get Add-ins’ button
*   search for “advanced formula environment”
*   click the ‘Add’ button

Once the add-in is installed, you should be able to find it on your Home tab. The Ribbon button appears as follows:

![](<Base64-Image-Removed>)

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/announcing-lambdas-to-production-and-advanced-formula-environment/#0)
    
*   [Register](https://sumproduct.com/news/announcing-lambdas-to-production-and-advanced-formula-environment/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/announcing-lambdas-to-production-and-advanced-formula-environment/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/announcing-lambdas-to-production-and-advanced-formula-environment/#0)

[](https://sumproduct.com/news/announcing-lambdas-to-production-and-advanced-formula-environment/#0 "close")

top