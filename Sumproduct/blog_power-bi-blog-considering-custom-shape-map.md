# Power BI Blog: Considering Custom Shape Map

**Source:** https://sumproduct.com/blog/power-bi-blog-considering-custom-shape-map/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Considering Custom Shape Map

*   August 14, 2024

Power BI Blog: Considering Custom Shape Map
===========================================

Power BI Blog: Considering Custom Shape Map
===========================================

15 August 2024

_Welcome back to this week’s edition of the Power BI blog series. This week, we look at the Custom Shape Map._

**_Why Use Custom Shape Maps?_**

When using Shape Maps in Power BI, the available map types may not always suit specific needs. For example, there might be a requirement to illustrate housing data for each neighbourhood in Sydney, but Power BI’s default options only allow mapping Australia by states:

![](https://sumproduct.com/wp-content/uploads/2025/05/c5a7dfba960215889d1783b1d0fcd549-1.jpg)

Hence, to circumvent this limitation, the Power BI give us an option to have our own Custom map. Using this option, we can have a simple map of neighbourhood in Sydney that look like this:

![](https://sumproduct.com/wp-content/uploads/2025/05/104cbc4d7688a01a4200ce3f68b0979c-1.jpg)

Let’s dive in our step-by-step guide to make this map:

**_Step-by-Step Guide to Creating a Custom Shape Map_**

**Step 1: Prepare Files**

To create a Custom Shape Map, we will need a shape file (.shp) or a TopoJSON file that defines the boundaries of the custom regions. If we don’t have a pre-made shape file, we can create one using tools like [Mapshaper](https://mapshaper.org/)
, which allows us to draw and edit shapes. In this example, we will use 2 files from “Sydney Airbnb Open Data” dataset from [Kaggle](https://www.kaggle.com/datasets/tylerx/sydney-airbnb-open-data)
 which we have transformed and converted into suitable format. You can download the example files by clicking [here](https://sumproduct.com/assets/blog-pictures/2022/pbi/342/custom-shape-map.zip)
.

A small note we have here for you that Power BI prefer TopoJSON format for better compatibility and performance. Thus, if you have .shp you can use [Mapshaper](https://mapshaper.org/)
 to convert it in TopoJSON.

If you are creating your own custom shape map, please be consistent in naming of the area in both JSON and Excel file. Since Power BI will match the area base on the name you assign to the shape area.

**Step 2: Load CSV file into Power BI**

Then, we open the Power BI Desktop then we load the CSV file named “Listing Summary Dec18 Updated”:

![](<Base64-Image-Removed>)

**Step 3: Create Shape Map Visual**

Then, we will need to enable to Shape map visual features from the **File -> Options -> Global -> Preview features**.

![](<Base64-Image-Removed>)

Now, we can drag and drop this visual from into our page.

![](<Base64-Image-Removed>)

We will drag the **neighbourhood** into the Location field and **price** into the ColorSaturation field:

![](<Base64-Image-Removed>)

Instead of using Sum of price, we will adjust the summarization here as Average of price

![](<Base64-Image-Removed>)

**Step 4: Customise the Shape Map**

At this point, we will have a map of United States:

![](<Base64-Image-Removed>)

Then we will change the map by go to **Format your****Visual -> Visual -> Map Settings -> Map type -> Custom Map**:

![](<Base64-Image-Removed>)

At the ‘Add a map type’ option we will select the TopoJSON we have which is “neighbourhoods.json” and voila:

![](<Base64-Image-Removed>)

We have created a custom Shape Map visual to illustrate the average price to rent a property in each neighbourhood in Sydney in December 2018.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-considering-custom-shape-map/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-considering-custom-shape-map/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-considering-custom-shape-map/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-considering-custom-shape-map/#0)

[](https://sumproduct.com/blog/power-bi-blog-considering-custom-shape-map/#0 "close")

top