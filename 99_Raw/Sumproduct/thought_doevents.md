# DoEvents

**Source:** https://sumproduct.com/thought/doevents/

---

[Home](https://sumproduct.com/)

\> DoEvents

*   August 4, 2017

DoEvents
========

VBA Blogs: DoEvents
===================

4 August 2017

It’s a great feeling when you write an involved piece of code with grand loops that apply over thousands of rows. There’s a sweet sensation when you save the file, hit run, and watch your handiwork unfold in front of you… until the screen stops updating, Excel goes to “Not Responding” and you’re left wondering: “Has it crashed? Is it still running? What do I do now?”

![](<Base64-Image-Removed>)

This has happened to me in recent weeks, running a VBA script on a database of 50,000 names, and supposedly ceasing to respond a mere 39 rows in.

![](<Base64-Image-Removed>)

This happens essentially because Windows thinks that Excel isn’t responding (since Windows displays what’s at the top of your screen), and it thinks that because Excel is devoting all of its resources to actually running your macro. It also happens when you’re updating the status bar or immediate window, and you can actually see the updates stop and pause.

An easy way around this is to include the code “DoEvents” into your loop somewhere. DoEvents essentially passes control back to Windows, essentially pausing your code and allowing Windows to send all of the keystrokes, commands and any other events through to Excel.

![](<Base64-Image-Removed>)

So if you’re wondering why Excel sometimes doesn’t respond to Esc or Ctrl-Break, incorporating DoEvents into your code will help make it more responsive and ensure that it continues to update you while it’s running your macros. It’s the virtual equivalent of having Excel take its headphones off and look up, to see what the rest of the operating system is doing.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/doevents/#0)
    
*   [Register](https://sumproduct.com/thought/doevents/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/doevents/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/doevents/#0)

[](https://sumproduct.com/thought/doevents/#0 "close")

top