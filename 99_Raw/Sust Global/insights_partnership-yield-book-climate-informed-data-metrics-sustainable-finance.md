# Sust Global | Our partnership with Yield Book: Towards climate-informed metrics in sustainable finance

**Source:** https://www.sustglobal.com/insights/partnership-yield-book-climate-informed-data-metrics-sustainable-finance

---

Our partnership with Yield Book: Towards climate-informed metrics in sustainable finance
----------------------------------------------------------------------------------------

Since 1980, natural disasters and events have inflicted damages exceeding $2 trillion in the United States. Coupled with stricter regulations and heightened investor demands for risk management and reporting, it is essential for the market to adopt superior strategies for managing physical climate risk. Sust Global's partnership with Yield Book, a London Stock Exchange Group business builds towards such strategies. Gopal Erinjippurath, CTO and Head of Product at Sust Global, provides an overview of our collaboration.

At Sust Global, we obsess over working on the world's hardest problems in climate. 'Hardest' to us isn't just about technical complexity; it's about what's absolutely crucial for proactive, game-changing decisions that shape the global economy.

Over the past four years, we have been innovating to serve climate analytics and APIs that we serve through our product, Climate Explorer. The essence of our work is to integrate scientifically validated climate indicators into the foundations of financial decision-making processes.

The recent commentary around ESG funds and falling investor confidence in "green" investment practices shows that more robust and transparent climate data needs to be integrated into products to restore investor trust. Our products, a fusion of the best climate data with the [software for climate adaptation](https://medium.com/age-of-awareness/the-software-of-climate-adaptation-242d06ed7c0f)
, are essential solutions to catalyze the creation of a truly sustainable financial sector.

### Towards a sustainable financial sector

The financial sector is increasingly vulnerable to the economic fallout from more frequent and severe climate events, with the impacts affecting market dynamics and investment strategies. A [recent global survey of institutional asset owners](https://assets.kpmg.com/content/dam/kpmg/ca/pdf/2022/02/do-asset-prices-fully-reflect-climate-risks-and-opportunities.pdf)
 managing a combined $34.5 trillion worth of investments found that the vast majority of them do not think financial securities properly capture climate risks.

Analysts at financial institutions are therefore seeking ways to effectively measure and manage climate-related risks, with a consistent approach to risk assessment and reporting.

Sust Global has developed a comprehensive set of tools for analytics and metrics targeting the core challenges in portfolio level climate risk management and resilience building.

Our solution encompasses:

*   Analyzing critical climate scenarios derived from the latest IPCC guidelines;
    
*   Assessing physical climate risk through various lenses, including direct and indirect risk exposure, financial impact, and impact on business operations;
    
*   Providing flexible data aggregation at various levels – from individual assets to entire sectors – via API integrations.
    

Our proposition combines the latest in remote sensing, climate modeling, and geospatial artificial intelligence. This enables robust validation and is tailored for large-scale, global risk analysis, offering insights into both direct risk exposure and broader financial impacts across multiple asset classes (such as [nature-based carbon credits](https://medium.com/predict/the-role-of-ai-in-fireproofing-forest-carbon-4fb32269c339)
).

Sust Global’s API-first ethos prioritizes the seamless integration of our geospatial climate analytics into customer solutions sets. In doing so, we enable new and existing climate risk management processes (data compositions), as well as the creation of innovative new applications that help financial institutions to make climate-informed decisions.

### Composable climate analytics at Yield Book

Sust Global’s APIs serve climate data, analytics and industry standard metrics, enabling new and existing customer workflows across financial services, corporate risk management and nature-based carbon to be climate informed. We see each such workflow as a composition of the essential building blocks of analysis powered by climate data and refer to the class of such analytics as composable climate analytics.

Our partnership with Yield Book is a great example of composable climate analytics in action. Together, Sust Global and Yield Book recently launched tailored physical climate risk analytics for US commercial and residential mortgage-backed securities (MBS).

The joint solution combines Yield Book’s leading financial analytics and asset-level datasets with our climate metrics to provide a view into the pricing impact of various climate hazards on US MBS portfolios. Climate risk to MBS assets is then aggregated at the loan and pool level.

*   Scoreseverity = latest severity of risk event
    
*   Scoretrend = Change in severity for most recent periods
    
*   Scoreavg = historical average severity measure
    

YBCC Metric\_risk = βseverity \* Scoreseverity + βtrend \* Scoretrend + βavg \* Scoreavg where risk = cyclone, flood and wildfire, β is the corresponding weight.

![](https://www.sustglobal.com/assets/API-patterns-1-1024x576.png)

The collaboration introduces two main API integrations:

### Climate analytics for properties and loans

For on-demand climate analytics, Sust Global processes individual loans and issuer level assets through batch processing and search APIs, serving climate risk analytics on hazards like wildfire, floods, cyclones, sea level rise, heat stress and water stress based on frontier climate models and latest satellite-derived hazard event observations.

### Climate metrics for listed CMBS

Yield Book is able to analyze mortgage pools based on their underlying securities. This process covers securities including Agency RMBS (Residential Mortgage-Backed Securities) at state level, Non-Agency RMBS at zip code level, and Listed CMBS (Commercial Mortgage-Backed Securities) loans. As the loan level information in MBS pools is relatively static (a "fixed universe"), it can be processed and updated all at once. Yield Book integrates with a bulk query API from Sust Global to replicate data to their data warehouse, enabling partner applications like Yield Book plugin and Yield Book Classic with climate metrics.

These integrations enable a detailed, climate-aware evaluation of these investment instruments. The end product applies to a range of industry use cases, including automating reports to monitor climate risk metrics on portfolios and update key stakeholders, deal structuring, back-testing, and deep research and risk mitigation strategies using historical data.

Outcomes for climate informed structured finance
------------------------------------------------

The Yield Book analytics team [researched the impact of physical climate risk on Agency CMBS](https://thesource.lseg.com/thesource/getfile/index/2b3543b5-dcb6-4e72-b2b7-11040463ca55)
, powered by a combination of Sust Global data and their own industry-standard MBS models. They analyzed 54K active loans backing CMBS securities with a total $1,122B exposure, including $392B in Agency CMBS and $730B in non-Agency CMBS. Here are the key outcomes from their research:

### 1\. Climate-informed prepayment analysis

![](https://www.sustglobal.com/assets/Edited-Yield-Book-2-1.png)

**Left:** **_Geospatial distribution of Yield Book Metric_**_: Metric designed and computed based on satellite derived actuals of flood risk exposure at the zip code level using Sust Global’s global climate risk API._ **Right: _Actuals analysis of prepayment speeds (Low Flood Risk vs High Flood Risks)_**_: This analysis was run on GNPL actuals for lifetime average CPR. Analysis based on satellite derived actual flood risk exposure over loan periods from Sust Global’s global_.

Conditional Prepayment Rate (CPR) is a vital metric in the MBS market, influencing cash flows, yields, duration, and overall valuation. CPR provides a standardized measure of the annualized rate of prepayment of principal on mortgage loans. Since MBS are backed by these mortgages, prepayment rates directly affect the securities' value and performance.

Prepayments can occur when homeowners refinance, sell their homes, or make larger than required payments on their mortgage. The valuation of MBS is heavily dependent on the projected prepayment rates. CPR is a key input in financial models used to value these securities, affecting decisions on buying, selling, or holding these assets.

Modeling CPR helps in modeling prepayment risk – the risk that prepayments will occur at an unfavorable time, affecting the profitability of the investment. This is particularly important for portfolio managers and investors in structuring and choosing their MBS investments.

From their recently published study, the Yield Book research team found a connection between increased physical climate risk and lower prepayment rates in loans which in turn enables more accurate valuation models for MBS.

### 2\. Climate-informed pricing analysis

![](https://www.sustglobal.com/assets/Edited-Yield-Book-2.png)

**Left:** **_Geospatial distribution of Sample for Weighted Average Maturity (WAM) analysis:_** _100FN DUS securities (pools) backed by properties located in high flood risk areas._ **Right:** **_Valuation impact by Weighted Average Maturity (WAM) (Climate scenarios: SSP2-RCP4.5 and SSP5-RCP8.5):_** _Most pronounced valuation disparities in securities with longer WAM. The more severe climate scenario (SSP5-RCP8.5) manifests a bigger price impact. Analysis based on climate projections on flood risk exposure from Sust Global’s global climate risk API._

Weighted Average Maturity (WAM) calculates the average time until the mortgages in an MBS portfolio are paid off. It's weighted based on the principal balance of each loan, giving a more accurate representation of the portfolio's maturity profile compared to a simple average.

WAM is a key factor in assessing the interest rate risk of an MBS. Longer WAM indicates a longer duration, meaning the security is more sensitive to changes in interest rates. This is crucial for investors who need to manage the risk associated with rate fluctuations. Investors use WAM to tailor their portfolios to match their investment horizons or risk preferences. For instance, a portfolio with a shorter WAM might be preferred by investors seeking less interest rate risk and a quicker return of principal.

The Yield Book research team concluded that repricing risks with climate considerations, in this case accounting for flood risk projections, leads to prices that deviate from market norms.

### 3\. Customized, instrument-level risk metrics

Yield Book has developed a risk metric encapsulating the predominant climate risks, integrating present-day hazard severity, contemporary trends, and historical averages. This metric enables the representation of risk for such analysis applied to active loans. The metric will vary across loans based on their geographic distribution.

While this metric is indicative of representative climate risk quantification for CMBS, it is representative of climate informed metrics designed to address specific instruments in structured finance in the future.

### Global climate data coverage

Sust Global offers global data coverage. We have processed data for over 150,000 client assets worldwide using our platform and via our APIs across varied dynamic customer workflows .

Sust Global's partnership with Yield Book is a major landmark in the journey towards climate-aware financial markets. Such partnerships help investors quantify and visualize not only what climate risks and opportunities look like for them today, but also what they might look like in 2030, 2040, and 2050.

Commenting on our collaboration Cornelia Andersson, Group Head of Sustainable Finance and Investing, London Stock Exchange Group, said:

“_This strongly supports LSEG’s role in mobilizing capital for a sustainable global economy. This product is a great addition to our existing portfolio and efforts to support clients across the globe on sustainability challenges, through quantitative integration of climate risks and considerations in existing workflows and tooling._”

We are actively partnering to expand the use of AI-driven climate data and geospatial analytics in financial decision-making as we strive to ensure that every decision is climate-informed.

Reach out to us below and let’s talk about how we can work together climate-informed decision making across structured finance products.

**_Further reading:_**

[_The software of climate adaptation_](https://medium.com/age-of-awareness/the-software-of-climate-adaptation-242d06ed7c0f)
, Gopal Erinjippurath, December 2021

[_Do asset prices fully reflect climate risks and opportunities_](https://assets.kpmg.com/content/dam/kpmg/ca/pdf/2022/02/do-asset-prices-fully-reflect-climate-risks-and-opportunities.pdf)
, KPMG, February 2022

[_The role of AI in fireproofing forest carbon_](https://medium.com/predict/the-role-of-ai-in-fireproofing-forest-carbon-4fb32269c339)
, Gopal Erinjippurath, May 2023

[_Assessing physical climate risks on Agency CMBS_](https://thesource.lseg.com/thesource/getfile/index/2b3543b5-dcb6-4e72-b2b7-11040463ca55)
, Yield Book, September 2023

* * *

_Gopal serves as CTO and Head of Product. He is known for agile engineering execution from concept to scalable high quality products. He has been an invited speaker at global industry conferences like Google Cloud Next and leading technical conferences in the machine learning space such as ICML, CVPR and NeurIPS. He also led the Analytics Engineering team at Planet Labs. Gopal holds an MS from USC and completed the Ignite Program at the Stanford Graduate School of Business._

Cookie consent
--------------

We use cookies to give you the best online experience. Please let us know if you agree to all of these cookies.

**Analytics**

Accept all Decline