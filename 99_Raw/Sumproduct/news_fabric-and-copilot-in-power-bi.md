# Fabric and Copilot in Power BI

**Source:** https://sumproduct.com/news/fabric-and-copilot-in-power-bi/

---

[Home](https://sumproduct.com/)

\> Fabric and Copilot in Power BI

*   November 18, 2023

Fabric and Copilot in Power BI
==============================

Fabric and Copilot in Power BI
==============================

18 November 2023

You will probably have seen that there are a significant number of updates for Power BI this month. Several have caught our eye and may change how you work.

These updates include the General Availability of Microsoft Fabric and the public Preview of Copilot in Microsoft Fabric, including the experience for Power BI. With the launch of these next-generation analytics tools, you can empower your data teams to more easily scale to meet the demand of the business.

Microsoft Fabric is reshaping how teams work with data by bringing everyone together on a single end-to-end analytics platform. Data analysts can work side-by-side with data engineers, data warehousing professionals, data scientists, and business users, all working in the same software as a service (SaaS) experience and from the same unified data lake, OneLake, to uncover insights.

Microsoft also believes Copilot in Fabric has the potential to dramatically change the way organisations work with data. Seasoned business intelligence professionals can use Copilot to scale and create stunning reports faster. Less skilled users can use Copilot to explore their data, create reports, and answer their questions without burdening their data teams.

**_General Availability of Microsoft Fabric_**

Microsoft Fabric is now out there. It is an end-to-end data platform that can reshape how everyone accesses, manages and acts on data and insights by connecting every data source and analytics service together.

There are four \[4\] ways Microsoft Fabric may assist the current analytics market:

1.  **Fabric is a complete analytics platform.** By bringing together seven \[7\] role-specific workloads, Data Factory, Data Engineering, Data Warehouse, Data Science, Real-Time Analytics, Data Activator and Power BI, into a single, unified experience and architecture, Fabric can help to reduce the typical cost and effort of integrating services and streamline your data estate. This unified architecture also simplifies both governance with built-in features that span every workload and billing with a single pool of capacity and storage that can be used for every workload
2.  **Fabric is lake-centric and open.** You can easily connect all your data across clouds, accounts and domains to Fabric’s unified, multi cloud data lake, OneLake, to create a single source of truth for your data. OneLake is automatically wired into every Fabric workload and with OneLake’s open data format, you only need to load the data into the lake once to use it across every Fabric workload and engine, minimising data duplication and sprawl
3.  **Fabric empowers business users.** It can ensure business users in your organisation have access to the data and insights needed to make data-driven decisions. With Power BI natively built into Fabric, anyone can quickly go from data sitting in a lake to bespoke Power BI visuals embedded in a Microsoft 365 app
4.  **Fabric is AI-powered.** It has infused AI to help data professionals get more done, more quickly. With Copilot in Fabric, you can use natural language to create dataflows and pipelines, write SQL statements, build reports or even develop machine learning models.

**_Announcing the public Preview of Copilot in Microsoft Fabric_**

There is also the announcement of the public Preview of Copilot in Microsoft Fabric, including the experience for Power BI, which helps users quickly get started by helping them create reports in the Power BI web experience. Based upon a high-level prompt, Copilot for Power BI in Fabric creates an entire report page for you by identifying the tables, fields, measures and charts that would help you get started. You can then customise the page using. Copilot can also help you understand your semantic model and even suggest topics for your report pages. It’s a fast and easy way to get started with a report, especially if you’re less familiar with report creation in Power BI.

![](<Base64-Image-Removed>)

In addition to report creation, Copilot’s ability to summarise data has been brought to the ‘Smart Narrative’ visual, now rebranded as the ‘Narrative with Copilot’ visual. This visual summarises the data and insights on the page, across your report or even for your own template if you need to define a specific summary. This visual is available in the Power BI service and in Power BI Desktop.

![](<Base64-Image-Removed>)

Lastly, in Power BI Desktop, Copilot can help model authors improve their models and save time. The first capability is being released now, and helps authors generate synonyms for their fields, measures and tables using Copilot. But this is just the start. Future Power BI Desktop updates will bring even more new Copilot experiences, including the report creation experience from the Service, a Data Analysis Expressions (**DAX**) writing experience, and more.

The Preview of Copilot in Microsoft Fabric will be rolling out in stages with the goal that all customers with Power BI Premium capacity (P1 or higher) or Fabric capacity (F64 or higher) will have access to the Copilot preview by the end of March 2024. You don’t need to sign up to join the Preview, it will automatically become available to you as a new setting in the Fabric administrator (admin) portal when it is rolled out to your tenant. When charging begins for the Copilot in Fabric experiences, you can simply count Copilot usage against your existing Fabric or Power BI Premium capacity.

**_Power BI semantic model support for Direct Lake on Synapse Data Warehouse_**

The Power BI semantic models can now leverage Direct Lake mode in conjunction with Synapse Data Warehouses in Microsoft Fabric. Until now, Direct Lake mode was limited to semantic models on Fabric lakehouses, whilst warehouses were queried only in DirectQuery mode. Now, Microsoft has expanded Direct Lake mode to support warehouses in Fabric as well. Direct Lake mode is a groundbreaking data access technology for semantic models based on loading Delta-Parquet files directly from OneLake without having to import or duplicate the data. Direct Lake combines the advantages of import and DirectQuery modes to deliver quick query performance without any data movement.

**_Announcing public Preview of stored credentials for Direct Lake semantic model Row Level Security (RLS) and Object Level Security (OLS)_**

This latest set of updates also sees the public Preview of Row Level Security (RLS) and Object Level Security (OLS) and stored credentials for Direct Lake semantic models. RLS and OLS is a Power BI feature that enables you to define row-level and object-level access rules in a semantic model, so different users can see different subsets of the data based on their roles and permissions.

Stored credentials help reduce configuration complexity and are strongly recommended when using RLS and OLS with Direct Lake semantic models. The following screenshot shows how you can add users to RLS roles in a Direct Lake model using the web modelling experience.

![](<Base64-Image-Removed>)

The web modelling security roles dialog will be fully deployed in the coming days or weeks.

**_Instantly integrate your import-mode semantic models into OneLake_**

There is also the public Preview of Microsoft OneLake integration for import models. With the flick of a switch, you can enable OneLake integration and automatically write data imported into your semantic models to delta tables in OneLake and enjoy the benefits of Fabric without any migration effort. The data is instantly and concurrently accessible through these delta tables. Data scientists, database administrators, app developers, data engineers, citizen developers and any other type of data consumer now have direct access to the same data that drives your business intelligence.

**_Quickly answer your data questions with Explore_**

Another public Preview feature called Explore has been announced that will enable anyone to quickly explore a semantic model. Similar to exporting and building a PivotTable in Excel, you can open the Explore experience and create a matrix or visual view for your data. Analysts could use Explore to learn about a new semantic model before building a report for example or a business user could answer a specific question they have about the data without building an entire report.

![](<Base64-Image-Removed>)

**_Announcing the public Preview of Data Analysis Expressions Query view_**

**DAX** queries help you quickly explore and analyse your semantic model. The new **DAX** query view in Power BI Desktop lets you utilise the powerful **DAX** query language to discover, analyse and see the data in your semantic model. Like the Explore feature _(above)_, model authors can quickly validate data and measures in their semantic model without having to build a visual or use an additional tool. Changes made to measures can be seamlessly updated directly back to the semantic model. This capability along with several existing features like auto formatting, integration with the Report View’s Performance Analyzer, quick measures and measure-reference expansion all mean **DAX** query authoring in Power BI have just become much more productive for data professionals and advanced data analysts.

Microsoft has stated that they plan to continue adding functionality to the ‘**DAX** Query view’, including Copilot integration, support for live connect reports and adding it to the Power BI Service. You may get started by turning on this public Preview feature in **Power BI Desktop Options -> Preview features**.

![](<Base64-Image-Removed>)

**_Announcing the General Availability of semantic model scale-out, now with Direct Lake compatibility_**

The semantic model scale-out is now Generally Available. With scale-out, Power BI automatically scales out read-only replicas to ensure there are no performance slowdowns when many users are using the system at the same time, enabling large-scale production solutions to support high user concurrency. Automatic scale-out now works for Direct Lake semantic models too. Additionally, import-mode semantic models will benefit from refresh isolation, ensuring business users are unaffected by resource-intensive refresh operation, and continue to enjoy quick queries for interactive analysis.

Semantic-model scale-out is the last of the key features to make Microsoft Fabric and Power BI a superset of Microsoft Azure Analysis Services. Scale-out in Fabric is even superior to Analysis Services since scale-out takes place based on live user demand and adjusts automatically to changes in usage patterns. Analysis Services on the other hand requires detailed analysis to determine peak usage times, create automation scripts and monitor to ensure optimum set up. Additionally, cost in Analysis Services increases linearly per replica, unlike Fabric’s usage-based billing model.

**_New Microsoft Fabric licensing options_**

In June 2023, Microsoft announced pay-as-you-go prices for Fabric that allow you to dynamically scale up or scale down and pause capacity as needed. There is now “reservation pricing” for Fabric that will allow you to pre-commit Fabric Capacity Units in one-year increments, helping you save up to 40% over the pay-as-you-go prices (excluding Power BI Premium capacity SKUs). Microsoft has also announced OneLake business continuity and disaster recovery (BCDR) and cache storage prices, expanding on their already announced OneLake storage pricing. You may check out all these pricing options on the [Microsoft Fabric pricing page](https://azure.microsoft.com/en-us/pricing/details/microsoft-fabric/)
.

With these announcements, current Power BI Premium per capacity customers have an additional pricing option to experience everything Fabric has to offer.

**_Getting started with Power BI and Microsoft Fabric_**

If you are an existing Power BI Premium per capacity customer, you can already access Microsoft Fabric by simply turning on Fabric in your admin portal.

If you don’t already have Power BI Premium capacity, you can try out everything Fabric has to offer by signing up for the free trial — no credit card information is required. To start your free trial, sign up for a free account (Power BI customers can use their existing account), and once signed in, select Start Trial within the account manager tool in the Fabric app. Each trial user will receive a 64 CU trial capacity — your billing unit — to use against any workload during your 60-day free trial.

As always, we’ll be detailing these updates in our December newsletter. Please remember we have virtual / online training in Power BI which you can find out more about [here](https://www.sumproduct.com/courses)
. If you are not already a subscriber, why not sign up at the bottom of any [SumProduct](https://www.sumproduct.com/)
 web page? And don’t forget to download the latest version of Power BI Desktop [here](https://powerbi.microsoft.com/en-us/desktop/?WT.mc_id=Blog_Desktop_Update)
 too.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/fabric-and-copilot-in-power-bi/#0)
    
*   [Register](https://sumproduct.com/news/fabric-and-copilot-in-power-bi/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/fabric-and-copilot-in-power-bi/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/fabric-and-copilot-in-power-bi/#0)

[](https://sumproduct.com/news/fabric-and-copilot-in-power-bi/#0 "close")

top