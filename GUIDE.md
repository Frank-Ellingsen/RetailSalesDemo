# Power BI PBIP + TMDL + Tabular Editor 3 Guide

## Purpose

This project is a learning sandbox for:

- Power BI Desktop
- Power BI Projects (PBIP)
- Semantic modeling
- Star schema design
- DAX
- Tabular Editor 3
- TMDL (Tabular Model Definition Language)
- Git source control

The goal is to treat Power BI development like software development.

## Architecture Overview

```text
CSV files
    -> Power Query
    -> Semantic model
    -> Relationships
    -> Measures
    -> Report visuals
    -> PBIP
    -> Git
```

## Project Structure

```text
RetailSalesDemo.pbip
|
+-- Data
|   +-- FactSales.csv
|   +-- DimCustomer.txt
|   +-- DimDate.txt
|   +-- DimProduct.txt
|   +-- DimRegion.txt
|
+-- RetailSalesDemo.Report
|
+-- RetailSalesDemo.SemanticModel
```

## PBIP Structure Explained

### Report folder

```text
RetailSalesDemo.Report
```

Contains report pages, visual definitions, theme settings, bookmarks, and report layout.

Think of this as the report front end.

### Semantic model folder

```text
RetailSalesDemo.SemanticModel
```

Contains tables, relationships, measures, and model metadata.

Think of this as the analytical back end.

## TMDL Files

Location:

```text
RetailSalesDemo.SemanticModel\definition
```

Main files:

```text
database.tmdl
model.tmdl
relationships.tmdl
```

Table definitions:

```text
tables
+-- FactSales.tmdl
+-- DimCustomer.tmdl
+-- DimDate.tmdl
+-- DimProduct.tmdl
+-- DimRegion.tmdl
+-- _MEASURES.tmdl
```

## Current Model

```text
                DimDate
                   |
                   |
DimProduct ---- FactSales ---- DimRegion
                   |
                   |
              DimCustomer
```

## Table Purposes

### FactSales

Stores transactions:

```text
SalesKey
Date
ProductKey
RegionKey
CustomerKey
Revenue
Cost
UnitsSold
```

### DimDate

Provides date intelligence. Example columns:

```text
Date
Year
Quarter
Month
Month Number
Weekday
```

### DimProduct

Stores product attributes:

```text
ProductKey
ProductName
Category
SubCategory
Status
```

### DimRegion

Stores geographic and management attributes:

```text
RegionKey
RegionName
Country
SalesManager
```

### DimCustomer

Stores customer attributes:

```text
CustomerKey
CustomerID
Segment
City
```

## Relationships

Use one-to-many relationships with single-direction filtering from each dimension to `FactSales`:

```text
DimDate[Date]              1 --> * FactSales[Date]
DimProduct[ProductKey]     1 --> * FactSales[ProductKey]
DimRegion[RegionKey]       1 --> * FactSales[RegionKey]
DimCustomer[CustomerKey]   1 --> * FactSales[CustomerKey]
```

Before creating relationships, confirm that every dimension key is unique and contains no blanks.

## Why Use `_MEASURES`

Instead of scattering measures across data tables, use a dedicated measure table:

```text
_MEASURES
```

Benefits:

- Cleaner model organization
- Easier maintenance
- Consistent display folders
- Easier measure discovery
- Better separation between columns and calculations

## Creating Measures in Tabular Editor 3

Open Tabular Editor 3 from Power BI Desktop:

```text
External Tools > Tabular Editor 3
```

Open the C# scripting pane, commonly called **Advanced Scripting**, and run scripts with `F5`.

### Add one measure with C#

```csharp
var tbl = Model.Tables["_MEASURES"];

tbl.AddMeasure(
    "Total Revenue",
    "SUM(FactSales[Revenue])",
    "Revenue"
);
```

The parameters are:

```text
Measure name
DAX expression
Display folder
```

### Add multiple measures

