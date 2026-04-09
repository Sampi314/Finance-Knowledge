# Power Query: Three Sheets to the Table

**Source:** https://sumproduct.com/blog/power-query-three-sheets-to-the-table/

---

[Home](https://sumproduct.com/)

\> Power Query: Three Sheets to the Table

*   June 8, 2021

Power Query: Three Sheets to the Table
======================================

Power Query: Three Sheets to the Table
======================================

9 June 2021

_Welcome to our Power Query blog. This week, I look at combining sheets where the columns do not match._

_I have some data that has come in from John, one of my imaginary salespeople. He has sent in some sales data, and I need to pull it into one table. The data is spread over three sheets, which are all in a similar format:_

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-182.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-239.jpg)

_In my (new) Excel workbook, I go to the Data tab and choose to ‘Get Data’ and then ‘From Workbook’,_ _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-192.jpg)

_This allows me to see the data in John’s workbook:_

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-186.jpg)

_Because the columns are not the same for each sheet, if I tried to append my sheets, I would end up with the dates in the middle of my data, which is not what I want. I need to transform each sheet before I combine them. However, there is another option I can take if I right-click on the workbook:_

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-156.jpg)

_I can transform the data in the workbook. I select this option._

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-136.jpg)

_This gives me the source step (I know I could have chosen sheets and deleted steps to get to this point, but this is neater!). I make sure that I am only including those sheets I want to combine._

_Next, I create a duplicate query: I am going to work out what I will do with one of my sheets._

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-127.jpg)

_I call my new query **Process\_Sheet**._

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-107.jpg)

_I filter to keep Sheet1, and select the **Data** column, which I right-click in order to remove the other columns. I can then expand it to see my data._

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-97.jpg)

_I don’t need a prefix._

![](<Base64-Image-Removed>)

_If I am going to append my data, I need the dates to be in a column. First, I promote my headers, which I can do in the Transform tab by ‘Using First Row as Headers’. If a ‘Change Type’ step is created, I must delete it, so that the column names are not referenced (as they will be different for the other sheets)._

![](<Base64-Image-Removed>)

_I can then select the **Tent Type** column and unpivot everything else._

![](<Base64-Image-Removed>)

_This looks good; I can now move onto the next step. This query is going to be a function, but first I need to set up a parameter, which will indicate which sheet is being processed. I can manage parameters on the Home tab._

![](<Base64-Image-Removed>)

_I create a new parameter, **Sheet**._

_**Sheet**_ _must be text, and it will be required by my new function. To begin with, Sheet will have a value of ‘Sheet1’._

![](<Base64-Image-Removed>)

_Back in my **Process\_Sheet** query, I go back to the ‘Filtered Rows’ step where I selected ‘Sheet1’. I am going to use the parameter instead._

![](<Base64-Image-Removed>)

_I choose my new parameter and click ‘OK’._

![](<Base64-Image-Removed>)

_Because the default value is ‘Sheet1’, the parameter works in the same way as before. Now I need to make this query into a function._

![](<Base64-Image-Removed>)

_I am prompted for a function name, which I call **fx\_Process\_Sheet**._

![](<Base64-Image-Removed>)

_My function is ready to use._

![](<Base64-Image-Removed>)

_Back in my original query, I want to invoke my function. In the ‘Add Column’ tab, I can ‘Invoke Custom Function’ and pass in the sheet name._

![](<Base64-Image-Removed>)

_Clicking ‘OK’ gives me a new column. This should hold all the data I need._

![](<Base64-Image-Removed>)

_I can now expand it._

![](<Base64-Image-Removed>)

_I select all columns and click ‘OK’._

![](<Base64-Image-Removed>)

_I have my data, I just need to change the data types on the Transform tab, rearrange it, and rename my columns._

![](<Base64-Image-Removed>)

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-three-sheets-to-the-table/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-three-sheets-to-the-table/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-three-sheets-to-the-table/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-three-sheets-to-the-table/#0)

[](https://sumproduct.com/blog/power-query-three-sheets-to-the-table/#0 "close")

top