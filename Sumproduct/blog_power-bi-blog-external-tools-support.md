# Power BI Blog: External Tools Support

**Source:** https://sumproduct.com/blog/power-bi-blog-external-tools-support/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: External Tools Support

*   July 17, 2025

Power BI Blog: External Tools Support
=====================================

_Welcome back to this week’s edition of the Power BI blog series.  This week, we consider the support available for external tools in Power BI._

Power BI has a vibrant community of business intelligence professionals and developers.  Community contributors create free tools that use Power BI and Analysis Services APIs to extend and integrate with Power BI Desktop’s data modelling and reporting features.

The ‘External Tools’ tab on the Ribbon provides easy access to external tools that are installed locally and registered with Power BI Desktop.  When launched from the External Tools Ribbon, Power BI Desktop passes the name and port number of its internal data model engine instance and the current model name to the tool.  The tool then automatically connects, providing a seamless connection experience.

![](<Base64-Image-Removed>)

External tools generally fall into one of the following categories:

*   **Semantic modelling:** open-source tools such as DAX Studio, ALM Toolkit, Tabular Editor and Metadata Translator extend Power BI Desktop functionality for specific data modelling scenarios such as Data Analysis Expressions (**DAX**) query and expression optimisation, application lifecycle management (ALM), and metadata translation
*   **Data analysis:** tools for connecting to a model in read-only to query data and perform other analysis tasks.  For example, a tool might launch Python, Excel and Power BI Report Builder.  The tool connects the client application to the model in Power BI Desktop for testing and analysis without having to first publish the Power BI Desktop (**pbix**) file to the Power BI Service.  Tools to document a Power BI semantic model also fall into this category
*   **Miscellaneous:** some external tools don’t connect to a model at all but instead extend Power BI Desktop to make helpful tips and make helpful content more readily accessible.  For example, PBI.tips tutorials, DAX Guide from sqlbi.com and the PowerBI.tips Product Business Ops community tool make installation of a large selection of external tools easier.  These tools also assist registration with Power BI Desktop, including DAX Studio, ALM Toolkit, Tabular Editor and many others easy
*   **Custom:** integrate your own scripts and tools by adding a **\*.pbitool.json** document to the Power BI Desktop\\External Tools folder.

Before installing external tools, you should keep the following notes in mind:

*   external tools aren’t supported in Power BI Desktop for Power BI Report Server
*   external tools are provided by external, third-party contributors.  Except for the underlying public Microsoft APIs, Microsoft doesn’t provide support or documentation for external tools.  Microsoft does provide support if the issue can be reproduced with Microsoft tools.  These tools include SQL Server Management Studio (SSMS) or sample code that uses the public Microsoft APIs.

Consequently, external tools have become an important part of the Power BI ecosystem, especially for semantic modelling. They offer model authors enhanced capabilities to develop, manage and optimise semantic models.  Previously, some write operations were restricted, blocking external tools from altering tables, columns or query expressions, with changes reverted to the next Power BI Desktop refresh.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
.  If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.    

*   [Log in](https://sumproduct.com/blog/power-bi-blog-external-tools-support/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-external-tools-support/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-external-tools-support/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-external-tools-support/#0)

[](https://sumproduct.com/blog/power-bi-blog-external-tools-support/#0 "close")

top