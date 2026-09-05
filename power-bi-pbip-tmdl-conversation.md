# Power BI, Tabular Editor, PBIP, and TMDL Conversation

**Exported:** 2026-09-04  
**Topic:** Building Power BI semantic models with DAX, calculation groups, PBIP, and TMDL

---

## User

How can I use Tabular Editor to make DAX expressions for POWER BI?

## Microsoft 365 Copilot

Tabular Editor is one of the best tools for writing, organizing, and maintaining DAX measures in Power BI because it provides a dedicated DAX editor, IntelliSense, syntax checking, dependency analysis, and bulk editing capabilities.

### Typical workflow

1. Open your Power BI Desktop model.
2. On the **External Tools** ribbon, launch **Tabular Editor**.
3. In Tabular Editor, right-click a table and select **Create > Measure**.
4. Give the measure a name.
5. Enter the DAX formula in the Expression Editor.
6. Save with `Ctrl+S`. The measure is written back into the Power BI model.

### Example

```DAX
Total Sales =
SUM ( Sales[SalesAmount] )
```

```DAX
Sales YTD =
TOTALYTD (
    [Total Sales],
    'Date'[Date]
)
```

### Main benefits

- Faster measure creation and editing
- DAX IntelliSense and autocomplete
- Dependency visualization
- Bulk editing
- Best Practice Analyzer
- DAX scripting and automation

A useful measure-folder structure is:

```text
Measures
 ├─ Sales
 ├─ Profit
 ├─ KPIs
 └─ Time Intelligence
```

---

## User

Show a full workflow for time intelligence measures.

## Microsoft 365 Copilot

A professional workflow starts with a proper Date table, builds reusable base measures, and then adds time-intelligence measures that reference those base measures.

### 1. Create a Date table

```DAX
Date =
ADDCOLUMNS (
    CALENDAR ( DATE(2020,1,1), DATE(2030,12,31) ),
    "Year", YEAR([Date]),
    "Month Number", MONTH([Date]),
    "Month", FORMAT([Date], "MMM"),
    "Year Month", FORMAT([Date], "YYYY-MM")
)
```

In Power BI, mark `Date[Date]` as the model's date column.

### 2. Build base measures

```DAX
Total Sales =
SUM ( Sales[SalesAmount] )
```

```DAX
Total Cost =
SUM ( Sales[CostAmount] )
```

```DAX
Profit =
[Total Sales] - [Total Cost]
```

### 3. Year to date

```DAX
Sales YTD =
TOTALYTD (
    [Total Sales],
    'Date'[Date]
)
```

```DAX
Profit YTD =
TOTALYTD (
    [Profit],
    'Date'[Date]
)
```

### 4. Month to date

```DAX
Sales MTD =
TOTALMTD (
    [Total Sales],
    'Date'[Date]
)
```

### 5. Quarter to date

```DAX
Sales QTD =
TOTALQTD (
    [Total Sales],
    'Date'[Date]
)
```

### 6. Previous year

```DAX
Sales PY =
CALCULATE (
    [Total Sales],
    SAMEPERIODLASTYEAR ( 'Date'[Date] )
)
```

Alternative:

```DAX
Sales PY =
CALCULATE (
    [Total Sales],
    DATEADD (
        'Date'[Date],
        -1,
        YEAR
    )
)
```

### 7. Year-over-year growth

```DAX
Sales YoY =
[Total Sales] - [Sales PY]
```

```DAX
Sales YoY % =
DIVIDE (
    [Sales YoY],
    [Sales PY]
)
```

Recommended format string:

```text
0.0%
```

### 8. Rolling 12 months

```DAX
Sales Rolling 12M =
CALCULATE (
    [Total Sales],
    DATESINPERIOD (
        'Date'[Date],
        MAX('Date'[Date]),
        -12,
        MONTH
    )
)
```

### 9. Rolling average

```DAX
Sales 12M Avg =
DIVIDE (
    [Sales Rolling 12M],
    12
)
```

### 10. Calculation groups

Instead of creating separate time measures for every business measure, create a reusable calculation group:

```text
Time Intelligence
 ├─ Current
 ├─ YTD
 ├─ MTD
 ├─ QTD
 ├─ PY
 ├─ YoY
 └─ YoY %
```

