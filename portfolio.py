import streamlit as st

st.set_page_config(page_title="Vijaykumar C | Data Engineer", layout="wide")

# Sidebar navigation
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["About Me", "Skills", "Projects", "Experience", "Achievements", "Contact"])

# About Me
with tab1:
    st.title("👋 About Me")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        I'm **Vijaykumar C**, a passionate and results-driven **Data Engineer** with over 5 years of experience in building scalable data solutions across cloud platforms.
        I specialize in:
        - **Snowflake** performance engineering and cost optimization
        - **ETL development** using Informatica, Databricks, and AWS DMS
        - **Data visualization** with Tableau and Streamlit
        - **Cloud-native data workflows** using AWS Lambda and S3 
        My mission is to transform raw data into actionable insights that drive business performance. I thrive in agile environments and enjoy solving complex data challenges with clean, efficient solutions.
        """)

    with col2:
        st.image("/Users/vijay/Downloads/photo.jpg", width=200, caption="Vijaykumar C")

# Skills
with tab2:
    st.title("🛠️ Skills")

# Create three columns for parallel layout
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 🚀 Core Data Engineering")
        st.markdown("""
     🧊 **Snowflake**
    - Advanced query optimization  
    - Cost reduction strategies (70%+)  
    - Data pipelines, tasks, procedures  
    - AWS integration (Lambda, S3, DMS)  
    - Event-driven workflows  

     🧮 **SQL**
    - Complex query writing  
    - Stored procedures & views  
    - Data validation & transformation  
    - MySQL, Oracle, BigQuery  
    """)

    with col2:
        st.markdown("#### 📈 Data Visualization")
        st.markdown("""
    - **Tableau**: Performance dashboards  
    - **Streamlit**: Incident tracking apps  
    """)

    with col3:
        st.markdown("#### ⚙️ DevOps & Version Control")
        st.markdown("""
    - **Jenkins**: Job automation  
    - **GitLab & Bitbucket**: CI/CD pipelines  
    - **Keystone**: Data replication orchestration  
    """)





# Projects
with tab3:
    st.title("📁 Projects")
    st.subheader("Snowflake Cost Optimization")
    st.write("Reduced daily compute costs by over 70% by identifying and restructuring high-credit-consuming queries and procedures.")
    
    st.subheader("Data Replication Pipelines")
    st.write("Built pipelines from Teradata and Kafka to Snowflake using Keystone and AWS S3. Migrated procedures for performance gains.")
    
    st.subheader("Incident Dashboard")
    st.write("Developed a Streamlit dashboard to insert/update incident details into Snowflake, enabling real-time tracking and suggestions.")

# Experience
with tab4:
    st.subheader("💼 Experience")

    col1, col2 = st.columns([4, 1])

    with col1:
        st.markdown("#### 📍 Infosys Limited")
        st.markdown("*Senior Associate Consultant*  \n🗓️ Jun 2022 – Present")
        st.markdown("""
- Led Snowflake performance engineering and cost optimization  
- Built data workflows using AWS Lambda and Snowflake tasks  
- Created Tableau dashboards for warehouse monitoring  
        """)
        st.markdown("<hr style='margin-top:5px;margin-bottom:5px;'>", unsafe_allow_html=True)

        st.markdown("#### 📍 Cognizant Technology Solutions")
        st.markdown("*Data Engineer*  \n🗓️ Apr 2020 – May 2022")
        st.markdown("""
- Managed Oracle to Snowflake replication using AWS DMS and Databricks  
- Automated ETL tasks and developed Spark jobs  
        """)
        st.markdown("<hr style='margin-top:5px;margin-bottom:5px;'>", unsafe_allow_html=True)

        st.markdown("#### 📍 Cognizant Technology Solutions")
        st.markdown("*Informatica Developer & Intern*  \n🗓️ 2019 – 2020")
        st.markdown("""
- Designed ETL mappings and workflows using Informatica PowerCenter  
- Assisted in client-based data transformation projects  
        """)

    with col2:
        st.empty()


# Achievements
with tab5:
    st.title("🏆 Achievements & Certifications")
    st.write("""
    - ⭐ Star Performer Award (Infosys)  
    - 🏅 Rookie of the Quarter (Infosys)  
    - 🙌 Client Appreciation for Snowflake performance  
    - 📜 Snowflake & Tableau Internal Certifications  
    - 🧠 SnowPro Certification (In Progress)  
    """)
    
# Contact Section
with tab6:
    st.title("📬 Contact Me")
    st.write("Feel free to reach out via the form below or connect with me on LinkedIn.")
    
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    
    if st.button("Send"):
        st.success("Thank you! Your message has been noted. Please email me directly at Vijaychoodesh@gmail.com for a faster response.")

    st.markdown("📧 **Email:** Vijaychoodesh@gmail.com")
    st.markdown("🔗 **LinkedIn:** linkedin.com/in/vijaykumar17")
