# VBA Blogs: An Eventful Month Coming up!

**Source:** https://sumproduct.com/blog/vba-blogs-an-eventful-month-coming-up/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: An Eventful Month Coming up!

*   July 6, 2017

VBA Blogs: An Eventful Month Coming up!
=======================================

VBA Blogs: An Eventful Month Coming up!
=======================================

7 July 2017

Welcome back to our VBA blog series – we’ve got an eventful month coming up! Over the next few weeks, we’re going to cover a range of Events – these are the actions that can trigger when something happens, such as opening a file, changing sheets, selecting certain cells, and so on.

Let’s take a look at one of the most common Event macros – the Disclaimer macro.

The Disclaimer macro is commonly used to force people to enter the file on a ‘landing page’, usually containing some key details that people are required to agree to before using the file. Of course, like most popups in Excel, I think people generally won’t read it anyway, so they’ll be happy to sign away their rights to sue, agree that their inputs belong to you, and to give you their first born child, right?

The place to start setting this up is in the “ThisWorkbook” section of the Project Explorer window.

![](<Base64-Image-Removed>)

The actual subroutine can be selected by using the dropdown items at the top of the code window. On the left-hand side, choose “Workbook” to access an expanded dropdown box on the right. By default, the right-hand side will change to Open, though you can choose a different event instead if you want. Also by default, a subroutine will be created called “Workbook\_Open”, allowing you to specify what happens when workbooks are opened.

![](<Base64-Image-Removed>)

The general steps to follow for a disclaimer macro work as follows:

*   Make sure that the disclaimer page is visible
*   Run through each of the sheets
*   If the sheet is anything but the Disclaimer page, then set it to be Very Hidden

The reason we have to make sure the disclaimer page is visible is because there must always be at least one visible worksheet in the workbook. If it starts off hidden, and then you will reach an error if the macro tries to hide all of the other sheets without first unhiding the disclaimer.

The other thing to be aware of is the Very Hidden status of the other sheets. There’s little point in having a disclaimer that can easily be circumvented by right-clicking on the sheet name and unhiding the sheets! Therefore, it’s a good idea to set the Visible property to Very Hidden to be sure that people can’t easily unhide the sheets again.

The code that we’re going to use is as follows:

Private Sub Workbook\_Open()

Dim ws As Worksheet

Sheets(“DisclaimerSheet”).Visible = xlSheetVisible

For Each ws In Sheets

    If ws.Name <> “DisclaimerSheet” Then

        ws.Visible = xlSheetVeryHidden

    End If

Next ws

End Sub

The code, line for line, equates to:

*   Declare a Worksheet variable called “ws”
*   Make sure the “DisclaimerSheet” sheet is visible
*   Start looping through all of the worksheets in Sheets (i.e. all sheets in this workbook)
*   Check if the name of the worksheet is not “DisclaimerSheet” (i.e. don’t hide the disclaimer sheet)
*   If it’s not, change the sheet status to Very Hidden
*   Close the If statement
*   Close the For loop

Then, once they’ve read the disclaimer, you can get them to click on an “I agree” button that runs a similar macro:

Private Sub Unhide\_All()

Dim ws As Worksheet

For Each ws In Sheets

    ws.Visible = xlSheetVisible

Next ws

End Sub

… which will unhide all of the sheets in the file again.

Of course, this requires the person receiving the file to enable macros, meaning that if they choose not to enable, they may well be able to use the file directly without it hiding all of the sheets. Next week, we’ll look at the other side of the equation – setting up a macro to hide everything in a file before it saves. Have a good weekend!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-an-eventful-month-coming-up/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-an-eventful-month-coming-up/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-an-eventful-month-coming-up/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-an-eventful-month-coming-up/#0)

[](https://sumproduct.com/blog/vba-blogs-an-eventful-month-coming-up/#0 "close")

top