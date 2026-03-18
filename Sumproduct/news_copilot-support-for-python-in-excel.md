# Copilot Support for Python in Excel

**Source:** https://sumproduct.com/news/copilot-support-for-python-in-excel/

---

[Home](https://sumproduct.com/)

\> Copilot Support for Python in Excel

*   October 2, 2023

Copilot Support for Python in Excel
===================================

Copilot Support for Python in Excel
===================================

2 October 2023

They are all coming together like buses. After the recent announcements of Python in Excel, Copilot joins the gang too. For those (like me) who know little about programming in Python, Copilot allows you to leverage artificial intelligence (AI) to exploit Python in Excel.

![](https://sumproduct.com/wp-content/uploads/2025/05/c1dedff50c1ab136f8d8733610c4645a.jpg)

In addition to helping you write formulae, format your data and perform data analysis, Copilot in Excel will help you analyse and explore your data using Python code. All you have to do is use everyday language (“Natural Language”) to describe what you want to do with your data, and Copilot will generate and insert working Python code in the Excel grid for you. Perhaps it can do the washing and ironing too.

Whether you are new to Python or an experienced user, Copilot enables you to achieve more with your data in Excel by accessing advanced analytics. You can use Copilot as a learning tool, to unlock productivity, and as creative inspiration. Here are some of the benefits of using Copilot and Python in Excel:

*   **Use natural language for data analysis with Python.** Simply describe the analysis you want to undertake, and Copilot will generate and insert Python code for you. For example, you can type, “Forecast sales for the next 4 quarters” and Copilot will produce a Python cell with the code and the forecast

![](https://sumproduct.com/wp-content/uploads/2025/05/3084fa543ab34537933dcdeb9c46a73f.jpg)

*   **Access popular libraries and visualisations.** You don’t need to know Python to get started. Copilot leverages the power and flexibility of Python and its popular libraries, such as pandas, matplotlib, and scikit-learn to name a few. You can use Copilot to perform advanced analytics such as forecasting, clustering, optimisation, causal models, statistical tests, classification, sampling, and more. You can also create a variety of charts that are not available in Excel alone, such as boxplots, network graphs and pairplots

![](https://sumproduct.com/wp-content/uploads/2025/05/cca392f206de94f61faff8b8b54bf25e.jpg)

*   **Break down complex problems iteratively.** Use Copilot as your sounding board and guide to perform your data analysis in an iterative fashion. Copilot remembers the context of your previous queries and results, allowing you to continue the conversation with additional analyses, follow-up questions and ideas

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Copilot adheres to Microsoft’s AI principles and Responsible AI Standard, and it follows their commitment to data security and privacy. Python in Excel runs in a secure container on the Microsoft Cloud with enterprise-level security as a compliant Microsoft 365 connected experience.

**_Security Concerns_**

Many were concerned when Power BI Service was introduced regarding privacy and security. Microsoft has learned from that feedback and has been proactive in explaining security protocols this time.

Python code runs on “hypervisor isolated containers built on Azure Container Instances” (I am glad I cleared that up). The container has Python and a curated set of secured libraries provided by Anaconda. The environment uses the Anaconda Distribution for Python, which contains source-built Python and libraries, provided directly from Anaconda. With this borne in mind, it should be noted that the Python code:

*   does not have access to your computer, devices or account
*   does not have network access
*   does not have access to a user token
*   can access data through the references via the built-in **xl()** function as part of a Python formula. This means that Python formulae have access to read cell values within the workbook, based upon the cell reference, or values from external data sources, through the Power Query connection name
*   returns output to your workbooks through the **\=PY()** Excel function, which displays the result of the Python code in the cell where the function is entered. Python functions cannot return other object types like macros, VBA code or other formulae
*   doesn’t have access to other properties in the workbook, such as formulae, charts, PivotTables, macros or VBA code.

Python in Excel follows the same security policies as Excel when it comes to opening workbooks from the internet or untrusted sources. If you open a workbook that contains Python code from the internet, Excel Protected View won’t run Python formulae in the workbook. If a workbook is opened with Microsoft Defender Application Guard, Python formulae do not run by default. In addition, Python in Excel runs the Python formulae in the untrusted workbook within its own dedicated hypervisor isolated container, helping prevent potential interaction or interference with other Python code running from other open workbooks.

Python in Excel uses containers to run Python code on Azure. Containers are isolated and secure environments that can run applications and services without affecting the rest of the system. To help ensure the security and reliability of the containers, regular updates and patches are applied to them.

Python and the libraries are updated in the following ways to help keep your data secure and your numerical results consistent:

*   patches are applied to the underlying operating system that the Azure Container Instance runs on. This helps ensure that the container is protected from vulnerabilities and exploits that may affect your data. This is done automatically with no input required from you

*   once Python in Excel becomes Generally Available (it is presently only available in the Beta Channel Insider level), periodic updates of the Python environment will be released, with Python and the libraries provided by Anaconda. These versions include the latest security fixes and enhancements from the Python and Anaconda communities. These releases will be announced through blog posts and documentation. This will be done automatically with no setup required, and Microsoft will default to the latest environment. Existing workbooks will still calculate against the version of the environments the workbook was created on, and users will be prompted to upgrade if there is a newer version. This approach helps ensure that your numerical results stay consistent and allows you and your organisation to stay up to date.

It should also be noted that the Microsoft privacy policy – the same one you accept for other Microsoft products such as Excel, Word and PowerPoint – still applies.

Furthermore, it is possible to update the registry to toggle security warnings for Python in Excel. The following commands show how to update the registry to change security warning settings for Python in Excel. You can run the commands from an elevated command prompt on a Windows device.

*   Use this command to disable all security warnings. This is the default setting for Python in Excel:

reg add HKCUsoftwarepoliciesmicrosoftoffice16.0excelsecurity /v  
PythonFunctionWarnings /t REG\_DWORD /d 0 /f 

*   Use this command to enable a security prompt when opening a workbook that contains a Python formula. It enables a Security Warning notice in the Excel business bar

![](<Base64-Image-Removed>)

reg add  
HKCUsoftwarepoliciesmicrosoftoffice16.0excelsecurity /v  
PythonFunctionWarnings /t REG\_DWORD /d 1 /f 

*   Use this command to disable all Python functions from running. Python functions will return the error _**#BLOCKED!**_

reg add HKCUsoftwarepoliciesmicrosoftoffice16.0excelsecurity  
/v PythonFunctionWarnings /t REG\_DWORD /d 2 /f 

Microsoft will continue to monitor and adjust Python in Excel to keep data safe. This may involve future changes to the user experience and registry settings.

**_Availability_**

Copilot support for Python in Excel will be available in Preview later this year.

To use Copilot and Python in Excel, you will need access to Python in Excel and Microsoft 365 Copilot. It will initially be available in Excel for Windows in English.

To use Python in Excel, you will need to join the Microsoft 365 Insider Program. You must choose the Beta Channel Insider level to get the latest builds of the Excel application. After you’ve installed the latest Insider build of Excel, open a blank workbook and take the following steps:

*   select the Formulas tab in the Ribbon
*   select ‘Insert Python’
*   in the dialog that appears, select the ‘Try preview’ button.

You may also enable the Python in Excel preview by entering **\=PY** into an Excel cell and then choosing **PY** from the function AutoComplete menu. Selecting the **PY** function will trigger a dialog that allows you to enable the Preview.

The prerequisites for Microsoft 365 Copilot are a little more stringent. Before you can access Copilot, you must meet these requirements:

*   the following applications must be deployed for your users, which will integrate with Microsoft 365 Copilot and other applications:
    *   Excel
    *   Exchange
    *   OneDrive
    *   Outlook
    *   PowerPoint
    *   SharePoint
    *   Teams
    *   Word
    

*   To get started with the implementation process, you will need to deploy the application in the usual way for Microsoft 365 Apps.
    *   **OneDrive Account:** you need to have a OneDrive account for several features within Microsoft 365 Copilot, such as saving and sharing your files
    *   **New Outlook for Windows:** for integration of Microsoft 365 Copilot with Outlook, you are required to use the new Outlook for Windows, currently in Preview. You can switch to Outlook Mobile to access the new Outlook experience
    *   **Microsoft Teams:** to use Microsoft 365 Copilot with Microsoft Teams, you must use the Teams desktop client or web client. You can download the desktop client or sign into the web app at [https://teams.microsoft.com](https://teams.microsoft.com/)
        . Both the current and the new version of Teams are supported
    *   **Microsoft Loop:** to use Copilot in Microsoft Loop, you must have Loop enabled for your tenant.

For Enterprise subscribers wishing to use Microsoft 365 Apps, users must be on the Current Channel to access Copilot.

Microsoft previously stated that support for the Monthly Enterprise Channel was available for Microsoft 365 Copilot. As Microsoft continues to make frequent product updates and enhancements during the early access program, the time between updates in the Monthly Enterprise Channel limits Microsoft’s ability to provide an optimum Copilot experience on desktop clients. Going forward, users in the early access program must be on the Current Channel to receive Copilot updates when they become available. It is expected support will be available in the Monthly Enterprise Channel in the future.

You can manage Microsoft 365 Copilot licenses from the **Microsoft 365 admin center**. You can assign licenses to individual users or to groups of users, as well as reassign licenses to other users. To access license management in the Microsoft 365 admin center, go to **Billing -> Licenses**.

You may also assign licenses in bulk to groups of users through the Azure admin center or assign licenses to users with PowerShell.

Simple if you’re an expert!?

_Watch out for our upcoming training on all things Python in Excel, Copilot and ChatGPT. Coming soon!_

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/copilot-support-for-python-in-excel/#0)
    
*   [Register](https://sumproduct.com/news/copilot-support-for-python-in-excel/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/copilot-support-for-python-in-excel/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/copilot-support-for-python-in-excel/#0)

[](https://sumproduct.com/news/copilot-support-for-python-in-excel/#0 "close")

top