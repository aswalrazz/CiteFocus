import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Streamlit App Configuration
st.set_page_config(page_title="📊 CiteFocus App", layout="wide")

# Streamlit App Title
st.markdown("""
<style>
.title { font-size: 30px !important; font-weight: bold; color: #2c3e50; }
.subtitle { font-size: 14px !important; color: #16a085; }
.note { font-size: 14px !important; color: #34495e; }
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="title">📚 Welcome to CiteFocus App!</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Analyze Titles, Authors, Institutions, and Concepts.</p>', unsafe_allow_html=True)

# User File Upload
uploaded_file = st.file_uploader("📂 Upload your Excel or CSV file:", type=["csv", "xlsx"])
data_from_file = pd.DataFrame()

# If a file is uploaded, read it into a DataFrame
if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            data_from_file = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            data_from_file = pd.read_excel(uploaded_file)
        st.success(f"✅ Successfully uploaded: {uploaded_file.name}")
        st.markdown("### 📄 Preview of Uploaded File")
        st.dataframe(data_from_file.head(), use_container_width=True)
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")

# User Input for Search (Title from Uploaded File)
st.markdown('<p class="note">🔎 Search for relevant keywords from a title in the file uploaded above :</p>', unsafe_allow_html=True)
search_query = st.text_input("Enter the relevant keywords:", placeholder="Type your title here...")

# Display Matching Data from Uploaded File
if not data_from_file.empty and search_query:
    matching_data = data_from_file[data_from_file.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
    if not matching_data.empty:
        st.markdown("### 🔍 Matching Data from Uploaded File")
        st.dataframe(matching_data, use_container_width=True)
    else:
        st.warning("⚠️ No matching data found in the uploaded file.")

# Existing Functionality for OpenAlex API
def fetch_data_from_openalex(search_query):
    base_url = "https://api.openalex.org/works?"
    query_param = f"filter=title.search:{search_query}"
    url = base_url + query_param
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        st.error("❌ Failed to fetch data from OpenAlex API.")
        return []

# Extract and Analyze Relevant Data
def extract_and_analyze_data(data):
    extracted_data = []
    author_data = {}
    institution_data = {}
    concepts_counter = {}

    for item in data:
        title = item.get("title", "Unknown Title")
        year = item.get("publication_year", 0)
        cited_by_count = item.get("cited_by_count", 0)
        authorships = item.get("authorships", [])
        concepts = [concept["display_name"] for concept in item.get("concepts", [])]

        for concept in concepts:
            concepts_counter[concept] = concepts_counter.get(concept, 0) + 1

        for author_entry in authorships:
            author = author_entry.get("author", {})
            author_name = author.get("display_name", "Unknown Author")
            institutions = [inst.get("display_name", "Unknown Institution") for inst in author_entry.get("institutions", [])]

            # Update Author Data
            if author_name not in author_data:
                author_data[author_name] = {"Citations": 0, "Papers": 0}
            author_data[author_name]["Citations"] += cited_by_count
            author_data[author_name]["Papers"] += 1

            # Update Institution Data
            for inst in institutions:
                if inst not in institution_data:
                    institution_data[inst] = {"Citations": 0, "Papers": 0}
                institution_data[inst]["Citations"] += cited_by_count
                institution_data[inst]["Papers"] += 1

            extracted_data.append({
                "Title": title,
                "Year": year,
                "Author Name": author_name,
                "Institution": ", ".join(institutions),
                "Citations": cited_by_count,
                "Category": ", ".join(concepts),
            })

    return create_dataframes(extracted_data, author_data, institution_data, concepts_counter)

def create_dataframes(extracted_data, author_data, institution_data, concepts_counter):
    # Convert Author and Institution Metrics to DataFrames
    author_df = pd.DataFrame([{
        "Author Name": author,
        "Citations": info["Citations"],
        "Papers": info["Papers"],
        "Avg Citations/Paper": round(info["Citations"] / info["Papers"], 2) if info["Papers"] > 0 else 0,
    } for author, info in author_data.items()]).sort_values(by="Citations", ascending=False).reset_index(drop=True)

    author_df.insert(0, "Rank", range(1, len(author_df) + 1))

    institution_df = pd.DataFrame([{
        "Institution": inst,
        "Citations": info["Citations"],
        "Papers": info["Papers"],
        "Avg Citations/Paper": round(info["Citations"] / info["Papers"], 2) if info["Papers"] > 0 else 0,
    } for inst, info in institution_data.items()]).sort_values(by="Citations", ascending=False).reset_index(drop=True)

    institution_df.insert(0, "Rank", range(1, len(institution_df) + 1))

    return pd.DataFrame(extracted_data), author_df, institution_df, concepts_counter

# Visualization Functions
def plot_author_performance(author_df):
    fig = px.bar(author_df.head(10), x='Author Name', y='Citations', color='Citations',
                 title='Top 10 Authors by Citations', text='Citations')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(yaxis_title='Total Citations', xaxis_title='Authors')
    st.plotly_chart(fig)

def plot_citation_distribution(author_df):
    fig = px.treemap(author_df, path=['Author Name'], values='Citations',
                      title='Citations Distribution by Author')
    st.plotly_chart(fig)

def plot_citation_trends(trend_df):
    fig = px.line(trend_df, x='Year', y='Citations', title='Total Citations Over Years', markers=True)
    st.plotly_chart(fig)

def plot_citation_scatter(extracted_df):
    scatter_df = extracted_df.groupby(['Year', 'Author Name'])['Citations'].sum().reset_index()
    fig = px.bar(scatter_df, x='Year', y='Citations', color='Author Name',
                 title='Total Citations by Year (Stacked Bar Chart)', text='Citations')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    st.plotly_chart(fig)

def plot_institution_performance(institution_df):
    fig = px.bar(institution_df.head(10), x='Institution', y='Citations', color='Institution',
                 title='Top Institutions by Citations', text='Citations')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(yaxis_title='Total Citations', xaxis_title='Institutions')
    st.plotly_chart(fig)

# Proceed with OpenAlex API if the user clicks the button
if st.button("🚀 Search With DataSparkLabs"):
    if search_query:
        st.markdown(f'<p class="note">🔄 Fetching data for Title: <b>{search_query}</b></p>', unsafe_allow_html=True)
        data = fetch_data_from_openalex(search_query)

        if data:
            extracted_df, author_df, institution_df, concepts_counter = extract_and_analyze_data(data)

            # Display Extracted Data
            st.subheader("📑 Extracted Data")
            st.dataframe(extracted_df, use_container_width=True)

            # Author Rankings Visualization
            st.subheader("👩‍🔬 Top Authors by Citations")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.dataframe(author_df.head(20), use_container_width=True)
            with col2:
                plot_author_performance(author_df)

            # Citation Distribution Visualization (Treemap)
            st.subheader("📊 Citations Distribution by Author")
            plot_citation_distribution(author_df)

            # Citation Trends Visualization (Line Chart)
            st.subheader("🕰️ Total Citations Over Years")
            trend_df = extracted_df.groupby("Year")["Citations"].sum().reset_index()
            plot_citation_trends(trend_df)

            # Stacked Bar Chart of Citations by Year and Author
            st.subheader("🔍 Total Citations by Year")
            plot_citation_scatter(extracted_df)

            # Institution Rankings Visualization
            st.subheader("🏢 Top Institutions by Citations")
            col3, col4 = st.columns([1, 1])
            with col3:
                st.dataframe(institution_df.head(20), use_container_width=True)
            with col4:
                plot_institution_performance(institution_df)

            # Concepts/Category Distribution
            st.subheader("🧠 Concepts Distribution")
            concepts_df = pd.DataFrame([{"Concept": concept, "Frequency": freq} for concept, freq in concepts_counter.items()])
            concepts_df.sort_values(by="Frequency", ascending=False, inplace=True)
            
            st.dataframe(concepts_df.head(20), use_container_width=True)
            
            fig_concepts = px.bar(concepts_df.head(10), x="Concept", y="Frequency", color="Frequency",
                                  title="Top Concepts by Frequency", text="Frequency")
            st.plotly_chart(fig_concepts)

        else:
            st.warning("⚠️ No data found for the given title!")
    
    else:
        st.error("❌ Please enter a title to search!")
