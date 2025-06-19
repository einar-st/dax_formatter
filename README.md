# DAX Formatter

A command-line tool to format DAX (Data Analysis Expressions) code using the [daxformatter.com](https://www.daxformatter.com) API service.

## What is DAX?

DAX (Data Analysis Expressions) is a formula language used in Microsoft Power BI, SQL Server Analysis Services, and Power Pivot in Excel. It's designed to work with tabular data and provides functions for creating calculated columns, measures, and custom tables.

## Installation

### Using uv for quick one-line installation
```bash
uv tool install git+https://github.com/einar-st/dax_formatter.git
```

## Usage

The `daxfmt` command reads DAX code from stdin and outputs the formatted version to stdout.

### Basic usage

```bash
echo "CALCULATE(SUM(Sales[Amount]),FILTER(Sales,Sales[Date]>TODAY()-30))" | daxfmt
```

### Format a file

```bash
daxfmt < your_dax_file.dax
```

### Format and save to a new file

```bash
daxfmt < input.dax > formatted_output.dax
```

### Example

**Input DAX:**
```
CALCULATE(SUM(Sales[Amount]),FILTER(Sales,Sales[Date]>TODAY()-30))
```

**Output:**
```
CALCULATE (
    SUM ( Sales[Amount] ),
    FILTER (
        Sales,
        Sales[Date] > TODAY () - 30
    )
)
```

## Requirements

- Python 3.13 or higher
- Internet connection (to access daxformatter.com)

## Dependencies

- `beautifulsoup4` - For parsing HTML responses
- `requests` - For making HTTP requests
- `ruff` - For code formatting and linting

## How it works

This tool sends your DAX code to the daxformatter.com API service via HTTP POST request and returns the formatted result. The service handles the actual DAX formatting logic.

## License

See [LICENSE](LICENSE) file for details.
