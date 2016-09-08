from setuptools import setup, find_packages

import ajax_upload


setup(
    name='django-ajax-upload-widget',
    packages=find_packages(exclude=['example']),
    include_package_data=True,
    zip_safe=False,  # Because of static and template files
    version=ajax_upload.__version__,
    description=ajax_upload.__doc__,
    long_description=open('README.rst').read(),
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
    author='Domin Morales',
    url='http://github.com/kal3ls/django-ajax-upload-widget',
    license='BSD',
)
