# Power Query: Picky Pivoting

**Source:** https://sumproduct.com/blog/power-query-picky-pivoting/

---

[Home](https://sumproduct.com/)

\> Power Query: Picky Pivoting

*   September 22, 2020

Power Query: Picky Pivoting
===========================

Power Query: Picky Pivoting
===========================

23 September 2020

_Welcome to our Power Query blog. This week, I look at unpivoting data with multiple headings._

I have some tent data:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-139-1.jpg)

I want to get this data into a standard table format so that I can analyse it and combine it with other data. I want to do this in a dynamic way, so that if more months are added to my Excel sheet, then the data will be transformed correctly.

I start by extracting the data to Power Query by selecting ‘From Table’ in the ‘Get & Transform’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-128-1.jpg)

Power Query automatically selects my data without the ‘Grand Total’ line, and this is fine for my purposes. I choose not to select the ‘My table has headers’ box as it wouldn’t find the correct headers in any case.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-120-1.jpg)

I start by sorting out my supplier data, so I right click on **Column1** and choose to ‘Fill Down’.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-105-1.jpg)

_I know that I want to keep the supplier data and the tent type data, so I choose to combine these columns. The remaining columns will need more manipulation to sort out the headings._

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-92-1.jpg)

On the Transform tab, I can select **Column1** and **Column2** and choose to ‘Merge Columns’.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-79-1.jpg)

I choose to separate my data by a colon (:), and use a meaningful name for my column name.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-69-1.jpg)

On the Transform tab, I also have the option to ‘Transpose’ my data, which will treat columns as rows and rows as columns.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-54-1.jpg)

When I click ‘Transpose’, my data is swapped around:

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-44-1.jpg)

Next, I need to fill down the data in my first column so that ‘Rented’ or ‘Sold’ appears next to each month.

![](<Base64-Image-Removed>)

Now, I can promote the row with the supplier and tent type information to be my headers from the ‘Use First Row as Headers’ section.

![](<Base64-Image-Removed>)

The data is already looking much better. I am ready to unpivot the quantities. I select the first column (Rented / Sold), and the **Supplier:Tent Type** column and choose to unpivot the other columns. I can do this by right clicking with my columns selected.

![](<Base64-Image-Removed>)

I can now split the **Attribute** column into my original columns.

![](<Base64-Image-Removed>)

I choose to split by colon.

![](<Base64-Image-Removed>)

I can now rename my columns.

![](<Base64-Image-Removed>)

_I remove my total rows by filtering on **Supplier**, looking for the word ‘Total’._

![](<Base64-Image-Removed>)

I choose ‘Does Not End With…’ just to reduce my chances of coinciding with an actual supplier name.

![](<Base64-Image-Removed>)

I click ‘OK’ to see my data.

![](<Base64-Image-Removed>)

I reorder the columns.

![](<Base64-Image-Removed>)

I can now use ‘Close & Load’ on the ‘Home’ tab to upload my data to Excel.

![](<Base64-Image-Removed>)

Finally, I need to add data for July to my original Excel spreadsheet to check my query still works.

![](<Base64-Image-Removed>)

I refresh my query and check the data.

![](<Base64-Image-Removed>)

The data for July has been included.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-picky-pivoting/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-picky-pivoting/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-picky-pivoting/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-picky-pivoting/#0)

[](https://sumproduct.com/blog/power-query-picky-pivoting/#0 "close")

top