# CNTL TAB Fix

**Source:** https://edbodmer.com/cntl-tab-fix

---

Excel has changed the CNTL TAB key so you can only switch between two sheets. But you may often want the old method were you want Tab across and go through all the sheets that you have open. This page demonstrates how you can write a simple macro to get back the old CNTL TAB method. The macro is simple, but wen you implement it or modify it, you should understand public variables that save the last value of a variable and also the method for assigning a short-cut like CNTL, TAB with Application.OnKey “^{TAB}”, “x\_CNTL\_TAB”. You can also see how to use the workbooks.activate and the workbooks.count items in VBA. I have put the macro below that you can put into your own file or alternatively you can use the generic macros file. The Application.OnKey statement can be in a place such as the auto\_open that runs when you open the file.

The macro code that you could you use for the CNTL TAB is shown below. Note that the public statement should be at the top of the module and then the name last\_book is retained from the previous go around. When the last\_book variable gets too high, you have to re-set it.

Public last\_book

Sub x\_CNTL\_TAB()

`last_book = last_book + 1` 
`If last_book < Workbooks.Count Then` 
     `Workbooks(last_book).Activate` 
`Else If last_book >= Workbooks.Count Then` 
     `Workbooks(last_book).Activate` 
     `last_book = 0` 
`End If`
End Sub

The application.OnKey statement that assures the CNTL TAB will be called is shown below.

    Application.OnKey "^{TAB}", "x_CNTL_TAB"

The generic macro file that contains the code is attached to the button below and below the button I have put a short little video that describes the process.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=14147&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=0&rand=0.2544769881852982)