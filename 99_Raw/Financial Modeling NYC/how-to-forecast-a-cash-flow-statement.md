# How to Forecast a Cash Flow Statement: Guide for Financial Planning

**Source:** https://www.financial-modeling.com/how-to-forecast-a-cash-flow-statement

---

[Skip to content](https://www.financial-modeling.com/how-to-forecast-a-cash-flow-statement#content "Skip to content")

How to Forecast a Cash Flow Statement
=====================================

![A man analyzes the forecast for the next few years on his tablet, looking ahead to the calendar year 2024. Financial Modeling, New York.](https://www.financial-modeling.com/wp-content/uploads/2024/10/Cash-Flow-Statement-Financial-Modeling-New-York--2048x1366.jpeg "Column chart with company progress and growth by year, 2024")

How to Forecast a [Cash Flow Statement](https://www.financial-modeling.com/glossar/cash-flow-statement/)
 (CFS)
---------------------------------------------------------------------------------------------------------------

Understanding how to prepare a cash flow forecast is crucial for insightful [financial modeling](https://www.financial-modeling.com/glossar/financial-modeling/)
. This article will guide you through the intricacies of [forecasting](https://www.financial-modeling.com/glossar/forecasting/)
 a Cash Flow Statement (CFS) and explain its purpose as one of the big three [financial statements](https://www.financial-modeling.com/glossar/financial-statements/)
. We’ll cover essential topics such as the components of the cash flow statement, methods of cash flow forecasting, and where this step fits into the overall model building process. Additionally, you’ll learn about each cash flow statement section in detail, including cash flows from operating, investing, and financing activities, and how to link these forecasts to other financial statements and schedules.

What are the Components of the Cash Flow Statement?
---------------------------------------------------

The Cash Flow Statement is essential for understanding a company’s financial health, detailing cash inflows and outflows. This article breaks down the individual components of the Cash Flow Statement, including net income, [working capital](https://www.financial-modeling.com/glossar/working-capital/)
, and how to reconcile cash movements. We’ll explain the impact of non-cash items like [depreciation](https://www.financial-modeling.com/glossar/depreciation/)
 and [amortization](https://www.financial-modeling.com/glossar/amortization/)
, and how they influence beginning cash and ending cash balances. You’ll also learn about movements in operating assets and how they affect cash flow, e.g., changes in inventory and receivables, enhancing your overall understanding of cash flow dynamics in financial models.

### How do companies report cash flows? Direct vs. Indirect Method

Companies can report cash flows through either the direct or the indirect method. The direct method starts with actual cash transactions, focusing on cash inflows and outflows directly linked to operating activities, such as revenue and payments. This method provides a clear view of the company’s cash movements. The indirect method begins with net income from the [income statement](https://www.financial-modeling.com/glossar/income-statement/)
 and adjusts for non-cash items and changes in working capital. It reconciles net income to actual cash flow from operations, offering a broader perspective on financial performance by accounting for non-cash items and operational adjustments.

It is very uncommon among US companies to find cash flow statements using the direct method. A prominent example can be found on page 62 of the 10-K of EMC Corporation from 2016, prior to Dell acquiring the firm in the same year ([Link](https://www.sec.gov/Archives/edgar/data/790070/000079007016000229/emc-2015123110xk.htm#sD6193B20426281FA7D10F1CB38540473)
). While the Financial Accounting Standards Board [(FASB](https://www.fasb.org/)
) recommends the use of the Direct method for greater transparency, most major US corporations opt for the Indirect method. 

Below you can see the difference in the “Cash from operating activities” section of the CFS of EMC Corporation (Direct) andDell Technologies Inc. (Indirect):

|     |     |
| --- | --- |
|     |     |
| ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20width='0'%20height='0'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20width='0'%20height='0'%20viewBox='0%200%200%200'%3E%3C/svg%3E) |

Why is a cash flow forecast important?
--------------------------------------

A cash flow forecast is essential in financial modeling as it provides a clear picture of a business’s future financial health. From a business’s perspective, predicting cash inflows and outflows serves as the basis for planning for debt repayments and managing obligations effectively. For example, understanding upcoming capital expenditures helps ensure that funds are available when needed, preventing financial shortfalls. For investment banks, investors, and stakeholders, a well-constructed cash flow forecast enhances the accuracy of a business’s [valuation](https://www.financial-modeling.com/glossar/valuation/)
 by demonstrating financial stability and foresight or the lack thereof. Overall, it’s a critical tool for maintaining [liquidity](https://www.financial-modeling.com/glossar/liquidity/)
, supporting strategic planning, and ensuring long-term success.

How to prepare cash flow forecast in Excel?
-------------------------------------------

Given the scarcity of Direct method cash flow reporting in US public companies, we will focus entirely on forecasting indirect method cash flow statements. Ideally, we recommend students to lay out the company’s CFS **line by line in excel as reported** when forecasting cash flows, as this helps to better understand each individual factor driving a change in cash. In the following sections, you will get a better understanding of the key line items that require projections within the 3 major sections of the CFS, i.e, (i) Cash from operations (ii) Cash from investing (iii) Cash from financing. 

### How to Forecast Cash Flows From Operating Activities

Cash flow from operating activities shows the cash generated from net income or profit. Since sales recorded on the Income Statement can be in cash or credit, and expenses can be either cash or non-cash, adjustments are needed. Non-cash expenses, including depreciation and amortization (D&A), are added back to the net income. This ensures that the cash flow statement accurately reflects the net sales and expenses in terms of actual cash flow.

Cash from operations is essentially the company’s net income after removing all non-cash items. This means that the revenue which was collected on credit and the expenses which were paid on credit are removed. While both are booked on the P&L, neither of them affects cash. Once the company collects the outstanding sales on credit and pays the outstanding invoices (Note: These do not have to happen simultaneously and they depend on the agreements with customers and suppliers), the CFS is affected with cash in and outflows, respectively.

To illustrate this further, the following table provides and overview of the most common income statement items which can be deferred, i.e., the cash impact can happen in a different period as when they are booked on the income statement, and which items on the cash flow statement are affected if this is the case.

| **Income Statement Item** | **Effect on Cash Flow Statement** | **Specific Cash Flow Statement Item Affected** |
| --- | --- | --- |
| **Revenue** | Increases cash flow from operations when cash is received or decreases when receivables increase | **Accounts Receivable (Operating Activities)** |
| **Cost of Sales** | Decreases cash flow from operations when inventory increases over a period or when payables decrease. Increases cash flow from operations when inventory decreases over a period or payables increase. | **Inventory and Accounts Payable (Operating Activities)** |
| **Selling, General & Administrative (SG&A) Expenses** | Decreases cash flow from operations when cash is paid for expenses, or increases when expenses are accrued or prepaid | **Accrued Expenses and Prepaid Expenses (Operating Activities)** |

**Additional Explanation:**

*   **Revenue** impacts cash flow mainly through changes in **Accounts Receivable**. When cash is received at the time of sale, it directly increases cash flow from operations. However, if sales are made on credit (leading to an increase in accounts receivable), cash is not yet collected, which ties up funds and reduces cash flow from operations.
*   **Cost of Sales** influences cash flow through **Inventory** and **Accounts Payable**. When a company sells more inventory than it purchased during a given period, the cash inflow from these sales increases cash flow from operations. However, when a company purchases more inventory than it sells, the cash used to acquire this inventory hasn’t yet been recovered through sales, leading to a reduction in cash flow from operations. If the inventory is purchased on credit (increasing accounts payable), it delays the cash outflow, thereby conserving cash and positively affecting cash flow from operations. However, once the invoices for the inventory purchased on credit are paid in cash, accounts payable decrease, which in turn reduces cash flow from operations.
*   **SG&A** expenses typically affect cash flow through **Accrued Expenses** and **Prepaid Expenses**, both of which are components of working capital. When cash is paid to cover SG&A expenses, it reduces cash flow from operations. If these expenses are accrued (meaning they are recognized as liabilities but not yet paid), they temporarily increase cash flow from operations because no cash outflow has occurred yet. Conversely, when expenses are prepaid (such as rent paid in advance), cash flow from operations is reduced upfront, but the expense is recognized later. The timing of these transactions significantly impacts how cash flow from operations is reported, as it reflects when cash actually leaves or enters the business.

We want to highlight that Accounts Receivable, Inventory, Accounts Payable, and other Working Capital Items are typically modeled in a separate Working Capital Schedule (Link to Article) and linked to the projection years of the cash flow statement.

### _How to Forecast Cash Flows From Investing Activities_

Forecasting cash flow from investing activities, particularly focusing on [capital expenditures (CapEx)](https://www.financial-modeling.com/glossar/capital-expenditures/)
, involves projecting a company’s future investments in long-term assets. To forecast CapEx, start by analyzing historical spending trends and understanding the company’s growth strategy or expansion plans. Companies typically disclose planned capital projects in financial reports or investor presentations, which can be used to estimate future expenditures. Additionally, consider industry benchmarks and economic conditions, as these factors can influence spending. Once forecasted, CapEx is subtracted from net cash provided by operating activities to calculate the net cash flow from investing activities in a financial model.

### How to Forecast Cash Flows From Financing Activities

Forecasting cash flow from financing activities involves projecting future inflows and outflows related to debt and [equity](https://www.financial-modeling.com/glossar/equity/)
. To forecast debt, assess existing loan agreements, repayment schedules, and potential new borrowing based on the company’s capital needs and [leverage](https://www.financial-modeling.com/glossar/leverage/)
 strategy. Consider interest rates, maturity dates, and any planned refinancing. For equity, review past trends in stock issuance or buybacks and management’s plans for future actions, like raising capital or repurchasing shares. [Dividends](https://www.financial-modeling.com/glossar/dividends/)
 and changes in [equity financing](https://www.financial-modeling.com/glossar/equity-financing/)
 should also be considered. These projections help estimate net cash flows from financing activities, which are essential for understanding the company’s funding and capital structure.

### How to Forecast “Other” and Exceptional Cash Flows

When preparing cash flow projections, you will quickly notice that certain line items become tricky to forecast, specifically those that are have either no clear connection to revenues or cost categories on the P&L statement. To solve this, there are typically certain line items which will simply be estimated as “zero” in future periods if they are considered “one-time” cash outflows. An example of a cash flow which fits this description could be a restructuring cost, a debt extinguishment cost, or net proceeds from acquisitions/divestitures, **unless**the company has disclosed specific information of such upcoming events. “Other” line items with low visibility on the company’s plans can be tricky to project as well, as these frequently net multiple different items together and are not always broken down in detail. A good analyst must then recognize if there is a pattern over the past 3-5 years, and pick an appropriate conservative projection method, e.g, an average or the maximum cash outflow in the past 3 years.

Forecasting other cash flows, such as changes in working capital or miscellaneous inflows and outflows, can be approached using three main methods: the 3-year maximum, minimum, and average, or based on last year’s performance. These methods provide different scenarios, helping to predict future trends. The 3-year average gives a balanced view, while max/min capture potential extremes. Foreign exchange (FX) rates also impact cash flow, especially for multinational companies; fluctuations in FX rates can lead to gains or losses that affect cash balances. Ultimately, these factors combined influence the change in cash and cash equivalents, a key metric in cash flow forecasting.

Forecasting Free Cash Flow – Different Variations for Different Purposes
------------------------------------------------------------------------

Forecasting [Free Cash Flow (FCF)](https://www.financial-modeling.com/glossar/free-cash-flow/)
 requires understanding its various forms, tailored to different financial analyses. At its core, FCF is typically defined as Cash Flow from Operations (CFO) minus Capital Expenditures (Capex), with some variations excluding or including dividends. Since FCF is a non-GAAP metric, companies have flexibility in its calculation, making it crucial to adjust for these differences based on the analysis at hand. [Unlevered Free Cash Flow (UFCF)](https://www.financial-modeling.com/glossar/unlevered-free-cash-flow/)
 and [Levered Free Cash Flow (LFCF)](https://www.financial-modeling.com/glossar/levered-free-cash-flow/)
 are essential for [discounted cash flow (DCF)](https://www.financial-modeling.com/glossar/discounted-cash-flow/)
 and leveraged buyout (LBO) models. UFCF ignores financing structure, while LFCF factors in debt obligations, offering more granular insights into equity returns. To fully grasp these variations and their practical applications, consider joining our 1-on-1 tutoring sessions, where we dive deep into real-world forecasting through hands-on practice.

Do you have an inquiry? Schedule a free initial consultation

[Schedule a consultation here](tel:01737209772)
 [info@financial-modeling.com](mailto:info@financial-modeling.com)

**Opening hours**

**Appointment** by  
prior arrangement

****ADDRESS****

777 McCarter Hwy, Newark, **NJ**  
1541 NE 42nd Ct, Pompano Beach, **FL**  

**Telephone**

[+1-754-249-7916](tel:+1(754)2497916)

**E-Mail**

[info@financial-modeling.com](mailto:info@financial-modeling.com)

[](https://www.financial-modeling.com/how-to-forecast-a-cash-flow-statement# "Scroll back to top")