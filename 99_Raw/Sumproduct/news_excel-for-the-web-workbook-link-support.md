# Excel for the Web Workbook Link Support

**Source:** https://sumproduct.com/news/excel-for-the-web-workbook-link-support/

---

[Home](https://sumproduct.com/)

\> Excel for the Web Workbook Link Support

*   August 19, 2020

Excel for the Web Workbook Link Support
=======================================

Excel for the Web Workbook Link Support
=======================================

19 August 2020

One common action undertaken in the PC and Mac desktop variants of Excel is linking between files. This provides a record of where the data was sourced from and, if the data changes, it is easily refreshed. This has been missing from Excel for the Web. But not anymore: Microsoft has just announced that workbook link support is now rolling out for its online cousin.

To create a new workbook link, follow these simple steps:

*   open two workbooks in Excel for the web (they should be stored in either OneDrive or SharePoint)

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-39.jpg)

*   in the source workbook, copy the range

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-31.jpg)

*   in the destination workbook, ‘Paste Links’ via the right-click menu or via ‘Paste Special’ on the ‘Home’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-28.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-22.jpg)

Alternatively, you may reference the workbook explicitly (no, not by swearing at it!) using the following reference pattern:

**\=’https://domain/folder/\[workbookName.xlsx\]sheetName’!CellOrRangeAddress**

Now that linked workbooks are possible, when you open a workbook that contains workbook links in Excel for the Web, you will see a yellow bar notifying you that the workbook is referencing external data, similar to the desktop versions of Excel:

![](https://sumproduct.com/wp-content/uploads/2025/05/7e80bcfa618b223856fe7be0a117e62f.jpg)

If you ignore or dismiss the bar, we will not be able to update the links. This will mean the values will remain as previously displayed. If you click the ‘Enable Content’ button, Excel for the Web will retrieve the values from **all** the linked workbooks.

To help you manage these links, Microsoft has added a new ‘Workbook Links’ task pane. This task pane may be accessed by pressing the ‘Workbook Links’ button on the Data tab

![](<Base64-Image-Removed>)

or via the ‘Manage Workbook Links’ button _(on the yellow bar above)_.

The task pane looks like this:

![](<Base64-Image-Removed>)

The task pane will list all of your linked workbooks and provides you with information on the status of each of the linked workbooks. If the link cannot be updated, the status _should_ explain the cause. This way you should quickly spot issues, with any workbook that cannot be updated highlighted at the top of the list.

At a global level you may take the following actions:

*   **Refresh all:** this triggers an immediate refresh of all linked workbooks
*   **Refresh links automatically:** when enabled, this causes Excel to periodically check for updated values while you are in the workbook
*   **Break all links:** this removes all the workbook links by replacing those formulae with their current values (_i.e._ Paste Special as Values).

At a workbook level you may take the following actions:

*   **Refresh workbook:** this triggers an immediate refresh of the linked workbook
*   **Open workbook:** this opens the linked workbook in another tab
*   **Break links:** this removes links to that workbook by replacing those formulae with their values (_i.e._ Paste Special as Values)
*   **Find next link:** this selects the next occurrence of a link to that linked workbook (yay, finally – a quick method for finding those pesky [phantom links](https://www.sumproduct.com/thought/locating-links)
     – it would be nice if this could be done for the desktop more simply too…).

There’s one more thing to note. Microsoft is at it again. Not content with renaming Windows and Office applications and channels, they have decided to start renaming other things end users have understood well for years. Microsoft notes that direct links to external workbooks have historically been referred to simply as **external links**. They feel it is time to make a change, as more external data sources are added to Excel, this term will become more ambiguous (no, they will still be external links). Therefore, please note to “…improve clarity going forward…”, the term **workbook links** will be used instead. You have been warned – but at least you can now link using Excel for the Web!

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/excel-for-the-web-workbook-link-support/#0)
    
*   [Register](https://sumproduct.com/news/excel-for-the-web-workbook-link-support/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/excel-for-the-web-workbook-link-support/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/excel-for-the-web-workbook-link-support/#0)

[](https://sumproduct.com/news/excel-for-the-web-workbook-link-support/#0 "close")

top