```csharp
var tbl = Model.Tables["_MEASURES"];

tbl.AddMeasure(
    "Total Revenue",
    "SUM(FactSales[Revenue])",
    "Revenue"
);

tbl.AddMeasure(
    "Total Cost",
    "SUM(FactSales[Cost])",
    "Costs"
);

tbl.AddMeasure(
    "Total Units",
    "SUM(FactSales[UnitsSold])",
    "Volume"
);

tbl.AddMeasure(
    "Profit",
    "[Total Revenue] - [Total Cost]",
    "Profitability"
);

tbl.AddMeasure(
    "Profit Margin %",
    "DIVIDE([Profit], [Total Revenue])",
    "Profitability"
);
```

### Add properties while creating a measure

```csharp
var tbl = Model.Tables["_MEASURES"];

var measure = tbl.AddMeasure(
    "Total Revenue",
    "SUM(FactSales[Revenue])",
    "Revenue"
);

measure.FormatString = "#,##0.00";
measure.Description = "Total sales revenue in the current filter context.";
```

## Display Folders

Display folders organize measures without changing DAX behavior.

Example structure:

```text
_MEASURES
+-- Revenue
|   +-- Total Revenue
|
+-- Costs
|   +-- Total Cost
|
+-- Volume
|   +-- Total Units
|
+-- Profitability
    +-- Profit
    +-- Profit Margin %
```

The third argument passed to `AddMeasure()` sets the display folder:

```csharp
tbl.AddMeasure(
    "Total Revenue",
    "SUM(FactSales[Revenue])",
    "Revenue"
);
```

## Core Measures

### Total Revenue

```DAX
Total Revenue =
SUM ( FactSales[Revenue] )
```

### Total Cost

```DAX
Total Cost =
SUM ( FactSales[Cost] )
```

### Total Units

```DAX
Total Units =
SUM ( FactSales[UnitsSold] )
```

### Profit

```DAX
Profit =
[Total Revenue] - [Total Cost]
```

### Profit Margin %

```DAX
Profit Margin % =
DIVIDE ( [Profit], [Total Revenue] )
```

### Customer Count

```DAX
Customer Count =
DISTINCTCOUNT ( FactSales[CustomerKey] )
```

### Revenue per Customer

```DAX
Revenue per Customer =
DIVIDE ( [Total Revenue], [Customer Count] )
```

## Formatting Measures

### Number formatting

```csharp
Model.AllMeasures["Total Revenue"].FormatString = "#,##0.00";
Model.AllMeasures["Total Cost"].FormatString = "#,##0.00";
Model.AllMeasures["Profit"].FormatString = "#,##0.00";
Model.AllMeasures["Total Units"].FormatString = "#,##0";
Model.AllMeasures["Customer Count"].FormatString = "#,##0";
```

### Percentage formatting

```csharp
Model.AllMeasures["Profit Margin %"].FormatString = "0.00%";
```

Use a currency format string that matches the reporting requirements and report locale.

## SWITCH Logic

### Profitability Band

```DAX
Profitability Band =
SWITCH (
    TRUE (),
    [Profit Margin %] < 0, "Loss",
    [Profit Margin %] < 0.10, "Low Margin",
    [Profit Margin %] < 0.25, "Medium Margin",
    "High Margin"
)
```

Create the measure through C# scripting:

```csharp
var tbl = Model.Tables["_MEASURES"];

tbl.AddMeasure(
    "Profitability Band",
    @"SWITCH(
        TRUE(),
        [Profit Margin %] < 0, ""Loss"",
        [Profit Margin %] < 0.10, ""Low Margin"",
        [Profit Margin %] < 0.25, ""Medium Margin"",
        ""High Margin""
    )",
    "Profitability"
);
```

### Profit KPI

```DAX
Profit KPI =
SWITCH (
    TRUE (),
    [Profit] < 0, -1,
    [Profit Margin %] < 0.10, 0,
    1
)
```

C# script:

```csharp
var tbl = Model.Tables["_MEASURES"];

tbl.AddMeasure(
    "Profit KPI",
    @"SWITCH(
        TRUE(),
        [Profit] < 0, -1,
        [Profit Margin %] < 0.10, 0,
        1
    )",
    "Profitability"
);
```

Text-returning measures work well in cards, conditional titles, and tooltips. A measure does not provide a reusable categorical column for a chart axis.

## Time Intelligence Roadmap

Time-intelligence measures depend on a valid date table and an active relationship between `DimDate[Date]` and `FactSales[Date]`.

Potential future measures:

```text
Revenue YTD
Revenue MTD
Revenue Previous Year
Revenue YoY
Revenue YoY %
```

Example:

```DAX
Revenue YTD =
TOTALYTD (
    [Total Revenue],
    DimDate[Date]
)
```

```DAX
Revenue Previous Year =
CALCULATE (
    [Total Revenue],
    SAMEPERIODLASTYEAR ( DimDate[Date] )
)
```

```DAX
Revenue YoY =
[Total Revenue] - [Revenue Previous Year]
```

```DAX
Revenue YoY % =
DIVIDE (
    [Revenue YoY],
    [Revenue Previous Year]
)
```

The current demo data covers a short period in 2023, so previous-year measures will return blank until comparable prior-year data exists.

## TMDL Editing

Measures appear inside the `_MEASURES` table definition, typically:

```text
RetailSalesDemo.SemanticModel\definition\tables\_MEASURES.tmdl
```

A measure may look similar to:

```tmdl
measure 'Total Revenue' =
    SUM ( FactSales[Revenue] )
    formatString: #,##0.00
    displayFolder: Revenue
```

Use the generated TMDL files to inspect model changes and review Git diffs.

## What to Edit Where

### Prefer Power BI Desktop for

- Power Query transformations
- Data source configuration
- Report pages
- Visual creation and placement
- Themes
- Bookmarks
- Slicers and visual interactions
- Basic relationship management while learning

### Prefer Tabular Editor 3 for

- Measures
- Display folders
- Descriptions
- Format strings
- Hidden properties
- Calculation groups
- Perspectives
- Best Practice Analyzer
- Bulk model changes

### Prefer VS Code and TMDL for

- Reviewing semantic-model source
- Comparing Git changes
- Carefully editing known model properties
- Resolving simple source-control conflicts
- Searching across all model definitions

## Editing Risk Levels

### Lower risk

- Measure expressions
- Measure descriptions
- Measure display folders
- Measure format strings
- Column descriptions
- Hidden properties

### Use caution

- `relationships.tmdl`
- `model.tmdl`
- Data source expressions
- Partitions
- Report visual JSON
- Page and visual identifiers

Before manually editing TMDL or report JSON:

1. Commit the current working version.
2. Close Power BI Desktop if file locking or synchronization is a concern.
3. Make one small change.
4. Reopen the PBIP project.
5. Confirm that the model loads.
6. Review `git diff`.

## Theme Tweaking

A custom theme can be created or imported in Power BI Desktop and stored with the report definition.

Recommended workflow:

1. Make theme changes in Power BI Desktop.
2. Save the PBIP project.
3. Review changes inside `RetailSalesDemo.Report`.
4. Commit the theme separately from unrelated semantic-model changes.
5. Use manual report-definition editing only after creating a Git restore point.

## Git Workflow

### Inspect repository state

```powershell
git status
```

### Review changes

```powershell
git diff
```

### Stage changes

```powershell
git add .
```

### Commit changes

```powershell
git commit -m "Add core sales measures"
```

### Push changes

```powershell
git push
```

### Show the Windows directory tree from PowerShell

```powershell
cmd /c tree /F
```

## Suggested Commit Strategy

```text
Initialize PBIP project
Import fact and dimension tables
Add star schema relationships
Add dedicated measure table
Add core sales measures
Add profitability SWITCH measures
Add report theme
Build executive overview page
Add time-intelligence measures
Apply semantic-model best practices
```