Example calculation item:

```DAX
CALCULATE (
    SELECTEDMEASURE(),
    DATESYTD ( 'Date'[Date] )
)
```

Previous-year calculation item:

```DAX
CALCULATE (
    SELECTEDMEASURE(),
    SAMEPERIODLASTYEAR ( 'Date'[Date] )
)
```

Calculation groups allow measures such as Total Sales, Profit, Margin, Units Sold, and Revenue to share the same time-intelligence logic.

---

## User

How do I create a calculation group?

## Microsoft 365 Copilot

Calculation groups let you write a transformation once and apply it to many measures.

### 1. Open Tabular Editor

In Power BI Desktop:

```text
External Tools > Tabular Editor
```

### 2. Create the calculation group

In Tabular Editor:

```text
Model
  Right-click
    > Create New
      > Calculation Group
```

Name it:

```text
Time Intelligence
```

### 3. Add Current

Create a calculation item named `Current`:

```DAX
SELECTEDMEASURE()
```

### 4. Add YTD

Create a calculation item named `YTD`:

```DAX
CALCULATE(
    SELECTEDMEASURE(),
    DATESYTD('Date'[Date])
)
```

### 5. Add previous year

Create a calculation item named `PY`:

```DAX
CALCULATE(
    SELECTEDMEASURE(),
    SAMEPERIODLASTYEAR('Date'[Date])
)
```

### 6. Add YoY difference

Create a calculation item named `YoY`:

```DAX
SELECTEDMEASURE()
-
CALCULATE(
    SELECTEDMEASURE(),
    SAMEPERIODLASTYEAR('Date'[Date])
)
```

### 7. Add YoY percentage

Create a calculation item named `YoY %`:

```DAX
DIVIDE(
    SELECTEDMEASURE()
        -
    CALCULATE(
        SELECTEDMEASURE(),
        SAMEPERIODLASTYEAR('Date'[Date])
    ),
    CALCULATE(
        SELECTEDMEASURE(),
        SAMEPERIODLASTYEAR('Date'[Date])
    )
)
```

Use this format string:

```text
0.0%
```

### 8. Set Ordinal

```text
Current    0
MTD        1
QTD        2
YTD        3
PY         4
YoY        5
YoY %      6
```

### 9. Save back to Power BI

Press `Ctrl+S` in Tabular Editor.

### 10. Use the group in a report

Add a base measure, such as `Total Sales`, to a matrix and add the calculation-group column to the matrix columns or to a slicer.

### 11. Dynamic format strings

For items that should retain the original measure formatting, use:

```DAX
SELECTEDMEASUREFORMATSTRING()
```

For the `YoY %` item, use:

```DAX
"0.0%"
```

---

## User

How can I build a Power BI project from scratch using TMDL and PBIP?

## Microsoft 365 Copilot

A modern project structure can combine:

```text
PBIP + TMDL + Git + Tabular Editor
```

### Recommended structure

```text
FinanceAnalytics/
│
├─ FinanceAnalytics.pbip
│
├─ FinanceAnalytics.SemanticModel/
│   ├─ definition/
│   │   ├─ model.tmdl
│   │   ├─ tables/
│   │   │   ├─ FactSales.tmdl
│   │   │   ├─ DimDate.tmdl
│   │   │   └─ DimCustomer.tmdl
│   │   ├─ relationships.tmdl
│   │   └─ roles.tmdl
│   └─ diagramLayout.json
│
├─ FinanceAnalytics.Report/
│   ├─ definition.pbir
│   └─ StaticResources/
│
├─ .gitignore
└─ README.md
```

### Workflow

1. In Power BI Desktop, save the work as a **Power BI Project (`.pbip`)**.
2. Initialize a Git repository.
3. Build the semantic model first using dimension and fact tables.
4. Open Tabular Editor and organize measures.
5. Create base measures.
6. Add reusable calculation groups.
7. Save semantic-model definitions as TMDL text files.
8. Run Best Practice Analyzer.
9. Commit small, reviewable changes to Git.
10. Add deployment automation when the model is ready.

Example Git setup:

```bash
git init
git add .
git commit -m "Initial PBIP project"
```

