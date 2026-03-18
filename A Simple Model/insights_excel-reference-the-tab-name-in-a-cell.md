# Excel: Reference the tab name in a cell. | A Simple Model

**Source:** https://www.asimplemodel.com/insights/excel-reference-the-tab-name-in-a-cell

---

Excel: Reference the tab name in a cell.
========================================

*   [](https://www.asimplemodel.com/contributors/peter-lynch)
    [Peter Lynch](https://www.asimplemodel.com/contributors/peter-lynch)
    
*   [X](https://www.asimplemodel.com/#x)
     [Facebook](https://www.asimplemodel.com/#facebook)
    

Occasionally when you are working with a lot of tabs it helps to have a reference to the tab name on the worksheet. An example might be a workbook containing financials for 100 restaurants.

To understand how this works first input the following in any worksheet.

\=CELL(“filename”,A1)

This formula will retrieve the file path for your workbook. Since we are only interested in the name of the worksheet, we can modify this formula with the =MID function to retrieve only that portion of the file path.

Expand upon the previous formula with the following:

\=MID(CELL(“filename”,A1),FIND(“\]”,CELL(“filename”,A2))+1,255)

_Note: 255 characters is the maximum length for a directory path._ 

In the image below you will see that the formula in cell D18 (which is visible in cell D17) returns “Consolidated.”

[Download Template](https://www.asimplemodel.com/insights/excel-reference-the-tab-name-in-a-cell#mailSentPopup)

![](https://www.asimplemodel.com/wp-content/uploads/2021/10/Reference-Tab-Name-in-Cell.png "Reference-Tab-Name-in-Cell")

*   [X](https://www.asimplemodel.com/#x)
     [Facebook](https://www.asimplemodel.com/#facebook)
    

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

Download links are sent directly to your inbox! Input your email address below and we will send you an email with the information requested.

 I agree to ASM's [Terms of Use](https://www.asimplemodel.com/insights/excel-reference-the-tab-name-in-a-cell#)
 and [Privacy Policy](https://www.asimplemodel.com/insights/excel-reference-the-tab-name-in-a-cell#)
.  

     

You will only need to provide your email address the first time. All future downloads will be sent to the same email address.

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

A link to this file will be sent to the following email address:

If you would like to send this to a different email address, Please click here then click on the link again.

X ![](https://www.asimplemodel.com/insights/excel-reference-the-tab-name-in-a-cell) [Click Here to Visit URL](https://www.asimplemodel.com/insights/excel-reference-the-tab-name-in-a-cell)

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

A link to this file will be sent to the following email address:

If you would like to send this to a different email address, Please click here then click on the link again.

Copy link

✓

Thanks for sharing!

Find any service

[AddToAny](https://www.addtoany.com/ "Share Buttons")

[More…](https://www.asimplemodel.com/insights/excel-reference-the-tab-name-in-a-cell#addtoany "Show all")