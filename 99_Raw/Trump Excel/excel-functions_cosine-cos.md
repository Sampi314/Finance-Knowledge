# Cosine Function (COS) in Excel

**Source:** https://trumpexcel.com/excel-functions/cosine-cos

---

[Skip to content](https://trumpexcel.com/excel-functions/cosine-cos/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-functions/cosine-cos/#below-title)

You can use the COS function in Excel to return the cosine of an angle.

While it might bring back memories of high school geometry, this little function is actually super useful for everything from analyzing waves to building engineering models.

There is just one golden rule you need to remember: **Excel thinks in Radians, not Degrees**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-functions/cosine-cos/#)

COS Function Syntax
-------------------

The syntax is short and sweet:

\=COS(number)

*   number: The angle you want to measure, in radians.

In the following examples, I will show you how to use the COS function in various scenarios.

Example #1: Calculate Cosine for an Angle in Radians
----------------------------------------------------

If your data is already in radians, you’re in luck. You can pass the number directly into the function.

Below is a dataset showing the inclination angles (in radians) for several ramps.

![Data in radians that needs to be converted  into cosine value.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20457%20166'%3E%3C/svg%3E)

You can calculate the cosine of each inclination angle using the simple formula: 

\=COS(B2)

![The COS formula in Excel.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20192'%3E%3C/svg%3E)

Example #2: Calculate Cosine for an Angle in Degrees
----------------------------------------------------

This is where most people get stuck.

If your angles are in degrees (like 45° or 60°), you must convert them to radians first. If you don’t, Excel will treat “60” as “60 radians,” which is definitely not what you want!    

Below is the dataset where I have the angles in degrees, and I want to get the cosine value.

![Dataset with the inclination angle in degrees that needs to be converted into cosine.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20166'%3E%3C/svg%3E)

You have two easy ways to fix this:

### Option 1: The RADIANS Function (Recommended)

This is the cleanest way to do it. Wrap your angle in the `RADIANS` function inside your formula.

\=COS(RADIANS(B2))

![COS function along with the Radians function in Excel.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20435%20187'%3E%3C/svg%3E)

### Option 2: The Math Way

If you prefer doing the math yourself, you can multiply your degree value by PI divided by 180.

\=COS(B2\*PI()/180)

![Using COS function with PI function in Excel.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20201'%3E%3C/svg%3E)

“Wait, why isn’t the result zero?” (A Common Gotcha)
----------------------------------------------------

If you calculate the cosine of 90 degrees, you know the answer should be exactly 0.

However, if you type =COS(RADIANS(90)) into Excel, you might get a weird result like 6.12E-17.

Don’t panic!

This is just a tiny “floating point” rounding error that happens in computers. The number is incredibly close to zero ($0.0000000000000000612$), but not quite.

If you need it to be exactly zero for a logical test, just wrap it in the [ROUND function](https://trumpexcel.com/excel-round-function/)
:

\=ROUND(COS(RADIANS(90)), 10)

Quick Tip: Going Backwards (Inverse Cosine)
-------------------------------------------

What if you have the cosine value (like 0.5) and want to find out what angle created it? You need the **ACOS** function.

\=ACOS(0.5)

Just remember, Excel will give you the answer back in **radians**. To see it in degrees, wrap it up like this:

\=DEGREES(ACOS(0.5)) 2

I hope this guide helps you master the COS function in Excel!

**Other articles you may also like:**

*   [Excel Functions](https://trumpexcel.com/excel-functions/)
    
*   [How to Convert Inches to MM, CM, or Feet in Excel?](https://trumpexcel.com/convert-inches-to-mm-cm-feet-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK