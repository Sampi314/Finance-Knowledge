# No Filter

**Source:** https://sumproduct.com/thought/no-filter/

---

[Home](https://sumproduct.com/)

\> No Filter

*   April 21, 2023

No Filter
=========

VBA Blogs: No Filter
====================

21 April 2023

_Welcome back to our VBA blog series. It’s been a long time! In this blog, we look at how to remove the filter dropdowns from PivotTables._

Consider the following example of a very simple dashboard:

![](<Base64-Image-Removed>)

Having created slicers to manipulate the data in the PivotTable, we would like to remove the filtering from **Store** and **Salesperson**. We could do this by unchecking the ‘Field Headers’ in the ‘Show’ section of the ‘PivotTable Analyze’ tab:

![](<Base64-Image-Removed>)

However, this also removes the headings:

![](<Base64-Image-Removed>)

We would like to remove the filter dropdowns without removing the headings. We can do this with **VBA**. In the **VBA** Editor, we enter the following code:

![](<Base64-Image-Removed>)

The code is:

**Sub  
DisableFilterArrows()**

**Dim pt As  
PivotTable**

**Dim pf As  
PivotField**

**Dim i As Integer**

**On Error Resume  
Next**

**For i = 1 To 100**

  **Set pt = ActiveSheet.PivotTables(i)**

  **For Each pf In pt.PivotFields**

  **pf.EnableItemSelection = False**

  **Next pf**

**Next i**

**End Sub**

This subroutine runs a loop (currently set to run 100 times) which checks each PivotField on each PivotTable in the currently selected sheet and sets the property **EnableItemSelection** to ‘False’. To enable the filters, we would set **EnableItemSelection** to ‘True’. Having run the subroutine to switch off the filters, we can check the PivotTable.

![](<Base64-Image-Removed>)

The filters have been removed, and the users will use the slicers to filter the data.

See you next time for more **VBA** tips!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/no-filter/#0)
    
*   [Register](https://sumproduct.com/thought/no-filter/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/no-filter/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/no-filter/#0)

[](https://sumproduct.com/thought/no-filter/#0 "close")

top