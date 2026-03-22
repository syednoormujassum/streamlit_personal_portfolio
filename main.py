import streamlit as st
st.set_page_config(page_title="Syed Portfolio", page_icon="✨",
                   layout='wide',initial_sidebar_state="expanded" )
#st.set_page_config(page_title="My Web App", page_icon="🌐",layout='wide')
st.title("Syed Noor Mujassum – Data | AI | Engineering")

st.write("**Email:** " \
        "syednoormujassum@gmail.com")
col1,col2=st.columns(2)
with col1:
    st.link_button(label="🔗 Github",url="https://github.com/syednoormujassum")

with col2:
    st.link_button(label="ℹ️ LinkedIn",url="https://www.linkedin.com/in/syed-noor-mujassum-53b501106/")
if "page" not in st.session_state:
    st.session_state.page="home"

tab1,tab2=st.tabs(["About","Projects"])
st.divider()
with tab1:
    
    st.write("I am **Syed Noor Mujassum**, a Senior Data Engineer working with one of North America’s leading financial institutions.\n\n"\
            "With over 3+ years of experience in the data engineering space, I have built and maintained robust, scalable data solutions that power critical business operations and analytics."\
            "\n\nMy expertise lies in designing end-to-end data pipelines, optimizing data processing frameworks, and ensuring high data quality and reliability across large-scale systems. I have hands-on experience working with both traditional enterprise systems and modern big data platforms, allowing me to bridge legacy and cloud-based architectures effectively."\
            "\n\n I am passionate about solving complex data problems, improving system efficiency, and enabling data-driven decision-making. I also have growing expertise in Artificial Intelligence, where I actively explore and build LLM-powered applications, combining data engineering with next-generation AI capabilities."\
            "\n\n Outside of work, I enjoy spending quality time with my family and continuously learning new technologies to stay ahead in this fast-evolving field.")
    
    import streamlit as st

# Core Expertise
    st.write(
    "**Core Expertise**\n\n"
    "1. Designing and building scalable ETL/ELT pipelines.\n"
    "2. Architecting data solutions for both batch and distributed systems.\n"
    "3. Working with big data ecosystems and cloud-based data platforms.\n"
    "4. Data processing, transformation, and performance optimization.\n"
    "5. Workflow orchestration and automation.\n"
    "6. Ensuring data quality, reliability, and system performance.\n"
    "7. Exploring AI/LLM integrations with data engineering platforms."
    )

# Tech Stack
    st.write(
    "**Tech Stack**\n\n"
    "1. **Programming & Scripting:**\n"
    "   * Python (data processing, automation, API integration)\n"
    "   * SQL (advanced queries, performance tuning, data modeling)\n"
    "   * Scala (distributed data processing, Spark applications)\n"
    "   * Shell Scripting & PowerShell (automation, job orchestration)\n\n"
    "2. **Data Engineering & Big Data:**\n"
    "   * Apache Spark (PySpark, Spark-Scala, distributed data processing)\n"
    "   * Hadoop Ecosystem (HDFS, Hive)\n\n"
    "3. **ETL Tools:** IBM DataStage (enterprise-grade data integration)\n\n"
    "4. **Workflow Orchestration:** Apache Airflow (DAGs, scheduling, monitoring)\n\n"
    "5. **Data Platforms & Warehousing:**\n"
    "   * Snowflake (cloud data warehousing, ELT pipelines, optimization)\n"
    "   * Experience with large-scale structured and semi-structured datasets\n\n"
    "6. **Enterprise & Legacy Systems:**\n"
    "   * IBM Mainframe (batch processing, legacy system integration)\n\n"
    "7. **Emerging Technologies:**\n"
    "   * LLM Applications (RAG pipelines, prompt engineering, AI workflows)\n"
    "   * Data + AI integration for intelligent, next-gen systems\n"
    "   * Claude Code"
    )
with tab2:
    st.markdown(
        """
        <p style="
            color: red;
            font-size: 24px;
            font-weight: bold;
            text-align: center;
        ">
        🚧 THIS TAB IS UNDER MAINTENANCE & SHALL BE UPDATED SHORTLY
        </p>
        """,
        unsafe_allow_html=True
    )