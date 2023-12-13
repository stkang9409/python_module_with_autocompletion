from setuptools import setup, find_packages

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        print("Please run 'source ~/.bashrc' or 'source ~/.zshrc' to complete the installation.")


setup(
    name='python_module_with_autocompletion',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pm=python_module_with_autocompletion.main:main',
        ],
    },
    # Add other necessary information here
    # your setup arguments here
    cmdclass={
        'install': PostInstallCommand,
    },
)
