CiteFocus App
 
Overview
CiteFocus is a Streamlit-based web application designed for analyzing academic publications by leveraging data from uploaded CSV/Excel files and the OpenAlex API. It provides insights into titles, authors, institutions, and concepts through interactive visualizations like bar charts, treemaps, and line charts. Users can upload datasets, search for specific keywords, and explore citation trends, author rankings, and concept distributions.
Features

File Upload: Upload CSV or Excel files to analyze publication data.
Keyword Search: Filter uploaded data by keywords in titles or other columns.
OpenAlex API Integration: Fetch publication data based on title searches.
Data Analysis:
Author rankings by citations and papers.
Institution rankings by citations and papers.
Concept frequency analysis.


Visualizations:
Bar charts for top authors and institutions by citations.
Treemap for citation distribution by author.
Line chart for citation trends over time.
Stacked bar chart for citations by year and author.
Bar chart for top concepts by frequency.


Interactive UI: Clean, responsive interface with customizable styles and real-time feedback.

Installation
Prerequisites

Python 3.8+
Internet connection for OpenAlex API access

Setup

Clone the repository:
git clone https://github.com/your-username/citefocus.git
cd citefocus


Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Run the application:
streamlit run app.py



Requirements
Create a requirements.txt file with the following:
streamlit==1.25.0
requests==2.31.0
pandas==2.0.3
plotly==5.15.0
openpyxl==3.1.2

Usage

Launch the App: Run streamlit run app.py and open the provided local URL (e.g., http://localhost:8501).
Upload a File: Upload a CSV or Excel file containing publication data (e.g., titles, authors, citations).
Search Keywords: Enter keywords to filter matching rows from the uploaded file.
Search with OpenAlex: Enter a title and click "Search With DataSparkLabs" to fetch data from the OpenAlex API.
View Results:
Preview uploaded file data.
Explore matching data based on keyword search.
Analyze OpenAlex data with tables and visualizations for authors, institutions, citation trends, and concepts.


Interact with Visualizations: Hover over charts for details or adjust the view as needed.

Example

Upload a CSV file with columns like Title, Author, Year, and Citations.
Search for a keyword (e.g., "machine learning") to filter matching rows.
Enter a title (e.g., "Deep Learning for NLP") and click "Search With DataSparkLabs".
View:
A table of extracted data (titles, authors, institutions, citations, concepts).
Top authors ranked by citations (bar chart and table).
Citation distribution (treemap).
Citation trends over years (line chart).
Stacked bar chart of citations by year and author.
Top institutions by citations (bar chart and table).
Top concepts by frequency (bar chart and table).



Screenshots
   
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For issues or suggestions, please open an issue on GitHub or contact your-email@example.com.
Acknowledgments

Powered by OpenAlex API for academic publication data.
Built with Streamlit and Plotly for interactive visualizations.
