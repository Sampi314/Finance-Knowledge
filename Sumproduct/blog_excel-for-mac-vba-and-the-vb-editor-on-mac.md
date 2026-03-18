# Excel for Mac: VBA and the VB Editor on Mac

**Source:** https://sumproduct.com/blog/excel-for-mac-vba-and-the-vb-editor-on-mac/

---

[Home](https://sumproduct.com/)

\> Excel for Mac: VBA and the VB Editor on Mac

*   December 5, 2024

Excel for Mac: VBA and the VB Editor on Mac
===========================================

Excel for Mac: VBA and the VB Editor on Mac
===========================================

6 December 2024

_This week in our series about Microsoft Excel for Mac, we cover differences in VBA and the VB Editor in Excel for Mac. The short story is that most things work: some are a little different and some things are just not possible._

![](<Base64-Image-Removed>)

**_Good news first_**

Most of the things you can write with Visual Basic for Applications (VBA) to control what happens in Excel will work on Mac just as it does on Windows. Saying “what happens in Excel” generally means things that happen within your workbooks. Actions such as getting or changing values in ranges, adjusting charts, copying sheets, formatting cells, modifying PivotTables, refreshing data, working with Tables, setting conditional formatting and data validation rules, _etc_. should work, assuming the feature you’re trying to interact with is supported. For example, you can’t run code that’s meant to interact with Power Pivot, because that’s not supported on Mac.

Although you may find articles online that would lead you to believe you can’t do much with VBA on Mac, that’s not the case. We know there are differences, some for good reason, but VBA is still very capable and powerful in Excel for Mac. Microsoft has worked in recent years to improve consistency across Windows and Mac. One good example is the ‘Use Relative References’ mode for recording macros. This was only available on Windows, but in 2019 it was brought to Mac.

**_Why are there differences?_**

Microsoft uses the term “earned differences” to describe cases where there is an intentional reason for differences in their applications between Windows and Mac or other platforms. One of the best examples is the overall look and feel of the applications. It would be unexpected if Excel on Mac used the same style of window on Mac as on Windows, with the minimise, maximise and close buttons near the top-right, when the convention on Mac is for the red, yellow and green buttons that serve a similar function to appear on the top-left. The same goes for dialogs, buttons, drop-downs and other parts of the interface. There are numerous earned differences when it comes to VBA and most are due to inherent differences in the operating systems.

We will cover some of these in more detail.

**_Interacting with the operating system_**

When you want to interact with the operating system, you will likely encounter some differences. For example, on Windows, you can use the **FileSystemObject** to create files on the computer. This will likely cause an error on Mac. Also, the **Application.GetOpenFileName** method has some differences, so you may need to account for those if you’re writing code that you want to use on both Mac and Windows. Microsoft has these differences documented here – [Programmatically Selecting Files in Excel for Windows and Excel for the Mac](https://learn.microsoft.com/en-us/previous-versions/office/developer/office-2010/hh710200(v=office.14))
. A good resource with examples about how to interact with files and folders on Mac is found at a website called ‘Mac Excel Automation’ at [https://macexcel.com/](https://macexcel.com/)
.

Mac has ‘sandboxing’ of applications as a security measure. You need to consider this whenever you want to interact with files or folders. You might use the **GrantAccessToMultipleFiles** command, which Microsoft has documented at [https://learn.microsoft.com/en-us/office/vba/office-mac/grantaccesstomultiplefiles](https://learn.microsoft.com/en-us/office/vba/office-mac/grantaccesstomultiplefiles)
. Otherwise, there may be a prompt shown to the person running the VBA code asking them to give Excel permission to the appropriate files.

**_Differences in display sizes_**

When dealing with the size of things, such as document windows, images, charts and other objects, you may encounter some differences due to the different ways that display dimensions are handled on Mac as opposed to Windows. There is a long history of differences between the operating systems with regard to DPI (dots per inch), which we won’t get into here. Just be aware that you may need to take special care in your code when working with the size and position of things.

**_AppleScript_**

Mac has its own scripting language that you can take advantage of through VBA to do things that are done differently or can’t be done on Windows. This can be very useful to interact with the operating system, especially for actions that VBA doesn’t support directly on Mac. You can write snippets of AppleScript into your VBA code and use the **AppleScriptTask** command to run it. Microsoft has this command with some examples documented at [Run an AppleScript with VB – Microsoft Learn](https://learn.microsoft.com/en-us/office/vba/office-mac/applescripttask)
.

**_Working with the Ribbon_**

You can use RibbonX to customise the arrangement, look and behaviour of the Ribbon, but you may find that some things behave differently or don’t work the same on Mac as they do on Windows. For your specific needs, you’ll need to test and see what works and what doesn’t. Microsoft has documentation of how to work with the ribbon at [Customize the Office Fluent ribbon by using an Open XML formats file](https://learn.microsoft.com/office/vba/Library-Reference/Concepts/customize-the-office-fluent-ribbon-by-using-an-open-xml-formats-file)
.

**_Considerations for compiling your VBA code_**

Some code may not compile successfully if the associated objects, methods or properties are not available on the operating system where you need it to run. To avoid compilation errors, you can use conditional compilation directives documented at [#If…Then…#Else directive – Microsoft Learn](https://learn.microsoft.com/en-us/office/vba/language/reference/user-interface-help/ifthenelse-directive)
. This is a way to tell Excel skip compiling some lines of code depending on the current operating system where your code project is being compiled.

**_What’s missing or not supported_**

*   Editing or creating UserForms is not supported in Excel for Mac. You can run them, but they can only be created and edited in Excel for Windows

*   The VB Editor on Mac is missing the drop-down list of events for **ThisWorkbook** and **Worksheet**. If you want to write a macro that runs when an event happens in Excel, you’ll need to look up the name of it in Microsoft’s documentation, because the VB Editor doesn’t let you pick the event from a drop-down as it does on Windows. On Windows, you would be able to select ‘ThisWorkbook’ or one of the worksheets in the project explorer, and in the code window, you can pick ‘Workbook’ or ‘Worksheet’ from the drop-down at the top of the window.

![](<Base64-Image-Removed>)

Then the second drop-down would include all the available events. On Mac, you’ll get an error when you choose ‘Workbook’ or ‘Worksheet’ from the first drop-down.

![](<Base64-Image-Removed>)

**TIP:** This doesn’t mean you can’t program for something to happen when an event is triggered. You just need to look up the proper name and syntax for the event procedure.

To find the name and syntax for events, go to the Excel VBA documentation at [https://learn.microsoft.com/office/vba/api/excel.workbook#events](https://learn.microsoft.com/office/vba/api/excel.workbook#events)
. Find the appropriate event in the list that suits your needs and look at the article for that event. There are examples for each that will show you the syntax you need to use to make it work. Simply copy the first line of code from the example and paste it into your VBA project. Just make sure to paste it in the right place. If it’s a workbook event, double-click the ‘**ThisWorkbook**‘ object and paste into its code window.

If it’s a worksheet event, then double-click the sheet where you want the code to go and then paste into that sheet’s code window

*   ActiveX is not supported on Mac. While not technically part of VBA, it’s worth noting that ActiveX is a Windows technology, so its controls are not available or supported on Mac
*   Any VBA related to Excel features that are not supported will not work on Mac. This stands to reason. For example, Power Pivot doesn’t work on Mac, so any VBA that applies to Power Pivot will not work.

**_The Visual Basic Editor_**

The editor is essentially the same between Mac and Windows, but you may run into some rough edges on Mac. Some items may have very small text, such as the Project Explorer. Sometimes when you try to arrange the main window or individual code windows, the windows can become misaligned, not look great, and be hard to control. The way to fix this is to close and re-open Excel and try it again. You may be able to get back to a good state by going to the Window menu and using one of the options to arrange the windows.

![](<Base64-Image-Removed>)

The VB Editor is a good example of an application that is not consistent with the style of the operating system where it’s running. You will see that scroll bars, drop-down lists and some other parts of the UI appear more like Windows applications than Mac applications.

We hope you found this topic helpful. Check back for more details about Excel for Mac and how it’s different from Excel for Windows.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/blog/excel-for-mac-vba-and-the-vb-editor-on-mac/#0)
    
*   [Register](https://sumproduct.com/blog/excel-for-mac-vba-and-the-vb-editor-on-mac/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/excel-for-mac-vba-and-the-vb-editor-on-mac/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/excel-for-mac-vba-and-the-vb-editor-on-mac/#0)

[](https://sumproduct.com/blog/excel-for-mac-vba-and-the-vb-editor-on-mac/#0 "close")

top