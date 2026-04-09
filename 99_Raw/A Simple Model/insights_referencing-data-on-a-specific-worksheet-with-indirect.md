# Referencing Data on a Specific Worksheet with =INDIRECT | A Simple Model

**Source:** https://www.asimplemodel.com/insights/referencing-data-on-a-specific-worksheet-with-indirect

---

Referencing Data on a Specific Worksheet with =INDIRECT
=======================================================

*   [](https://www.asimplemodel.com/contributors/peter-lynch)
    [Peter Lynch](https://www.asimplemodel.com/contributors/peter-lynch)
    
*   [X](https://www.asimplemodel.com/#x)
     [Facebook](https://www.asimplemodel.com/#facebook)
    

_Note:_ [_Template available for download._](https://www.asimplemodel.com/insights/referencing-data-on-a-specific-worksheet-with-indirect#mailSentPopup)

The =INDIRECT function permits referencing information in a workbook using strings of text. This can be a very handy tool when you want to create dynamic references in formulas without changing the formulas themselves. It is also a terrific way to reference data on different worksheets.

To provide an example of how this function can be used, assume that you want to reference information on a different worksheet with tab name Sheet 1 in cell C6. On any other tab in the workbook you could input the following formula to retreive this information:

\=INDIRECT(“‘Sheet 1’!C6”)

But this is a very static approach. The =INDIRECT function can be made far more useful with dynamic references to text. For example, if all worksheets have the same name with the exception of a number (i.e. Sheet 1, Sheet 2, Sheet 3, etc.), then the worksheet name can be a cell reference:

\=INDIRECT(“‘Sheet”&\[REFERENCE TO CELL WITH SHEET NUMBER\]&”‘!C6”)

Or as another alternative, you can input a function that will count up from one as you drag the formula down:

\=INDIRECT(“‘”&”Sheet”&ROW(A1)&”‘!C6”)

_Note: The ROW() function returns the row number. So =ROW(A1) returns the value 1. As you paste this formula down it will return a value that increases by 1 with each new row._

This is the formula used in the image below in the array D38:D42 with the \[REFERENCE TO CELL WITH SHEET NUMBER\] linking to B38:B42. _(The only difference being that the sheet name is Sheet (1) vs Sheet 1.)_

The biggest challenge is when all of the worksheets have unique names. For a solution to this please scroll to the bottom of this post.

[Download Template](https://www.asimplemodel.com/insights/referencing-data-on-a-specific-worksheet-with-indirect#mailSentPopup)

![](https://www.asimplemodel.com/wp-content/uploads/2021/10/Reference-Data-on-a-Specific-Worksheet.png "Reference-Data-on-a-Specific-Worksheet")

*   [X](https://www.asimplemodel.com/#x)
     [Facebook](https://www.asimplemodel.com/#facebook)
    

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

Download links are sent directly to your inbox! Input your email address below and we will send you an email with the information requested.

 I agree to ASM's [Terms of Use](https://www.asimplemodel.com/insights/referencing-data-on-a-specific-worksheet-with-indirect#)
 and [Privacy Policy](https://www.asimplemodel.com/insights/referencing-data-on-a-specific-worksheet-with-indirect#)
.  

     

You will only need to provide your email address the first time. All future downloads will be sent to the same email address.

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

A link to this file will be sent to the following email address:

If you would like to send this to a different email address, Please click here then click on the link again.

X ![](https://www.asimplemodel.com/insights/referencing-data-on-a-specific-worksheet-with-indirect) [Click Here to Visit URL](https://www.asimplemodel.com/insights/referencing-data-on-a-specific-worksheet-with-indirect)

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

A link to this file will be sent to the following email address:

If you would like to send this to a different email address, Please click here then click on the link again.

Copy link

✓

Thanks for sharing!

Find any service

[AddToAny](https://www.addtoany.com/ "Share Buttons")

[More…](https://www.asimplemodel.com/insights/referencing-data-on-a-specific-worksheet-with-indirect#addtoany "Show all")