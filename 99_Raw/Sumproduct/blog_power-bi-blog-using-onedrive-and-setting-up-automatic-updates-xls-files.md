# Power BI Blog: Using OneDrive and Setting up Automatic Updates – .xls Files

**Source:** https://sumproduct.com/blog/power-bi-blog-using-onedrive-and-setting-up-automatic-updates-xls-files/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Using OneDrive and Setting up Automatic Updates – .xls Files

*   November 21, 2018

Power BI Blog: Using OneDrive and Setting up Automatic Updates – .xls Files
===========================================================================

Power BI Blog: Using OneDrive and Setting up Automatic Updates – .xls Files
===========================================================================

22 November 2018

Welcome back to our Power BI blog series! This week, we’re going to continue the process of setting up our dataset to automatically update from a file on OneDrive.

This week, our data source is a little different. This is inspired by a question raised by someone who was trying to do a similar task but was running into an error. I’m loading a .xls file into Onedrive to perform the same upload task.

![](<Base64-Image-Removed>)

We’re going to follow the same steps that we did before. Open the .xls file in Excel, then copy the path, and connect to it via web in Power BI Desktop.

![](<Base64-Image-Removed>)

Depending on your setup, this may return you an error:

![](<Base64-Image-Removed>)

Longstanding readers of our blog may recognise this – this is the same problem that you get when you try to get data from an Access database. Trying to import .xls files will cause you the same issues. No worries – follow the link provided, which will give you instructions to download the Access Database Engine and install it (make sure that you choose the version that matches your Power BI Desktop version).

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

For the avoidance of doubt, X64 refers to if you have 64-bit, and the other one is for 32-bit.

Once you have this installed and try again, you may run into a more fundamental issue:

![](<Base64-Image-Removed>)

Wait, what? You’ll find that even if you try to connect to the .xls file directly, you’ll still run into this issue. This is for those of you using Office 365 – unfortunately, this approach to connecting to a .xls file isn’t going to work. For those of you using Office 2010/2013/2016/2019, the experience is much smoother, and hopefully you’re able to connect to your file correctly.

Once you’re in, create some charts, publish it, and go to the website to check that the refresh works…

![](<Base64-Image-Removed>)

Oh no… let’s look in the technical details…

![](<Base64-Image-Removed>)

Well, that was underwhelming! Unfortunately, if you’re connecting to a OneDrive source, you can’t refresh your data if it’s being stored as a .xls or as an Access database. So what’s the solution? You need to sync OneDrive to your computer, and schedule refreshes from there instead. Next week – learning how to use Gateways to access your data. Join us then!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-using-onedrive-and-setting-up-automatic-updates-xls-files/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-using-onedrive-and-setting-up-automatic-updates-xls-files/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-using-onedrive-and-setting-up-automatic-updates-xls-files/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-using-onedrive-and-setting-up-automatic-updates-xls-files/#0)

[](https://sumproduct.com/blog/power-bi-blog-using-onedrive-and-setting-up-automatic-updates-xls-files/#0 "close")

top