Keep semantic-model, report-layout, and theme changes in separate commits when practical. Smaller commits make Git diffs easier to understand and reverse.

## First Report Page

Suggested page name:

```text
Executive Overview
```

Recommended cards:

```text
Total Revenue
Profit
Profit Margin %
Customer Count
```

Recommended charts:

```text
Revenue by Product
Revenue by Region
Revenue by Date
Profit by Product
```

Recommended slicers:

```text
Region
Product Category
Customer Segment
Date
```

Use explicit measures for numeric visual values instead of implicit aggregation of fact-table columns.

## Best Practice Analyzer

Run Best Practice Analyzer in Tabular Editor 3 and review findings such as:

- Missing descriptions
- Missing format strings
- Visible technical key columns
- Inconsistent naming
- Unused columns
- Potential model-design problems

Treat analyzer findings as review items. Understand each recommendation before applying bulk changes.

## Recommended Learning Progression

### Phase 1: Foundation

- Import source data
- Configure data types
- Build a star schema
- Create and mark `DimDate`
- Save as PBIP
- Commit and push to Git

### Phase 2: Measures

- Create `_MEASURES`
- Add core measures
- Add display folders
- Add descriptions
- Add format strings
- Review generated TMDL

### Phase 3: DAX context

- Learn filter context
- Learn row context
- Learn `CALCULATE`
- Learn `FILTER`
- Learn `REMOVEFILTERS`
- Learn `DIVIDE`
- Learn `SWITCH(TRUE())`

### Phase 4: Time intelligence

- Validate the date relationship
- Add YTD and MTD
- Add prior-period measures
- Add variance measures
- Add percentage variance measures

### Phase 5: Advanced semantic modeling

- Best Practice Analyzer
- Calculation groups
- Dynamic format strings
- Perspectives
- Field parameters
- Dynamic measure selection

### Phase 6: Report development

- Create overview page
- Apply the theme
- Add drill-through
- Add tooltips
- Add conditional formatting
- Test filter interactions

## Troubleshooting Checklist

### A measure does not appear

1. Confirm that the C# script ran successfully.
2. Expand `_MEASURES` in Tabular Editor 3.
3. Save changes in Tabular Editor 3.
4. Return to Power BI Desktop.
5. Refresh the Fields or Data pane if required.
6. Save the PBIP project.

### A measure references another missing measure

Create base measures first:

```text
Total Revenue
Total Cost
Total Units
```

Then create dependent measures:

```text
Profit
Profit Margin %
Revenue per Customer
```

### A relationship cannot be created as one-to-many

Check the dimension key for:

- Duplicates
- Blank values
- Incorrect data type
- Text-versus-number mismatch

### A time-intelligence measure returns blank

Check:

- `DimDate` contains the required date range
- `DimDate[Date]` has Date data type
- `FactSales[Date]` has Date data type
- The relationship is active
- The date table is marked correctly
- Comparable prior-period data actually exists

### Power BI reports an invalid project change

1. Use `git diff` to identify the last manual edit.
2. Revert or correct that edit.
3. Validate brackets, indentation, object names, and quoting.
4. Reopen the `.pbip` file.
5. Prefer TE3 or Power BI Desktop for the change if the format is unclear.

## Working Routine

Use this routine for each meaningful change:

```text
1. Pull the latest Git changes
2. Open RetailSalesDemo.pbip
3. Make one focused model or report change
4. Save in Tabular Editor 3 when applicable
5. Save in Power BI Desktop
6. Close or reload if required
7. Run git status
8. Review git diff
9. Reopen and validate the project
10. Commit with a focused message
11. Push to GitHub
```

## Final Goal

Understand how these components work together:

```text
Power BI Desktop
+
Power Query
+
Star schema
+
DAX
+
Tabular Editor 3
+
TMDL
+
PBIP
+
Git
```

The intended result is a source-controlled semantic model and report that can be inspected, compared, reviewed, and developed more like a software project than a single binary report file.
