# Adjust Excel Scroll Bar Maximum Value based on Cell Value

**Source:** https://trumpexcel.com/adjust-scroll-bar-maximum-value

---

[Skip to content](https://trumpexcel.com/adjust-scroll-bar-maximum-value/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/adjust-scroll-bar-maximum-value/#below-title)

I often wonder why there is no provision to adjust the maximum value of a [scroll bar in Excel](https://trumpexcel.com/create-a-scroll-bar-in-excel/)
 based on a cell value. Had this been available, a scroll bar would automatically adjust its maximum value when the cell value changes.

Something, as shown below, could then have been possible:![Adjust Scroll Bar Maximum Value based on a Cell Value in Excel Test2](https://trumpexcel.com/wp-content/uploads/2014/01/Scroll-Bar-Max-Value-Test2.gif)

Until the time it is not made available by the Microsoft Office team, this tip can help you link the maximum value for a scroll bar to a cell.

#### Adjust Scroll Bar Maximum Value in Excel

1.  Go to Developer Tab –> Insert –> ActiveX Controls –> Scroll Bar (ActiveX Control)
    *   Do not have the developer tab?? Read here on how to [add the developer tab to the ribbon](https://trumpexcel.com/excel-developer-tab/)
        .

![Adjust Scroll Bar Maximum Value based on a Cell Value in Excel Activex Control Insert](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20286%20213'%3E%3C/svg%3E)

1.  Click Anywhere in your worksheet to insert the [Scroll Bar](https://trumpexcel.com/create-a-scroll-bar-in-excel/)
    .
2.  Right-click on the Scroll Bar and select Properties.
3.  Set the linked cell as C10 and close the properties box.
    *   I have used C10 in this example. You can have a different cell where you have the maximum value.

![Adjust Scroll Bar Maximum Value based on a Cell Value in Excel Set Max Value Property](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20463%20303'%3E%3C/svg%3E)

1.  Double Click on the Scroll Bar. It will open the VBA Editor with a code that looks like this:

Private Sub ScrollBar1\_Change()

End Sub

1.  Add a line so that your code looks like this:

Private Sub ScrollBar1\_Change()
Activesheet.Scrollbar1.Max = Range("C7").Value
End Sub

1.  Close the VBA Editor window.
2.  Go to the Developer tab and left-click on Design Mode button.
3.  That’s It!! You Scroll Bar is all set to be used.

Note that since the file has a macro, you need to save the file in either .**xls** or .**xlsm** format.

_Once you are done setting this up, and **IF** the scroll bar is not working, follow these steps:_

*   _Go to Developer Tab click on Design Mode._
*   _Double click on the scroll bar._
*   _In the VBA Editor, Press F5, or click on the Run Sub/User form button._
*   _Close the VBA Editor._

![Adjust Scroll Bar Maximum Value based on a Cell Value in Excel VBA Code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20375%20144'%3E%3C/svg%3E)

**Try it yourself.. Download the file  
[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://www.dropbox.com/s/vzn121r8xblqxku/Adjust-Scroll-Bar-Maximum-Scroll-Value.xlsm?dl=1)
**

**You May Also Like the Following Excel Tutorials:**

*   [How to Create Dynamic Labels in Excel Scroll Bar](https://trumpexcel.com/dynamic-labels-in-excel-scroll-bar/)
    .
*   [How to Insert and Use Check Boxes in Excel](https://trumpexcel.com/insert-checkbox-in-excel/)
    .
*   [How to Insert and Use Radio Buttons in Excel](https://trumpexcel.com/insert-use-radio-button-in-excel/)
    .
*   [Free Online Excel Training](https://trumpexcel.com/)
     (7 Part Online Video Course).
*   [Insert Check Mark (Tick ✓) Symbol in Excel](https://trumpexcel.com/check-mark/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “Adjust Scroll Bar Maximum Value based on a Cell Value in Excel”
------------------------------------------------------------------------------

1.  Nice tip
    
    [Reply](https://trumpexcel.com/adjust-scroll-bar-maximum-value/#comment-11302)
    
2.  Hi great tutorial, if I wanted the scroll bar to always display newest data added at the bottom of the scroll whenever added. How is this possible?
    
    [Reply](https://trumpexcel.com/adjust-scroll-bar-maximum-value/#comment-2528)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/adjust-scroll-bar-maximum-value/#respond)

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