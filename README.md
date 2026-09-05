# Retail Sales Power BI Project Demo

A small, source-controlled Power BI learning project for practicing:

- Power BI Project (`.pbip`) development
- Star schema modeling
- Power Query imports
- DAX measures
- Tabular Editor 3
- Tabular Model Definition Language (TMDL)
- Git-based version control

The project uses a deliberately small retail sales dataset so the focus stays on model design, DAX, PBIP structure, and development workflow.

## Project Status

Initial data files are ready. The Power BI project, semantic model, relationships, measures, and report pages will be built incrementally.

## Repository Structure

Before creating the Power BI project, the repository starts with this structure:

```text
DAX/
├── README.md
├── power-bi-pbip-tmdl-conversation.md
└── Data/
    ├── DimCustomer.csv
    ├── DimDate.txt
    ├── DimProduct.csv
    ├── DimRegion.csv
    └── FactSales.csv
```

After saving the report as a Power BI Project, the expected structure is:

```text
DAX/
├── README.md
├── RetailSalesDemo.pbip
├── power-bi-pbip-tmdl-conversation.md
├── Data/
│   ├── DimCustomer.csv
│   ├── DimDate.txt
│   ├── DimProduct.csv
│   ├── DimRegion.csv
│   └── FactSales.csv
├── RetailSalesDemo.Report/
└── RetailSalesDemo.SemanticModel/
```

> Power BI Desktop creates the `.Report` and `.SemanticModel` folders when the report is saved using the Power BI Project format.

## Data Model

The intended model is a star schema with `FactSales` at the center.

```text
                    DimDate
                       |
                       |
DimProduct ------ FactSales ------ DimRegion
                       |
                       |
                  DimCustomer
```

### FactSales

The fact table contains one row per sales transaction.

| Column | Purpose |
|---|---|
| `SalesKey` | Unique transaction identifier |
| `Date` | Transaction date |
| `ProductKey` | Foreign key to `DimProduct` |
| `RegionKey` | Foreign key to `DimRegion` |
| `CustomerKey` | Foreign key to `DimCustomer` |
| `Revenue` | Sales revenue |
| `Cost` | Transaction cost |
| `UnitsSold` | Number of units sold |

### DimProduct

Contains product attributes such as product name, category, subcategory, launch year, and status.

### DimRegion

Contains region attributes such as region name, country, and sales manager.

### DimCustomer

Contains customer attributes such as customer ID, segment, and city.

### DimDate

Provides the calendar structure required for time-based analysis. It can be imported from the supplied text file or replaced with a calculated date table during the learning exercise.

## Relationships

Create the following one-to-many relationships with single-direction filtering from each dimension to the fact table:

```text
DimDate[Date]           1 --> * FactSales[Date]
DimProduct[ProductKey]  1 --> * FactSales[ProductKey]
DimRegion[RegionKey]    1 --> * FactSales[RegionKey]
DimCustomer[CustomerKey] 1 --> * FactSales[CustomerKey]
```

Before creating relationships, confirm that every dimension key is unique and contains no blank values.

## Getting Started

### 1. Open Power BI Desktop

Create a blank report.

### 2. Import the data tables

For each file:

1. Select **Home > Get data > Text/CSV**.
2. Select the file from the `Data` folder.
3. Choose **Transform Data** rather than loading immediately.
4. Rename each Power Query query to match its intended table name.
5. Verify column data types.

Import:

```text
FactSales.csv
DimProduct.csv
DimRegion.csv
DimCustomer.csv
```

Handle `DimDate.txt` separately after reviewing its delimiter and contents.

### 3. Verify FactSales data types

Use these data types in Power Query:

| Column | Data type |
|---|---|
| `SalesKey` | Whole Number |
| `Date` | Date |
| `ProductKey` | Whole Number |
| `RegionKey` | Whole Number |
| `CustomerKey` | Whole Number |
| `Revenue` | Decimal Number |
| `Cost` | Decimal Number |
| `UnitsSold` | Whole Number |

Dimension key columns should also use the **Whole Number** data type.

### 4. Load the tables

Select **Close & Apply** in Power Query.

### 5. Create relationships

Open Model view and connect the dimension keys to the matching foreign keys in `FactSales`.

Use:

