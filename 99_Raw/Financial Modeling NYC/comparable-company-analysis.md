# How to Perform Comparable Company Analysis (Comps)

**Source:** https://www.financial-modeling.com/comparable-company-analysis

---

[Skip to content](https://www.financial-modeling.com/comparable-company-analysis#content "Skip to content")

How to Perform a Comparable Company Analysis (Comps) in Investment Banking: A Step-by-Step Valuation Guide to Choose Comparable Companies
=========================================================================================================================================

![Street signs in New York City at the corner of Wall Street and Broad Street. Financial Modeling New York.](https://www.financial-modeling.com/wp-content/uploads/2025/05/Comparable-Company-Analysis-New-York-1-2048x1367.jpg "Comparable-Company-Analysis-New-York")

Comparable company analysis (also known as “comps analysis”) is one of the most widely used [valuation](https://www.financial-modeling.com/glossar/valuation/)
 methods in [investment banking](https://www.financial-modeling.com/glossar/investment-banking/)
, [private equity](https://www.financial-modeling.com/glossar/private-equity/)
, [corporate finance](https://www.financial-modeling.com/glossar/corporate-finance/)
, and [equity](https://www.financial-modeling.com/glossar/equity/)
 research. This technique values a company by comparing it to other public companies with similar financial and operational characteristics. The goal is to understand the current market pricing and determine whether the company is overvalued or undervalued relative to selected group of comparable companies.

This guide will walk you through the full process of conducting a comps analysis. You’ll learn how to select the right comparable companies, calculate the valuation multiples, and apply them to value a company. Along the way, we’ll highlight common pitfalls, best practices, and tools you can use to ensure accuracy in your business valuation.

What Is Comparable Company Analysis and Why Do Analysts Use Comparable Company Analysis in a Financial Model? 
--------------------------------------------------------------------------------------------------------------

Comparable company analysis is a relative valuation technique that involves comparing companies with similar size, industry, and financial performance. It is one of the most common methods to arrive at a valuation of the target company you are analyzing, establishing a valuation range based on how similar public companies are currently trading in the market.

This form of valuation is especially useful when the target company operates in a well-established sector with available data on comparable public companies. It is a key valuation method in situations like mergers and acquisitions, IPO pricing, and fairness opinions.

Like any valuation method, comparable company analysis has its strengths and limitations. The table below highlights the most important pros and cons to keep in mind when deciding whether to use this approach.

![Pros and Cons overview of comparable company analysis. Financial Modeling New York.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20width='1024'%20height='683'%20viewBox='0%200%201024%20683'%3E%3C/svg%3E)

_Note: Weighing the pros and cons of a comps analysis, and other valuation methods is one of the most common investment banking and private equity interview questions._

When to Use Comps Analysis and What It Tells You About Market Value Through Relative Valuation
----------------------------------------------------------------------------------------------

This valuation technique is often used in comparable company analysis to assess what a company is worth by examining a set of companies that are similar to the company they are trying to value, while carefully accounting for differences between the comparable companies in terms of growth, margins, and capital structure. Analysts must gather detailed information about the companies and screen for potential comparable companies to ensure they choose companies of similar size and financial profile.

It’s also helpful for benchmarking a private company against public companies in the same industry. Investment bankers and analysts use comparable company analysis to get a sense of real-time investor sentiment, helping them balance valuation advice with discounted cash flow models that rely heavily on future projections.

Step 1: How to Choose Comparable Companies and Build a Relevant Peer Group
--------------------------------------------------------------------------

Selecting comparable companies is the foundation of a reliable comps analysis. The goal is to find similar companies that match the target company based on industry, geography, size, and financial metrics. 

**Peer selection is often as much an art as it is a science.** While objective criteria like industry classification and revenue size provide a starting point, analysts must use judgment to identify companies with comparable business models and financial profiles. For instance, comparable company analysis is used to assess two firms that may operate in different sectors—such as retail and tech—but both can be relevant peers if they are e-commerce platforms with similar monetization strategies. In contrast, a company may seem like a good peer on the surface, but deeper research might reveal that the company has a higher degree of diversification, generating a significant share of revenue from unrelated industries. In such cases, it may no longer qualify as a reliable comp. These subtleties make it essential to go beyond surface-level screening and fully understand how each business actually operates.

**Key selection criteria:**

*   Industry classification (NAICS/SIC codes)
*   Business model and revenue streams
*   Geography (regional vs. global presence)
*   Size (market capitalization, revenue, EBITDA)
*   Growth rate and margins

You want to build a set of comparable companies that operate in the same industry and serve similar customers. This means looking for companies that are similar in both qualitative and quantitative ways. It’s important to note that perfect comps rarely exist in the real world—no two companies are exactly alike. However, some pairings come remarkably close; for example, Coca-Cola and Pepsi are often considered near-perfect comparables based on the selection criteria outlined above.

**Best-practice tip:** Start by reviewing the 10-K / 10-Q filings (freely available on [sec.gov](https://www.sec.gov/)
) or investor presentations of the company you are trying to value—many firms list a peer group in their own filings.

Other sources include equity research reports, Bloomberg, Capital IQ, and PitchBook. These platforms also help you find similar companies that analysts and investment bankers already track. Keep in mind that these are subscription-based platforms, and unless you have access through your employer or university, it may not be cost-effective to purchase a personal subscription solely for this information.

Step 2: Normalize Financials and Spread Key Metrics into Your Comps Analysis
----------------------------------------------------------------------------

After you choose comparable companies with similar characteristics and market value, the next step is to spread their financial data into a comps table. This involves standardizing metrics so that you can compare them on a like-for-like basis.

### [Calendarization](https://www.financial-modeling.com/glossar/calendarization/)
: Aligning Fiscal Periods Across Your Peer Group for Better Enterprise Value Comparisons

Often, your selected universe of companies to compare will have different fiscal years, i.e., not every company reports January to December. When this happens, you’ll need to **calendarize** their financials—such as revenue, EBITDA, or net income—to ensure a meaningful, apples-to-apples comparison across your peer group.

Let’s say a company’s fiscal year ends on March 31. That means three months (January to March) fall into the current fiscal year, while the remaining nine months (April to December) fall into the next fiscal year. To reflect this properly, you use a **weighted average** of the two estimates—based on how many months from each fiscal period fall within the calendar year. For example:

`Calendar Year Revenue = (3 months x FY1 Sales) / 12 + (9 months x FY2 Sales) / 12`

This is important when companies have different fiscal year ends, otherwise you would be comparing financials from different periods, which makes it hard to justify calling it a _“comparable”_ company analysis.

### Capital Structure and Valuation Inputs: Equity, Enterprise Value, and Market Capitalization

You’ll need to calculate both [equity value](https://www.financial-modeling.com/glossar/equity-value/)
 and enterprise value for each company:

**Equity Value** = Share Price x Fully Diluted Shares Outstanding  
Use the Treasury Stock Method to account for in-the-money [options](https://www.financial-modeling.com/glossar/options/)
, RSUs, and convertibles.

**Enterprise Value** = Equity Value + Net Debt + Preferred Equity + Minority Interest

Understanding a company’s capital structure is essential to choosing the appropriate valuation multiples.

Also, adjust EBITDA and EBIT for non-recurring items like [asset](https://www.financial-modeling.com/glossar/asset/)
 sales, impairments, or restructuring charges. This ensures the valuation reflects core operations.

Step 3: Calculate the Right Valuation Multiples for Each Metric
---------------------------------------------------------------

Valuation multiples are the backbone of any comps analysis. The most commonly used valuation multiples include:

*   **EV / Revenue**
*   **EV / EBITDA**
*   **EV / EBIT**
*   **Price / Earnings (P/E)**

These multiples reflect how much investors are willing to pay for each unit of revenue, EBITDA, or earnings. Key valuation multiples will differ across sectors—some industries may also use industry-specific metrics like EV/Subscribers or EV/Barrels.

Always use LTM (Last Twelve Months) or NTM (Next Twelve Months) figures depending on the context. Make sure to be consistent across your peer group. Forward-looking multiples are generally preferred, as they reflect future performance expectations. However, they are more vulnerable to [forecasting](https://www.financial-modeling.com/glossar/forecasting/)
 errors and unknown non-recurring items, which can distort the valuation if not carefully adjusted for.

Furthermore, **Price-to-Sales (P/S) multiples** can be extremely useful and more appropriate for companies with negative, volatile, or unusually high or low [earnings per share (EPS)](https://www.financial-modeling.com/glossar/earnings-per-share/)
, i.e., negative net income. For example, high-growth businesses that haven’t yet reached profitability—or are intentionally operating at a loss to scale rapidly—may be more appropriately valued using revenue-based multiples. One of the key advantages of using Price/Sales is the relative stability of sales figures, which are less prone to accounting manipulation compared to earnings metrics

Step 4: Apply Valuation Multiples and Interpret Enterprise Value and Equity Ranges
----------------------------------------------------------------------------------

Once you’ve calculated the valuation multiples for each peer, analyze the distribution: high, low, mean, and median. Then apply those multiples to your target company’s financial metric (e.g., EBITDA) to estimate its valuation range.

**Example:** If the median EV/EBITDA is 9.0x and your company’s EBITDA is $120 million:

`Implied Enterprise Value = 9.0x * $120 million = $1.08 billion`

From there, back into the equity value using the company’s capital structure.

### Handling Outliers and Adjustments in Your Peer Group Analysis

Remove outliers that skew the average. Also, consider qualitative differences between the comparable companies—like customer concentration, cyclicality, and management quality.

This step is essential to avoid over- or under-valuing your target company based on irrelevant comps.

How to Build a Professional Comps Table in Excel as Part of Your Financial Model
--------------------------------------------------------------------------------

Use Excel to create a comps table that’s both functional and presentable.

**Best practices:**

*   Color hard-coded inputs (blue), formulas (black), and links to separate worksheets (green)
*   Clearly flag estimates and adjustments
*   Add footnotes to explain key assumptions
*   Use excel shortcuts to speed up formatting and formula consistency

A clean, well-organized table helps you communicate your analysis clearly in investment banking pitchbooks or private equity memos.

Avoiding Common Mistakes in Comps Analysis: How to Perform Investment Banking Valuation Work
--------------------------------------------------------------------------------------------

*   **Choosing the wrong peer group**: Not all companies in the same industry are relevant. Choose the right comparable companies to the company you are valuing based on business model and scale, ensure your analysis gives you an accurate valuation range.
*   **Ignoring calendarization**: Misaligned fiscal periods distort valuation.
*   **Overlooking [dilution](https://www.financial-modeling.com/glossar/dilution/)
    **: Failing to use diluted share count leads to incorrect equity value.
*   **Relying on a single metric**: Combine multiple metrics and valuation multiples to triangulate a fair value.

These mistakes can undermine your entire analysis and lead to misinformed conclusions.

Real-World Example: Sample Comps Table with Enterprise Value, Equity, and Multiples by Metric
---------------------------------------------------------------------------------------------

When presenting to stakeholders, a clear summary table like the one below is usually expected. Our Expert Valuation Package guides you through the entire process—from choosing the right peer group and gathering financial data to building a polished final output like this. Want to try it yourself? Download our free Excel template and start calculating comps metrics on your own. If you need support or would like the full solution file, just send us an email—we’re happy to share it with you.

![Output table of a comparable company analysis. Financial Modeling New York.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20width='970'%20height='465'%20viewBox='0%200%20970%20465'%3E%3C/svg%3E)

### How to Interpret the Valuation Results for Our Target, Firm A

To keep things simple, let’s use one equity-based multiple and one enterprise-value-based multiple in our analysis. Using the **median of the peer comps** is common practice, as it helps reduce the influence of outliers within the peer group.

For FY25E, the **median forward P/E ratio** among the comps is **15.3x**. If Firm A is expected to generate **EPS of $3.67**, we calculate the implied share price as:  
**$3.67 × 15.3 = $56.15 per share**.

Next, to estimate Firm A’s implied share price using an **enterprise value multiple**, we apply the **FY25E peer median EV/EBITDA multiple of 8.4x** to Firm A’s projected **EBITDA of $27,360 million**:  
**8.4 × $27,360 million = $229,824 million in Enterprise Value**.

To convert this into equity value, we subtract net debt. For simplicity, assume net debt stays constant from FY24A to FY25E. Using FY24A financials:  
**Net Debt = Enterprise Value ($225,008 million) – Market Cap ($186,344 million) = $38,663 million**

Then, we calculate equity value:  
**$229,824 million – $38,663 million = $191,160 million**

Now, divide this equity value by the **total diluted shares outstanding of 2,254 million** (share counts included in practice excel model):  
**$182,761 million ÷ 2,254 million shares = $75.74 per share**

This gives us a **forward-looking valuation range** for Firm A between **$56.15 and $75.74 per share**, based on FY25E P/E and EV/EBITDA multiples from public comps. Given the breadth of this valuation range, it’s important to investigate the underlying drivers more closely—it may also indicate that the market is undervaluing the business. Comparing the results with other valuation methods—such as DCF analysis or Precedent Transactions—can offer additional perspective and help triangulate the most appropriate value for the firm.

Conclusion and Next Steps: Why You Should Use Comparable Company Analysis in Your Next Financial Model
------------------------------------------------------------------------------------------------------

Comparable company analysis is a powerful valuation methodology that lets you estimate the value of a company using current market data. By comparing companies that operate in the same industry, you get a real-time view of how investors price similar businesses.

This comparative analysis is a critical tool in [financial analysis](https://www.financial-modeling.com/glossar/financial-analysis/)
 and investment banking, often forming the backbone of valuation work alongside discounted cash flow models and precedent transactions.

Whether you’re analyzing a private company or a publicly traded one, comps valuation provides an efficient and market-aligned perspective on the value of the company you are analyzing.

**Want to learn how to build a comps model step-by-step in Excel?** Reach out for private training, or enroll in our [financial modeling](https://www.financial-modeling.com/glossar/financial-modeling/)
 bootcamp to gain hands-on experience with valuation methods and real-world deal analysis.

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

[](https://www.financial-modeling.com/comparable-company-analysis# "Scroll back to top")