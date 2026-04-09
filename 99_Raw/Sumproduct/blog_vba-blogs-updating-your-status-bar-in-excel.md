# VBA Blogs: Updating your Status (Bar) in Excel

**Source:** https://sumproduct.com/blog/vba-blogs-updating-your-status-bar-in-excel/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Updating your Status (Bar) in Excel

*   March 9, 2017

VBA Blogs: Updating your Status (Bar) in Excel
==============================================

VBA Blogs: Updating your Status (Bar) in Excel
==============================================

10 March 2017

Last week, we talked about putting a message box into your VBA code. This week, we’re going to look at another useful way of giving information back: the Status Bar.

The Status Bar is the little bit at the bottom of the Excel screen. By default, it often tells you useful information such as when you need to manually calculate your spreadsheet. However, we can take control of it using VBA to deliver a customised message to users.

To change this, we have to use the Application.StatusBar property. This is because the Status Bar is something that is application-wide (i.e. it’s not linked to just your spreadsheet or worksheet), and the StatusBar is the name of the object associated with it.

To take control, we can write a macro that looks like this:

![](https://sumproduct.com/wp-content/uploads/2025/05/9b00a899fa10e9b9433ee37e5007d82b.jpg)

Then, to release it, we can write an even simpler macro:

![](https://sumproduct.com/wp-content/uploads/2025/05/e123c161992134514380d17cdaa60cb7.jpg)

That’s it – to give Excel control back, you use the same code, but simply type in “False” instead of the text that you would normally use.

So now you know how to use the Status Bar, you can start changing your status in Excel just as you would on Facebook. Won’t that be grand? See you next week!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-updating-your-status-bar-in-excel/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-updating-your-status-bar-in-excel/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-updating-your-status-bar-in-excel/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-updating-your-status-bar-in-excel/#0)

[](https://sumproduct.com/blog/vba-blogs-updating-your-status-bar-in-excel/#0 "close")

top