- Cardinality: **One to many**
- Cross-filter direction: **Single**
- Active relationship: **Yes**

### 6. Configure the date table

After loading or creating `DimDate`:

1. Confirm that `DimDate[Date]` contains unique and continuous dates.
2. Select `DimDate`.
3. Use **Table tools > Mark as date table**.
4. Select the `Date` column.
5. Sort month names by the month-number column if both are available.

### 7. Save as a Power BI Project

Use **File > Save As** and select the Power BI Project format.

Suggested project name:

```text
RetailSalesDemo
```

Save it in the repository root, not inside the `Data` folder.

Expected entry point:

```text
RetailSalesDemo.pbip
```

## Starter Measures

Create measures in Tabular Editor 3 or Power BI Desktop.

```DAX
Total Revenue =
SUM ( FactSales[Revenue] )
```

```DAX
Total Cost =
SUM ( FactSales[Cost] )
```

```DAX
Total Units =
SUM ( FactSales[UnitsSold] )
```

```DAX
Profit =
[Total Revenue] - [Total Cost]
```

```DAX
Profit Margin % =
DIVIDE ( [Profit], [Total Revenue] )
```

```DAX
Customer Count =
DISTINCTCOUNT ( FactSales[CustomerKey] )
```

```DAX
Revenue per Customer =
DIVIDE ( [Total Revenue], [Customer Count] )
```

## Suggested Measure Folders

Organize measures with display folders:

```text
Revenue
├── Total Revenue
└── Revenue per Customer

Costs
└── Total Cost

Sales Volume
└── Total Units

Profitability
├── Profit
└── Profit Margin %

Customers
└── Customer Count
```

## Suggested First Report Page

Create a simple overview page with:

- Card: Total Revenue
- Card: Profit
- Card: Profit Margin %
- Card: Customer Count
- Column chart: Revenue by Product
- Bar chart: Revenue by Region
- Line chart: Revenue by Date
- Slicer: Product Category
- Slicer: Region
- Slicer: Customer Segment

Use measures for numeric visual values rather than implicit aggregation of fact-table columns.

## Tabular Editor 3 Workflow

Once the model has been loaded in Power BI Desktop:

1. Open **External Tools > Tabular Editor 3**.
2. Inspect tables, columns, measures, and relationships.
3. Add descriptions and display folders.
4. Apply measure format strings.
5. Save model changes.
6. Return to Power BI Desktop and save the PBIP project.
7. Review the resulting TMDL changes with Git.

Suggested formats:

| Measure | Format |
|---|---|
| Total Revenue | Currency |
| Total Cost | Currency |
| Profit | Currency |
| Profit Margin % | Percentage |
| Total Units | Whole Number |
| Customer Count | Whole Number |
| Revenue per Customer | Currency |

## Recommended Learning Sequence

1. Import and clean the source tables in Power Query.
2. Build and validate the star schema.
3. Save the model as a PBIP project.
4. Inspect the generated project folders and TMDL files.
5. Create explicit DAX measures.
6. Organize and format measures in Tabular Editor 3.
7. Build a small report page.
8. Run Best Practice Analyzer rules.
9. Review model changes in Git.
10. Add time-intelligence measures after the base model is stable.

## Git Workflow

Example initial commands:

```powershell
git init
git add .
git commit -m "Initialize retail sales Power BI demo"
```

After completing the star schema:

```powershell
git add .
git commit -m "Build initial retail sales star schema"
```

After adding the first measures:

```powershell
git add .
git commit -m "Add core sales and profitability measures"
```

To display the project tree from PowerShell using the Windows `tree` command:

```powershell
cmd /c tree /F
```

## Data Notes

The dataset is synthetic and intended for learning only. It includes a few intentionally unprofitable transactions, which are useful for practicing:

- Profit and margin calculations
- Conditional formatting
- Loss-making product analysis
- Filter context
- Exception reporting

## Learning Goals

By completing this demo, the goal is to understand how these layers work together:

```text
Source files
    -> Power Query
    -> Semantic model
    -> Star schema
    -> DAX measures
    -> Tabular Editor 3
    -> TMDL
    -> PBIP
    -> Git
    -> Power BI report
```

## License

This demo project and its synthetic data may be used for personal learning and experimentation.
