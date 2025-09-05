# CiteFocus App

CiteFocus is a Streamlit-based web application designed for analyzing academic publications. It leverages data from uploaded CSV/Excel files and the Open API to provide insights into titles, authors, institutions, and concepts through interactive visualizations like bar charts, treemaps, and line charts. Users can upload datasets, search for specific keywords, and explore citation trends, author rankings, and concept distributions.

## Features
- **File Upload**: Upload CSV or Excel files containing publication data (e.g., titles, authors, citations).
- **Keyword Search**: Filter uploaded data by keywords in titles or other columns.
- **Open API Integration**: Fetch publication data based on title searches using the Open API.
- **Data Analysis**:
  - Author rankings by citations and number of papers.
  - Institution rankings by citations and number of papers.
  - Concept frequency analysis.
- **Visualizations**:
  - Bar charts for top authors and institutions by citations.
  - Treemap for citation distribution by author.
  - Line chart for citation trends over time.
  - Stacked bar chart for citations by year and author.
  - Bar chart for top concepts by frequency.
- **Interactive UI**: Clean, responsive Streamlit interface with customizable styles and real-time feedback.

## Installation

### Prerequisites
- Python 3.8 or higher
- Internet connection for Open API access
- No API key required for Open(public API, but rate limits apply)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/citefocus.git
   cd citefocus
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Requirements
The following dependencies are listed in `requirements.txt`:
- streamlit==1.25.0
- requests==2.31.0
- pandas==2.0.3
- plotly==5.15.0
- openpyxl==3.1.2

## Usage
1. **Launch the App**:
   - Run `streamlit run app.py` and open the local URL (e.g., `http://localhost:8501`) in your browser.
2. **Upload a File**:
   - Upload a CSV or Excel file with publication data (expected columns: `Title`, `Author`, `Year`, `Citations`, etc.).
3. **Search Keywords**:
   - Enter keywords (e.g., "machine learning") to filter matching rows from the uploaded file.
4. **Search with Open api**:
   - Enter a publication title (e.g., "Deep Learning for NLP") to fetch data from the Open API.
5. **View Results**:
   - Preview uploaded file data in a table.
   - Explore filtered data from keyword searches.
   - Analyze  data with tables and visualizations for:
     - Top authors by citations (bar chart and table).
     - Top institutions by citations (bar chart and table).
     - Citation distribution by author (treemap).
     - Citation trends over time (line chart).
     - Citations by year and author (stacked bar chart).
     - Top concepts by frequency (bar chart and table).
6. **Interact with Visualizations**:
   - Hover over charts for details or adjust views using Plotly’s interactive features.

## Example
- **Input**: Upload a CSV with columns: `Title`, `Author`, `Year`, `Citations`.
- **Keyword Search**: Search for "machine learning" to filter relevant publications.
   Search**: Enter "Deep Learning for NLP" to fetch related data.
- **Output**:
  - **Table**: Extracted data (titles, authors, institutions, citations, concepts).
  - **Author Rankings**: Bar chart showing top authors by citations.
  - **Institution Rankings**: Bar chart of top institutions by citations.
  - **Citation Trends**: Line chart showing citations over years.
  - **Citation Distribution**: Treemap of citations by author.
  - **Concepts**: Bar chart of top concepts (e.g., "machine learning", "NLP").
- **Example Insight**: "Author X has 500 citations across 10 papers, with 'machine learning' as the top concept."

## Project Structure
```
citefocus/
├── data/
│   └── sample_data.csv  # Sample dataset (not included in repo)
├── app.py               # Main Streamlit application
├── requirements.txt     # Dependencies
├── README.md            # This file
└── LICENSE              # MIT License file
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a Pull Request on GitHub.

**Ideas for Improvement**:
- Add support for additional file formats (e.g., JSON).
- Enhance visualizations with more interactive features (e.g., filters).
- Integrate other academic APIs (e.g., Semantic Scholar).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For issues or suggestions, open an issue on GitHub or email vaswal919@gmail.com
