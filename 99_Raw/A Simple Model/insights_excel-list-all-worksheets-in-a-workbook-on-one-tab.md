# Excel: List All Worksheets in a Workbook on One Tab | A Simple Model

**Source:** https://www.asimplemodel.com/insights/excel-list-all-worksheets-in-a-workbook-on-one-tab

---

Excel: List All Worksheets in a Workbook on One Tab
===================================================

*   [](https://www.asimplemodel.com/contributors/peter-lynch)
    [Peter Lynch](https://www.asimplemodel.com/contributors/peter-lynch)
    
*   [X](https://www.asimplemodel.com/#x)
     [Facebook](https://www.asimplemodel.com/#facebook)
    

If you are working with dozens of worksheets that are formatted in identical fashion (think of a company that has multiple locations with the same line items), then the ability to list all of these worksheets on one tab can be extremely helpful. As you will see in the [template available for download](https://www.asimplemodel.com/insights/excel-list-all-worksheets-in-a-workbook-on-one-tab#mailSentPopup)
, this permits retreiving data with the =INDIRECT function from each individual worksheet.

To create a list of tab names in your workbook follow these two steps:

**Step 1:**

Name the following formula “Sheets”

\=(GET.WORKBOOK(1))&T(NOW())

_Note: If you are not familiar with this process select Formulas > Name Manager > New and then input the formula._

**Step 2:**

Then use this formula to retreive all worksheet names:

\=INDEX(MID(Sheets,FIND(“\]”,Sheets)+1,255),ROW(A1))

[Download Template](https://www.asimplemodel.com/insights/excel-list-all-worksheets-in-a-workbook-on-one-tab#mailSentPopup)

![](https://www.asimplemodel.com/wp-content/uploads/2021/10/List-all-Worksheet-in-a-Workbook.png "List-all-Worksheet- in-a-Workbook")

*   [X](https://www.asimplemodel.com/#x)
     [Facebook](https://www.asimplemodel.com/#facebook)
    

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

Download links are sent directly to your inbox! Input your email address below and we will send you an email with the information requested.

 I agree to ASM's [Terms of Use](https://www.asimplemodel.com/insights/excel-list-all-worksheets-in-a-workbook-on-one-tab#)
 and [Privacy Policy](https://www.asimplemodel.com/insights/excel-list-all-worksheets-in-a-workbook-on-one-tab#)
.  

     

You will only need to provide your email address the first time. All future downloads will be sent to the same email address.

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

A link to this file will be sent to the following email address:

If you would like to send this to a different email address, Please click here then click on the link again.

X ![](https://www.asimplemodel.com/insights/excel-list-all-worksheets-in-a-workbook-on-one-tab) [Click Here to Visit URL](https://www.asimplemodel.com/insights/excel-list-all-worksheets-in-a-workbook-on-one-tab)

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

A link to this file will be sent to the following email address:

If you would like to send this to a different email address, Please click here then click on the link again.

Copy link

✓

Thanks for sharing!

Find any service

[AddToAny](https://www.addtoany.com/ "Share Buttons")

[More…](https://www.asimplemodel.com/insights/excel-list-all-worksheets-in-a-workbook-on-one-tab#addtoany "Show all")