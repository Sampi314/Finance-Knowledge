# Announcing Microsoft Fabric

**Source:** https://sumproduct.com/news/announcing-microsoft-fabric/

---

[Home](https://sumproduct.com/)

\> Announcing Microsoft Fabric

*   May 24, 2023

Announcing Microsoft Fabric
===========================

Announcing Microsoft Fabric
===========================

24 May 2023

Time for conditioning! Microsoft Fabric, now in Preview, is an end-to-end, human-centred analytics product that brings together all of an organisation’s data and analytics in one place. It combines Power BI, Azure Synapse and Azure Data Factory into one unified software as a service (SaaS) platform. Data engineers, data warehousing professionals, data scientists, data analysts and business users can seamlessly collaborate within Fabric to foster a well-functioning data culture across the organisation.

Generative AI and language model services, such as Azure OpenAI Service, are enabling customers to use and create everyday AI experiences that are reinventing how analysts spend their time. Powering organisation-specific AI experiences requires a constant supply of clean data from a well-managed and highly integrated analytics system. However, most organisations’ analytics systems struggle to integrate their specialised yet often disconnected services.

Microsoft Fabric is an end-to-end, unified analytics platform that brings together all the data and analytics tools that organizations need. Fabric integrates technologies like Azure Data Factory, Azure Synapse Analytics and Power BI into a single unified product, empowering data and business professionals alike to unlock the potential of their data and lay the foundation for the era of AI.

Fabric is an end-to-end analytics product that addresses every aspect of an organisation’s analytics needs. There are five \[5\] areas that really Microsoft wants to emphasise:

**_1\. Fabric is a complete analytics platform_**

Every analytics project has multiple subsystems. Every subsystem needs a different array of capabilities, often requiring products from multiple vendors. Integrating these products can be a complex, fragile and expensive endeavour.

With Fabric, users may implement a single product with a unified experience and architecture that provides all the capabilities required for a developer to extract insights from data and present it to the business user. By delivering the experience as software as a service (SaaS), everything is automatically integrated and optimized, and users can sign up within seconds and get real business value within minutes.

Fabric empowers every team in the analytics process with the role-specific experiences they need, so data engineers, data warehousing professionals, data scientists, data analysts and business users can get on with what they are paid to do.

![](<Base64-Image-Removed>)

Fabric comes with seven core workloads:

1.  **Data Factory (Preview)** provides more than 150 connectors to cloud and on-premises data sources, drag-and-drop experiences for data transformation and the ability to orchestrate data pipelines
2.  **Synapse Data Engineering (Preview)** enables better authoring experiences for Spark, instant start with live pools and the ability to collaborate
3.  **Synapse Data Science (Preview)** provides an end-to-end workflow for data scientists to build sophisticated AI models, collaborate easily, and train, deploy and manage machine learning models
4.  **Synapse Data Warehousing (Preview)** provides a converged lake house and data warehouse experience with industry-leading SQL performance on open data formats
5.  **Synapse Real-Time Analytics (Preview)** enables developers to work with data streaming in from the Internet of Things (IoT) devices, telemetry, logs and more, and analyse large volumes of semi-structured data with high performance and low latency
6.  **Power BI** in Fabric provides visualisation and AI-driven analytics that enable business analysts and business users to gain insights from data. The Power BI experience is also deeply integrated into Microsoft 365, providing relevant insights where business users already work
7.  **Data Activator (coming soon)** provides real-time detection and monitoring of data and can trigger notifications and actions when it finds specified patterns in data all in a no-code experience.

You can try these experiences today by signing up for a Microsoft Fabric free trial.

**_2\. Fabric is lake-centric and open_**

You don’t need us to tell you that today’s data lakes can be messy and complicated, making it hard for customers to create, integrate, manage and operate them. Once they are operational, multiple data products using different proprietary data formats on the same data lake can cause significant data duplication and concerns about vendor lock-in.

Fabric comes with a SaaS, multi-cloud data lake called OneLake that is built-in and automatically available to every Fabric tenant. All Fabric workloads are automatically wired into OneLake, just like all Microsoft 365 applications are wired into OneDrive. Data is organised in an intuitive data hub, and automatically indexed for discovery, sharing, governance, and compliance.

OneLake serves developers, business analysts and business users alike, helping eliminate pervasive and chaotic data silos created by different developers provisioning and configuring their own isolated storage accounts. Instead, OneLake provides a single, unified storage system for all developers, where discovery and sharing of data are easy with policy and security settings enforced centrally. At the API layer, OneLake is built on and fully compatible with Azure Data Lake Storage Gen2 (ADLSg2), instantly tapping into ADLSg2’s vast ecosystem of applications, tools and developers.

A key capability of OneLake is “Shortcuts”. OneLake allows easy sharing of data between users and applications without having to move and duplicate information unnecessarily. Shortcuts allow OneLake to virtualise data lake storage in ADLSg2, Amazon Simple Storage Service (Amazon S3), and Google Storage (coming soon), enabling developers to compose and analyse data across clouds.

Fabric is deeply committed to open data formats across all its workloads and tiers. It treats Delta on top of Parquet files as a native data format that is the default for all workloads. This deep commitment to a common open data format means that customers need to load the data into the lake only once and all the workloads can operate on the same data, without having to separately ingest it. It also means that OneLake supports structured data of any format and unstructured data, giving customers total flexibility.

By adopting OneLake as a store and Delta and Parquet as the common format for all workloads, Microsoft offers its customers a data stack that’s unified at the most fundamental level. Customers do not need to maintain different copies of data for databases, data lakes, data warehousing, business intelligence or real-time analytics. Instead, a single copy of the data in OneLake can directly power all the workloads.

Managing data security (table, column and row levels) across different data engines can be a persistent nightmare for customers. Fabric will provide a universal security model that is managed in OneLake, and all engines enforce it uniformly as they process queries and jobs. This model is coming soon.

**_3\. Fabric is powered by AI_**

Microsoft has announced they are infusing Fabric with Azure OpenAI Service at every layer to help customers unlock the full potential of their data, enabling developers to leverage the power of generative AI against their data and assisting business users to find insights in their data. With Copilot in Microsoft Fabric in every data experience, users may use conversational language to create dataflows and data pipelines, generate code and entire functions, build machine learning models, or visualise results. Customers can even create their own conversational language experiences that combine Azure OpenAI Service models and their data and publish them as plug-ins.

Copilot _(see below)_ in Microsoft Fabric builds on existing commitments to data security and privacy in the enterprise. Copilot inherits an organisation’s security, compliance and privacy policies. Microsoft does not use organisations’ tenant data to train the base language models that power Copilot.

Copilot in Microsoft Fabric will be coming soon. Stay tuned for the latest updates and public release date for Copilot in Microsoft Fabric.

**_4\. Fabric empowers every business user_**

Customers aspire to drive a data culture where everyone in their organisation is making better decisions based on data. To help users foster this culture, Fabric integrates with the Microsoft 365 applications people use every day.

Power BI is a core part of Fabric and is already infused across Microsoft 365. Through Power BI’s deep integrations with popular applications such as Excel, Microsoft Teams, PowerPoint and SharePoint, relevant data from OneLake is easily discoverable and accessible to users right from Microsoft 365 helping users drive more value from their data

With Fabric, you can turn your Microsoft 365 apps into hubs for uncovering and applying insights. For example, users in Microsoft Excel can directly discover and analyse data in OneLake and generate a Power BI report with a click of a button. In Teams, users may infuse data into their everyday work with embedded channels, chat and meeting experiences. Business users can bring data into their presentations by embedding live Power BI reports directly in Microsoft PowerPoint. Power BI is also natively integrated with SharePoint, enabling sharing and dissemination of insights. With Microsoft Graph Data Connect (Preview), Microsoft 365 data is natively integrated into OneLake so analysts may unlock insights on their customer relationships, business processes, security and compliance, and people productivity.

**_5\. Fabric reduces costs through unified capacities_**

Today’s analytics systems typically combine products from multiple vendors in a single project. This results in computing capacity provisioned in multiple systems like data integration, data engineering, data warehousing and business intelligence. When one of the systems is idle, its capacity cannot be used by another system causing significant wastage.

Purchasing and managing resources is massively simplified with Fabric. Users may purchase a single pool of computing that powers all Fabric workloads. With this all-inclusive approach, analysts can create solutions that leverage all workloads freely without any friction in their experience or commerce. The universal compute capacities significantly reduce costs, as any unused compute capacity in one workload can be utilised by any of the workloads.

**_Current Microsoft analytics solutions_**

Existing Microsoft products such as Azure Synapse Analytics, Azure Data Factory and Azure Data Explorer will continue to provide a robust, enterprise-grade platform as a service (PaaS) solution for data analytics. Fabric represents an evolution of those offerings in the form of a simplified SaaS solution that can connect to existing PaaS offerings. Users will be able to upgrade from their current products into Fabric at their own pace.

Microsoft Fabric is currently in Preview. You may sign up for the free trial. Everyone who signs up gets a fixed Fabric trial capacity, which may be used for any feature or capability from integrating data to creating machine learning models. Existing Power BI Premium users can simply turn on Fabric through the Power BI administrator portal. After 1 July 2023, Fabric will be enabled for all Power BI tenants.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/announcing-microsoft-fabric/#0)
    
*   [Register](https://sumproduct.com/news/announcing-microsoft-fabric/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/announcing-microsoft-fabric/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/announcing-microsoft-fabric/#0)

[](https://sumproduct.com/news/announcing-microsoft-fabric/#0 "close")

top