# Power Query: Binary Function

**Source:** https://sumproduct.com/blog/power-query-binary-function/

---

[Home](https://sumproduct.com/)

\> Power Query: Binary Function

*   January 19, 2021

Power Query: Binary Function
============================

Power Query: Binary Function
============================

20 January 2021

_Welcome to our Power Query blog. This week, I look at using a function when processing binary data._

I have some data for my salespeople. The data is in the form of a collection of Excel files held in one folder. I would like to create a custom function that I can run against this data before I combine the files into one query.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-69-1.jpg)

I start in the ‘Get & Transform’ section of the Data tab, where I choose to create a ‘New Query’. From the dropdown, I can select ‘From File’ and then ‘From Folder’.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-57-1.jpg)

I select the folders location and view the files. I choose to ‘Transform Data’.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-48-1.jpg)

I right-click on the first value in the **Content** column.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-41-1.jpg)

I am going to ‘Add as New Query’.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-32-1.jpg)

This has created a new query which points at my first Excel file, that just happens to be Derek’s. I rename my query **Sample\_Expenses**.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-26-1.jpg)

I create a new parameter from the Home tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-23-1.jpg)

I call my new parameter **Expense\_Parameter**, and once I choose type Binary. It finds the **Sample\_Expenses** query, and allows me to select it as the default and current value.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-19-1.jpg)

Once I have created **Expense\_Parameter**, I can right-click it in the Query pane and create a Reference query.

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-17-1.jpg)

I call my new query **Transform\_Sample\_Expenses**.

![](https://sumproduct.com/wp-content/uploads/2025/05/daf8c4f0259ce428269c0d3d4badd32b-16-1.jpg)

I can right-click on my new query and choose ‘Create Function’.

![](<Base64-Image-Removed>)

This function will be linked to my current query, **Transform\_Sample\_Expenses**. I call this function **Transform\_Expenses**.

![](<Base64-Image-Removed>)

My function query expects a binary file as a parameter, and defaults to Derek’s expenses. I can now return to my **Transform\_Sample\_Expenses** and make some transformations.

![](<Base64-Image-Removed>)

I need to treat my file as an Excel file, so I right-click on the file and choose Excel.

![](<Base64-Image-Removed>)

Since this is the format of all the files in my folder, I continue to transform my data.

![](<Base64-Image-Removed>)

I have removed the first row, expanded the table data, and removed the columns I don’t need. Finally, I fill down on the name. I ‘Close & Load’ from the File tab to save my query.

![](<Base64-Image-Removed>)

Back in the query for my Expense folder (‘Expenses Folder Custom’), I can add a column which will call the function I have created.

![](<Base64-Image-Removed>)

I can select the **Transform\_Expenses** function.

![](<Base64-Image-Removed>)

I am then prompted to enter the binary parameter, and I choose the **Content** column.

![](<Base64-Image-Removed>)

Table data appears in my new column, and if I select one of the lower table values, I can see that I have transformed all of my Excel files, ready to be combined.

![](<Base64-Image-Removed>)

_I can expand the table data and remove the columns I don’t need._

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-binary-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-binary-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-binary-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-binary-function/#0)

[](https://sumproduct.com/blog/power-query-binary-function/#0 "close")

top