Recommended repository layout:

```text
project-finance-ai/
│
├─ powerbi/
│   ├─ FinanceAnalytics.pbip
│   ├─ FinanceAnalytics.SemanticModel/
│   └─ FinanceAnalytics.Report/
│
├─ data/
├─ sql/
├─ notebooks/
├─ scripts/
└─ docs/
```

---

## User

What are best practices for TMDL structure?

## Microsoft 365 Copilot

Treat TMDL as source code and organize it for readability, maintainability, code review, and mergeability.

### 1. One subject area per table

```text
tables/
├─ DimDate.tmdl
├─ DimCustomer.tmdl
├─ DimProject.tmdl
├─ FactBudget.tmdl
└─ FactActual.tmdl
```

### 2. Consider a dedicated measure table

```text
tables/
├─ FactSales.tmdl
├─ DimDate.tmdl
└─ _Measures.tmdl
```

This keeps DAX measures easy to locate and organizes the Power BI Fields pane.

### 3. Use consistent names

```text
DimDate
DimCustomer
DimProject
FactSales
FactBudget
BridgeCustomerProject
```

Avoid ambiguous or temporary names such as:

```text
tbl1
Sales_v2
Revenue_NEW
```

### 4. Organize measures with display folders

```text
Measures
├─ Revenue
├─ Cost
├─ Profitability
├─ Forecast
├─ KPIs
└─ Operational
```

### 5. Use calculation groups where they reduce duplication

```text
Calculation Groups
└─ Time Intelligence
   ├─ Current
   ├─ MTD
   ├─ QTD
   ├─ YTD
   ├─ PY
   ├─ Rolling 12M
   ├─ YoY
   └─ YoY %
```

### 6. Prefer a clear star schema

Use one-to-many relationships from dimensions to facts and prefer single-direction filters unless the model specifically requires another design.

### 7. Add descriptions

Descriptions should explain the business meaning of tables, columns, and measures, including important exclusions or assumptions.

### 8. Define format strings explicitly

Examples:

```text
Revenue: #,0.00
Margin %: 0.0%
Units Sold: #,0
```

### 9. Keep Git diffs small

Prefer commits such as:

```text
Added Budget Variance measure
Added YTD calculation item
Added Project dimension
```

### 10. Version model-support assets

Where relevant, include:

```text
semantic model
Power Query definitions
DAX standards
Tabular Editor BPA rules
model documentation
validation scripts
```

---

## User

Let's say I want to make a very simple dataset and create a Power BI project without using PBIX.

### Sample data

```csv
Date,Product,Region,Revenue,Cost,UnitsSold,CustomerID
2/10/2023,Product A,North,594,336.78,22,CUST-38
2/17/2023,Product A,North,1386,706.22,42,CUST-17
1/6/2023,Product B,South,1443,732.99,37,CUST-39
1/13/2023,Product D,South,1254,731.66,33,CUST-18
2/25/2023,Product A,South,1617,973.56,49,CUST-47
1/10/2023,Product B,East,242,148.58,11,CUST-31
1/23/2023,Product C,East,301,191.99,7,CUST-13
1/8/2023,Product D,North,1160,868.63,40,CUST-27
2/9/2023,Product C,South,1100,565.12,50,CUST-14
1/15/2023,Product C,North,893,473.56,19,CUST-22
1/18/2023,Product D,East,465,282.06,15,CUST-6
2/12/2023,Product C,North,1720,948.31,43,CUST-39
2/16/2023,Product B,South,1088,632.11,34,CUST-1
3/1/2023,Product B,East,216,161.25,8,CUST-1
2/21/2023,Product C,West,484,272.63,22,CUST-3
3/2/2023,Product C,South,1610,996.09,46,CUST-6
2/28/2023,Product D,South,504,289.29,21,CUST-3
2/5/2023,Product C,West,1344,817.96,42,CUST-16
1/9/2023,Product D,North,376,200.37,8,CUST-49
2/10/2023,Product B,West,946,582.2,43,CUST-23
2/11/2023,Product U,North,0,800,500,CUST-25
2/18/2023,Product V,South,10,600,600,CUST-49
1/10/2023,Product W,West,5,1200,700,CUST-34
```

