import streamlit as st

def main():
    st.title("Ali Haider - Python Developer")

    st.header("About me")
    st.write("Extremely motivated to constantly develop my skills and grow professionally. Wanted to become a part of a Leading Organization and fulfil my desire of acquiring knowledge and pleasure working with the Most  competent Professionals.")    
    
    st.header("Personal Information")
    st.write("Name: Ali Haider")
    st.write("Email: haideralyee46@gmail.com")
    st.write("Phone: 03049176147")
    st.write("[LinkedIn](linkedin.com/in/ali-haider46)")
    st.write("[GitHub](github.com/haideralyee)")
    
    st.header("Expertise")
    st.write("Programming languages:")
    st.write("  - Python")
    st.write("  - JavaScript")
    st.write(" Web development:")
    st.write("  - HTML")
    st.write("  - CSS")
    st.write("  - Django")
    st.write("  - DjangoRestFramework")
    st.write("  - Restful APIs")
    st.write("Version control:")
    st.write("  - Git")
    
    st.header("Education")
    st.write("UET Taxila")
    st.write("BS Electronics")
    st.write("2016-2020")
    
    
    st.header("Projects")
    project = st.selectbox("Select a project", ["FileBolt", "E-Commerce Store"])
    
    if project == "FileBolt":
        st.subheader("FileBolt:")
        st.write("“Elevate Your File Sharing with FileBolt.”")
        st.write("- Developed a web application using Django framework to facilitate seamless file management for users.")
        st.write("- Implemented a secure user authentication system to control access to file upload and download files uploaded from other users.")
        st.write("- Utilized Django’s built-in features for form handling and validation to enhance user input reliability.")
        st.write("- Utilized Django templates and views to render dynamic content and provide a cool user interface")
    
    elif project == "E-Commerce Store":
        st.subheader("E-Commerce Store:")
        st.write("“Your Gateway to Seamless E-Commerce”")
        st.write("- Developed a fully functional e-commerce platform using Django, showcasing a product line and seamless cart functionality")
        st.write("- Implemented a responsive user interface for the product list, ensuring an optimal user experience across devices.")
        st.write("- Integrated secure user authentication and authorization features to protect sensitive user information and manage access control.")
        st.write("- Implemented a robust cart system allowing users to add, remove, and update items, providing a smooth and intuitive shopping experience")

if __name__ == "__main__":
    main()
