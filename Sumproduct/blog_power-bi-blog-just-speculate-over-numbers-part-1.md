# Power BI Blog: Just Speculate Over Numbers – Part 1

**Source:** https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-1/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Just Speculate Over Numbers – Part 1

*   May 2, 2018

Power BI Blog: Just Speculate Over Numbers – Part 1
===================================================

Power BI Blog: Just Speculate Over Numbers – Part 1
===================================================

3 May 2018

**JSON** (or **J**ava**S**cript **O**ject **N**otation) is a free file format used data transfer similar to XML. Instead of using text mark-up notation, it uses a subset of the JavaScript language. The JSON format is often preferred in newer web applications over XML because it is more lightweight. Read this great [Guide to JSON in 3 minutes](http://secretgeek.net/json_3mins)
 for an in-depth comparison between JSON and XML.

The reason why JSON is preferred in modern applications is that it is more lightweight than XML as it uses metadata i.e. data that describes and gives information about other data. The JSON file starts with a description of the file and details the information about the columns in the data. Then the data is then simply output to an array.

We’re going to be using the New York Lottery Powerball results and payouts information. This is available in JSON format [here](https://catalog.data.gov/dataset/lottery-powerball-winning-numbers-beginning-2010)
. Download the file and save it locally on your computer.

If we view the JSON data in a text editor, this is what will appear:

![](https://sumproduct.com/wp-content/uploads/2025/05/f15c12540bc6050f69a0cd3bf3dcebe0.jpg)

Notice that the first section is called “meta” which carries the metadata. This describes what the dataset is and how it is structured.

Scrolling down after the “meta” section is closed off we can see this:

![](https://sumproduct.com/wp-content/uploads/2025/05/d834176d9096828e65e107ae75a996f8.jpg)

The “data” section contains the actual data. Notice how it’s been put in rows with no description of what each individual item is. This is the key difference to XML files used in our previous exercise. Because there is no descriptor before each item it shrinks the file size, thereby making it more “lightweight”

Now we’re comfortable with the structure of our JSON file, let’s import it using “Get Data” selecting the “JSON” option:

![](https://sumproduct.com/wp-content/uploads/2025/05/d0760a0a35dbbd1f1e5a6f1ca28766b1.jpg)

Select and open your file. Unlike the other imports, it will bring you straight to the Power Query Editor instead of previewing the file and allowing you to choose “Load” or “Edit”.

![](<Base64-Image-Removed>)

Notice how the fields are yellow. This means that you can “navigate” and click through to drill down. The metadata is separate to the actual data so we’re going to have to split them. Firstly, duplicate the query so it accesses the same source – we will use the two queries to navigate through to the components of the file. One query to focus on parsing the “meta” section and the other on the “data” section.

To duplicate the query, just right click on the query on the “Queries” pane.

![](<Base64-Image-Removed>)

I’m going to rename the first one “Metadata” and the second one “Dataset” to be clear which query will focus on what parts.

Great! Now we’re ready to start performing transformations. We will step through the data cleansing process next week by going through **Dataset**.

_Tune in next week for more Power BI Tips!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-1/#0)

[](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-1/#0 "close")

top