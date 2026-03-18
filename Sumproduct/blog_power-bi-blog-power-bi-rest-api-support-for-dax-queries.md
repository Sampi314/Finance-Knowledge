# Power BI Blog: Power BI REST API Support for DAX Queries

**Source:** https://sumproduct.com/blog/power-bi-blog-power-bi-rest-api-support-for-dax-queries/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Power BI REST API Support for DAX Queries

*   September 15, 2021

Power BI Blog: Power BI REST API Support for DAX Queries
========================================================

Power BI Blog: Power BI REST API Support for DAX Queries
========================================================

16 September 2021

_Welcome back to this week’s edition of the Power BI blog series. This week, we discuss the Power BI REST API support for DAX queries now in Preview._

In the [last Power BI update](https://www.sumproduct.com/news/article/august-2021-updates-for-power-bi)
, there is a Preview of the new REST API to query datasets in Power BI by using Data Analysis Expressions (DAX). Amongst other things, this new DAX REST API helps to address feedback concerning programmatic access to the data in a dataset (_e.g._ the idea REST API should have access to read datasets). The new DAX REST API avoids dependencies on Analysis Services client libraries, requires no connection to XMLA endpoints and works in Power BI Premium, as well as in Power BI shared capacity.

One of the advantages of a REST API to query datasets is that you may use this REST API in almost any modern development environment on any platform, including low-code no-code Power Apps, Power Automate, Logic Apps, JavaScript-based languages, PowerShell, Java, PHP, Ruby, Python or any other technology that can authenticate against Azure Active Directory (AAD) and construct a Web request. You may also use .NET to call this REST API. As with other Power BI REST APIs, the DAX REST API supports user accounts, service principals and works in B2B scenarios. Since the caller is fully identifiable, row-level security and other controls at the dataset level are applied as expected too.

You should note that the tenant-level setting Allow XMLA endpoints and ‘Analyze in Excel’ with on-premises datasets must be enabled in the Power BI Admin Portal.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-177.jpg)

This setting is enabled by default, but you should double-check with your Power BI administrator. At least for the duration of the Preview period, Microsoft believed it seemed appropriate to govern this new DAX REST API with the existing XMLA endpoints tenant setting: the DAX query functionality is comparable to XMLA read access.

As well as XMLA read access, you will also require the Build permission for the dataset you want to query by using this new REST API. Contributors and workspace administrators have this permission, but you can also grant it directly.

![](<Base64-Image-Removed>)

You should also note that the workspace must be a modern (v2) workspace. Classic (legacy) workspaces are not supported. Therefore, if your datasets still reside in a classic workspace, make sure you upgrade the workspace to the new (v2) workspace experience first.

One way to test the DAX REST API is to query a dataset by using the Power BI Management cmdlets. As an example, consider Microsoft’s much used _AdventureWorks_ dataset:

![](<Base64-Image-Removed>)

In summary, the above script performs the following main steps:

*   construct the request parameters; this includes the request URL and the request body
*   the request URL references **executeQueries** endpoint of the dataset you want to query. The dataset ID (**Id**) identifies the dataset. There are many ways to determine the dataset ID. Perhaps the easiest is to display the dataset settings in the browser and then copy the dataset Id from the URL in the address bar
*   the URL has the format: **https:****//****api.powerbi.com/v1.0/myorg/datasets/{datasetId}/executeQueries**. If you use the Power BI Management cmdlets, you also can work with relative URLs, as in the script above
*   the request body is a JSON document containing the DAX query you want to run and an optional parameter to specify if blanks should be returned as _null_ values or not. The default omits blanks, which helps to reduce the data volume. More importantly, you should note that the request body consists of a queries array, but currently you can only specify a single query. The queries array provides flexibility for future improvements, although presently it can only contain a single query item. As a template for the request body, replace ‘**<Your DAX Query>**‘ with your actual DAX expression and don’t forget to escape quotation marks with a backslash (““)

**{ “queries”: \[{“query”:”<Your DAX Query>”}\], “serializerSettings”:{“includeNulls”: true}}**

*   send the request to Power BI. The DAX REST API expects a POST request, which you can construct in PowerShell by using the **Invoke-PowerBIRestMethod** cmdlet. Don’t forget to login to Power BI and then specify Post as the Method and pass the request URL and request body as demonstrated above. The Power BI Management cmdlets have the required app permissions to use the DAX REST API

*   if you want to use your own app registration, make sure your app has the **Dataset.Read.All** or **Dataset.ReadWrite.All** permission
*   parse the JSON response and process the results. The DAX REST API returns a JSON document with a results array containing one result per input query. Because the API currently only supports a single DAX query, the results array will also only include a single item. This item might include one or multiple tables, depending upon what the DAX query returns, which in turn contain the rows with the actual results as key / value pairs with the keys referring to the column names.

In the script above, the line $parsed.results\[0\].tables\[0\].rows | Format-List outputs the rows of the first (and only) table of the first (and only) result item returned for the (one and only) DAX query.

A .NET implementation that produces the same results as the PowerShell script above is equally uncomplicated _(see below)._

![](<Base64-Image-Removed>)

Do remember that the request body currently can only contain one DAX query and accordingly there is only one result set. Future versions of the API might support more. Also, you should note that the result set is currently capped at 100,000 rows. If you need to retrieve more rows, you must construct and submit multiple DAX queries that each only retrieves an appropriate portion of the results. Moreover, the result set does not support binary data. Make sure your values are of the type string, numeric, Boolean, blank, Date Time or variant. Furthermore, this is a Power BI API and therefore not available in Azure Analysis Services or SQL Server Analysis Services. Also, because this is a DAX REST API, you cannot submit MDX queries.

While it is certainly not too difficult to construct a web request manually, Microsoft is also aiming at adding the DAX REST API to the Power BI .NET SDK and the Power BI Connector for Power Automate, Power Apps and Logic Apps so that it is even easier to leverage the data from your Power BI datasets in your business solutions. For example, you could then query certain key performance indicators in Power Automate and trigger appropriate subprocesses based on the results.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-power-bi-rest-api-support-for-dax-queries/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-power-bi-rest-api-support-for-dax-queries/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-power-bi-rest-api-support-for-dax-queries/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-power-bi-rest-api-support-for-dax-queries/#0)

[](https://sumproduct.com/blog/power-bi-blog-power-bi-rest-api-support-for-dax-queries/#0 "close")

top