# VBA Blogs: Handling VBA Errors

**Source:** https://sumproduct.com/blog/vba-blogs-handling-vba-errors/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Handling VBA Errors

*   May 11, 2017

VBA Blogs: Handling VBA Errors
==============================

VBA Blogs: Handling VBA Errors
==============================

12 May 2017

Welcome back to the weekly VBA Blog! In this week’s edition, we look at what happens when you run into errors.

Last time we were here, we talked about a macro you could use to loop through all of the sheets in a file and unhide them and unprotect them. This presents problems when there are passwords that you’re not aware of. If this happens, you get a debug error that looks something like this when it keeps trying to run:

![](https://sumproduct.com/wp-content/uploads/2025/05/5d21dfcb2e538dab313347b01c1b4320.jpg)

Well, what can we do about it? It depends what do you want it to do, really. Error handling is an important part of VBA because it helps us dictate what you do in these circumstances. Here are some common tools you can use:

*   On Error Goto <abc>

This Is generally followed up somewhere else in your code by the text “<abc>:”. This line tells Excel that it if it runs into an error, it should jump to that section in your code and run the next statement. This is generally how you can jump out of an error that might cause other parts of your code to have problems.

*   On Error Goto 0

It seems a little strange, in the context of the last point, but this line undoes the effect of the previous line and causes errors to stop the code and prompt you for instructions. While this stops your code from running smoothly, it alerts you to problems so that you can address them appropriately.

*   On Error Resume Next

This is a useful but dangerous tool that will ignore any errors and plough on with the next line of code. This should only be used if you expect to have errors occur that will have no follow-up consequences.

Here’s how we might use it to improve our macro code:

For Each ws In ActiveWorkbook.Sheets

    ws.Visible = xlSheetVisible 

    ws.Activate 

    ws.Unprotect 

    On Error GoTo NextSheet   

    ws.Rows.EntireRow.Hidden = False 

    ws.Columns.EntireColumn.Hidden = False 

NextSheet: 

      On Error GoTo 0 

Next ws

Now, when a sheet can’t be unprotected, it will skip trying to unhide rows and columns, and just move straight onto the next sheet. Important to note – we reset the error check so that if another unexpected error occurs, we can ensure that it gets raised just like it should.

Hopefully this is a useful tip for working with your macros moving forward!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-handling-vba-errors/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-handling-vba-errors/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-handling-vba-errors/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-handling-vba-errors/#0)

[](https://sumproduct.com/blog/vba-blogs-handling-vba-errors/#0 "close")

top