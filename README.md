# 🏆 Nobel Prize Data Dashboard

[![CI Pipeline](https://github.com/YOUR_USERNAME/streamlit-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/streamlit-demo/actions/workflows/ci.yml)

An interactive data dashboard for exploring Nobel Prize winners from 1901 to 2025, built with Streamlit and featuring automated CI/CD.

## ✨ Features

- 📊 **Interactive Dashboard**: Filter and explore Nobel Prize data
- 🔍 **Advanced Filters**: Year range, category, gender, and country filters
- 📈 **Visualizations**: Charts showing trends, distributions, and geographic analysis
- 📥 **Data Export**: Download filtered data as CSV
- 🧪 **Tested**: Comprehensive test suite with pytest
- 🚀 **CI/CD Pipeline**: Automated testing and deployment with GitHub Actions

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/streamlit-demo.git
cd streamlit-demo

# 2. Create and activate virtual environment
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📊 Dashboard Sections

### Overview Metrics
- Total prizes awarded
- Unique laureates
- Countries represented
- Gender distribution

### Data Table
- Filterable data view
- Key information: Year, Name, Category, Country, Motivation
- Export functionality

### Statistical Analysis
- Prizes by category
- Top countries by laureate count
- Gender distribution over time
- Shared vs solo prizes

### Geographic Analysis
- Top 20 countries
- Category distribution by country

## 🧪 Running Tests

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=term

# Run specific test file
pytest tests/test_app.py -v
```

## 🔄 CI/CD Pipeline

The project uses GitHub Actions for continuous integration:

- ✅ Code linting with `ruff`
- ✅ Format checking with `black`
- ✅ Unit and integration tests with `pytest`
- ✅ Code coverage reporting
- ✅ Automated on every push and pull request

### Pipeline Status

All checks must pass before merging:
- Linting
- Formatting
- Tests (100% passing)
- Import checks

## 📁 Project Structure

```
streamlit-demo/
├── app.py                     # Main Streamlit application
├── data/
│   └── nobel_prizes_1901-2025_cleaned.csv
├── tests/
│   ├── __init__.py
│   ├── conftest.py           # Test fixtures
│   ├── test_app.py           # Unit tests
│   └── test_integration.py   # Integration tests
├── .github/
│   └── workflows/
│       └── ci.yml            # CI/CD pipeline
├── requirements.txt          # Production dependencies
├── requirements-dev.txt      # Development dependencies
└── README.md                 # This file
```

## 🛠️ Technologies

- **Framework**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly
- **Testing**: pytest, pytest-cov
- **Code Quality**: ruff, black
- **CI/CD**: GitHub Actions

## 📊 Data Source

The dataset contains Nobel Prize information from 1901 to 2025, including:
- Award year and category
- Laureate information (name, gender, birth country)
- Prize details (amount, sharing, motivation)
- Affiliation data

**Data Credit**: Nobel Prize dataset (publicly available data)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

All pull requests must pass CI checks:
- Tests must pass
- Code must be linted and formatted
- No breaking changes

## 📝 Development

```bash
# Format code
black app.py tests/

# Lint code
ruff check .

# Run tests with coverage
pytest --cov=. --cov-report=html
```

## 📄 License

See [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Nobel Prize dataset
- Streamlit community
- Open source contributors

---

**Built with ❤️ using Streamlit | Deployed with GitHub Actions**
