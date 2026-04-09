# Calculate travel time and distance between two addresses using Excel + Maps API

**Source:** https://chandoo.org/wp/distance-between-places-excel-maps-api

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Calculate travel time and distance between two addresses using Excel + Maps API
===============================================================================

*   Last updated on July 19, 2018

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**Ever wanted to calculate distance using Excel  – between two locations (physical addresses)?**_

![calculate distance using Excel - Distance and travel time between two places using formulas + Maps API](https://chandoo.org/wp/wp-content/uploads/2018/07/distance-between-places-excel-maps-api-formula.png)

If we know the addresses, we can go to either Google Maps or Bing Maps and type them out to find the distance and travel time. But what if you are building some model (or calculator) and want to find out the distance, travel time, address points (latitude, longitude) and may be even distance matrix (given two sets of points, all distances between them)? We can use the public APIs from Bing maps or Google Maps to get the answer to our spreadsheet.

**What you need:**

*   Free maps API from either [Google Maps](https://developers.google.com/maps/documentation/javascript/get-api-key)
     or [Bing Maps](https://www.bingmapsportal.com/Account/Register)
    
*   Excel 2013 or above (we will be using WEBSERVICE() and FILTERXML() functions in Excel)

**How to get the API Key from Google Maps or Bing Maps:**

The API key process is somewhat technical and can be confusing. Plus for Google Maps API, you need to provide your credit card details (according to Google, you will not be billed automatically though). I made a small video explaining the process. Watch it below (or [on our YouTube channel](https://youtu.be/RU9D-CyKwEQ)
).

Using Excel to calculate distance & travel time between two points – Bing Maps API
----------------------------------------------------------------------------------

As the process for getting Bing Maps API key is easy, let’s assume that is what you have.

Let’s say you have the api key in a cell named _bingmaps.key_

In this demo, we focus on calculating distance & travel time between one set of points, _but you can use the ideas to calculate distance matrix for a range of points._ For example, you can calculate travel time between all your warehouses and customer locations easily.

Start by creating a range of cells to capture origin & destination addresses. For Bing maps API, we need address to be broken in to below pieces.

![data format - geolocation lookup - bingmaps api](https://chandoo.org/wp/wp-content/uploads/2018/07/address-format-bing-maps-api.png)

### Step 1: Fetch Latitude and Longitude for the addresses

Before calculating the distance, we need to know where on earth our addresses are. So we will use point lookup API to convert address to geolocation (lat&long). To do this, we call

http://dev.virtualearth.net/REST/v1/Locations?countryRegion=$1&adminDistrict=$2&locality=$3&postalCode=$4&addressLine=$5&maxResults=1&o=**xml**&key=_bingmaps.key_

with our address.

Notice all $ symbols? Use SUBSTITUTE to replace them with actual location values.

When you call this URL using WEBSERVICE(), you will get an XML output (as our output parameter is o=xml, if you omit this, you will get json).

Sample output for this looks like below:

> <?xml version=”1.0″ encoding=”utf-8″?><Response xmlns:xsd=”http://www.w3.org/2001/XMLSchema” xmlns:xsi=”http://www.w3.org/2001/XMLSchema-instance” xmlns=”http://schemas.microsoft.com/search/local/ws/rest/v1″><Copyright>Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright><BrandLogoUri>http://dev.virtualearth.net/Branding/logo\_powered\_by.png</BrandLogoUri><StatusCode>200</StatusCode><StatusDescription>OK</StatusDescription><AuthenticationResultCode>ValidCredentials</AuthenticationResultCode><TraceId>\_REMOVED\_</TraceId><ResourceSets><ResourceSet><EstimatedTotal>1</EstimatedTotal><Resources><Location><Name>Phillip St, Johnsonville, Wellington 6037, New Zealand</Name><Point>**<Latitude>-41.22292</Latitude><Longitude>174.80164</Longitude>**</Point><BoundingBox><SouthLatitude>-41.2241799</SouthLatitude><WestLongitude>174.80136</WestLongitude><NorthLatitude>-41.22166</NorthLatitude><EastLongitude>174.80196</EastLongitude></BoundingBox><EntityType>RoadBlock</EntityType><Address><AddressLine>Phillip St</AddressLine><AdminDistrict>Wellington</AdminDistrict><AdminDistrict2>Wellington City</AdminDistrict2><CountryRegion>New Zealand</CountryRegion><FormattedAddress>Phillip St, Johnsonville, Wellington 6037, New Zealand</FormattedAddress><Locality>Wellington</Locality><PostalCode>6037</PostalCode></Address><Confidence>High</Confidence><MatchCode>Good</MatchCode><GeocodePoint><Latitude>-41.22292</Latitude><Longitude>174.80164</Longitude><CalculationMethod>Interpolation</CalculationMethod><UsageType>Display</UsageType></GeocodePoint><GeocodePoint><Latitude>-41.22292</Latitude><Longitude>174.80164</Longitude><CalculationMethod>Interpolation</CalculationMethod><UsageType>Route</UsageType></GeocodePoint></Location></Resources></ResourceSet></ResourceSets></Response>

From this XML, we need to extract the LAT & LONG values highlighted in blue. We can use FILTERXML() to do that.

Let’s say the output of WEBSERVICE is in cell C21.

We can use FILTERXML() like this:

\=FILTERXML(C21,”//Latitude\[1\]”)

\=FILTERXML(C21,”//Longitude\[1\]”)

This will give us both lat & long values.

> **How does FILTERXML() work?** It takes the XML value in C21 and finds the first Latitude tag (hence \[1\]) anywhere (hence //)

You can use FILTERXML to test the status code for the response or other interesting bits too.

### Step 2: Calculate distance between two geolocations

Once we have lat & long values for both origin and destination, we can call distance lookup API to calculate distance, travel time values.

The distance lookup URL is:

https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=$1&destinations=$2&travelMode=$3&o=xml&key=_bingmaps.key_

For example, the distance lookup URL for above addresses is:

https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=-**41.22292,174.80164**&destinations=**\-41.27868,174.77506**&travelMode=**driving**&o=xml&key=$k

The output for this is an XML that looks like:

> <?xml version=”1.0″ encoding=”utf-8″?><Response xmlns:xsd=”http://www.w3.org/2001/XMLSchema” xmlns:xsi=”http://www.w3.org/2001/XMLSchema-instance” xmlns=”http://schemas.microsoft.com/search/local/ws/rest/v1″><Copyright>Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright><BrandLogoUri>http://dev.virtualearth.net/Branding/logo\_powered\_by.png</BrandLogoUri><StatusCode>200</StatusCode><StatusDescription>OK</StatusDescription><AuthenticationResultCode>ValidCredentials</AuthenticationResultCode><TraceId>\_REMOVED\_</TraceId><ResourceSets><ResourceSet><EstimatedTotal>1</EstimatedTotal><Resources><Resource xsi:type=”DistanceMatrix”><ErrorMessage>Request accepted.</ErrorMessage><Origins><Coordinate><Latitude>-41.22292</Latitude><Longitude>174.80164</Longitude></Coordinate></Origins><Destinations><Coordinate><Latitude>-41.27868</Latitude><Longitude>174.77506</Longitude></Coordinate></Destinations><Results><Distance><DepartureTime xsi:nil=”true” /><OriginIndex>0</OriginIndex><DestinationIndex>0</DestinationIndex>**<TravelDistance>8.96955555555556</TravelDistance><TravelDuration>7.29166666666667</TravelDuration>**<TotalWalkDuration>0</TotalWalkDuration></Distance></Results></Resource></Resources></ResourceSet></ResourceSets></Response>

Again, we can use FILTERXML() to extract the relevant bits (=FILTERXML(C32,”//TravelDistance\[1\]”) and =FILTERXML(C32,”//TravelDuration\[1\]”))

The default output values are in KM for distance and minutes for duration. You can change this  to miles, hours etc. too by using extra parameters in the lookup URL. Please [read the Bing maps developer documentation](https://msdn.microsoft.com/en-us/library/ff701713.aspx)
 for more.

Distance & travel time in Excel – Google Maps API
-------------------------------------------------

Let’s say your Google Maps API key is in a cell named _gmaps.key_

This API is really easy to use compared to Bing maps (as we need to make just one call).

The request URL is:

https://maps.googleapis.com/maps/api/distancematrix/**xml**?origins=$1&destinations=$2&mode=$3&key=_gmaps.key_

For example, let’s lookup the travel time and distance between Microsoft & APPLE offices.

![format for address - google distance matrix api](https://chandoo.org/wp/wp-content/uploads/2018/07/address-format-google-maps-api.png)

The sample URL is:

https://maps.googleapis.com/maps/api/distancematrix/xml?origins=1,+Infinity+loop,+San+Francisco,+CA&destinations=Redmond,+Seattle,+WA&mode=driving&key=_gmaps.key_

The response is XML (if you want json, then replace **xml** with json) like below:

> <?xml version=””1.0″” encoding=””UTF-8″”?>  
> <DistanceMatrixResponse>  
> <status>OK</status>  
> <origin\_address>Apple Campus, Cupertino, CA 95014, USA</origin\_address>  
> <destination\_address>Redmond, WA, USA</destination\_address>  
> <row>  
> <element>  
> <status>OK</status>  
> <duration>  
> <value>47736</value>  
> <text>**13 hours 16 mins**</text>  
> </duration>  
> <distance>  
> <value>1379709</value>  
> <text>**1,380 km**</text>  
> </distance>  
> </element>  
> </row>  
> </DistanceMatrixResponse>

We can FILTERXML this response to extract the important bits like this:

\=FILTERXML(C15,”//distance\[1\]/text”)

\=FILTERXML(C15,”//duration\[1\]/text”)

Download distance calculator template
-------------------------------------

[**Click here to download distance, travel time calculator template**](https://chandoo.org/wp/wp-content/uploads/2018/07/distance-calculator-up.xlsx)
 to see all these formulas in action. You must enter your API key to get it work. Examine the formulas and XML formats to learn more about how these APIs work and how to integrate them to your spreadsheet models.

**More examples of WEBSERVICE():**

*   [Finding nearest zip codes using webservice() and filterxml()](https://chandoo.org/wp/finding-nearby-zipcodes-using-excel-formulas/)
    
*   [Integrating WEBSERVICE() with trip planner spreadsheet](https://www.microsoft.com/en-us/microsoft-365/blog/2013/03/21/use-webservice-functions-to-automatically-update-excel-2013-spreadsheets-with-online-data/)
     \[Microsoft blog\]

### Made something cool with WEBSERVICE()?

Did you make something cool and fun using WEBSERVICE() and FILTERXML()? Please share the ideas and tips in comments section.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [79 Comments](https://chandoo.org/wp/distance-between-places-excel-maps-api/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/distance-between-places-excel-maps-api/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [api](https://chandoo.org/wp/tag/api/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [filterxml()](https://chandoo.org/wp/tag/filterxml/)
    , [google maps](https://chandoo.org/wp/tag/google-maps/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    , [webservice()](https://chandoo.org/wp/tag/webservice/)
    , [xpath](https://chandoo.org/wp/tag/xpath/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousMutual Fund Portfolio Tracker using MS Excel](https://chandoo.org/wp/mutual-fund-portfolio-tracker-using-ms-excel/)

[NextTop 5 HR Analytics Examples – Free Video MasterclassNext](https://chandoo.org/wp/excel-for-hr-people/)

![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)

Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.

![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)

Rebekah S

Reporting Analyst

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)

[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)

Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)

Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.

Recent Articles on Chandoo.org

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

Best of the lot

*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)
    
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)
    
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)
    

Related Tips
------------

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Learn Excel

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

Excel Challenges

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

Excel Howtos

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)

Excel Howtos

### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)

[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

Excel Howtos

### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

Excel Howtos

### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”

1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:
    
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)
    
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.
    
    [Reply](https://chandoo.org/wp/distance-between-places-excel-maps-api/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/distance-between-places-excel-maps-api/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/distance-between-places-excel-maps-api/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