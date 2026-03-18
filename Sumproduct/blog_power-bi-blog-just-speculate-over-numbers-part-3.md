# Power BI Blog: Just Speculate Over Numbers – Part 3

**Source:** https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-3/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Just Speculate Over Numbers – Part 3

*   May 16, 2018

Power BI Blog: Just Speculate Over Numbers – Part 3
===================================================

Power BI Blog: Just Speculate Over Numbers – Part 3
===================================================

17 May 2018

Remember last week we brought in our JSON file and focused on transforming and preparing the dataset portion. This time, we’re going to retrieve the column names from the metadata.

Last time, we created our Metadata query. In the Power Query editor, let’s view the query and click “Record” next to Metadata.

![](<Base64-Image-Removed>)

It’ll show:

![](<Base64-Image-Removed>)

Click onto “Record”.

![](<Base64-Image-Removed>)

Here we can see all the information about the data that the JSON file has recorded. What we are interested in is the **columns** field of this record. It has a “List” item and that’s what we want to click on.

![](<Base64-Image-Removed>)

We can’t expand any of these records because we are in a List data type. Convert it to a table.

Once that is done, we can view what is in a record by selecting one in the table and the preview at will show at the bottom of the screen:

![](<Base64-Image-Removed>)

These records give detailed information about each column. Click on the expansion arrow and it’ll show all the data available in the record.

![](<Base64-Image-Removed>)

However, we only want **name** as the name of the column is what we will use in our headers. Check only the **name** field and press OK.

![](<Base64-Image-Removed>)

Great! So how do we transfer the column names to be across the row instead of down the column like we have them now? Just Transpose so now it is in the correct orientation we need.

![](<Base64-Image-Removed>)

Fantastic! Now we are ready to combine this with our data set.

Tune back next week to see how we finalise our table!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-3/#0)

[](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-3/#0 "close")

top