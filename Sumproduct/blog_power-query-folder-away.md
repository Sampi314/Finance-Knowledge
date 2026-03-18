# Power Query: Fold(er) Away

**Source:** https://sumproduct.com/blog/power-query-folder-away/

---

[Home](https://sumproduct.com/)

\> Power Query: Fold(er) Away

*   February 26, 2019

Power Query: Fold(er) Away
==========================

Power Query: Fold(er) Away
==========================

27 February 2019

_Welcome to our Power Query blog. This week, I look at some of the M functionality for dealing with folders._

**_Folder.Contents()_**

This returns a table containing the properties and contents of the files and folders found at **path**:

**Folder.Contents(path** as text**)** as table

where **path** is the path to the folder to retrieve contents for.

I will use **Folder.Contents()** to show the contents of my Power Query Blog folder:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-479.jpg)

The **M** code I have used is

**\=Folder.Contents(“C:UserskathrOneDriveDocumentsPQ\_StandardExpensesPQ Blog”)**

When I execute the code, I get the following screen:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-495.jpg)

This is a table of the names and some of the attributes of the files in the folder I specified. More detailed attributes are also available under the **_Attributes_** column, which may be expanded if required.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-466.jpg)

**_  
Folder.Files()_**

This returns a table containing a row for each file found at a folder path, and subfolders. Each row contains properties of the folder or file and a link to its content.

**Folder.Files(path** as text**)** as table 

where **path** is the path to the folder to retrieve contents for.

I will use **Folder.Files()** to show the contents of the folder above my Power Query Blog folder:

![](<Base64-Image-Removed>)

The **M** code I have used is

**\=Folder.Files(“C:UserskathrOneDriveDocumentsPQ\_StandardExpenses”)**

When I execute the code, I get the following results:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-359.jpg)

I have reordered the columns to show that **Folder.Files()** also retrieves information about files in subfolders below the specified folder. This can be compared to the results I get if I use **Folder.Contents()** on the same folder.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-311.jpg)

**Folder.Contents()** only shows me those files and folders that are in the specified folder, and does not interrogate data in the subfolders. Next time I will look at an example which extracts file data according to more specific conditions.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-folder-away/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-folder-away/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-folder-away/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-folder-away/#0)

[](https://sumproduct.com/blog/power-query-folder-away/#0 "close")

top