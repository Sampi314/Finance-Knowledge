# Final Friday Fix: January 2019 Challenge

**Source:** https://sumproduct.com/blog/final-friday-fix-january-2019-challenge/

---

[Home](https://sumproduct.com/)

\> Final Friday Fix: January 2019 Challenge

*   January 24, 2019

Final Friday Fix: January 2019 Challenge
========================================

Final Friday Fix: January 2019 Challenge
========================================

25 January 2019

_On the final Friday of each month, we’re going to set an Excel challenge for you to puzzle over so that you can get your “Excel fix”. Challenge your office colleagues to see who can solve the puzzle quickest. There’s no prizes at this stage, you’re playing for bragging rights only!_

February’s newsletter covers several date functions in Excel, so we thought it might be good to make our Final Friday Fix tie in with that theme. Apologies to US readers who can still do this month’s challenge – you’ll just have to do it the other way around. All will make sense below!

**_Working with Dates in Excel_**

Dates are not quite what they seem in Excel. They can cause issues for the unwary, so they are important to understand. For example, August 17, 2008 may be expressed as:

*   8/17/08 (month/day/year, US format)
*   17-8-08 (day – month – year, UK / Europe format, as it’s called by Microsoft, but pretty much anywhere else)
*   August 17, 2008
*   17 Aug 2008
*   …

Therefore, it does not make sense for Excel to try and force a particular format and many formats are thus supported. Indeed, one thing that is more sophisticated is the fact that whether by default, day comes before month or vice versa is down to your regional settings. This means if I type in

**17/8/08**

on some computers, this will be recognised as a date, whereas on others it will be seen as a ‘General’ text format because 17 exceeds the number of months in a year. For our American readers, I apologise in advance: my computer is not set to US settings and therefore, the examples here will be displayed as day followed by month followed by year. In the US, the month preceded the day.

The point is, these are display issues only. As a non-US Excel user, I will type “17/8/08” into cell **A1**, and then format the cell as ‘General’ (using the drop-down box in the ‘Number’ grouping of the ‘Home’ tab):

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-497.jpg)

This changes cell **A1** as follows:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-516.jpg)

It becomes “39677”, which is known as a **serial number** (if I were to delete this value, it would make me a serial killer). This serial number is a count from “Day 1” which is defined as 1 January 1900, so Day 2 would be 2 January 1900, Day 3 would be 3 January 1900, and so on. Therefore, according to Excel, 17 August 2008 is Day 39,677.

In essence, we just need Excel to recognise the date as a date – and that’s this month’s challenge…

**_The Challenge_**

This month’s challenge is to convert from US date format (month – day – year) to what is known as the non-US, or more commonly, the European, date format (day – month – year). If you’re in the US, the challenge is the opposite!

The problem arises when you receive date data in a spreadsheet that is not recognised by your regional settings. Therefore, for me, my computer cannot make sense of US date formats such as

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-485.jpg)

I have left the data in ‘General’ style deliberately so you can see only one entry, cell **A4**, is recognised as a number (date). The problem is, even that’s wrong as that represents 5 December 2022 not 12 May 2022.

How do I convert it? The simplest answer would be to use Power Query / Get & Transform – but that’s not what I want here. It may also be done with Excel’s ‘Text to Columns’ feature, but that’s not the solution here either. I want **one**_formula_ to do the following:

![](<Base64-Image-Removed>)

_Sound easy? Have a go. We’ll publish a couple of solutions in Monday’s blog. Have a great weekend!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/final-friday-fix-january-2019-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/final-friday-fix-january-2019-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/final-friday-fix-january-2019-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/final-friday-fix-january-2019-challenge/#0)

[](https://sumproduct.com/blog/final-friday-fix-january-2019-challenge/#0 "close")

top