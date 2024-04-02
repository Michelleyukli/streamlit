import streamlit as st

def create_section(header, markdown_content, divider_option='yellow'):
    st.header(f'{header}', divider=divider_option)
    st.markdown(markdown_content)

# Create two columns for the introduction
col1, col2 = st.columns(2)

with col1:
    st.image('WechatIMG719.jpeg', caption=None, width=250, channels='RGB', output_format='JPG')

with col2:
    st.title('Hi, I am Yulin :sunglasses:')
    st.header('I am a product designer based in Bellevue, WA')

education_content = '''**BFA in Product Design** @ Parsons School of Design  
**MS in Technology Innovation** @ University of Washington'''
create_section('Education :mortar_board:', education_content)

work_experience_content = '''**Product Design Intern** @ Icy Coffee in Jiangmen City, Guangdong, China  
**Industrial Designer** @ EASTERME in Shunde City'''
create_section('Work Experience :Design Experience:', work_experience_content)

hobbies_interests_content = '''Ultimate Frisbee :
Hand Pourover coffee:  
R&B Music Lover :'''
create_section('Hobbies & Interests :smiling_face_with_3_hearts:', hobbies_interests_content)

# Contact information
contact_info = '''**Email :** yli247@uw.edu  
**Phone :** +1 425 548 7548  
**Instagram :** Michelleyukli  '''
create_section('Contact me :e-mail: ', contact_info)


my_work = '''Check out my work below:'''
create_section('My work :ceramic: ', my_work)
st.image('egg.png', caption=None, width=180, channels='RGB', output_format='PNG')