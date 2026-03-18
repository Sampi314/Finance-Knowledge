# VBA Blogs: Multiple Criteria Filter

**Source:** https://sumproduct.com/blog/vba-blogs-multiple-criteria-filter/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Multiple Criteria Filter

*   September 5, 2019

VBA Blogs: Multiple Criteria Filter
===================================

VBA Blogs: Multiple Criteria Filter
===================================

6 September 2019

_Welcome back to the VBA blog. This week, we are going to learn how to use VBA to filter a data table based upon multiple criteria._

Today, we want to create a VBA script to automatically filter a data table based upon multiple criteria. It is a useful method to filter a target data table without instigating a repetitive manual operation.

For example, let’s filter the following data table below based upon the region and item:

![](https://sumproduct.com/wp-content/uploads/2025/05/dcb7919da6963fc52ac2a5a24ce02bf6-1-1.jpg)

If we want to filter the data table with the criteria region equal to **East** and item equal to **Binder**, the result would look like this:

![](https://sumproduct.com/wp-content/uploads/2025/05/35ed0ed300c27dc491f23da7a153b734-1.jpg)

The first step is to set the **ScreenUpdating** application to False. This **ScreenUpdating** application property in VBA is used to toggle screen updating on or off. When we set the **ScreenUpdating** property of an application object to False it will speed up the macro. It’s an example of what is known as an optimising technique.

Application.ScreenUpdating = False

Then, we use the **With** statement to locate the Data worksheet. If the **FilterMode** is set to ‘on’, then this will make the data table show all data. **AutoFilter** syntax is added to the worksheet at range **A1** and the parameter **Field** is set to two (2), which points to the second column (**Region** column) in the data table. The first criterion we want to use for the region column is **East**. Similarly, applying the same logic to the fourth column, we will use the criterion for the **Item** column to be **Binder**.

With Worksheet(“Data”)

If .FilterMode = True Then .ShowAllData

.Range(“A1″).AutoFilter Field:=2, Criteria1:=”East”

.Range(“A1″).AutoFilter Field:=4, Criteria1:=”Binder”

End With

The last code is to turn on **ScreenUpdating** property as shown below.

Application.ScreenUpdating = True

Combing all the lines of code together, we get this:

Sub DataFilter()

    Application.ScreenUpdating = False

    With Worksheet(“Data”)

        If .FilterMode = True Then .ShowAllData

        .Range(“A1″).AutoFilter Field:=2, Criteria1:=”East”

        .Range(“A1″).AutoFilter Field:=4, Criteria1:=”Binder”

    End With

    Application.ScreenUpdating = True

End Sub

By using this method, we can change the criteria in the code and run the code to obtain filtered data table.

See you next week for more VBA tips!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-multiple-criteria-filter/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-multiple-criteria-filter/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-multiple-criteria-filter/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-multiple-criteria-filter/#0)

[](https://sumproduct.com/blog/vba-blogs-multiple-criteria-filter/#0 "close")

top