## Microsoft 365 Copilot

For this small model, use a simple PBIP project with the source data, semantic model, report definition, and documentation in source control.

### 1. Project structure

```text
simple-sales-demo/
│
├─ SalesDemo.pbip
│
├─ SalesDemo.SemanticModel/
│   └─ definition/
│       ├─ tables/
│       │   ├─ FactSales.tmdl
│       │   ├─ DimDate.tmdl
│       │   ├─ DimProduct.tmdl
│       │   ├─ DimRegion.tmdl
│       │   ├─ DimCustomer.tmdl
│       │   └─ _Measures.tmdl
│       └─ relationships.tmdl
│
├─ SalesDemo.Report/
├─ data/
│   └─ sales.csv
└─ docs/
    └─ model.md
```

### 2. Logical model

#### FactSales

```text
DateKey
ProductKey
RegionKey
CustomerKey
Revenue
Cost
UnitsSold
```

#### DimDate

```text
DateKey
Date
Year
Month
MonthName
Quarter
```

#### DimProduct

```text
ProductKey
ProductName
```

#### DimRegion

```text
RegionKey
RegionName
```

#### DimCustomer

```text
CustomerKey
CustomerID
```

### 3. Relationships

```text
DimDate ───────┐
DimProduct ────┤
DimRegion ─────┼──> FactSales
DimCustomer ───┘
```

Use one-to-many, single-direction relationships from the dimensions to `FactSales`.

### 4. Core measures

```DAX
Revenue =
SUM(FactSales[Revenue])
```

```DAX
Cost =
SUM(FactSales[Cost])
```

```DAX
Profit =
[Revenue] - [Cost]
```

```DAX
Margin % =
DIVIDE(
    [Profit],
    [Revenue]
)
```

```DAX
Units Sold =
SUM(FactSales[UnitsSold])
```

```DAX
Customers =
DISTINCTCOUNT(FactSales[CustomerKey])
```

### 5. Additional KPIs

```DAX
Revenue Per Unit =
DIVIDE(
    [Revenue],
    [Units Sold]
)
```

```DAX
Revenue per Customer =
DIVIDE(
    [Revenue],
    [Customers]
)
```

### 6. Data-quality examples

The Product U, V, and W records have very low revenue compared with cost and units sold. They are useful for creating an anomaly or data-quality report page.

A simple loss indicator could be:

```DAX
Loss Indicator =
IF(
    [Profit] < 0,
    1,
    0
)
```

### 7. Calculation group

```text
Time Intelligence
├─ Current
├─ YTD
├─ PY
├─ YoY
└─ YoY %
```

YTD expression:

```DAX
CALCULATE(
    SELECTEDMEASURE(),
    DATESYTD(DimDate[Date])
)
```

Previous-year expression:

```DAX
CALCULATE(
    SELECTEDMEASURE(),
    SAMEPERIODLASTYEAR(DimDate[Date])
)
```

### 8. Example TMDL measure definitions

```tmdl
table _Measures

    measure Revenue =
        SUM(FactSales[Revenue])

    measure Cost =
        SUM(FactSales[Cost])

    measure Profit =
        [Revenue] - [Cost]

    measure 'Margin %' =
        DIVIDE(
            [Profit],
            [Revenue]
        )
```

### 9. Suggested report pages

#### Executive Summary

- Revenue
- Cost
- Profit
- Margin percentage

#### Sales Analysis

- Revenue by product
- Revenue by region
- Revenue trend

#### Customer Analysis

- Revenue by customer
- Top customers
- Customer count

#### Data Quality and Anomalies

- Negative-profit products
- Low-revenue, high-cost products
- Unit-sales outliers

### 10. Suggested Git history

```text
Initial PBIP project
Added FactSales and dimensions
Added revenue and profit measures
Added Time Intelligence calculation group
Added anomaly-detection KPIs
Added report pages
```

---

## User

Can you save our conversation to an MD file that I can download?

---

## Notes

- `TMDL` is the abbreviation for **Tabular Model Definition Language**.
- `PBIP` refers to the **Power BI Project** format.
- The sample model intentionally includes unusual Product U, Product V, and Product W records so that the report can demonstrate anomaly and data-quality analysis.
