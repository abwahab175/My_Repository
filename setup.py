from setuptools import setup, find_packages

def get_requirements(file_path):

    with open(file_path,'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n",'')for req in requirements]
    return requirements


setup(

    name = "datasciencetestproject",
    version = "0.0.1",
    author = 'Abdul Wahab Memon',
    author_email = 'abwahab175@gmail.com',
    packages= find_packages(),
    install_requirements = get_requirements('requirements.txt')
)
