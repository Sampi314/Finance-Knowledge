# Avoid Nested IF Function in Excel...VLOOKUP to Rescue

**Source:** https://trumpexcel.com/avoid-nested-if-function-vlookup

---

[Skip to content](https://trumpexcel.com/avoid-nested-if-function-vlookup/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/avoid-nested-if-function-vlookup/#below-title)

A lot of times people ask me to help them in rectifying an error in their nested IF function. And sometimes their formula is bigger than this blog post (seriously! not kidding).

However, in some of the cases, this long formula can be cut short by using the [VLOOKUP function](https://trumpexcel.com/excel-vlookup-function/)
.

##### Avoiding Nested IF Function

Consider a scenario as shown below. You have a list of students and their marks in an exam. Now you need to assign a grade to each student, based on predefined criteria.

Something as shown below:

![Nested IF Function - Vlookup to rescue Criteria and Data set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20569%20271'%3E%3C/svg%3E)

Now one way is to write a long nested IF function and waste your time. Other, more time efficient, is the VLOOKUP way.

##### **Vlookup to Rescue**

To use VLOOKUP we need to slightly modify the criteria table, and make something as shown below

![Nested IF Function - Vlookup criteria](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20589%20264'%3E%3C/svg%3E)

A **prerequisite** for this method is that criteria numbers in column I should be **sorted in ascending order**. The VLOOKUP method would not work if this list is not sorted.

Now use the below formula:

\=VLOOKUP(C3,$I$3:$J$10,2,TRUE)

While this is our same standard VLOOKUP formula, notice it has an argument ‘TRUE’ at the end, which means an approximate match.

This means that when the marks are less than 30, VLOOKUP returns the grade for 0, which is F, but when it is 30, it will return E. Similarly, when marks are between 30 and 40, it returns grade E, but when it becomes 40 (or between 40 and 50) it returns grade D.

This is definitely a time saver, and easy to use than the long nested [IF Function](https://trumpexcel.com/excel-if-function/)
.

**Other Excel articles you may also like:**

*   [SWITCH Function in Excel](https://trumpexcel.com/excel-functions/switch-function/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

3 thoughts on “Avoid Nested IF Function in Excel…VLOOKUP to Rescue”
-------------------------------------------------------------------

1.  it’s so helpful and this video tutorials give me a boost of learning
    
    [Reply](https://trumpexcel.com/avoid-nested-if-function-vlookup/#comment-12304)
    
2.  I like the method
    
    [Reply](https://trumpexcel.com/avoid-nested-if-function-vlookup/#comment-3222)
    
3.  Thanks…this is useful!
    
    [Reply](https://trumpexcel.com/avoid-nested-if-function-vlookup/#comment-13)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/avoid-nested-if-function-vlookup/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

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