# Power Query: Find the Folder

**Source:** https://sumproduct.com/blog/power-query-find-the-folder/

---

[Home](https://sumproduct.com/)

\> Power Query: Find the Folder

*   March 5, 2019

Power Query: Find the Folder
============================

Power Query: Find the Folder
============================

6 March 2019

_Welcome to our Power Query blog. This week, I look at an example which uses some of the M functionality for dealing with files and folders._

[Last week](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-folder-away)
, I created blank queries and used **M** code to extract data from a folder in Power Query. In [Power Query: One Folder, One Query](https://sumproduct.com/blog/power-query-one-folder-one-query/)
, I created a query that contained similar data from a folder, which I could then combine. This time, I am going to use a similar method and take a different path through the options so that I can view the subfolders in a folder.

![](<Base64-Image-Removed>)

I begin by creating a new query ‘From Folder’ by choosing this option from the ‘From File’ dropdown in the ‘New Query’ section of the ‘Get & Transform’ functionality on the ‘Data’ tab.

![](<Base64-Image-Removed>)

Power Query prompts me for the location of the folder and I choose to browse:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

I find the folder which contains my ‘PQ Blogs’ folder.

![](<Base64-Image-Removed>)

In the preview, I can see a list of documents and workbooks, but no folders. Unlike the aim in [Power Query: One Folder, One Query](https://sumproduct.com/blog/power-query-one-folder-one-query/)
, this time I want to see **all** file types in the folder. I don’t want to combine the data; I want to edit it so that I can look for specific data in the folder.

![](<Base64-Image-Removed>)

Now I have chosen to edit the data, I can see the **M** code behind the query.

**\= Folder.Files(“C:UserskathrOneDriveDocumentsPQ\_StandardExpenses”)**

This is the same code used in [last week’s blog](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-folder-away)
. In this case, I want to use **Folder.Contents()** instead of **Folder.Files()**, because I want to see the subfolders, and not just the files in the subfolders.

![](<Base64-Image-Removed>)

The first row shows me the ‘PQ Blog’ folder. The **_Content_** column indicates that this is a table, and I can see the contents of that table (the files) by clicking on ‘Table’:

![](<Base64-Image-Removed>)

I want to just show **_Content_** which contains a table, which will allow me to only view folders.

![](<Base64-Image-Removed>)

However, I can’t do this via a filter since ‘Table’ is an entity and not a value – instead I need some **M** code to create a new column which does contain values.

![](<Base64-Image-Removed>)

The **M** code I have used is

**let**

    **Source = Folder.Contents(“C:UserskathrOneDriveDocumentsPQ\_StandardExpenses”),**

    **FileType =Table.AddColumn(Source,”Folder”,each Value.Is(\[Content\],type table))**

**in**

**FileType**

This creates a Boolean – a column which is TRUE or FALSE – in this case, it is TRUE if **_Content_** contains a table. I will look at the function **Value.Is()** in more detail in next week’s blog.

![](<Base64-Image-Removed>)

I can then filter on **_Folder_**:

![](<Base64-Image-Removed>)

and I am left with my filtered result, _viz_.

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-find-the-folder/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-find-the-folder/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-find-the-folder/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-find-the-folder/#0)

[](https://sumproduct.com/blog/power-query-find-the-folder/#0 "close")

top