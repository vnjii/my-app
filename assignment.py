Last login: Mon Oct 30 10:38:54 on ttys000
Rodneys-MBP:~ rodneyvictornjii$ cd homebrew
-bash: cd: homebrew: No such file or directory
Rodneys-MBP:~ rodneyvictornjii$ clear




















Rodneys-MBP:~ rodneyvictornjii$ sudo easy_install pip
Password:
Searching for pip
Reading https://pypi.python.org/simple/pip/
Best match: pip 9.0.1
Downloading https://pypi.python.org/packages/11/b6/abcb525026a4be042b486df43905d6893fb04f05aac21c32c638e939e447/pip-9.0.1.tar.gz#md5=35f01da33009719497f01a4ba69d63c9
Processing pip-9.0.1.tar.gz
Writing /tmp/easy_install-LBk5sp/pip-9.0.1/setup.cfg
Running pip-9.0.1/setup.py -q bdist_egg --dist-dir /tmp/easy_install-LBk5sp/pip-9.0.1/egg-dist-tmp-lwOcKW
/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/dist.py:267: UserWarning: Unknown distribution option: 'python_requires'
  warnings.warn(msg)
warning: no previously-included files found matching '.coveragerc'
warning: no previously-included files found matching '.mailmap'
warning: no previously-included files found matching '.travis.yml'
warning: no previously-included files found matching '.landscape.yml'
warning: no previously-included files found matching 'pip/_vendor/Makefile'
warning: no previously-included files found matching 'tox.ini'
warning: no previously-included files found matching 'dev-requirements.txt'
warning: no previously-included files found matching 'appveyor.yml'
no previously-included directories found matching '.github'
no previously-included directories found matching '.travis'
no previously-included directories found matching 'docs/_build'
no previously-included directories found matching 'contrib'
no previously-included directories found matching 'tasks'
no previously-included directories found matching 'tests'
creating /Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg
Extracting pip-9.0.1-py2.7.egg to /Library/Python/2.7/site-packages
Adding pip 9.0.1 to easy-install.pth file
Installing pip script to /usr/local/bin
Installing pip2.7 script to /usr/local/bin
Installing pip2 script to /usr/local/bin

Installed /Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg
Processing dependencies for pip
Finished processing dependencies for pip
Rodneys-MBP:~ rodneyvictornjii$ pip install Django
Collecting Django
  Downloading Django-1.11.7-py2.py3-none-any.whl (6.9MB)
    100% |████████████████████████████████| 7.0MB 188kB/s
Requirement already satisfied: pytz in /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python (from Django)
Installing collected packages: Django
Exception:
Traceback (most recent call last):
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/basecommand.py", line 215, in main
    status = self.run(options, args)
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/commands/install.py", line 342, in run
    prefix=options.prefix_path,
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/req/req_set.py", line 784, in install
    **kwargs
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/req/req_install.py", line 851, in install
    self.move_wheel_files(self.source_dir, root=root, prefix=prefix)
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/req/req_install.py", line 1064, in move_wheel_files
    isolated=self.isolated,
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/wheel.py", line 345, in move_wheel_files
    clobber(source, lib_dir, True)
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/wheel.py", line 316, in clobber
    ensure_dir(destdir)
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/utils/__init__.py", line 83, in ensure_dir
    os.makedirs(path)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/os.py", line 157, in makedirs
    mkdir(name, mode)
OSError: [Errno 13] Permission denied: '/Library/Python/2.7/site-packages/django'
Rodneys-MBP:~ rodneyvictornjii$ pip list
DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.
altgraph (0.10.2)
bdist-mpkg (0.5.0)
bonjour-py (0.3)
macholib (1.5.1)
matplotlib (1.3.1)
modulegraph (0.10.4)
numpy (1.8.0rc1)
pip (9.0.1)
py2app (0.7.3)
pyobjc-core (2.5.1)
pyobjc-framework-Accounts (2.5.1)
pyobjc-framework-AddressBook (2.5.1)
pyobjc-framework-AppleScriptKit (2.5.1)
pyobjc-framework-AppleScriptObjC (2.5.1)
pyobjc-framework-Automator (2.5.1)
pyobjc-framework-CFNetwork (2.5.1)
pyobjc-framework-Cocoa (2.5.1)
pyobjc-framework-Collaboration (2.5.1)
pyobjc-framework-CoreData (2.5.1)
pyobjc-framework-CoreLocation (2.5.1)
pyobjc-framework-CoreText (2.5.1)
pyobjc-framework-DictionaryServices (2.5.1)
pyobjc-framework-EventKit (2.5.1)
pyobjc-framework-ExceptionHandling (2.5.1)
pyobjc-framework-FSEvents (2.5.1)
pyobjc-framework-InputMethodKit (2.5.1)
pyobjc-framework-InstallerPlugins (2.5.1)
pyobjc-framework-InstantMessage (2.5.1)
pyobjc-framework-LatentSemanticMapping (2.5.1)
pyobjc-framework-LaunchServices (2.5.1)
pyobjc-framework-Message (2.5.1)
pyobjc-framework-OpenDirectory (2.5.1)
pyobjc-framework-PreferencePanes (2.5.1)
pyobjc-framework-PubSub (2.5.1)
pyobjc-framework-QTKit (2.5.1)
pyobjc-framework-Quartz (2.5.1)
pyobjc-framework-ScreenSaver (2.5.1)
pyobjc-framework-ScriptingBridge (2.5.1)
pyobjc-framework-SearchKit (2.5.1)
pyobjc-framework-ServiceManagement (2.5.1)
pyobjc-framework-Social (2.5.1)
pyobjc-framework-SyncServices (2.5.1)
pyobjc-framework-SystemConfiguration (2.5.1)
pyobjc-framework-WebKit (2.5.1)
pyOpenSSL (0.13.1)
pyparsing (2.0.1)
python-dateutil (1.5)
pytz (2013.7)
scipy (0.13.0b1)
setuptools (18.5)
six (1.4.1)
xattr (0.6.4)
zope.interface (4.1.1)
Rodneys-MBP:~ rodneyvictornjii$ pip install Django
Collecting Django
  Using cached Django-1.11.7-py2.py3-none-any.whl
Requirement already satisfied: pytz in /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python (from Django)
Installing collected packages: Django
Exception:
Traceback (most recent call last):
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/basecommand.py", line 215, in main
    status = self.run(options, args)
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/commands/install.py", line 342, in run
    prefix=options.prefix_path,
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/req/req_set.py", line 784, in install
    **kwargs
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/req/req_install.py", line 851, in install
    self.move_wheel_files(self.source_dir, root=root, prefix=prefix)
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/req/req_install.py", line 1064, in move_wheel_files
    isolated=self.isolated,
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/wheel.py", line 345, in move_wheel_files
    clobber(source, lib_dir, True)
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/wheel.py", line 316, in clobber
    ensure_dir(destdir)
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/utils/__init__.py", line 83, in ensure_dir
    os.makedirs(path)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/os.py", line 157, in makedirs
    mkdir(name, mode)
OSError: [Errno 13] Permission denied: '/Library/Python/2.7/site-packages/django'
Rodneys-MBP:~ rodneyvictornjii$ pip freeze
altgraph==0.10.2
bdist-mpkg==0.5.0
bonjour-py==0.3
macholib==1.5.1
matplotlib==1.3.1
modulegraph==0.10.4
numpy==1.8.0rc1
py2app==0.7.3
pyobjc-core==2.5.1
pyobjc-framework-Accounts==2.5.1
pyobjc-framework-AddressBook==2.5.1
pyobjc-framework-AppleScriptKit==2.5.1
pyobjc-framework-AppleScriptObjC==2.5.1
pyobjc-framework-Automator==2.5.1
pyobjc-framework-CFNetwork==2.5.1
pyobjc-framework-Cocoa==2.5.1
pyobjc-framework-Collaboration==2.5.1
pyobjc-framework-CoreData==2.5.1
pyobjc-framework-CoreLocation==2.5.1
pyobjc-framework-CoreText==2.5.1
pyobjc-framework-DictionaryServices==2.5.1
pyobjc-framework-EventKit==2.5.1
pyobjc-framework-ExceptionHandling==2.5.1
pyobjc-framework-FSEvents==2.5.1
pyobjc-framework-InputMethodKit==2.5.1
pyobjc-framework-InstallerPlugins==2.5.1
pyobjc-framework-InstantMessage==2.5.1
pyobjc-framework-LatentSemanticMapping==2.5.1
pyobjc-framework-LaunchServices==2.5.1
pyobjc-framework-Message==2.5.1
pyobjc-framework-OpenDirectory==2.5.1
pyobjc-framework-PreferencePanes==2.5.1
pyobjc-framework-PubSub==2.5.1
pyobjc-framework-QTKit==2.5.1
pyobjc-framework-Quartz==2.5.1
pyobjc-framework-ScreenSaver==2.5.1
pyobjc-framework-ScriptingBridge==2.5.1
pyobjc-framework-SearchKit==2.5.1
pyobjc-framework-ServiceManagement==2.5.1
pyobjc-framework-Social==2.5.1
pyobjc-framework-SyncServices==2.5.1
pyobjc-framework-SystemConfiguration==2.5.1
pyobjc-framework-WebKit==2.5.1
pyOpenSSL==0.13.1
pyparsing==2.0.1
python-dateutil==1.5
pytz==2013.7
scipy==0.13.0b1
six==1.4.1
xattr==0.6.4
zope.interface==4.1.1
Rodneys-MBP:~ rodneyvictornjii$ cd Desktop
Rodneys-MBP:Desktop rodneyvictornjii$ pip freeze>requirement.txt
Rodneys-MBP:Desktop rodneyvictornjii$ ls
DojoAssignments			jq.js
Exam				lesson.py
Exam.zip			ll.html
bday.js				ll.js
birthday.js			p.js
declare.js			practice_vic.html
for-loop.js			requirement.txt
indentation_practice.html	test_1
index.html			time.html
internet_test.css		time.js
internet_test.html		web-fundamentals
james-test.css			while-loop.js
james-test.html
Rodneys-MBP:Desktop rodneyvictornjii$ pip uninstall Django
Cannot uninstall requirement Django, not installed
Rodneys-MBP:Desktop rodneyvictornjii$ pip show Django
Rodneys-MBP:Desktop rodneyvictornjii$ pip search Flask
Flask-User-05 (0.5)                            - Customizable User Account
                                                 Management for Flask:
                                                 Register, Confirm email,
                                                 Login, Change username,
                                                 Change password, Forgot
                                                 password and more.
flask-restless-swagger-2 (0.0.3)               - Magically create swagger
                                                 documentation as you
                                                 magically create your RESTful
                                                 API
flask-restful-swagger-2 (0.35)                 - Extract swagger specs from
                                                 your flask-restful project.
                                                 Project based on flask-
                                                 restful-swagger by Ran
                                                 Tavory.
3color-Press (0.2.1)                           - A Flask based static site
                                                 generator for comics
flask-ab (0.0.1)                               -
abilian-core (0.9.23)                          - A framework for enterprise
                                                 applications (CRM, ERP,
                                                 collaboration...), based on
                                                 Flask and SQLAlchemy
AC-Flask-HipChat (0.2.12)                      - Atlassian Connect library
                                                 based on Flask for HipChat
acceptable (0.9)                               - API version negotiation for
                                                 flask-based web services.
Flask-Access (0.1)                             - A Flask extension which
                                                 limits access to views.
Flask-Personal-Access-Token (0.1.2)            - Flask Personal Access Token
                                                 Management Extension
Flask-ACL (0.0.1)                              - Access control lists for
                                                 Flask.
flask-miracle-acl (0.2)                        - The fabric between the Flask
                                                 framework and Miracle ACL
Flask-Actions (0.6.6)                          - custom actions for flask to
                                                 help manage your application
Flask-ActiveRecord (0.2.3)                     - ActiveRecord support for
                                                 Flask-SQLAlchemy models
flask-ad-auth (0.1)                            - Flask Azure Active Directory
                                                 Auth
fab-addon-audit (0.0.1)                        - Audit functionality to flask-
                                                 appbuilder apps.
Flask-ADFS (0.1.7)                             - User session management for
                                                 Flask
kore-plugins-flask-admin (0.0.1)               -
flaskpress-flask-admin (1.4.2.2)               - Fork of Flask-Admin for
                                                 flaskpress
flask-admin-barin (0.0.1)                      - A Barin backend for Flask-
                                                 Admin
flask-admin-lite (0.1.0)                       - Build lightweight admin panel
                                                 for your models
flask-admin-elasticsearch-dsl (0.0.1)          -
Flask-Admin-Utils (0.0.3)                      - Utils for Flask-Admin
quokka-flask-admin (1.4.2.1)                   - Fork of Flask-Admin for
                                                 QuokkaCMS
flask-admin-s3-upload (0.1.4)                  - Field types for allowing file
                                                 and image uploads to Amazon
                                                 S3 (as well as default local
                                                 storage) in Flask-Admin.
flask-admin-openerp (0.3.3)                    - OpenERP Backend for Flask-
                                                 Admin
Flask-Admin (1.5.0)                            - Simple and extensible admin
                                                 interface framework for Flask
flask-admin.py (0.1.3)                         - copy from djang-admin.py
Flask-Administration (0.1.42)                  - UNKNOWN
afg (0.2)                                      - Alexa Flask Guide for Flask-
                                                 ASK
agaveflask (0.2.0)                             - Common package for authoring
                                                 Agave services in flask
                                                 /Flask-RESTful
kolekti-agent-python-flask (0.0.1)             - Lightweight monitoring system
                                                 agent
burp-ui-agent (0.5.1)                          - Burp-UI is a web-ui for burp
                                                 backup written in python with
                                                 Flask and jQuery/Bootstrap
Flask-Aggregator (0.2.0)                       - Batch the GET requests to
                                                 your REST API into a single
                                                 POST
Flask-Airbrake (0.0.3)                         - Flask extension for Airbrake
airbrake-flask (1.0.7)                         - airbrake-flask - Airbrake
                                                 client for Python Flask
alchemist (0.3.12)                             - A server architecture built
                                                 on top of a solid foundation
                                                 provided by flask,
                                                 sqlalchemy, and various
                                                 extensions.
flask-wtf-alchemy-utils (0.1.0)                - Form and field utility base
                                                 classes for use with Flask,
                                                 Flask-WTF, and wtforms-
                                                 alchemy.
Flask-Alchemy (0.1)                            - The fastest markdown parser
                                                 in pure Python
flask-btsn-alchemy (0.0.2)                     - BITSON's SQLAlchemy Models
flask-simple-alchemy (0.3.0)                   - A Simplification of
                                                 SQLAlchemy's declarative
                                                 using Flask-SQLAlchemy
Flask-AlchemyDumps (0.0.10)                    - SQLAlchemy backup/dump tool
                                                 for Flask
Flask-AlchemyView (0.1.4)                      - Simple ModelView for auto-
                                                 generating Flask Views based
                                                 on SQLAlchemy models
Flask-Alchy (0.5.0)                            - Flask extension for alchy
Flask-Alcool (0.3)                             - Implement access control
                                                 lists as decorators for
                                                 flask.
Flask-Alembic (2.0.1)                          - Flask extension to integrate
                                                 Alembic migrations
flask-allows (0.4)                             - Impose authorization
                                                 requirements on Flask routes
Flask-Analytics (0.6.0)                        - Analytics snippets generator
                                                 extension for the Flask
                                                 framework
Flask-And-Redis (0.7)                          - Simple as dead support of
                                                 Redis database for Flask
                                                 apps.
andromeda (0.1.2)                              - declarative, class-driven
                                                 framework written around
                                                 flask
Flask-Annex (0.4.2)                            - Efficient integration of
                                                 external storage services for
                                                 Flask
just-another-settings (1.0)                    - Small lib to manage settings
                                                 as object for
                                                 Flask/Bottle/custom apps
Flask-Api-Awesomesauce (0.1)                   - Flask Api Awesomesauce!
rest-api-blueprint (0.1)                       - Pedagogical blueprint of a
                                                 REST API in Flask.
Flask-Debug-API (0.1.0)                        - API Browser for Flask-
                                                 DebugToolbar
Flask-API-Utils (1.0.2)                        - Flask-API-Utils helps you to
                                                 create APIs.
api-star (0.1.4)                               - An API framework for Flask &
                                                 Falcon.
flask-simple-api (1.4.1)                       - Simple API endpoints for
                                                 Flask using Flask-Restful
                                                 reqparse and Python 3
                                                 annotations
Flask-API (1.1b1)                              - Browsable web APIs for Flask.
li-api-flask (0.1.18)                          - Loja Integrada's API Flask
Flask-API.yandex (0.6.2.1)                     - Browsable web APIs for Flask.
apiaiwebhook (0.1.0.dev2)                      - API.AI Webhook is a
                                                 fulfillment microframework
                                                 for API.AI based on Flask for
                                                 getting started quickly with
                                                 API.AI webhooks.
Flask-APIBlueprint (1.0.0)                     - Route inheritance for Flask
                                                 Blueprints
flask-apidoc (1.1.1)                           - Adds ApiDoc support to Flask
Flask-APIForm (1.0)                            - A simple form validator for
                                                 REST APIs in Flask
flask-apify (0.7.1)                            - A Flask extension to create
                                                 API to your application as a
                                                 ninja
apikit (0.3.2)                                 - A set of utility functions
                                                 for RESTful Flask
                                                 applications.
apispec-flask-restful (0.1)                    - Flask-RESTful plugin for
                                                 apispec
flask-apispec (0.4.2)                          - Build and document REST APIs
                                                 with Flask and apispec
flask-app-router (0.0.1)                       - UNKNOWN
social-auth-app-flask-peewee (1.0.0)           - Python Social Authentication,
                                                 peewee Flask models
                                                 integration.
social-auth-app-flask-mongoengine (1.0.0)      - Python Social Authentication,
                                                 Mongoengine Flask models
                                                 integration.
social-auth-app-flask (1.0.0)                  - Python Social Authentication,
                                                 Flask integration.
social-auth-app-flask-sqlalchemy (1.0.1)       - Python Social Authentication,
                                                 SQLAlchemy Flask models
                                                 integration.
create-flask-app (0.2.1)                       - Create flask web apps with
                                                 directory layout
flask-app-core (1.2.7)                         - Flask app core
Flask-AppBuilder (1.9.4)                       - Simple and rapid application
                                                 development framework, built
                                                 on top of Flask. includes
                                                 detailed security, auto CRUD
                                                 generation for your models,
                                                 google charts and much more.
Flask-Appcache (0.1.2)                         - Semi-automagically sets up
                                                 appcache for you
flask-appconfig (0.11.1)                       - Configures Flask applications
                                                 in a canonical way. Also
                                                 auto-configures Heroku. Aims
                                                 to standardize configuration.
Flask-AppFactory (0.2.1)                       - Flask-AppFactory is an
                                                 dynamic application loader.
flask-applauncher-bundle (1.01)                - flask support for applauncher
flask-apps (0.0.2)                             - UNKNOWN
Flask-AppUtils (1.2.0)                         - A collection of useful
                                                 patterns and helpers for
                                                 Flask applications
Flask-APScheduler-fork (1.5.4)                 - Test package and a fork of
                                                 flask_apscheduler.
Flask-APScheduler (1.7.1)                      - Adds APScheduler support to
                                                 Flask
apy (0.2.3)                                    - Pythonic API development with
                                                 flask
Flask-Arango (0.1.1)                           - Flask extension providing
                                                 integration with Arango.
Flask-Arangodb (1.0.4)                         - Flask extension for ArangoDB
                                                 using python-arango
archer (0.5)                                   - Thrift app the flask way
archerv2 (0.6)                                 - Thrift app the flask
                                                 way...The Right Way
Flask-Argon2 (0.1.2.1)                         - Flask-Argon2 provides
                                                 convenient wrappers for
                                                 Argon2 password hashing
Flask-Argonaut (0.21)                          - Flask extension use hashing
                                                 data with Argon2
flask-request-args-parser (1.1.0)              - flask.request's args parser
flask-args (0.3.0)                             - auto type convertion for flas
                                                 k.request.form/args/values
Flask-arrest (0.5.0)                           - A small Flask extension to
                                                 ease the creation of REST
                                                 apis.
arrested (0.1.1)                               - A framework for rapidly
                                                 building REST APIs in Flask.
Flask-Ask (0.9.7)                              - Rapid Alexa Skills Kit
                                                 Development for Amazon Echo
                                                 Devices in Python
Flask-Aspen (0.0)                              - UNKNOWN
assentio (0.1)                                 - A minimal, lightweight flask-
                                                 based blog
Flask-AssetRev (1.0.0)                         - UNKNOWN
Flask-Assets (0.12)                            - Asset management for Flask,
                                                 to compress and merge CSS and
                                                 Javascript files.
Flask-Assistant (0.2.93)                       - Framework for Building
                                                 Virtual Assistants with
                                                 API.AI
selenium-astride (0.2.2)                       - Framework to use Selenium
                                                 loud and clear, astride. Use
                                                 it with Django, Flask or your
                                                 favourite web framework.
Flask-Async (0.11-dev-20140215)                - A fork of Flask to support
                                                 asyncio
atilla (1.2.6)                                 - flask API projects helper
Flask-AtlassianConnect (0.0.5)                 - Atlassian Connect Helper
Flask-Attest (0.1dev)                          - Test Flask applications with
                                                 Attest
Flask-Augment (0.5)                            - Python decorators
                                                 implementing contracts for
                                                 flask framework
flask-modular-auth (0.2)                       -
flask-social-auth (0.0)                        -
flask-wechat-auth (0.0.1)                      - WeChat Flask Blueprint Module
pixelpin-auth-flask (1.0.0)                    - Python Social Authentication,
                                                 Flask integration.
pixelpin-auth-flask-sqlalchemy (1.0.1)         - Python Social Authentication,
                                                 SQLAlchemy Flask models
                                                 integration.
Flask-Auth (0.85)                              - Auth extension for Flask.
Flask-Heroku-Auth (0.0.5)                      - Flask Based Heroku
                                                 Authentication.
Flask-Authbone (0.3)                           - Plugguble Auth framework for
                                                 Flask.
flask-authjwt (0.1.1)                          - Module to secure flask
                                                 endpoints in appengine using
                                                 jwt token.
Flask-AuthMgr (1.0.0)                          - A flask extension based on
                                                 Flask-HTTPAuth for managing
                                                 restful API Auth.
Flask-Authority (0.0.1)                        -
Flask-Authorization-Panda (0.3)                - Flask Authorization for
                                                 Pandas!
Flask-Restful-Autodoc (0.0.1.1)                - Simple library for auto
                                                 generating documentation for
                                                 Flask-Restful package
Flask-Autodoc (0.1.2)                          - Documentation generator for
                                                 flask
Flask-AutoFixture (0.2.3)                      - Flask extension for recording
                                                 JSON fixtures right from your
                                                 test suite
Flask-AutoIndex (0.6)                          - The mod_autoindex for Flask
flask-automation (1.1)                         - Common functionality across
                                                 the different Flask
                                                 microservices of the UofC UIS
                                                 Automation team
flask-restful-autoroute (0.1)                  - Blueprint based auto routing
                                                 library for flask-restful
flask-autorouter (0.2.1)                       - a utility for generating
                                                 flask URL routing
Flask-Avatar (0.1.2)                           - To generate avatar for flask
Flask-Avatars (1.0)                            - All avatar generators in one
                                                 place.
flask-avro (0.0.1)                             - Simple AVRO IPC endpoint
                                                 registration for Flask
flask-awesomemongokit (0.3.3)                  - Sets up an extremely
                                                 opinionated MongoKit
                                                 environment in Flask, based
                                                 selfishly on my own needs.
Flask-AYAH (0.1)                               - Are you a Human? Flask
                                                 Extension
Flask-Azure-Storage (0.2.1)                    - Flask extension that provides
                                                 integration with Azure
                                                 Storage
Flask-Imagine-AzureAdapter (0.4)               - Microsoft Azure BLOB adapter
                                                 for Flask-Imagine extension.
Flask-B1Connector (0.0.1)                      - Use to connect SAP B1 RESTful
                                                 API.
Flask-B3 (0.0.4)                               - B3 header access and
                                                 propagation for Flask.
flask-babel-utclocal-utils (0.1.0)             - UTC to local (and vice versa)
                                                 datetime conversion utilities
                                                 for use with Flask-Babel.
Flask-Babel (0.11.2)                           - Adds i18n/l10n support to
                                                 Flask applications
Flask-Babel2 (0.1)                             - Adds i18n/l10n support to
                                                 Flask applications
Flask-Babeled (0.9.3)                          - Adds i18n/l10n support to
                                                 Flask applications
Flask-BabelEx (0.9.3)                          - Adds i18n/l10n support to
                                                 Flask applications
Flask-BabelPkg (0.9.6)                         - Adds i18n/l10n support to
                                                 Flask applications and
                                                 extensions
Flask-BabelPlus (2.1.1)                        - Adds i18n/l10n support to
                                                 Flask applications
Barista (0.0.22)                               - A Flask application creator
Flask-BasicAuth (0.2.0)                        - HTTP basic access
                                                 authentication for Flask.
Flask-HAL-BBVA (1.0.5)                         - Provides easy integration of
                                                 the HAL specification for
                                                 your REST Flask Applications.
Flask-Bcrypt (0.7.1)                           - Brcrypt hashing for Flask.
Flask-BCS (0.9.1)                              - Baidu Cloud Storage for Flask
Flask-BDEA (0.1.0)                             - Flask-BDEA
Flask-Beaker (0.2.0)                           - Beaker session interface for
                                                 Flask.
flask-beans (1.2)                              - A simple API for counting
                                                 beans with Flask and Redis.
Flask-Beanstalk (0.0.3)                        - Utilities for using Beanstalk
                                                 with Flask
Flask-BearyChat (0.2.0)                        - A Flask extension to help
                                                 interact with BearyChat
behave-models-steps (0.1.6)                    - Provides testing for Flask-
                                                 SQLAlchemy models with Behave
flask-bigtempo (0.8)                           - Flask extension for bigtempo
                                                 features
Flask-bitjws (0.1.1.5)                         - A Flask extension for bitjws
                                                 authentication.
Flask-Bitmapist (0.1.2)                        - Flask extension that creates
                                                 a simple interface to
                                                 Bitmapist analytics library
biweeklybudget (0.5.0)                         - Responsive Flask/SQLAlchemy
                                                 personal finance app,
                                                 specifically for biweekly
                                                 budgeting.
Flask-Bleach (0.0.2)                           - Easy integration of bleach
flask-blitzdb (0.1)                            - Flask extension for blitzdb
flask-block (0.0.1)                            -
flask-blocks (1.0.9)                           - The common blocks which solve
                                                 common problems encountered
                                                 when creating Flask
                                                 applications.
blocky (0.0.2)                                 - Block rendering for flask and
                                                 django using jinja2.
Blogging-Plugins (0.2.0)                       - A plugin library for Flask-
                                                 Blogging flask extension
                                                 blog.
Flask-Blogging (1.0.2)                         - A flask extension for adding
                                                 Markdown blog support to your
                                                 site
Flask-BlogTheme (0.2.2)                        - Flask extension to read
                                                 switch theme easily
Bluebook (0.0.1)                               - Pylot is a Flask extension
                                                 that adds structure and map
                                                 your views and templates
                                                 together for rapid
                                                 application development
blueflask (0.1.4)                              - Flask boilerplate to create
                                                 an application with the idea
                                                 of pluggable blueprints.
flask-bluelogin (0.2.7)                        - Flask BlueLogin module
flask-social-blueprint (0.7.2)                 - An OAuth based authentication
                                                 blueprint for flask. Easy to
                                                 extend and override
flask-blueprint (1.2.2)                        - Flask blueprint generator
flask-bluestatic (0.1.0)                       - Flask BlueStatic module
flask-boilerplate-utils (0.1.65)               - Additional functionality with
                                                 easy upgrading for the flask-
                                                 boilerplate.
Flask-Turbo-Boost (0.0.10)                     - Forked Flask-Boost - Flask
                                                 application generator for
                                                 boosting your development.
Flask-Boost (0.7.5)                            - Flask application generator
                                                 for boosting your
                                                 development.
Flask-SQLAlchemy-Booster (0.4.112)             - Querying and JSON Response
                                                 generation wrappers for
                                                 Flask-SQLAlchemy
BootFlask (0.1)                                - A simple tool for turn your
                                                 flask projects more quick and
                                                 fun.
Flask-Bootstrap (3.3.7.1)                      - An extension that includes
                                                 Bootstrap in your project,
                                                 without any boilerplate code.
Flask-Bootstrap3 (3.1.1.3)                     - UNKNOWN
Flask-Bootstraps (3.3.7.8)                     - An extension that includes
                                                 Bootstrap in your project,
                                                 without any boilerplate code.
bootstraps (1.0.1)                             - A library to handle user
                                                 related tasks in Flask
Facebook-Bot-Library (0.1)                     - A facebook messaging SDK for
                                                 Flask
Flask-Boto3 (0.2.2)                            - Flask extension that ties
                                                 boto3 to the application
Flask-BotoSQS (0.2.0)                          - Boto3 SQS integration for
                                                 Flask
zulip-botserver (0.3.7)                        - Zulip's Flask server for
                                                 running bots
flask-bouncer (0.1.13)                         - Flask Simple Declarative
                                                 Authentication based on Ryan
                                                 Bates excellent cancan
                                                 library
Flask-S3-Bower (0.7)                           - Seamlessly serve the static
                                                 files of your Flask app from
                                                 Amazon S3 and also use bower
                                                 for development
Flask-Bower (1.3.0)                            - An extension to manage and
                                                 serve your javascript assets
                                                 with bower
Flask-BowerCDN (0.1.0)                         - Work easily with Bower and
                                                 CDN content.
Flask-SSLify-bp (0.1.6)                        - Force SSL on your Flask app.
flask-shell-bpython (0.0.3)                    - Replace the default ``flask
                                                 shell`` command with a
                                                 similar one running BPython.
flask-braintree (0.01)                         -
Flask-Breadcrumbs (0.4.0)                      - Flask-Breadcrumbs adds
                                                 support for generating site
                                                 breadcrumb navigation.
Flask-Breathalyzer (0.2.2)                     - Flask module for submitting
                                                 timings and exceptions to
                                                 Datadog
Flask-Breve (0.2)                              - Breve templating with Flask
Flask-Bridgekeeper (0.1.1)                     - Manage the access control of
                                                 a flask application
Broadway-Migrate (0.0.1)                       - A set of tools to reduce the
                                                 boilerplate code in Flask
                                                 apps
Broadway-SQLAlchemy (0.0.1)                    - A broadway extension wrapping
                                                 Flask-SQLAlchemy
Broadway (0.0.2)                               - A set of extensions for Flask
                                                 that take the boilerplate out
                                                 of your project.
Flask-outdated-browser (0.1)                   - Easily add outdated-browser
                                                 project to your Flask
                                                 application
browser-markdown-editor (0.2.0)                - Markdown editor for web
                                                 browsers, built with Flask.
Flask-BrowserID (0.0.4)                        - Flask support for BrowserID
                                                 authentication
Flask-BS (0.5.5)                               - Another flask extension that
                                                 provides Bootstrap CSS, JS
                                                 and HTML5 boilerplate.
Flask-BSON (0.1.1)                             - Let your flask endpoints
                                                 handle BSON requests and
                                                 responses
buchner (0.1.dev)                              - Flask project template and
                                                 helper library
flask-buckets (0.1.dev)                        - Simple and easy file storages
                                                 for Flask
bugsnag (3.3.0)                                - Automatic error monitoring
                                                 for django, flask, etc.
buildbot-wsgi-dashboards (0.9.12)              - Buildbot plugin to integrate
                                                 flask or bottle dashboards to
                                                 buildbot UI
Flask-Bulbs (0.1)                              - Flask extension for
                                                 [Bulbs](http://bulbflow.com/)
                                                 supporting the factory
                                                 pattern with the init_app
                                                 method.
flask-bundle-system (0.1)                      - Flask extension for work with
                                                 blueprints as bundles
Flask-Bundle (0.4)                             - Class based tool that behaves
                                                 like blueprints
flask-static-bundle (0.1.3)                    - Flask extension for static-
                                                 bundle
flask-graylog-bundle (0.0.11)                  - Flask Graylog client
Buro (0.1.27)                                  - A very simple Python-powered
                                                 open-source web framework
                                                 inspired by Flask, but
                                                 following different design
                                                 decisions
burp-ui (0.5.1)                                - Burp-UI is a web-ui for burp
                                                 backup written in python with
                                                 Flask and jQuery/Bootstrap
http-butler (0.4.0)                            - Light flask server
flask-buzz (0.1.3)                             - Extra bindings on py-buzz
                                                 specifically for flask apps
Flask-Cache-PyLibMC (0.1)                      - PyLibMC cache for Flask-
                                                 Cache, supports multiple
                                                 operations and other awesome
                                                 things.
Flask-Cache-Latest (0.12)                      - Adds cache support to your
                                                 Flask application
Flask-Cache-Redis-Cluster (0.0.5)              - Adds redis cluster caching
                                                 support to the Flask
                                                 Cache(ing) extension
Flask-SQLAlchemy-Cache (0.1.5)                 - CachingQuery implementation
                                                 to Flask using Flask-
                                                 SQLAlchemy and Flask-Cache
Flask-Cache-Cassandra (0.14.6)                 - Adds cache support to your
                                                 Flask application
Flask-Dogpile-Cache (0.2)                      - Adds dogpile.cache support to
                                                 your Flask application
Flask-Cache (0.13.1)                           - Adds cache support to your
                                                 Flask application
Flask-CacheControl (0.1.2)                     - Set Cache-Control headers on
                                                 the Flask response
Flask-Heroku-Cacheify (1.6.0)                  - Automatic Flask cache
                                                 configuration on Heroku.
Flask-CacheOBJ (0.2.2)                         - Flask-CacheOBJ provides some
                                                 caching decorators
Flask-SQLAlchemy-Caching (1.0.1)               - CachingQuery implementation
                                                 to Flask using Flask-
                                                 SQLAlchemy and Flask-Caching
Flask-Caching (1.3.3)                          - Adds caching support to your
                                                 Flask application
Flask-Cachual (0.2.0)                          - Flask extension for the
                                                 Cachual library
Flask-Cake (0.3.1)                             - Flask extension to execute
                                                 Cake on filesystem events.
Flask-Canonical (0.1.1)                        - Easy canonical logging for
                                                 Flask
flask-canvas (0.1)                             - A Flask extension for
                                                 Facebook canvas-based apps
capitains-hook (1.0.0)                         - Hook Flask App for Github/CTS
                                                 repositories
Flask-Captain (0.1.1)                          - Handle webhooks with Flask
flask-session-captcha (1.1.0)                  - Captcha implementation for
                                                 flask and flask-session.
Flask-Captcha (0.1.8)                          - A very simple, yet powerful,
                                                 Flask captcha extension
carafe (0.4.7)                                 - Collection of Flask
                                                 extensions geared towards
                                                 JSON APIs
cartographer (0.2.0-alpha5)                    - Python library for using JSON
                                                 API, especially with Flask.
Flask-CAS (1.0.1)                              - Flask extension for CAS
Flask-Cassandra (0.14)                         - Provides a connection to a
                                                 Cassandra cluster in a Flask
                                                 app
cassandra_flask_sessions (0.3)                 - Server side sessions with
                                                 Apache Cassandra
Flask-CassandraDB (0.0.1)                      - connect cassandra to flask
Flask-Caster (0.1.0)                           - A simple Flask extension for
                                                 automatically casting the
                                                 type of query arguments.
castle-flask (0.0.1)                           - A Flask client for Castle.io
Flask-Cavage (0.4.3)                           - Verify cavage-http-signatures
                                                 requests made to Flask
flask-cbv (0.0.1)                              - Class based views for Flask.
Flask-CDN-NG (1.3.0)                           - Serve the static files in
                                                 your Flask app from a CDN.
Flask-CDN (1.5.3)                              - Serve the static files in
                                                 your Flask app from a CDN.
Flask-Celery-Helper (1.1.0)                    - Celery support for Flask
                                                 without breaking PyCharm
                                                 inspections.
Flask-Celery (2.4.3)                           - Celery integration for Flask
Flask-Celery-py3 (0.2.4)                       - Celery 3.0+ integration for
                                                 Flask (Python 3 version)
Flask-Celery3 (0.2)                            - Add Celery3 integration to
                                                 your Flask apps.
Flask-CeleryExt (0.3.0)                        - Flask-CeleryExt is a simple
                                                 integration layer between
                                                 Celery and Flask.
Flask-Cent (0.1.3)                             - centrifugal/cent client for
                                                 flask
centralsession (0.3.0)                         - A redis based session storage
                                                 that works for flask and
                                                 django
Flask-Multipass-LDAP-CERN (1.0.3)              - CERN-specific Flask-Multipass
                                                 providers
python-cfworker (1.6.0)                        - This module makes it easier
                                                 to deploy Python workers by
                                                 wrapping Flask and
                                                 multiprocess functionality
                                                 into a single module. When
                                                 instanced, your app will be
                                                 serving http via Flask, as
                                                 well as performing work.
Flask-Chargebee (0.0.1)                        - Flask-Chargebee
cheddar (1.4)                                  - PyPI clone with Flask and
                                                 Redis
chiki (1.1.1)                                  - Common libs of flask web
                                                 develop
chill (0.3.3)                                  - Database driven web
                                                 application framework in
                                                 Flask
Flask-Church (0.0.1)                           - Flask-Church is a extension
                                                 for     Flask that help you
                                                 generate fake data for
                                                 testing
Flask-CI (1.2.9.1)                             - Continuous Integration
                                                 support for Flask
Flask-CKEditor (0.2)                           - Implementation of CKEditor
                                                 for WTForms/Flask-WTF.
flask-clacks (1.0.1)                           - A man is not dead while his
                                                 name is still spoken.
Flask-Classful (0.14.1)                        - Class based views for Flask
Flask-Classy (0.6.10)                          - Class based views for Flask
clay-flask (2.1.8)                             - Clay is a framework for
                                                 building RESTful backend
                                                 services using best
                                                 practices.
Flask-Clearbit (0.1.0)                         - Flask-Clearbit
Flask-CLI (0.4.0)                              - Backport of Flask 1.0 new
                                                 click integration.
Flask-Click-Migrate (0.1.0)                    - A library to glue flask +
                                                 alembic + click
flask-test-requests-client (0.2.0)             - A Flask test client which
                                                 replicates the requests
                                                 interface.
platformo-client (0.0.1)                       - 收集Flask的请求响应时间并发送至logstash
Potion-client (2.5.1)                          - A client for APIs written in
                                                 Flask-Potion
klue-client-server (1.0.122)                   - Swagger + Flask + Bravado =
                                                 Client/Server auto-spawning
inovonics-cloud-oauth (0.1.0.6)                - Classes implementing
                                                 functionality for flask-
                                                 oauthlib using Redis as the
                                                 backing store.
Flask-Cloudy (1.0.1)                           - Flask-Cloudy is a simple
                                                 flask extension and
                                                 standalone library to upload
                                                 and save files on S3, Google
                                                 storage or other Cloud
                                                 Storages
Flask-CMDB (0.1.4)                             - A cmdb api client for Flask
                                                 applications.
Flask-CMS (0.0.1)                              - Extensible Content Management
                                                 System for Flask: Pages,
                                                 Blogs, Comments and more.
Flask-CMS-Core (0.01)                          -
coaster (0.6.0)                                - Coaster for Flask
Flask-Swagger-Codegen (0.0.6)                  - Generate Flask code from
                                                 Swagger docs.
swagger-py-codegen (0.2.9)                     - Generate Flask code from
                                                 Swagger docs.
flask-codemirror (1.0)                         - Use CodeMirror Javascript
                                                 library with Flask-WTF
Flask-Coffee (0.3)                             - Fill your flask with coffee.
flask-coffee2js (0.1.2)                        - A small Flask extension that
                                                 adds CoffeScript support to
                                                 Flask.
Flask-Collect (1.3.2)                          - Flask-Collect -- Collect
                                                 static files in Flask
                                                 application
Flask-Color (0.2.1)                            - flask-color is an extension
                                                 for Flask that improves the
                                                 built-in web server with
                                                 colors when debugging.
                                                 Unnecessary clutter such as
                                                 time or IP are hidden.
flask-command (0.0.3)                          - flask-command - Run you
                                                 flask+gunicorn app as a
                                                 command
Flask-Common (0.2.0)                           - A Flask extension with lots
                                                 of common time-savers (file-
                                                 serving, favicons, etc).
Flask-Compass (0.2)                            - Adds automatic Compass
                                                 compilation to Flask
Flask-Components (0.1.1)                       - A simple flask extension to
                                                 discover files in a declared
                                                 array of components.
Flask-Composer (0.4.1)                         - Composite Web UI extension
                                                 for Flask
Flask-Compress-nondebug (1.0.2)                - Compress responses in your
                                                 Flask app with gzip.
Flask-Static-Compress (1.0.2)                  - Auto-detects your static
                                                 files for minification,
                                                 combination, and versioning.
                                                 Like Django-Compressor for
                                                 Flask.
Flask-Compress (1.4.0)                         - Compress responses in your
                                                 Flask app with gzip.
Flask-Compressor (0.2.0)                       - Compress your CSS and JS
                                                 files.
flask-conditional (0.1)                        - Conditional decorators for
                                                 Flask routes
Flask-Config-Helper (0.1.1)                    - Flask configuration helper
Flask-Config-Override (0.0.2)                  - Override Flask configuration
                                                 via Cookie at runtime.
Flask-Config (0.2.1)                           - Flask configuration class
flask-confighelper (1.0.0)                     - Helper for setting up
                                                 environment configurations
flask-pre-configured-loggers (0.1.1)           - Flask request / script pre-
                                                 configured loggers.
Congo (0.0.1)                                  - Portfolio is a Flask based
                                                 framework that adds structure
                                                 and map your views and
                                                 templates together for rapid
                                                 application development
conmongo (0.0.2)                               - A Flask microplugin based on
                                                 pymongo
connexion (1.1.16)                             - Connexion - API first
                                                 applications with
                                                 OpenAPI/Swagger and Flask
flask-consulate (0.2.0)                        - flask extension that provides
                                                 an interface to consul via a
                                                 flask app
Container-WhooshAlchemyPlus (0.7.5.post3)      - Whoosh extension to
                                                 Flask/SQLAlchemy which used
                                                 in sina container
Flask-Context (0.1)                            - Provide an arbitrary context
                                                 object to Flask. Useful for
                                                 microservice environments.
Flask-REST-Controller (1.0.0)                  - Flask-REST-Controller is
                                                 added Class-Based-
                                                 View(Controller) extension on
                                                 Flask
hepdata-converter-ws (0.1.6)                   - Flask webservices enabling
                                                 usage of hepdata-converter as
                                                 a separate server over the
                                                 network
flask-secure-cookie (0.1.2)                    - Tornado's secure cookie
                                                 support in Flask
flask-extension-cookiecutter (0.1.1)           - Cookiecutter template for a
                                                 Flask Extension
Flask-Copilot (0.2.0)                          - Simple navbar generation for
                                                 Flask applications.
Flask-Coralillo (0.1.2)                        - Flask module for the
                                                 Coralillo redis ORM
corkscrew (0.18)                               - ooviews, settings, auth &
                                                 more for flask
Sanic-Cors (0.9.0)                             - A Sanic extension adding a
                                                 decorator for CORS support.
                                                 Based on flask-cors by Cory
                                                 Dolphin.
Flask-Cors (3.0.3)                             - A Flask extension adding a
                                                 decorator for CORS support
Flask-CORSify (0.1.1)                          - Add CORS support for your
                                                 Flask app.
Flask-COS (0.1.0)                              - 腾讯云对象存储的Flask扩展
Flask-CouchDB-Schematics (1.0.0)               - Provides utilities for using
                                                 CouchDB + Schematics with
                                                 Flask
Flask-CouchDB (0.2.1)                          - Provides utilities for using
                                                 CouchDB with Flask
Flask-CouchDBKit (0.3.5)                       - Flask extension that provides
                                                 integration with CouchDBKit.
Flask-CQLAlchemy (1.2.0)                       - Flask-CQLAlchemy handles
                                                 connections to Cassandra
                                                 clusters and provides an
                                                 interface through cqlengine
hero-crawl (0.1.4)                             - Helpers for Scrapy and Flask
                                                 on Heroku
Flask-Creole (0.4.4)                           - Creole parser filters for
                                                 Flask
flask-crossdomain (0.1)                        - HTTP Access Control helper.
Flask-Crossdomain2 (0.1.0)                     - Module for enabling cross-
                                                 site/cross-origin HTTP
                                                 requests on Flask app
                                                 endpoints.
Flask-SQLAlchemy-CRUD-Mixin (0)                -
Flask-Crud (0.0.2)                             - Quick and Easy CRUD for
                                                 Flask, built on top of Flask-
                                                 Classy
flask-peewee-crud (0.3.0)                      - A REST API framework for
                                                 building CRUD APIs using
                                                 Flask and peewee (forked from
                                                 sanic_crud https://github.com
                                                 /Typhon66/sanic_crud)
crumby (0.7.1)                                 - A Flask based web analytics
                                                 app
flask-csp (0.9)                                - Flask Content Security Policy
                                                 header support
flask-csrf (0.9.2)                             - A small Flask extension for
                                                 adding CSRF protection.
Flask-CSV (1.0.1)                              - Easily render CSVs within any
                                                 flask application
CTRegisterMicroserviceFlask (0.3.1)            - Library to interact with the
                                                 Control-Tower api-gateway
                                                 (register, do requests to
                                                 other microservices, etc)
flask-ctx (1.0.0)                              - A simple integration of the
                                                 CTX defense against side-
                                                 channel attacks for Flask
                                                 projects.
Flask-CuddlyRest (0.1.15)                      - Flask restful API framework
                                                 for MongoDB/MongoEngine
flask-daapserver (3.0.2)                       - DAAP server framework
                                                 implemented with Flask
Flask-Dance (0.12.0)                           - Doing the OAuth dance with
                                                 style using Flask, requests,
                                                 and oauthlib
flask-monitoring-dashboard (1.8)               - A dashboard for automatic
                                                 monitoring of python web-
                                                 services
Flask-Dashboard (0.0.6a)                       - Yet another admin interface
                                                 for Flask
Flask-Dashed (0.1b2)                           - Adds a way to easily build
                                                 admin apps
Flask-Datadog (0.1.4)                          - Access to dogstatsd in your
                                                 app.
Flask-DB2 (0.0.10)                             - Creates connections for use
                                                 with DB2
Flask-DBConfig (0.3.12)                        - Configure Flask applications
                                                 from a local DB
Flask-DBKit (0.0.1)                            - dbkit integration for Flask.
Flask-DBMigrate (0.1)                          - Database schema change
                                                 management for
                                                 Flask\SQLAlchemy
Flask-DbShell (1.0)                            - Django-like dbshell
Flask-Debug (0.4.3)                            - Shows
                                                 reflection/configuration to
                                                 aid the development of Flask
                                                 applications.
flask-debugtb-elasticsearch (0.1.3)            - Flask debug toolbar panel for
                                                 elasticsearch queries.
Flask-DebugTool (0.1.8)                        - A toolbar overlay for
                                                 debugging Flask applications.
Flask-DebugToolbar-Mongo (0.1)                 - MongoDB panel for the Flask
                                                 Debug Toolbar
flask-debugtoolbar-flamegraph (0.1.2)          - Flamegraphs for Flask Debug
                                                 Toolbar
Flask-DebugToolbar-LineProfilerPanel (1.0.2)   - Panel for the Flask Debug
                                                 toolbar to capture and view
                                                 line-by-line profiling stats
Flask-DebugToolbar (0.10.1)                    - A toolbar overlay for
                                                 debugging Flask applications.
Flask-Decorators (0.0.1)                       - A list of Flask decorator
                                                 utilitiesnot include in the
                                                 origin flask project.
Flask-Defer (1.1.0)                            - Flask extension to defer task
                                                 execution under after request
                                                 teardown
Flask-Devices (0.0.1)                          - Flask extension for switching
                                                 template folder automatically
                                                 by User Agent
flask-oauth2-devices (0.0.1)                   - OAuth2 for devices flow
                                                 implementation for Flask
Flask-Diamond (0.5.1)                          - Flask-Diamond provides some
                                                 opinions about data-centric
                                                 Internet applications and
                                                 systems. Flask-Diamond is a
                                                 batteries-included Flask
                                                 framework, sortof like Django
                                                 but radically decomposable.
Flask-Diced (0.3)                              - Flask-Diced - CRUD views
                                                 generator for Flask
Flask-Digest (0.2.1)                           - A RESTful authentication
                                                 service for Flask
                                                 applications
flask-discoverer (0.0.2)                       - Flask API autodiscovery
Flask-Disqus (0.0.1)                           - Small extension for Flask to
                                                 make possible using Disqus
                                                 comments
Flask-Dissect (1.0.10)                         - Dissect Distributed Session
                                                 Control
Djam (0.9.8)                                   - Extends Django to work with
                                                 sqlalchemy and make it behave
                                                 like Flask
sqlalchemy-django (0.0.3)                      - similar flask sqlalchemy
django-fsu (0.1.2)                             - Flask-Style URL Patterns for
                                                 Django
django-kungfu (0.2)                            - A Flasky approach to
                                                 distributed Django
                                                 configuration
Flask-DjangoQuery (0.2.4)                      - Django like query for Flask-
                                                 SQLAlchemy
flask-djcelery (0.1)                           - An integration of djcelery
                                                 with flask application
djeasyroute (0.0.2)                            - A simple class based route
                                                 system for django similar to
                                                 flask
djroute (1.1)                                  - Flask inspired dynamic
                                                 routing for Django
Flask-Dmango (0.0.7)                           - Contents managements support
                                                 for Flask + MongoDB
                                                 applications
ums-doc-swag (1.0.1)                           - Extract swagger specs from
                                                 your flask project
doc-swag (1.0.1)                               - Extract swagger specs from
                                                 your flask project
ums-doc-swagger (1.0.2)                        - Extract swagger specs from
                                                 your flask project
flask-docjson (0.1.7)                          - Validate flask request and
                                                 response json schemas via
                                                 docstring.
Flask-Docker (0.2.0)                           - Using Docker client in your
                                                 Flask application.
doctor (1.3.3)                                 - A module that assists in
                                                 using JSON schemas to
                                                 validate data in Flask APIs
                                                 and generate API
                                                 documentation.
Flask-DogStatsd (0.5.0)                        - A Flask extension for
                                                 dogstatsd-python
pylot-dojo (0.1.0)                             - MVC framework build on top of
                                                 flask
Flask-Sitemap-Domain (0.2.4)                   - Flask extension that helps
                                                 with sitemap generation.
Flask-DotEnv (0.1.1)                           - The .env file support for
                                                 Flask
python-dotenv (0.7.1)                          - Add .env support to your
                                                 django/flask apps in
                                                 development and deployments
webshare-download-manager (0.2.6)              - Download manager for
                                                 webshare.cz site. Flask +
                                                 requests.
Flask-Downloader (0.2)                         - Allow a Flask web app to
                                                 download files on behalf of
                                                 the user.
draftin_a_flask (0.1.5)                        - A simple Flask server that
                                                 allows you to publish Pelican
                                                 blags from http://draftin.com
Flask-Dropbox (0.3)                            - Dropbox Python SDK support
                                                 for Flask applications.
Flask-DropIn (0.0.1)                           - Flask-DropIn let you easily
                                                 organize large flask project.
Flask-Dropzone (1.4.1)                         - Upload file in Flask with
                                                 Dropzone.js.
Flask-Dry-Transaction (0.1.0)                  - A python package implementing
                                                 the strategy of business
                                                 transaction in flask
                                                 microservices developement
Flask-RESTful-DRY (0.3.1)                      - Flask-RESTful APIs using
                                                 declarations, not code
dscsrf (1.0)                                   - Double-submit CSRF protection
                                                 for Flask applications.
Flask-Should-DSL (0.4)                         - A flask extension for testing
                                                 with should-dsl
Flask-DStore (0.1.2)                           - DStore Web API and JS Client
                                                 using FLask
Flask-DWConnector (0.0.1)                      - Use to connect DataWald
                                                 RESTful API.
flask-dynamo-session (0.0.3)                   - Flask extension for storing
                                                 session in dynamodb. Uses
                                                 flask_dynamo.
flask-dynamo (0.1.2)                           - DynamoDB integration for
                                                 Flask.
flask-east (1.0.0)                             - Flask extension for creating
                                                 REST APIs
flask-easy-model (0.4.0)                       - A great base model, bringing
                                                 Django conveniences to Flask
Python-EasyConfig (0.1.7)                      - A simple library for loading
                                                 configurations easily in
                                                 Python, inspired by
                                                 `flask.config`.
easyflask (0.0.2)                              - Flask project generator
easyforms (0.0.27)                             - Form processing library for
                                                 Flask and Jinja2
flask-easymode (0.0.17)                        - Make Flask development even
                                                 easier
ecstatic (0.4)                                 - A small flask application to
                                                 serve files.
Flask-Ecstatic (0.3.0)                         - Serves static files with
                                                 optional directory index
Flask-Edits (0.8)                              - Editable Content in Flask
efs (0.1.1)                                    - A simple wrapper around fs to
                                                 work with flask and switch
                                                 between local and s3fs
Flask-Elastic (0.2)                            - Integrates official client
                                                 for Elasticsearch into Flask
Flask-Elasticsearch (0.2.5)                    - Flask extension for
                                                 Elasticsearch integration
Flask-ElasticUtils (0.1.7)                     - ElasticUtils for Flask
Eliza (1.0.0)                                  - Library with common features
                                                 for Python (Flask)
                                                 Microservices
elsa (0.1.3)                                   - Helper module for Frozen-
                                                 Flask based websites
Flask-Security-Elucidata (1.0.0)               - Simple security for Flask
                                                 apps.
Flask-Email (1.4.4)                            - Flask extension for sending
                                                 email
flask-emails (0.4)                             - Elegant and simple email
                                                 library for Flask.
flask-jsonify-emidln (0.1)                     - A small Flask decorator for
                                                 returning json. This is a
                                                 fork pushed to PyPI for easy
                                                 install.
flask-phantom-emoji (0.1.4)                    - Add phantom emoji's to your
                                                 flask application
Empty (0.4.2)                                  - Wrapper which makes Flask
                                                 development easier
Flask-MIME-Encoders (0.1.3)                    - Extensible Flask MIME
                                                 encoders and decoders
flask-endpoint (0.1)                           -
Flask-Enterprise (1.0)                         - Enterprise capabilities for
                                                 Flask
flask-env-settings (0.1.0)                     - Load application settings
                                                 from env variables
Flask-Env (1.0.1)                              - Easily set Flask settings
                                                 from environment variables
Flask-Heroku-Env (0.0.4)                       - Easily fetch Heroku
                                                 environment variables.
Flask-EnvConfig (0.2.0)                        - Configure Flask from
                                                 environment variables.
Flask-Environ (0)                              - os.environ wrapper for flask
                                                 config
Flask-Environment (0.3.1)                      - Configure a Flask application
                                                 with various file formats.
Flask-Environments (0.1)                       - Environment tools and
                                                 configuration for Flask
                                                 applications
Erlenmeyer (0.2.4)                             - Automatically generate Flask
                                                 servers from Core Data.
flask-erppeek (1.0.1)                          - ERPPeek Connector for Flask
Flask-ErrorHandler (0.1.0)                     - Generic error handlers for
                                                 Flask blueprints.
Flask-ErrorMail (0.2.2)                        - Flask extension for sending
                                                 administrators e-mails with
                                                 stacktraces when internal
                                                 server errors occur.
Flask-ESClient (0.1.1)                         - Flask extension for ESClient
                                                 (elasticsearch client)
Flask-Espresso (0.2.0)                         - Adds Coffescript support to
                                                 Flask applications
espressocup (0.0.3)                            - A gevent-intended very very
                                                 basic flask-like WSGI server
eventum (0.2.7)                                - A content management system
                                                 for event-driven Flask apps
evernode (0.2.0)                               - EverNode is built by
                                                 expanding upon flask by
                                                 adding great features and
                                                 easy-to-use modular design.
Flask-Evolution (0.6)                          - Simple migrations for
                                                 Flask/SQLAlchemy projects
Flask-Excel (0.0.7)                            - A flask extension that
                                                 provides one application
                                                 programming interface to read
                                                 and write data in different
                                                 excel file formats
flask-script-exception-handler (0.1.1)         - Exception handler designed
                                                 mainly to handle errors in a
                                                 flask-script custom command.
Flask-Exceptional (0.5.4)                      - Adds Exceptional support to
                                                 Flask applications
Flask-Pypi-Proxy-Ext (0.5.1)                   - A Pypi proxy
tradenity-flask-ext (0.1.0)                    - Flask framework extensions
                                                 for Tradenity Python SDK.
Flask-JSONSchema-Ext (0.1.2)                   - Flask JSONSchema Extended
                                                 Library
Flask-Statsd-Ext (0.0.3)                       - Statsd Extension for Flask
invenio-ext (0.3.2)                            - Invenio module that provides
                                                 integration with Flask
                                                 extensions.
Flask-ExtDirect (0.2)                          - Adds Ext.Direct support to
                                                 Flask.
Flask-RESTful-extend (0.3.7)                   - Improve Flask-RESTFul's
                                                 behavior. Add some new
                                                 features.
Flask-JWT-Extended (3.3.4)                     - Extended JWT integration with
                                                 Flask
Flask-Extension (1.0)                          - Demo for flask extension.
Honeybadger-Extensions (0.1.0)                 - Honeybadger extension that
                                                 can log exceptions raised by
                                                 Flask or Celery, adding more
                                                 context than the original
                                                 honeybadger python library.
Flask-Logging-Extras (0.1.0)                   - Extra logging functionality
                                                 for Flask apps
eyeflask (0.1.3)                               - Flask-based EyeFi Server
Flask-Factory (0.1.0dev)                       - Provide a general-purpose
                                                 application factory of the
                                                 Flask application, and the
                                                 configurator that is
                                                 independent of the app
                                                 object.
fah (0.1.0)                                    - Flask Against Humanity
                                                 (copyright infringement
                                                 pending).
Flask-Failsafe (0.2)                           - A failsafe for the Flask
                                                 reloader
fannypack (0.0.4)                              - a set of utilities for flask
Flask-Fanstatic (0.2.0)                        - Flask integration for the
                                                 Fanstatic resource publishing
                                                 system.
Flask-FAS (0.1.0)                              - Adds Fedora Account System
                                                 support to Flask
Flask-FastRPC (1.5)                            - Flask extension for
                                                 FastRPC/XMLRPC server
fawn (2.1.1)                                   - flask async uwsgi websocket
                                                 postgresql notify
Flask-FBLogin (0.0.1)                          - Extends Flask-Login to use
                                                 Facebook's OAuth2
                                                 authorization
fbones (0.0.6)                                 - A bootstrap toolkit to
                                                 kickoff a flask project
Flask-FCM (0.1)                                - Flask Extension for using
                                                 Firebase Cloud Messaging
                                                 service
Flask-FDS (0.0.6)                              - Xiaomi File Storage Service
                                                 for Flask
fdt-sqlalchemy (0.0.4)                         - Flask-debugtoolbar
                                                 configurable SQLAlchemy panel
Flask-FeatureFlags (0.6)                       - Enable or disable features in
                                                 Flask apps based on
                                                 configuration
Flask-FedoraCommons (0.0.8)                    - Library for manipulating
                                                 Fedora Commons digitial
                                                 repositories
feiwu (0.0.3)                                  - some useful module on flask
                                                 developer
FejsaFlaskProject (1.0)                        - UNKNOWN
flask-ffs (0.3.0)                              - A Flask library for the
                                                 storage and retrieval of
                                                 images on the file system.
Flask-FIDO-U2F (0.4.4)                         - A Flask plugin that adds FIDO
                                                 U2F support.
Flask-RESTful-Fieldsets (0.1.0)                - Extension to Flask-RESTful to
                                                 create fieldsets
Fifty-Flask (1.2.0)                            - Flask enhancements.
fighting (0.1.0)                               - A simple JSON API web
                                                 framework based on Flask
Flask-FileRev (0.1.0)                          - Flask-FileRev
Flask-FileUpload (0.5.0)                       - Flask-FileUpload is a Flask
                                                 extension for easy file
                                                 upload and management
Flask-fillin (0.2)                             - A flask extension that
                                                 provides utilities to test
                                                 forms.
Flask-Filtered-Response (1.0.2)                - Add filter capability to JSON
                                                 responses
flask-filters (0.3)                            - The Flask Filter to use with
                                                 flask-restful and Relational
                                                 DB
finny (0.3.10)                                 - Finny is the act of being
                                                 skinny and fat at the same
                                                 time.
                                                 Basic structure for an api-
                                                 centry approach to Flask -
                                                 that is both fat in skinny,
                                                 with basic and augmented
                                                 support over some popular
                                                 Flask libs
fireflask (0.2.0)                              - Simple, beautiful logging
                                                 from Flask web apps to
                                                 FireBug console
fis3 (0.0.8)                                   - 扩展flask,支持fis3
Flask-Fixtures (0.3.7)                         - A simple library for adding
                                                 database fixtures for unit
                                                 tests using nothing but JSON
                                                 or YAML.
fl-static (0.0.2)                              - Serve production static files
                                                 with Flask.
fl-flask-zipkin (0.0.6)                        - An zipkin extension for Flask
                                                 based on py_zipkin.
flachemy-session (0.0.3)                       - Ease to handle sqlalchemy
                                                 session with flask.
Flask-Flacro (0.0.8)                           - flask/jinja2 templating tools
flactory (0.2.0)                               - A handy tool for creating and
                                                 initializing flask
                                                 applications
flagen (0.1)                                   - A flask static site generator
                                                 that uses markdown and jinja2
                                                 templates.
flamyngo (0.9.2)                               - Flamyngo is a customizable
                                                 Flask frontend for MongoDB.
flango (0.0.1)                                 - Flask-like interface for
                                                 Django
Flask-Flarf (0.0.5)                            - Flask request filtering
flasgger (0.8.0)                               - Extract swagger specs from
                                                 your flask project
Flask-Flash (1.6.4)                            - Flask API framework (API +
                                                 Client) to create simple APIs
                                                 from database models.
quokka-flask-login (0.3.0)                     - User session management for
                                                 Flask
Flask-Humanoid (1.0)                           - Common humanization utilities
                                                 for Flask applications.
flask-iMail (0.1)                              - Mailgun integration for
                                                 Flask.
Flask-Imgur (0.1)                              - Upload images straight to
                                                 Imgur in your Flask app
Flask-kale (0.1)                               - Use kale models on a flask
                                                 project
Flask-Librato (0.0.1)                          -
Flask-Lock (0.0.1)                             -
Flask-Mage2Connector (0.0.1)                   - Use to connect Magento 2.
flask-manager (0.0.1a0)                        - A CRUD manager for Flask
flask-metrics (0)                              -
Flask-MongoMyAdmin (0.1)                       - Simple MongoDB Administrative
                                                 Interface for Flask
flask-multistatic (1.0)                        - Simple flask plugin to allow
                                                 overriding static files
Flask-OmMongo (1.0)                            - Add Flask support for MongoDB
                                                 using OmMongo.
Flask-Pika-NG (0.3.3)                          - Pika amqp flask extension
flask-ratelimit (0.0.1)                        -
Flask-ResponseFactory (0.1)                    - Create Flask response objects
                                                 in a declarative way
Flask-RESTive-MongoDB (0.0.1)                  - Flask-RESTive extension to
                                                 work with MongoDB.
Flask-Search (0.01)                            -
Flask-Sendmail (0.1)                           - Flask extension for sendmail
Flask-Shopify (0.1)                            - Shopify Flask
flask-sleep (0)                                -
Flask-SQLAlchemy-Meiqia (2016.8.1)             - Adds SQLAlchemy support to
                                                 your Flask application
Flask-Static (0.1)                             - Generates a static website
                                                 from a Flask application
Flask-Stripe (0.1.0)                           - Flask-Stripe
Flask-TaskTiger (0.0.1)                        - Flask TaskTiger
flask-urls (0.9.2)                             - A collection of URL-related
                                                 functions for Flask
                                                 applications.
Flask-User-Social (0.0.1)                      - Role based user
                                                 authentication for Flask.
                                                 Extends Flask-User.
Flask-Watson (0.1.0)                           - Flask-Watson
Flask-WebSocket (1.0)                          - simple websocket for Flask
Flask-XML-RPC-Re (0.1.3)                       - Adds support for creating
                                                 XML-RPC APIs to Flask
flask-xuacompatible (0.1.0)                    - Sets X-UA-Compatible HTTP
                                                 header in your Flask
                                                 application.
Flask-YunPian (0.0.1)                          - Flask extension for YunPian
                                                 API
Flask-Forward (0.1.0)                          - Flask-Forward extension
                                                 provides auto discovery,
                                                 prioritization and rendering
                                                 of template for Flask based
                                                 on endpoint
Flask-GripControl (0.0.1)                      - Flask GripControl
flask-funktional-gae (0.0.1)                   - flask-funktional-gae
                                                 ~~~~~~~~~~~~~~~~~~~~  flask
                                                 extension to make functional
                                                 testing of flask applications
                                                 with the app engine sdk
                                                 easier.  used on top of the
                                                 `flask-funktional <http://git
                                                 hub.com/gregorynicholas
                                                 /flask-funktional>`_
                                                 extension, it provides setup
                                                 of app engine sdk stubs with
                                                 a focus on being transparent
                                                 and minimally invasive.
                                                 links `````  * `docs <http://
                                                 gregorynicholas.github.io
                                                 /flask-funktional-gae>`_ *
                                                 `source <http://github.com/gr
                                                 egorynicholas/flask-
                                                 funktional-gae>`_ * `package
                                                 <http://packages.python.org
                                                 /flask-funktional-gae>`_ *
                                                 `travis-ci <http://travis-
                                                 ci.org/gregorynicholas/flask-
                                                 funktional-gae>`_
Flask-Gladiator (0.1)                          - Gladiator is a Data
                                                 Validation Framework for
                                                 Python3 (Flask Plugin)
Flask-GoogleFed (0.1)                          - Google Federated Logins for
                                                 Flask.
Flask-gzip (0.1)                               - Compress responses in your
                                                 Flask app with gzip.
Flask-Habitat (0.1)                            - Selectively load Flask
                                                 configuration values from
                                                 environment variables at
                                                 runtime.
flask-handlers (0.0.1)                         - Handlers for Flask
                                                 applications
flask-inliner (1.0.0)                          - Flask-Inliner converts CSS
                                                 <style> blocks to inline
                                                 style attributes
Flask-Intercom (0.1.0)                         - Flask-Intercom
Flask-JsonSchemer (0.0.1)                      - Flask extension for
                                                 validating JSON requets
Flask-JSON-Validation (0)                      -
Flask-Kadabra (0.1.0)                          - Flask extension for the
                                                 Kadabra metrics framework
flask-keystone (0.2)                           - This project wraps the
                                                 existing keystone middleware
                                                 to provide courtesy user
                                                 functions within an API.
Flask-Landing (0.1.0)                          - Landing page for collecting
                                                 emails.
Flask-Latch (0.1.0)                            - Latch extension for Flask
Flask-LiveScript (0.1)                         - implements the webassets
                                                 filter for livescript
Flask-MenuBuilder (0.9.2)                      - An easy way to create menus
                                                 to use with flask.
Flask-MongoObject (0.1)                        - Access MongoDB from your
                                                 Flask application
Flask-MultipleBlueprint (0.1)                  - Decorate function using
                                                 multiple blueprints at once.
Flask-OldSessions (0.10)                       - Provides a session class that
                                                 works like the one in Flask
                                                 before 0.10.
Flask-Paranoid (0.1.0)                         - Simple user session
                                                 protection
Flask-Prometheus (0.0.1)                       - Prometheus client
                                                 instrumentation for flask.
                                                 See
                                                 http://github.com/sbarratt
                                                 /flask-prometheus
Flask-PyMssql (0.1.0)                          - PyMssql support for Flask
                                                 applications
Flask-Raptor (0.1)                             - Raptor support for Flask
Flask-Registry (0.2.0)                         - Flask-Registry is an
                                                 extension for Flask that
                                                 allow frameworks to
                                                 dynamically assemble your
                                                 Flask application from
                                                 reusable packages consisting
                                                 of blueprints, extensions,
                                                 and configurations.
flask-reveal (0.3)                             - Make reveal.js presentations
                                                 with Flask
flask-revise (0)                               -
Flask-RIP (0.1)                                -
Flask-Roughage (0.1)                           - Very short description
Flask-RouteLogger (0.1)                        - Logging the meta route level
                                                 request- response information
                                                 in the structured manner for
                                                 your flask web application
flask-routes (0.1.0)                           - Command line extension to
                                                 list all routes in a Flask
                                                 project
flask-secretbox-session (0.1.0)                - Flask client side session
                                                 serializer, using Sodium
                                                 SecretBox authenticated
                                                 encryption
flask-send-mail-util (0.1.0)                   - Send an email via the Flask-
                                                 Mail extension, using text
                                                 and HTML templates.
Flask-Share (0.1.0)                            - Create social share component
                                                 in Jinja2 template based on
                                                 share.js.
Flask-SimpleSQLA (1.0)                         - Extension providing basic
                                                 support of SQLAlchemy in
                                                 Flask applications
Flask-Slacker (0.0.1)                          - Adds support to your Flask
                                                 application using Slacker.
Flask-SocketAPI (0.2)                          - Lightweight library to create
                                                 streaming APIs over Flask-
                                                 SocketIO
Flask-SockJS (0.1.0)                           - Simple integration of Flask
                                                 and SockJS
Flask-Token (1.0)                              - 快速生成API认证令牌
Flask-Twilio (0.0.1)                           - Make Twilio voice/SMS calls
                                                 with Flask
Flask-UltraJSON (0.0.1)                        - Integrates UltraJSON with
                                                 your Flask application.
Flask-UrlDiscovery (1.1.1)                     - A Flask extension for
                                                 discovering urls in a
                                                 service. Automatically
                                                 exposes urls for a service
flask-uuid-utils (0.1.0)                       - Utilities for working with
                                                 UUID fields in Flask.
Flask-WebGlEarth (0.1.3)                       - Simple extension for Flask to
                                                 use WebGl Earth
Flask-Whiteprint (0.0.1)                       - An enhancement of flask
                                                 blueprint.
flask-wikimediaui (0.0.1)                      - This library provides python
                                                 Flask utilities and static
                                                 assets for rendering
                                                 Wikimedia UI elements
Flask-WX-OAuth (0.1.1)                         - Flask Extension for wechat
                                                 oauth2.0.
google-oauth-flask (0.0.1)                     - UNKNOWN
flask-funktional (0.0.1)                       - flask-funktional
                                                 ~~~~~~~~~~~~~~~~  flask
                                                 extension which hopes to make
                                                 functional testing easier.
                                                 links `````  * `documentation
                                                 <http://gregorynicholas.githu
                                                 b.io/flask-funktional>`_ *
                                                 `package
                                                 <http://packages.python.org
                                                 /flask-funktional>`_ *
                                                 `source <http://github.com/gr
                                                 egorynicholas/flask-
                                                 funktional>`_ * `development
                                                 version   <http://github.com/
                                                 gregorynicholas/flask-
                                                 funktional>`_
Flask-GzipBomb (0.1.0)                         - Gzip Bomb responses for Flask
Flask-Headers (1.0)                            - A Flask extension making
                                                 adding headers one decorator
                                                 away
Flask-ICU (0.9.1)                              - Adds i18n/l10n support to
                                                 Flask applications
flask-id (0.0.1)                               -
Flask-InfluxDB (0.1)                           - Flask bindings for the
                                                 InfluxDB time series database
Flask-JIRA (0.0.2)                             - Flask extension that provides
                                                 simple integration with JIRA
                                                 REST API
Flask-JSUtils (0.1)                            - Flask utilities in your
                                                 javascript
Flask-MakoTemplates (0.2)                      - All future development will
                                                 be done under the name Flask-
                                                 Mako at
                                                 <http://pypi.python.org/pypi
                                                 /Flask-Mako>
flask-multiconfig (0.1)                        - A simple extension to add
                                                 advanced configuration source
                                                 support.
flask-myapi (0.1)                              - Flask-MyAPI - RESTful support
                                                 library for Flask
Flask-Negotiate (0.1.0)                        - Content negotiation utility
                                                 for Flask apps
Flask-NextCaller (0.1.0)                       - Flask-NextCaller
Flask-NoExtRef (0.1)                           - Support for hiding external
                                                 URL
Flask-Notifications (v0.1.0.dev20150000)       -
Flask-oDesk (0.4.1.1)                          - Adds oDesk API support to
                                                 Flask
Flask-OrientDB (0.1)                           - A Flask extension for using
                                                 OrientDB with Flask
Flask-OtpAuth (0.0.1)                          - One Time Password
                                                 Authentication for Flask
Flask-Passlib (0.1)                            - Flask extension for passlib
flask-paypal (0.1.0)                           - Flask integration with
                                                 PayPal, mainly focused on
                                                 subscriptions.
Flask-Quik (0.1.1)                             - Quik for Flask
Flask-RequestID (0)                            -
Flask-Roots (0.0.1)                            - Lightweight personal git
                                                 server.
flask-rst (0.1)                                - Create a static website from
                                                 simple reStructuredText files
Flask-SaeStorage (0.9.0)                       - SAE Storage for Flask
flask-samurai (0.1)                            - Easily create Heroku addons
                                                 in Flask.
flask-schematics (0)                           -
flask-segmentio (0.1.0)                        - Adds SegmentIO support to
                                                 your Flask application
flask-shell-ptpython (0.0.1)                   - Replace the default `flask
                                                 shell` command with a similar
                                                 command running Ptpython.
flask-simple (0.0.1)                           - SimpleDB integration for
                                                 Flask.
Flask-Sixpack (0.0.1)                          - Flask wrapper for Sixpack
Flask-SPF (0.0.0)                              - Flask-SPF
Flask-SSLify-flexme (0.1.6)                    - Force SSL on your Flask app.
Flask-WeChat (0.1.0)                           - a simple flask extension for
                                                 setup wechat service.
flask-wechat-kit (0.0.1)                       - flask blueprint for wechat
flask-yeoman (0.1.0)                           - UNKNOWN
flask-zabbix (0.1.1)                           - Zabbix API wrapper
Flask-ZODB (0.1)                               - Use the ZODB with Flask
nickw-flask-utils (1.2.1)                      - A set of utilities to make
                                                 working with flask web
                                                 applications easier.
Flask-Webhook (0.1.0)                          - Create Flask application
                                                 webhooks with attached
                                                 handlers
flask-webpackext (0.1.0)                       - Webpack integration for
                                                 Flask.
Flask-WkHTMLtoPDF (0.1.0)                      - Convert JavaScript dependent
                                                 Flask templates into PDFs
                                                 with wkhtmltopdf.
flask-ws (0.0.1.0)                             - Websocket for flask.
flask-wysiwyg (0.1)                            - flask-wysiwyg provides custom
                                                 form fields to render wysiwyg
                                                 editor instead of regular
                                                 textareas. It takes care of
                                                 cleaning html for you too.
                                                 With its super secure
                                                 defaults you do not want to
                                                 modified it's whitelisting
                                                 rules.
Flask-XStatic (0.0.1)                          - Flask support for XStatic
                                                 assets
Flask-FluidDB (0.1)                            - Fluiddb access for flask
Flask-FontAwesome-Headers (0.1.0)              - Sets CORS HTTP response
                                                 headers for Font-Awesome
                                                 files served by Flask's
                                                 send_file().
flask-gae (0.1.0-20140530)                     - Commons for Flask running on
                                                 Google App Engine
Flask-HipPocket (0.2.0b1)                      - A wrapper around Flask to
                                                 ease the development of
                                                 larger applications
Flask-HttpCaching (0.01)                       - flask http caching
Flask-HTTPS (0.1.0)                            - Make HTTPS required on any
                                                 Flask app
Flask-Imagine-GoogleAdapter (0.4)              - Google Cloud Storage adapter
                                                 for Flask-Imagine extension.
Flask-Imagine-S3Adapter (0.4)                  - Amazon AWS S3 adapter for
                                                 Flask-Imagine extension.
flask-jade2underscore (0.1)                    - A small Flask extension adds
                                                 suppot to Jade2Underscore
                                                 templates compiler (used in
                                                 Backbone) to Flask.
Flask-Maoko (0.1.1)                            - Mako templating support for
                                                 Flask applications.
Flask-Material-Lite (0.0.1)                    - An easy way to get started
                                                 with Google's Material Lite
                                                 in your next Flask project,
                                                 without any boilerplate code.
flask-memcache-session (2.0)                   - Use memcache for store
                                                 session data
Flask-Mime (0.1.0)                             - Provides MIME type based
                                                 request dispatching
                                                 mechanism.
Flask-Modus (0.0.1)                            - Flask Method Overriding
                                                 Middleware.
Flask-mongobit (0.1.2)                         - MongoBit support in Flask
flask-morepath (0.1)                           - UNKNOWN
flask-nap (0.0.1)                              - Flask REST Framework
Flask-OAuth2Server (0.1)                       - Flask-OAuth2Server allows you
                                                 to quickly add an OAuth2
                                                 provider to your Flask
                                                 application.
Flask-Obscure (0.1.2)                          - Obscure numerical IDs in URLs
flaskpress-flask-htmlbuilder (0.13)            - Fork of Flexible Python-only
                                                 HTML generation for Flask
Flask-PubSub (0.1.0)                           - Flask-PubSub
Flask-QSSession (0.3.0)                        - Add server-side session
                                                 support for Flask application
Flask-Resource (0.0.1)                         - Build resource-oriented Web
                                                 apps with Flask.
Flask-RethinkDB (0.2)                          - Adds RethinkDB support to
                                                 Flask
Flask-Sandbox (0.1.0)                          - ACL Route controls for Flask
flask-schema (0.1a)                            - Schema Validation for your
                                                 JSON APIs
Flask-SQLAlchemy-tw (3.0-dev-20160331)         - Adds SQLAlchemy support to
                                                 your Flask application
Flask-SRI (0.1.0)                              - Flask-SRI
flask-stacksentinel (1.2.1)                    - Stack Sentinel error tracking
                                                 integration with Flask
flask-stylus2css (0.1)                         - A small Flask extension that
                                                 adds Stylus support to Flask.
flask-swaggerui (0.0.1)                        - This library provides python
                                                 Flask utilities and static
                                                 assets for rendering Swagger
                                                 UI
flask-thumbor (0.1.0)                          - Flask utilities to use
                                                 thumbor images.
Flask-Tiger (0.1.2)                            - api client for flask
                                                 extension
Flask-Transit (0.1.0-pre)                      - A flask extension for working
                                                 with transit data.
Flask-Tweepy (0.1)                             - Tweet easily from Flask
                                                 applications
hyperdns-flask (0.9.4)                         - HyperDNS Flask Utilities
launchkey-flask (0.1.0)                        - LaunchKey authentication
                                                 extension for Flask
recast-flask-frontend (0.1.0)                  - new frontend for the RECAST
                                                 project
tdewitt_AC-Flask-HipChat (0.2.9.dev0)          - Atlassian Connect library
                                                 based on Flask for HipChat
flask-flywheel (0.1.0)                         - Adds Flywheel support to your
                                                 Flask application
Flask-Generator (0.1)                          - Generator tool to quickly
                                                 create flask application
                                                 skeleton.
Flask-Imagine-RackspaceAdapter (0.4)           - Rackspace Files adapter for
                                                 Flask-Imagine extension.
Flask-Keen (0.1.0)                             - Flask-Keen
flask-lambda2 (1.0.0)                          - Python package to add
                                                 compatibility between Flask
                                                 and AWS Lambda for creating
                                                 RESTful applications.
Flask-Leancloud-Sms (0.1)                      - Leancloud SMS Service for
                                                 Flask
flask-letsencrypt (0.1)                        - UNKNOWN
flask-log (0.1.0)                              - Configure logging in flask
                                                 applications
Flask-MongoRest-Swagger (0.1)                  - Swagger API generation for
                                                 Flask-MongoRest
Flask-MoSession (0.2)                          - Mongodb based server side
                                                 session management system for
                                                 Flask
flask-negotiate2 (0.2.0)                       - Content negotiation utility
                                                 for Flask apps
Flask-NIH (0.1.0.dev1)                         - A toolkit to write static
                                                 site generators using Flask
                                                 as a basis.
Flask-NSQ (0.1.0)                              - Adds NSQ support for your
                                                 Flask application
Flask-OAuth2 (0.01)                            -
flask-oslolog (0.1)                            - This project wraps the
                                                 existing oslo.log library to
                                                 providerequest logging and
                                                 logger access within flask..
Flask-PAM (0.1rc1)                             - Flask authentication using
                                                 PAM
Flask-Philo (3.0.0)                            - Simple web framework based on
                                                 Flask
Flask-PJAX (0.0.1)                             - PJAX Templating for Flask
                                                 Applications
Flask-Pony (1.0.1)                             - PonyORM for your Flask
                                                 application
Flask-PyOTP (0.0.1)                            - PyOTP warpper for flask.
Flask-Redlock (0.0.2)                          - Adds redis lock support to
                                                 your Flask application
Flask-Register (0.1.0)                         - A extension of Flask to
                                                 control Register view.
Flask-RegisterBlueprints (0.1.0)               - Dynamically register Flask
                                                 blueprints on application
                                                 object
Flask-ResponseExt (0.2.0)                      - An extension of the Flask
                                                 Response class.
Flask-RESTbolt (0.1.0)                         - Powerful and fast framework
                                                 for creating REST APIs with
                                                 Flask
flask-restful-swagger-flexme (0.20)            - Extract swagger specs from
                                                 your flast-restful project
flask-r-login (0.0.1)                          -
Flask-Scaffold (0.5.1)                         - Scaffold Database
                                                 Applications in MySQL or
                                                 PostgreSQL with Flask
flask-simple-login (0.0.1)                     - Easily turn your python data
                                                 into a flot graph in a static
                                                 html file.
Flask-SocialShare (0.0.1)                      - Flask social sharing helpers
flask-spring (0.1.0)                           - Adds the Spring framework
                                                 support to your Flask
                                                 application
Flask-SQLService (0.1.0)                       - Flask extension for
                                                 sqlservice
Flask-SSDB (0.0.1)                             - Flask simple ssdb client
flask-structlog (0)                            -
flask-toolbox (0.0.2)                          - A flask toolbox.
Flask-Upload (0.0.1)                           - A simple and brief utility
                                                 tools framework
Flask-UserEnvConfig (0.1.12)                   - Configure a flask app with
                                                 environment variables or a
                                                 file.
Flask-Validictory (0.1.0)                      - Simple integration between
                                                 Flask and Validictory.
flask-zappa (0.0.1)                            - Serverless Flask With AWS
                                                 Lambda + API Gateway
restaurant-service-flask (0.1.0)               - Restaurant Service - Flask
                                                 Version
nailpack-flask (0.1.0)                         - Flask support for nails
toga-flask (0.0.0)                             - A Flask backend for the Toga
                                                 widget toolkit.
quokka-flask-security (1.7.4dev2)              - Fork of Simple security for
                                                 Flask apps
Flask-Ink (3.1.10)                             - Easily integrate Sapo Ink's
                                                 framework in your Flask
                                                 project.
flask-ipblock (0.3)                            - Block certain IP addresses
                                                 from accessing your Flask app
flask-itemshop (0.2)                           - Simple flask blueprint
                                                 (ItemBP) that you can mount
                                                 in your app to get a basic
                                                 purchase flow for a single
                                                 item. Credit card processing
                                                 is done with stripe.js and
                                                 the stripe python API.
Flask-JsonSchemaValidator (0.2)                - Basic JSON Schema Validator
                                                 for the Flask web framework.
flask-jsontools-slippers (0.1.6)               - JSON API tools for Flask
Flask-Kerberos (1.0.4)                         - Kerberos authentication
                                                 support for Flask
Flask-Manifest (0.2.0)                         - Asset manifest integration
                                                 with Flask.
Flask-MarrowMailer (0.2.0)                     - Marrow Mailer integration for
                                                 Flask.
flask-MenuManager (1.0a2)                      - An easy way to build and
                                                 manage menus in Flask
flask-notifyAll (1.0.3)                        - Simple tool which will
                                                 provide sms and email
                                                 notifications
Flask-Postmark (0.2.0)                         - Postmark Flask extension
Flask-Project (0.1.1)                          - Flask project template
                                                 generator.
Flask-RateLimiter (0.2.0)                      - Flask-RateLimiter is an
                                                 extension for Flask that adds
                                                 support for rate limiting.
Flask-Redistore (1.0.1)                        - Adds Redis support to your
                                                 Flask applications
Flask-ReqArg (0.1.5)                           - The decorator that maps
                                                 request arguments into
                                                 function arguments.
flask-request-id (0.1)                         - Extract yourself some Request
                                                 IDs.
Flask-SlimREST (0.1.1)                         - Flask extension for building
                                                 RESTful APIs
Flask-SSE (0.2.1)                              - Server-Sent Events for Flask
Flask-StatsD (0.1.1)                           - Access to statsd in your app.
Flask-Webhelpers (0.1)                         - Simple integration of Flask
                                                 and Webhelpers
Flask-Fleem (0.0.5)                            - Theming for Flask
                                                 applications
Flask-Gist (0.1.1)                             - A simple flask extension to
                                                 render Github Gists on
                                                 template
thunderdome-flask (1.0.2)                      - Thunderdome Flask integration
Flask-FlatPagesCut (0.5.1)                     - Flask-FlatPagesCut is fork
                                                 Flask-FlatPages (Provides
                                                 flat static pages to a Flask
                                                 application)
Flask-fluentd (0.2)                            - Log fluentd events from Flask
Flask-Fundatio (0.1)                           - Flask extension to integrate
                                                 the Foundation front-end
                                                 framework
flask-gae_messages (1.0.1)                     - Flask extension for working
                                                 with messages using the mail
                                                 & xmpp apis on App Engine.
flask-gemoji (0.2.0)                           - Add gemojis to your Flask
                                                 apps
Flask-Heroku-Helpers (0.0.2)                   - Flask helpers for Heroku Apps
Flask-Heroku-Runner (2)                        - Minimalist Heroku bootstrap
                                                 for Flask
flask-http2-push (0.0.3)                       - A Flask extension to add
                                                 http2 server push to your
                                                 application.
Flask-JsonSchema (0.1.1)                       - Flask extension for
                                                 validating JSON requets
Flask-OpenAPI (0.1.0a1)                        - Generate a swagger.json
                                                 handler from a Flask app
Flask-Paginated-Response (1.0.1)               - Response maker for Flask with
                                                 RFC Standards such as Link
                                                 Headers
flask-request-id-middleware (1.1)              - Adds Request ID inside your
                                                 http requests to better
                                                 identify what's happening on
                                                 your app
Flask-Restdoc (0.0.2)                          - Flask-Restdoc is a simple
                                                 tool that generates RESTful
                                                 API documentation
                                                 automatically from python
                                                 files.
flask-restless-swagger (0.2.1)                 - Magically create swagger
                                                 documentation as you
                                                 magically create your RESTful
                                                 API
Flask-SAPB1 (0.0.2)                            - Use to connect SAP B1 DI API.
Flask-SL (0.0.4)                               - Basic recognition of Second
                                                 Life® requests.
Flask-Stache (0.1.1)                           - Simple mustache templating
                                                 for Flask applications
Flask-Theme (0.2.0)                            - Provides infrastructure for
                                                 theming Flask applications
flask-thumbs (1.2)                             - An extension managing
                                                 thumbnail based on flask-
                                                 thumbnails
flask-tml (0.3.1)                              - Flask SDK for
                                                 tranlationexchange.com API
Flask-Wdb (0.0.2)                              - Integrate Wdb instead of
                                                 Werkzeug debugger for Flask
                                                 applications
graphql-flask (1.1.0)                          - Adds GraphQL support to your
                                                 Flask application
flask-graphql-subscriptions-transport (0.1.4)  - Adds subscription transport
                                                 layer for Flask applications
                                                 using GraphQL
Flask-GSA (0.1.1)                              - A simple wrapper for the
                                                 Google OAuth2 client library
Flask-Gunicorn (0.1.1)                         -
Flask-Hashing (1.1)                            - Easy hashing of data in Flask
Flask-Inject (1.1.0)                           - A micro dependency injection
                                                 framework for Flask micro web
                                                 framework :)
Flask-Jigger (0.0.2)                           - Web APIs for Flask,
                                                 unintrusive.
Flask-JWTAuthorization (0.0.5)                 - Authorization framework based
                                                 on JWT for Flask applications
Flask-Migrate-tw (1.8.1)                       - A custom version of Flask-
                                                 Migrate, which depends on
                                                 Flask-SQLAlchemy-
                                                 tw(v3.0)using Alembic
flask-mixpanel (0.1.1)                         - Wrappers for using Mixpanel
                                                 in Flask
Flask-MongoSet (0.1.8)                         - Access MongoDB from your
                                                 Flask application
Flask-NYC (0.1.1)                              - New York Flask Meetup
Flask-Pagination (0.0.1)                       - Pagination Helpers for Flask
                                                 Apps
flask-passwordless (0.1.1)                     - Flask extension for
                                                 passwordless login
Flask-Phrase (1.0.0)                           - Connect your Flask apps to
                                                 PhraseApp, the powerful in-
                                                 context-translation solution.
Flask-SACore (0.0.3)                           - SQLAlchemy Core extension for
                                                 Flask
Flask-SES (0.1.1)                              - Flask extension for
                                                 interfacing with AWS' SES
                                                 service
flask-sqlalchemy-rls (0.0.2)                   - Flask-SQLAlchemy with row-
                                                 level security
Flask-Storage (0.1.1)                          - Flask upload and storage
                                                 extensions.
Flask-Storage-Helpers (0.1.5)                  - Various file storage backends
                                                 for Flask apps.
flask-template-loader (0.0.3)                  - UNKNOWN
Flask-Triangle-joeflack4 (0.5.6)               - Integration of AngularJS and
                                                 Flask, originally created by
                                                 Morgan Delahaye-Prat
                                                 (mdp@m-del.fr).
flask-wtf-storage (0.0.2)                      - extend flask-wtf to use
                                                 google storage
labirinto-flask (0.1.1)                        - Joguinho de labirinto usando
                                                 Flask + GTM
sockjs-flask (0.3)                             - SockJs for Flask
Flask-UUID (0.2)                               - UUID url converter for Flask
                                                 routes
Flask-WatQY (0.0.3)                            -
Flask-WTF-Polyglot (0.2)                       - Flask-WTF companion library
                                                 providing `PolyglotForm` for
                                                 polyglot HTML output
Flask-Zurb-Foundation (0.2.1)                  - A Foundation Wrapper for
                                                 Flask
Flask-FormEncode (0.10.1)                      - A form validation extension
                                                 for Flask using the
                                                 FormEncode package.
flask-go (0.1.1)                               - Let you create flask project
                                                 like use django-admin
flask-heroku-mongoengine (0.1.5)               - Heroku environment variable
                                                 configurations for Flask
Flask-Heroku-RQify (0.2)                       - Automatic RQ configuration
                                                 for your Heroku Flask
                                                 applications.
Flask-libsass (1.1.0)                          - Flask extension for building
                                                 css from sass or scss
Flask-Mobility (0.1.1)                         - A Flask extension to simplify
                                                 building mobile-friendly
                                                 sites.
Flask-MySQLdb (0.2.0)                          - MySQLdb extension for Flask
Flask-OAuthRes (0.2.0)                         - OAuth Resource for Flask
Flask-PaperTrail (0.0.2)                       - Adds PaperTrail logging to
                                                 your Flask application
Flask-Pigeon (0.11.0)                          - Flask messages extension.
Flask-PyFCM (0.1.1)                            - Flask extension for PyFCM
Flask-PyQuery (0.1)                            - PyQuery templating support
                                                 for Flask applications.
Flask-QiniuStorage (0.9.4)                     - Qiniu Storage for Flask
flask-rollbar (1.0.1)                          - A sane configuration for
                                                 Rollbar for Flask selfishly
                                                 based on my own needs
Flask-Router (0.1.1)                           - Tuned flask's URL routing
                                                 library
Flask-RQ (0.2)                                 - RQ (Redis Queue) integration
                                                 for Flask applications
Flask-Sass (0.9)                               - A small Flask extension that
                                                 makes it easy to use Sass
                                                 with your Flask application.
Flask-Shelve (0.1.1)                           - Shelve support for Flask
Flask-Sockets-Tornado (0.1.1)                  - Elegant WebSockets for your
                                                 Flask apps.Tornado style app
                                                 included
Flask-Sphinx-Themes (1.0.1)                    - Sphinx themes for Flask and
                                                 related projects.
flask-tmpl (0.2.0)                             - PasteScript templates for the
                                                 Flask+Celery+SQLAlchemy
Flask-Travis (0.0.2)                           - Easily fetch Travis CI
                                                 environment variables when
                                                 testing.
Thread-Flask-Prometheus (0.0.3)                - Prometheus client
                                                 instrumentation for flask.
Flask-FlatPages-Pandoc (0.2)                   - Pandoc rendering for Flask-
                                                 FlatPages
Flask-Gfwlist2Pac (0.0.2)                      - Flask application to generate
                                                 PAC file based on gfwlist
Flask-httpretty (1.3.0)                        - flask-httpretty help you to
                                                 mock http requests via flask.
flask-lesscss (0.9.1)                          - A small Flask extension that
                                                 adds LessCSS support to
                                                 Flask.
Flask-Mistune (0.1.1)                          - A interface between the Flask
                                                 web framework and the Mistune
                                                 Markdown parser.
Flask-OlinAuth (1.0.1)                         - A simple Flask extension
                                                 implementing Olin's
                                                 authentication
flask-optimize (0.2.6)                         - Flask optimization: cache,
                                                 minify html and gzip response
flask-otp (1.2)                                - One-Time Password extension
                                                 to Flask
Flask-Profile (0.2)                            - Flask Application Profiler
flask-project-templates (0.2)                  - Paster templates for creating
                                                 Flask projects
Flask-Pyco (0.2)                               - Simple flat file CMS inspired
                                                 by Pico and Jekyll
Flask-Reggie (0.0.2)                           - Flask Regex Routes.
Flask-Responses (0.2)                          - Simple response utility for
                                                 Flask
Flask-REST (1.1)                               - A simple REST toolkit for
                                                 Flask
flask-robohash (1.0.1)                         - robohash.org avatars that you
                                                 can use with the
                                                 microframework Flask.
Flask-SAResource (0.1.1)                       - Flask extension for building
                                                 routes from SQLAlchemy models
Flask-SOEditor (0.1.2a0)                       - A Stack Overflow editor
                                                 extension for Flask.
flask-sqlacodegen (1.1.6.1)                    - Automatic model code
                                                 generator for SQLAlchemy with
                                                 Flask support
Flask-SQLAlchemy-Session (1.1)                 - SQL Alchemy session scoped on
                                                 Flask requests.
flask-swagger-plus (0.0.3)                     - extract swagger spec from
                                                 source code and docstring for
                                                 a flask app
flask-telegram (0.0.2)                         - flask-telegram  flask
                                                 extension for delivering
                                                 messages. send via the app
                                                 engine mail or xmpp apis,
                                                 and/or other third party
                                                 providers such as sendgrid.
                                                 links:  * docs: http://gregor
                                                 ynicholas.github.io/flask-
                                                 telegram * source: http://git
                                                 hub.com/gregorynicholas
                                                 /flask-telegram * package:
                                                 http://packages.python.org
                                                 /flask-telegram * travis-ci:
                                                 http://travis-
                                                 ci.org/gregorynicholas/flask-
                                                 telegram
flask-transfer (0.1.0)                         - Validate and process file
                                                 uploads in Flask easily
flask-utils (0.1.1)                            - Various Flask utilities.
flask-whooshalchemy3 (0.1.1)                   - Whoosh indexing capabilities
                                                 for Flask-SQLAlchemy, Python
                                                 3 compatible.
Flask-WXApp (0.1.2)                            - Flask Extension for WeChat
                                                 App.
Flask-Zen (0.2)                                - Flask-Script commands to
                                                 integrate with PyZen.
Flask-Hopak (0.1.0)                            - Admin interface for Flask
                                                 that uses Hopak models
flask-lazyapi (0.4.8)                          - A Simple, Restful MongoDB
                                                 Server built on Flask and
                                                 Flask-Classy
Flask-MicroServices (0.34.5)                   - Self contained modules and
                                                 Django style URL routing for
                                                 Flask.
Flask-Multi-Session (0.2.0)                    - Mongo multidevice sessions
                                                 for Flask apps
Flask-PagedList (0.2.1)                        - Add pypagedlist support for
                                                 Flask
Flask-PluginEngine (0.3.1)                     -
Flask-Pushjack (1.0.0)                         - Flask extension for push
                                                 notifications on APNS (iOS)
                                                 and GCM (Android).
Flask-RestClient (0.1.2)                       - restful api client for flask
                                                 extension
Flask-RESTive-Identifiers (0.0.3)              - Flask-RESTive extension to
                                                 work with identifiers.
flask-rethinkview (0.1.2)                      - RESTful Flask View with
                                                 RethinkDB
Flask-ShellPlus (0.0.3)                        - UNKNOWN
Flask-Simple-Serializer (1.1.3)                - Simple Serializers for API
                                                 validations
Flask-Sockets (0.2.1)                          - Elegant WebSockets for your
                                                 Flask apps.
Flask-Soy (0.3)                                - Provides support for Closure
                                                 Templates (Soy) in Flask.
Flask-Twisted (0.1.2)                          - Simple integration of Flask
                                                 and Twisted
Flask-WeRoBot (0.1.2)                          - Writing WeChat Robot by
                                                 WeRoBot in Flask.
Flask-Zero (0.9.6)                             - Qiniu Storage for Flask
flask-gae_blobstore (1.0.2)                    - Flask extension module for
                                                 working with the blobstore &
                                                 files apis on App Engine.
Flask-HAL (1.0.4)                              - Provides easy integration of
                                                 the HAL specification for
                                                 your REST Flask Applications.
Flask-HashFS (0.3.0)                           - Flask extension for HashFS, a
                                                 content-addressable file
                                                 management system.
Flask-HMAC (0.1.3)                             - Flask HMAC generator,
                                                 checker, and route decorator
Flask-JWT-Simple (0.0.3)                       - Simple JWT integration with
                                                 Flask
Flask-Kaccel (1.0.1)                           - Add Flask support for Nginx
                                                 X-Accel
Flask-MongoNorm (0.2.0)                        - MongoNorm support for Flask
                                                 applications
Flask-naver (1.2)                              - Oauth2 wraper for Naver login
Flask-Navigation (0.2.0)                       - The navigation of Flask
                                                 application.
Flask-Neo4jDriver (0.2.0)                      - Flask extension for official
                                                 neo4j python driver.
Flask-Pilot (0.5.0)                            - Flask-Pilot is a Flask
                                                 extension that adds structure
                                                 and map your views and
                                                 templates together for rapid
                                                 application development
Flask-Simon (0.3.0)                            - Simple MongoDB Models for
                                                 Flask
flask-sparkle (0.2.1)                          - Flask app that publishes
                                                 Sparkle update feeds
flask-sqlite_admin (0.3)                       - SQLite DB Management
                                                 Blueprint for Flask
                                                 Applications
Flask-Storm (0.1.2)                            - Storm integration for Flask.
Flask-Thunderargs (0.3.1)                      - Implements thunderargs to
                                                 flask framework.
Flask-Views (0.2.1)                            - Class based views for Flask
Flask-XML-RPC (0.1.2)                          - Adds support for creating
                                                 XML-RPC APIs to Flask
Humanize-Flask (0.2.0)                         - Common humanization utilities
                                                 for Flask applications.
sa-flask-restful-resource (0.0.3)              - base class for sqlalchemy and
                                                 flask-restless
Flask-Healthcheck (0.1.2)                      - Healthchecks for flask
                                                 applications made easy
flask-hmacauth (0.3.9)                         - A module to simplify working
                                                 with HMAC auth in Flask apps
Flask-ini (0.2.1)                              - Allow Flask to be configured
                                                 with configparser ini files
Flask-Inputs (0.2.0)                           - Flask request data validation
flask-ldap-login (0.3.0)                       - UNKNOWN
Flask-Mitten (0.2.1)                           - Adds security functions to
                                                 Flask applications for
                                                 preventing some of the basic
                                                 threats.
flask-mongo-model (0.0.3a4)                    - A module provides basic ORM
                                                 feature for MongoDB to Flask
                                                 applications.
Flask-Obscurity (0.4)                          - Security-by-obscurity. Move
                                                 along, nothing to see here.
flask-oojsui (0.0.3)                           - This library provides python
                                                 Flask utilities and static
                                                 assets for rendering
                                                 Wikimedia UI elements
Flask-Pystmark (0.11.1)                        - A Flask extension for
                                                 Postmark API library Pystmark
Flask-QueryInspect (0.1.2)                     - Flask extension to provide
                                                 metrics on SQL queries per
                                                 request.
Flask-RESTive (0.0.3)                          - Flask RESTive is a REST API
                                                 Flask extension based on
                                                 Flask-RESTful & Marshmallow.
Flask-reStructuredText (1.2)                   - Small extension to make using
                                                 rst easy
Flask-Rev (0.1.2)                              - Easily integrate flask with
                                                 revisioned static files
Flask-Routing (0.0.21)                         - Alternative web.py style
                                                 routing for Flask
Flask-Sendwithus (1.0.2)                       - Forwards-compatible Flask
                                                 extension to interact with
                                                 the sendwithus API
Flask-SimpleMDE (0.3.0)                        - Flask-SimpleMDE - a Flask
                                                 extension for SimpleMDE
Flask-Sitemap (0.2.0)                          - Flask extension that helps
                                                 with sitemap generation.
Flask-Split-JS (0.2.1)                         - A JavaScript library for
                                                 Flask-Split.
Flask-TokenAuth (0.1.0)                        - Token-based authentication
                                                 for Flask routes
flask-wdb-hook (0.1.2)                         - Hook to replace flask
                                                 werkzeug debugger with wdb.
Flask-YAMLConfig (0.0.3)                       - YAML configurator for Flask
                                                 app.
flask-ypaginate (0.1.3)                        - Pagination for Flask
Flask-GCM (0.2.0)                              - Flask-GCM is a simple wrapper
                                                 for the python-gcm library to
                                                 be used with Flask
                                                 applications.
Flask-GSSAPI (1.1.1)                           - HTTP Negotiate (GSSAPI)
                                                 authentication support for
                                                 Flask applications.
Flask-HTAuth (0.1.2)                           - Easy to integrate basic HTTP
                                                 authentication for Flask apps
Flask-JSONPages (0.2)                          - Provides static pages to a
                                                 Flask application based on
                                                 JSON
Flask-Meter (0.1.2)                            - Flask-Meter adds a monitoring
                                                 endpoint for consuming
                                                 application host metrics.
flask-restful-routing (1.0.3)                  - An easier way to register
                                                 flask-restful routes
Flask-RSTPages (0.3)                           - Adds support for
                                                 reStructuredText to a Flask
                                                 application
Flask-Runner (2.1.1)                           - A set of standard command
                                                 line arguments for Flask
                                                 applications built on top of
                                                 Flask-Script
Flask-ServerInfo (0.1.2)                       - Flask server info view for
                                                 inspecting server app and
                                                 user requests
Flask-Sillywalk (2.1)                          - So you want to implement an
                                                 auto-documenting API?
Flask-SimpleACL (1.2)                          - Simple ACL extension
Flask-Spyne (0.3.1)                            - A Flask extension, provides
                                                 support for Spyne.
Flask-ThriftClient (0.2.0)                     - Adds thrift client support to
                                                 your Flask application
Flask-Upwork (1.0-pre2)                        - Upwork API support to Flask
Webstack-Flask-JWT (0.4)                       - JWT token authentication for
                                                 Flask apps
Flask-GAE-Mini-Profiler (0.1.2)                - Flask integration of
                                                 gae_mini_profiler
flask-gae_tests (1.0.2)                        - Flask Extension with base
                                                 test cases to simplify
                                                 testing Flask applications on
                                                 App Engine.
Flask-Geckoboard (0.2.1)                       - Geckoboard custom widgets for
                                                 Flask projects
Flask-GoogleCharts (0.0.3)                     - Google Charts API support for
                                                 Flask
Flask-Humanize (0.3.0)                         - Common humanization utilities
                                                 for Flask applications.
Flask-Hypertable (0.3.0)                       - A Flask extension for
                                                 Hypertable over Thrift.
Flask-Log-Request-ID (0.9.4)                   - Flask extension that can
                                                 parse and handle multiple
                                                 types of request-id sent by
                                                 request processors like
                                                 Amazon ELB, Heroku or any
                                                 multi-tier infrastructure as
                                                 the one used for
                                                 microservices.
Flask-MimeRender (0.1.3)                       - RESTful resource variant
                                                 rendering using MIME Media-
                                                 Types, for the Flask Micro
                                                 Web Framework
flask-mongo-sessions (0.2.1)                   - Server-side sessions for
                                                 Flask with MongoDB
Flask-ObjectRocket (0.2.1)                     - User authentication with the
                                                 ObjectRocket API.
flask-orator (0.2.0)                           - Adds Orator support to your
                                                 Flask application
Flask-RedisSession (0.1.2.0)                   - add server-side session,
                                                 stored by Redis
flask-resty-shared-session (0.1.2)             - An adapted flask-session
                                                 module and corresponding
                                                 OpenResty package, so flask
                                                 and Nginx can share session
                                                 information.
Flask-Settings (0.0.3)                         - Flask settings extension is
                                                 similar to Django settings.
Flask-SSO (0.4.0)                              - Flask-SSO extension that
                                                 eases Shibboleth
                                                 authentication.
Flask-Stats (1.0.1)                            - A flask plugin to keep stats
                                                 about your application
Flask-Swag (0.1.2)                             - Build swagger spec with
                                                 Flask.
Flask-thridy (0.0.3)                           - simple use thridy for login
                                                 you web
Flask-Zipkin (0.0.3)                           - An zipkin extension for Flask
                                                 based on py_zipkin.
quokka-flask-mongoengine (0.7.4)               - Fork of Flask support for
                                                 MongoDB and with WTF model
                                                 forms
Flask-Hooker (1.0.3)                           - Receive and manage webhooks
                                                 of several services at the
                                                 same time
Flask-Jsonpify (1.5.0)                         - A Flask extension adding a
                                                 decorator for JSONP support
Flask-JWT-Login (0.0.4)                        - Flask extension that helps
                                                 authentication using JWT
flask-konch (1.2.0.post0)                      - An improved shell command for
                                                 the Flask CLI
Flask-Mandrill (0.3)                           - Adds Mandrill support to
                                                 Flask applications
Flask-OASSchema (0.9.4)                        - Flask extension for
                                                 validating JSON requests
Flask-Psycopg2 (1.3)                           - postgresql adapter for Flask
Flask-RBAC (0.3.0)                             - RBAC support for Flask
flask-reverse-proxy (0.2.0.2)                  - A Flask extension for
                                                 applications in a reverse
                                                 proxy not at the root
Flask-SQLAlchemySession (0.0.4)                - UNKNOWN
Flask-Themes (0.1.3)                           - Provides infrastructure for
                                                 theming Flask applications
Flask-URS (0.1.3)                              - JWT token authentication
                                                 using NASA URS Oauth2 for
                                                 Flask apps
Flask-Venom (1.0.2)                            - Flask extension for the Venom
                                                 RPC framework
Flask-Widgets (0.4)                            - This extension provides basic
                                                 template widget feature for
                                                 Flask
kore-plugins-flask (0.0.4)                     -
Flask-Gulp (0.3.0)                             - Task executioner similar to
                                                 gulp for Python
Flask-FlatPages-Knitr (0.3.1)                  - Knitr preprocessing for
                                                 Flask-FlatPages
Flask-GeoIP (0.1.3)                            - Flask-GeoIP -------------
                                                 Simple Flask extension for
                                                 pygeoip.
Flask-Hierarchy (0.1.1)                        - Finally working permission
                                                 manager for Flask!
Flask-JSONRPC (0.3.1)                          - Adds JSONRPC support to
                                                 Flask.
flask-lambda (0.0.4)                           - Python module to make Flask
                                                 compatible with AWS Lambda
                                                 for creating RESTful
                                                 applications
Flask-Mailer (0.4.0)                           - A Flask extension for sending
                                                 emails with pluggable
                                                 backends.
Flask-MAuth (1.1)                              - MAuth Client and Server
                                                 Library for MAuth
flask-media (0.4.6)                            - Flask extestion helper
                                                 uploads files
Flask-MetaRoute (1.3.0)                        - Extra routing capabilities
                                                 for Flask
Flask-NewProject (0.2.1)                       - Create new Flask project.
Flask-Pages (0.1.4)                            - Another? flask extension that
                                                 provides dynamic pages.
Flask-WaffleConf (0.3.1)                       - Store variables in database
                                                 and update them at runtime
Flask-wechatpy (0.1.3)                         - wechatpy for flask extension
Flask-Graylog (1.1.2)                          - Configure Graylog logging
                                                 handlers and middleware for
                                                 your Flask app
Flask-OAuth (0.12)                             - Adds OAuth support to Flask
Flask-QR (0.1.3)                               - Flask extension for
                                                 generating qr codes
Flask-ServiceLayer (0.0.4)                     - Base classes to create a
                                                 Service Layer in Flask.
flask-skel (0.4)                               - Basic Flask paster skeleton
                                                 template
py-jsonapi-flask (1.0.3b0)                     - The Flask extension for py-
                                                 jsonapi
Flask-Gears (0.2)                              - Gears for Flask
Flask-Github (0.1.3)                           - Adds support for authorizing
                                                 users with Github to Flask
Flask-Goat (0.2.1)                             - Flask plugin for security and
                                                 user administration via
                                                 GitHub OAuth & organization
Flask-Logging (0.1.3)                          - UNKNOWN
flask-macros (0.1.5)                           - macros for flask projects
Flask-Mailgun (0.4)                            - Adds Mailgun support to Flask
                                                 applications
Flask-Mako (0.4)                               - Mako templating support for
                                                 Flask applications.
Flask-MoreSQL (0.4)                            - Call PostgreSQL stored
                                                 procedures from Flask
flask-restplus-patched (0.1.3)                 - Extends Flask-RESTplus so it
                                                 can handle Marshmallow
                                                 schemas and Webargs
                                                 arguments.
Flask-SendGrid (0.5.2)                         - Adds SendGrid support to
                                                 Flask applications
flask-sqlalchemy-plus (0.1.3)                  -
Flask-TwitterBootstrap (0.0.4)                 - UNKNOWN
Flask-Init (0.0.3)                             - Easy way to create Flask Web
                                                 application
Flask-JIRA-Helper (0.2.0)                      - JIRA support for Flask
                                                 without breaking PyCharm
                                                 inspections.
Flask-JSGlue (0.3.1)                           - Flask-JSGlue helps hook up
                                                 your Flask application nicely
                                                 with the front end.
Flask-JSONPlus (0.0.4)                         - Flask extension for non-basic
                                                 types' serialization to JSON
                                                 via jsonplus lib.
flask-logsocketio (0.1.4)                      - Flask LogSocketIo module
Flask-Nicely (0.2.0)                           - Pretty Flask JSON responses
                                                 for API building.
flask-nidhogg (1.1.1)                          - OpenSource Yggdrasil protocol
                                                 implementation
flask-oauthprovider (0.1.3)                    - A full featured and secure
                                                 OAuth provider base
Flask-OpenERP (0.3.1)                          - OpenERP Connector for Flask
Flask-ReportableError (0.4.3)                  - handle errors that can be
                                                 reported to the web client
Flask-RESTify (0.1.3)                          - Flask REST framework
Flask-Run (0.1.3)                              - Flask-based web application
                                                 runner
Flask-SAML (0.4.3)                             - Flask SAML integration
Flask-Sessions (0.1.5)                         - Adds server-side session
                                                 support to your Flask
                                                 application
flask-shell (0.1.3)                            - Flask extension to improve
                                                 shell command for the Flask
                                                 CLI.
Flask-Shield (0.2.2)                           - Flask-Shield is an extension
                                                 of Flask for permission
                                                 management based on RBAC.
Flask-ShortUrl (0.2.0)                         - Short URL generaotr for Flask
Flask-Silk (0.2)                               - Adds silk icons to your Flask
                                                 application or blueprint, or
                                                 extension.
Flask-Stormpath-test (0.4.7)                   - Simple and secure user
                                                 authentication for Flask via
                                                 Stormpath.
Flask-Velox (2014.04.25)                       - Velox is a set of classes &
                                                 mixins to help rapidly build
                                                 Flask applications.
Flask-Weixin-Login (0.2.1)                     - Weixin Login from Flask
flask-yamli18n (0.1.7)                         - Use yaml files as translation
                                                 files in flask
kt-flask-sessions (0.1.3)                      - Kyoto Tycoon backed sessions
                                                 for Flask
quokka-flask-htmlbuilder (0.13)                - Fork of Flexible Python-only
                                                 HTML generation for Flask
pylint-flask (0.5)                             - pylint-flask is a Pylint
                                                 plugin to aid Pylint in
                                                 recognizing and understanding
                                                 errors caused when using
                                                 Flask
Flask-Jasmine (1.4)                            - Execution of Jasmine
                                                 JavaScript tests within Flask
Flask-JqueryUiBootstrap (0.5.0.4)              - Flask jQuery UI Bootstrap
                                                 minimalistic fork of Flask-
                                                 Bootsrap extension
Flask-Pure (0.5)                               - Flask-Pure - a Flask
                                                 extension for Pure.css
Flask-StatsdTagged (0.9)                       - Flask extension for sending
                                                 statsd data with tags, for
                                                 use with telegraf statsd
                                                 plugin
Flask-Triangle (0.5.4)                         - Integration of AngularJS and
                                                 Flask.
Flask-Twip (0.0.5)                             - twitter API proxy extension
                                                 for Flask microframework
Flask-Versioned (0.9.4-20101221)               - Add version info to file
                                                 paths.
flask-hype (0.1.4)                             - Flask extension for hype
Flask-IIIF (0.3.1)                             - Flask-IIIF extension provides
                                                 easy IIIF API standard
                                                 integration.
Flask-IndieAuth (0.0.3.2)                      - Allow requests to be
                                                 authenticated with
                                                 https://indieauth.com/
Flask-Nytro (1.2)                              - Nytro is an extension to help
                                                 the developers providing a
                                                 set of useful tools giving
                                                 even more facility to
                                                 development apps with Flask.
Flask-Pika (0.3.8)                             - Pika amqp flask extension
Flask-RestPoints (0.0.8)                       - Adds some common health check
                                                 endpoints (ping, time,
                                                 status)
Flask-Sleuth (0.0.6)                           - Spring Cloud Sleuth logging
                                                 implementation for Python
                                                 2/3.
Flask-WhooshAlchemy-Redux (0.7.1)              - Whoosh extension to
                                                 Flask/SQLAlchemy
Flask-With-Glasses (0.1.5)                     - Enhanced flask app with
                                                 livereload and webassets.
                                                 More suitable for front end
                                                 development
flask-htpasswd (0.3.1)                         - Basic authentication support
                                                 via htpasswd files in flask
                                                 applications
Flask-Idempotent (0.1.0)                       - Idempotent requests for Flask
                                                 applications
Flask-JWT (0.3.2)                              - JWT token authentication for
                                                 Flask apps
Flask-MongoKit (0.6)                           - A Flask extension simplifies
                                                 to use MongoKit
flask-nav (0.6)                                - Easily create navigation for
                                                 Flask applications.
Flask-Redis-Helper (1.0.0)                     - Redis support for Flask
                                                 without breaking PyCharm
                                                 inspections.
Flask-Redtask (0.3.1)                          - Redqueue integration for
                                                 flask
Flask-SocialAPI (1.0.5)                        - Simple api for controlling
                                                 and login to provider
Flask-Statics-Helper (1.0.0)                   - Provides Bootstrap3 and other
                                                 static resources in a modular
                                                 fashion.
Flask-WeasyPrint (0.5)                         - Make PDF in your Flask app
                                                 with WeasyPrint.
flask-geokit (0.1.7)                           - Geocoding toolkit
Flask-JWE (0.0.5)                              - Add Flask Support for JWE
                                                 Requests
flask-pytest (0.0.5)                           - Runs pytest in a background
                                                 process when DEBUG is True.
Flask-Rauth (0.3.2)                            - Adds OAuth 1.0/a, 2.0, and
                                                 Ofly consumer support for
                                                 Flask.
Flask-RedisConfig (0.3.0)                      - Redis-backed config for Flask
                                                 applications
Flask-Themes2 (0.1.4)                          - Provides infrastructure for
                                                 theming Flask applications
                                                 (and supports Flask>=0.6!)
Flask-Tracy (0.1.3)                            - Logs tracing information on a
                                                 per-request basis
Flask-Turbolinks (0.2.0)                       - Turbolinks for Flask.
li-flask-validation (1.0.4)                    - Flask Validation.
Flask-Fulfil (0.2.1)                           - Fulfil.IO for Flask Apps
Flask-GoogleAuth (0.4.2)                       - Super simple OpenID and
                                                 Google Federated Auth for
                                                 Flask apps.
Flask-kinesis (0.1.8)                          - Flask plugin for aws kinesis
                                                 stream
Flask-MakeStatic (0.3.0)                       - Make for your flask app
                                                 assets
Flask-PyMemcache (0.0.5)                       - pymemcache integration for
                                                 Flask
Flask-Redis-Sentinel (2.0.1)                   - Redis-Sentinel integration
                                                 for Flask
flask-rest4 (0.1.8)                            - Elegant RESTful API for your
                                                 Flask apps.
Flask-Scss (0.5)                               - Adds support for scss files
                                                 to Flask applications
Flask-SERVICE (0.1.4)                          - A service api client for
                                                 Flask applications.
Flask-Smores (0.2.1)                           - Validate inputs and document
                                                 routes using marshmallow
                                                 schemas
flask-swagger-ui (3.0.12a0)                    - Swagger UI blueprint for
                                                 Flask
Flask-Uploads (0.2.1)                          - Flexible and efficient upload
                                                 handling for Flask
Flask-WhooshAlchemyPlus (0.7.5)                - Whoosh extension to
                                                 Flask/SQLAlchemy
Flask-HTMLmin (1.3.1)                          - Minimize render templates
                                                 html
Flask-Menu (0.6.0)                             - Flask-Menu is a Flask
                                                 extension that adds support
                                                 for generating menus.
Flask-PicoCMS (0.0.6)                          - Lightweight CMS backend for
                                                 Flask apps
Flask-Redislite (0.1.0rc0)                     - Using Flask with Redislite
flask-secure-headers (0.6)                     - Secure Header Wrapper for
                                                 Flask Applications
Flask-Slack (0.1.5)                            - Slack extension for Flask.
flask-keyauth (0.1.5)                          - A module to simplify working
                                                 with KEY auth in Flask apps
Flask-MySQL (1.4.0)                            - Flask simple mysql client
flask-pundit (1.1.0)                           - Simple library to manage
                                                 resource authorization and
                                                 scoping
Flask-reCaptcha (0.4.2)                        - The new Google ReCaptcha
                                                 implementation for Flask
                                                 without Flask-WTF
Flask-request-params (0.3.0)                   - Flask-request-params provides
                                                 Rails-like interface to HTTP
                                                 Request Parameters for Flask.
Flask-RQ2 (17.0)                               - A Flask extension for RQ.
Flask-Scrypt (0.1.3.6)                         - Flask-Scrypt provides
                                                 convenient wrappers forscrypt
                                                 password hashing and random
                                                 salt generation.
Flask-Split (0.3.0)                            - A/B testing for your Flask
                                                 application
Flask-StatHat (0.1.2)                          - StatHat extension for Flask
Flask-Weixin (0.5.0)                           - Weixin for Flask.
flask-idempotent2 (0.0.6)                      - Redis based idempotent
                                                 support for sqlalchemy based
                                                 flaskapplications.
Flask-MAB (1.1.1)                              - Multi-armed bandits for flask
flask-msearch (0.1.5)                          - full text search with whoosh
                                                 for flask
Flask-OFAUTH (0.1.7)                           - passport api client for Flask
                                                 applications.
Flask-Sleepy (0.3.0)                           - REST is hard. Let's go
                                                 shopping
Flask-SSLify (0.1.5)                           - Force SSL on your Flask app.
flask-xadmin (0.1.2)                           - eXtended Flask-Admin
Flask-MongoRest (0.2.3)                        - Flask restful API framework
                                                 for MongoDB/MongoEngine
Flask-PRISM (0.3.2)                            - Simple APIs with Flask PRISM
Flask-Pushrod (0.3)                            - Views for your API
Flask-Security-Fork (2.0.1)                    - Simple security for Flask
                                                 apps.
Flask-Staticify (0.2.2)                        - Looks for static files in the
                                                 additional locations as a
                                                 fallback
flask-talisman (0.4.0)                         - HTTP security headers for
                                                 Flask.
flask-thumbnails-s3 (0.1.5)                    - An extension to create image
                                                 thumbnails on Amazon S3 (or
                                                 on local storage) with the
                                                 Flask framework, based on
                                                 flask-thumbnails.
Flask-GraphQL (1.4.1)                          - Adds GraphQL support to your
                                                 Flask application
Flask-JSON (0.3.2)                             - Better JSON support for Flask
Flask-LogConfig (0.4.2)                        - Flask extension for
                                                 configuring Python logging
                                                 module
Flask-Misaka (0.4.1)                           - A pleasant interface between
                                                 the Flask web framework and
                                                 the Misaka Markdown parser.
flask-ponywhoosh (1.0.6)                       - A search engine for Flask
                                                 using Pony ORM and Whoosh.
Flask-PyBankID (0.3.1)                         - Flask Extension for PyBankID
                                                 client
Flask-qiniu (1.1.4)                            - Flask Qiniu extension
Flask-S3-gzip (0.1.8)                          - Seamlessly serve the static
                                                 files of your Flask app from
                                                 Amazon S3 (forked from
                                                 original flask-s3)
Flask-Test (0.1.6)                             - Various unit testing helpers
                                                 for Flask applications.
Flask-Track-Usage (1.1.0)                      - Basic metrics tracking for
                                                 the Flask framework.
Flask-Upstatic (0.0.6)                         - Opinionated library for
                                                 working with CDNs in Flask.
Flask-Via (2015.1.1)                           - Provides a clean, simple URL
                                                 routing framework for growing
                                                 Flask Applications.
Flask-WAT (0.1.2)                              -
flask-yoloapi (0.0.6)                          - Simply the best Flask API
                                                 library
Flask-Sentinel (0.0.7)                         - OAuth2 Provider for Flask
                                                 applications.
flask-zookeeper (0.0.8)                        - Flask Zookeeper client
Flask-Genshi (0.5.1)                           - An extension to Flask for
                                                 easy Genshi templating.
Flask-Snooze (0.1.6)                           - Backend agnostic REST API
                                                 provider for Flask
flask-uiface (0.7)                             - Random user avatars for the
                                                 rest of us!
Flask-Webpack (0.1.0)                          - Flask extension for managing
                                                 assets with Webpack.
Flask-IdentityClient (0.5.2)                   - PassaporteWeb connection for
                                                 Flask applications
Flask-Sessionstore (0.4.5)                     - Adds session support to your
                                                 Flask application
Flask-WePay (0.0.7)                            - WePay API support
flask-fs (0.4.1)                               - Simple and easy file storages
                                                 for Flask
flask-shell-ipython (0.3.0)                    - Replace default `flask shell`
                                                 command by similar command
                                                 running IPython.
Flask-FlatPages (0.6)                          - Provides flat static pages to
                                                 a Flask application
Flask-ImageAlchemy (0.0.7)                     - SQLAlchemy Standarized Image
                                                 Field for Flask
Flask-IPInfo (0.0.10)                          - Get IP, ISP, Location, OS
                                                 from flask request
flask-jsonapi (0.5.1)                          - JSONAPI 1.0 implementation
                                                 for Flask.
Flask-LazyViews (0.6)                          - Registers URL routes for
                                                 Flask application or
                                                 blueprint in lazy way.
Flask-LDAP (0.1.6)                             - Flask extension for LDAP auth
                                                 and profile user
Flask-LinkTester (0.3.0)                       - Link tester for Flask
                                                 applications
Flask-Marcos (0.0.7dev)                        - ERP apps Flask container
flask-statsd-tags (0.1.6)                      - Flask extention for sending
                                                 statsd data
Flask-thumbnails (1.0.3)                       - A simple extension to create
                                                 a thumbs for the Flask
Flask-Markdown (0.3)                           - Small extension to make using
                                                 markdown easy
Flask-Session (0.3.1)                          - Adds server-side session
                                                 support to your Flask
                                                 application
Flask-Styleguide (0.4.0)                       - A living Styleguide for your
                                                 Flask application.
Flask-WebSub (0.2.1)                           - A WebSub hub, publisher and
                                                 subscriber using Flask
Flask-Kits (0.0.8)                             - demo
Flask-Locale (1.0.2)                           - Adds i18n/l10n support to
                                                 Flask applications easily.
                                                 Uses CSV files(or database)
                                                 to load translations.
flask-openldap (0.0.9)                         - Flask extension to query an
                                                 openLDAP server
oleg-flask-sessions (0.2.5)                    - Oleg DB backed sessions for
                                                 Flask
Flask-Foundation (2.1)                         - An extension that includes
                                                 the Foundation css framework
                                                 in your project, without any
                                                 boilerplate code.
flask-kser (0.2.1)                             - Flask KSer example
Flask-SuperAdmin (1.7.1)                       - The best admin interface
                                                 framework for Python. With
                                                 scaffolding for MongoEngine,
                                                 Django and SQLAlchemy.
Flask-WhooshAlchemy (0.8)                      - Whoosh extension to
                                                 Flask/SQLAlchemy
Flask-Vue (0.3.5)                              - Vue.js 1.0+ integration for
                                                 Flask (Python 3 version)
Flask-Mustache (0.4.1)                         - Mustache for Flask
Flask-OpenTracing (0.1.7)                      - OpenTracing support for Flask
                                                 applications
Flask-OAuth2-Provider (0.3.2)                  - A simple flask oauth2
                                                 provider
Flask-Prose (0.1.56)                           - A flask extension for
                                                 generating markov prose
Flask-Redis (0.3.0)                            - Redis Extension for Flask
                                                 Applications
Flask-Stormpath-Plus (0.2.4)                   - Simple and more secure user
                                                 authentication for Flask via
                                                 Stormpath.
Flask-Principal (0.4.0)                        - Identity management for flask
flask-tat (0.0.10)                             - Flask TAT client
Flask-WebTest (0.0.9)                          - Utilities for testing Flask
                                                 applications with WebTest.
Flask-OAuth2-Login (0.0.9)                     - Simple OAuth2 login
Flask-INIConfig (0.1.0)                        - A flask extension to load ini
                                                 files via config
Flask-MQTT (0.0.9)                             - Flask extension for the MQTT
                                                 protocol
Flask-Multipass (0.1.1)                        -
flask-request-validator (2.0.3)                - Flask request data validation
Flask-RESTeasy (0.0.8)                         - Create easy REST APIs with
                                                 Flask
Flask-Store (0.0.4.4)                          - Provides Django-Storages like
                                                 file storage backends for
                                                 Flask Applications.
Flask-Gravatar (0.4.2)                         - Small extension for Flask to
                                                 make usage of Gravatar
                                                 service easy.
Flask-Multi-Redis (0.1.5)                      - MultiThreaded MultiServers
                                                 Redis Extension for Flask
                                                 Applications
Flask-PageDown (0.2.2)                         - Implementation of
                                                 StackOverflow's "PageDown"
                                                 markdown editor for Flask-
                                                 WTF.
Flask-Twitter-OEmbedder (0.1.8)                - Embedded tweets in Flask
                                                 Jinja2 Templates with only
                                                 the Tweet_ID
Flask-Json-Syslog (0.1.28)                     - Output syslog of the json
                                                 format.
Flask-Social (1.6.2)                           - Simple OAuth provider
                                                 integration for Flask-
                                                 Security
Flask-Z3950 (0.3.2)                            - Z39.50 integration for Flask
                                                 applications.
Flask-MxitGA (0.10)                            - Google analytics for flask
                                                 and mxit.
Flask-KVSession (0.6.2)                        - Transparent server-side
                                                 session support for flask
Flask-Lastuser (0.3.12)                        - Flask extension for Lastuser
flask-monitor (0.2.5)                          - Flask Monitor module
Flask-Negotiation (0.1.9)                      - Better content negotiation
                                                 for flask
Flask-Permissions (0.2.3)                      - Simple user permissions for
                                                 Flask
Flask-Weixin-Pay (0.3.4)                       - Weixin Pay from Flask
flask-oidc (1.3.0)                             - OpenID Connect extension for
                                                 Flask
Flask-NSFW (6)                                 - Flask-NSFW blocks all the
                                                 requests that contains images
                                                 with nudity.
Flask-Funnel (0.1.10)                          - Asset management for Flask.
Flask-Plugins (1.6.1)                          - Create plugins for your Flask
                                                 application
Flask-SimpleLDAP (1.2.0)                       - LDAP authentication extension
                                                 for Flask
flask-heroku (0.1.9)                           - Heroku environment variable
                                                 configurations for Flask
flask-login-openerp (0.5.1)                    - OpenERP Login for Flask using
                                                 Flask-Login
flask-logmanager (0.2.10)                      - Flask LogManager module
Flask-Loopback (1.4.5)                         - Library for faking HTTP
                                                 requests using flask
                                                 applications without actual
                                                 network operations
flask-marshmallow (0.8.0)                      - Flask + marshmallow for
                                                 beautiful APIs
Flask-Moment (0.5.2)                           - Formatting of dates and times
                                                 in Flask templates using
                                                 moment.js.
flask-ptrans (2.0.3)                           - Flask extension for
                                                 localisation of templates
                                                 from JSON files
Flask-Pusher (1.2.1)                           - Flask extension for Pusher
Flask-RAML (0.2.2)                             - Flask-RAML (REST API Markup
                                                 Language) API server with
                                                 parameter conversion,
                                                 response encoding, and
                                                 examples
Flask-Stride (0.2.9)                           - Flask adapter client for
                                                 pystride
Flask-Neo4j (0.5.1)                            - Flask extension providing
                                                 integration with Neo4j.
Flask-WebCache (0.9.1)                         - A Flask extension that adds
                                                 HTTP based caching to Flask
                                                 apps
Flask-Images (2.1.2)                           - Dynamic image resizing for
                                                 Flask.
Flask-Tus (0.7.1)                              - TUS protocol implementation
Flask-MailGun3 (0.1.5)                         - Flask extension to use the
                                                 Mailgun email parsing service
flask-hookserver (1.1.0)                       - Server for GitHub webhooks
                                                 using Flask
Flask-pyoidc (1.2.0)                           - Flask extension for OpenID
                                                 Connect authentication.
Flask-OpenID (1.2.5)                           - OpenID support for Flask
flask-spawn (0.1.11)                           - Generate new flask projects
                                                 quickly and easily, in a
                                                 variety of customisable
                                                 structures.
flask-ldap3-login (0.9.13)                     - LDAP Support for Flask in
                                                 Python3/2
flask-ripozo (1.0.4)                           - An extension for ripozo and
                                                 that brings
                                                 HATEOAS/REST/Hypermedia apis
                                                 to flask
Flask-GoogleMaps (0.2.5)                       - FlaskGoogleMaps - Google Maps
                                                 Extension for Flask
flask-resty-tenants (0.5.3)                    - Flask Resty Authorization
                                                 module for multitenancy
Flask-QRcode (1.0.1)                           - An concise flask extension to
                                                 render QR codes
Flask-JinjaHelpers (0.3.7)                     - Various helpers for Flask
                                                 based Jinja2 templates.
Flask-PyMongo (0.5.1)                          - PyMongo support for Flask
                                                 applications
Flask-Sijax (0.4.1)                            - An extension for the Flask
                                                 microframework that adds
                                                 Sijax support.
Flask-Navigate (0.2.2)                         - Another flask extension that
                                                 provides Navigation menus.
Flask-Holster (0.3.4)                          - Rigid MVC content negotiation
                                                 for Flask
Flask-Micropub (0.2.8)                         - Adds support for Micropub
                                                 clients.
Flask-Testing (0.6.2)                          - Unit testing for Flask
Flask-WXPay (0.1.13)                           - Flask Extension for WeChat
                                                 Pay.
Flask-Material (0.1.1)                         - An extension that includes
                                                 Materialize CSS
                                                 (http://materializecss.com/)
                                                 in your project, without any
                                                 boilerplate code.
flask-mwoauth (0.3.61)                         - Flask blueprint to connect to
                                                 a MediaWiki OAuth server
Flask-MustacheJS (0.6.0)                       - Mustache integration in
                                                 Flask, with Jinja and client-
                                                 side libraries.
flask-swagger (0.2.13)                         - Extract swagger specs from
                                                 your flask project
Flask-Imagine (0.5)                            - Extension which provides easy
                                                 image manipulation support in
                                                 Flask applications.
Frozen-Flask (0.15)                            - Freezes a Flask application
                                                 into a set of static files.
flask-musers (0.5.4)                           - Flask app for store user in
                                                 MongoDB and simple views for
                                                 login, logout and
                                                 registration.
Flask-Pypi-Proxy (0.5.1)                       - A Pypi proxy
Flask-JSONAPIView (0.1.0)                      - DEPRECATED: This library has
                                                 been renamed to Flask-RESTy
Flask-Validator (1.2.3)                        - Data validator for Flask and
                                                 SQL-Alchemy, working at Model
                                                 component with events
twopi-flask-utils (1.1.8)                      - A set of utilities to make
                                                 working with flask web
                                                 applications easier.
Flask-LwAdmin (0.6.3)                          - Flask-LwAdmin is minimalistic
                                                 administrative interface
                                                 building extension for the
                                                 Flask framework
flask-whooshee (0.5.0)                         - Flask-SQLAlchemy - Whoosh
                                                 Integration
Flask-SQLAlchemy (2.3.2)                       - Adds SQLAlchemy support to
                                                 your Flask application
flask-restful-swagger (0.19)                   - Extrarct swagger specs from
                                                 your flast-restful project
Flask-Login (0.4.0)                            - User session management for
                                                 Flask
Flask-MongoAlchemy (0.7.2)                     - Add Flask support for MongoDB
                                                 using MongoAlchemy.
Flask-GoogleLogin (0.3.1)                      - Extends Flask-Login to use
                                                 Google's OAuth2 authorization
flask-praetorian (0.3.15)                      - Strong, Simple, and Precise
                                                 security for Flask APIs
flask-mongoengine (0.9.3)                      - Flask-MongoEngine is a Flask
                                                 extension that provides
                                                 integration with MongoEngine
                                                 and WTF model forms.
Flask-Perm (0.2.8)                             - Flask Permission Management
                                                 Extension
flask-zeus (0.2.1)                             - UNKNOWN
pytest-flask (0.10.0)                          - A set of py.test fixtures to
                                                 test Flask applications.
Flask-MarcoPolo (0.6.3)                        - Flask-MarcoPolo  Flask-
                                                 MarcoPolo is a Flask
                                                 extension that adds structure
                                                 to both your views and
                                                 templates, by mapping them to
                                                 each other to provide a rapid
                                                 application development
                                                 framework. The extension also
                                                 comes with Flask-Classy,
                                                 Flask-Assets, Flask-Mail,
                                                 JQuery 2.x, Bootstrap 3.x,
                                                 Font-Awesome, Bootswatch
                                                 templates. The extension also
                                                 provides pre-made templates
                                                 for error pages and macros.
                                                 https://github.com/mardix
                                                 /flask-marcopolo
Flask-PW (1.1.3)                               - Peewee ORM integration for
                                                 Flask framework
Flask-Injector (0.10.1)                        - Adds Injector, a Dependency
                                                 Injection framework, support
                                                 to Flask.
Flask-LoginManager (1.1.6)                     - Flask-Loginmanager supports
                                                 multiple roles and
                                                 permissions for Flask,
                                                 inspired by Flask-Login
Flask-OAuthlib (0.9.4)                         - OAuthlib for Flask
Flask-paginate (0.5.1)                         - Simple paginate support for
                                                 flask
Flask-Maple (0.5.0)                            - captcha ,bootstrap,easy login
                                                 and more flask tips.
Flask-HTTPAuth (3.2.3)                         - Basic and Digest HTTP
                                                 authentication for Flask
                                                 routes
Flask-Slither (1.1.7)                          - A small library between
                                                 MongoDB and JSON API
                                                 endpoints
Flask (0.12.2)                                 - A microframework based on
                                                 Werkzeug, Jinja2 and good
                                                 intentions
Flask-Script (2.0.6)                           - Scripting support for Flask
Flask-SeaSurf (0.2.2)                          - An updated CSRF extension for
                                                 Flask.
Flask-Restless (1.0.0b1)                       - A Flask extension for easy
                                                 ReSTful API generation
Flask-Jerify (0.0.25)                          - Validate JSON requests
                                                 against schemas
Flask-LDAPConn (0.6.13)                        - Pure python, LDAP connection
                                                 and ORM for Flask
                                                 Applications
Flask-Resize (2.0.3)                           - Flask extension for resizing
                                                 images in code and templates
Flask-REST-JSONAPI (0.13.2)                    - Flask extension to create
                                                 REST web api according to
                                                 JSONAPI 1.0 specification
                                                 with Flask, Marshmallow
                                                 and data provider of your
                                                 choice (SQLAlchemy, MongoDB,
                                                 ...)
Flask-Migrate (2.1.1)                          - SQLAlchemy database
                                                 migrations for Flask
                                                 applications using Alembic
GitHub-Flask (3.2.0)                           - GitHub extension for Flask
                                                 microframework
Flask-WTF-FlexWidgets (0.1.25)                 - A flask extension that
                                                 provides customizable WTF
                                                 widgets and macros.
flask-peewee (0.6.7)                           - Peewee integration for flask
Flask-Security (3.0.0)                         - Simple security for Flask
                                                 apps.
Flask-Mail (0.9.1)                             - Flask extension for sending
                                                 email
Flask-RESTful (0.3.6)                          - Simple framework for creating
                                                 REST APIs
Flask-Table (0.4.1)                            - HTML tables for use with the
                                                 Flask micro-framework
flask-restplus (0.10.1)                        - Fully featured framework for
                                                 fast, easy and documented API
                                                 development with Flask
Flask-S3 (0.3.3)                               - Seamlessly serve the static
                                                 files of your Flask app from
                                                 Amazon S3
flask-transmute (1.3.0)                        - a flask plugin to generate
                                                 routes from objects.
Flask-uWSGI-WebSocket (0.6.0)                  - High-performance WebSockets
                                                 for your Flask apps powered
                                                 by uWSGI.
Flask-Stormpath (0.4.8)                        - Simple and secure user
                                                 authentication for Flask via
                                                 Stormpath.
flask-magic (0.0.53)                           - A full stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
flask-io (1.12.0)                              - Flask-IO is a library for
                                                 parsing Flask request
                                                 arguments into parameters and
                                                 for serialization of complex
                                                 objects into Flask response.
Flask-RESTy (0.12.1)                           - Building blocks for REST APIs
                                                 for Flask
Flask-WTF (0.14.2)                             - Simple integration of Flask
                                                 and WTForms.
Flask-User (0.6.19)                            - Customizable User
                                                 Authentication and
                                                 Management, and more.
Flask-Limiter (1.0.0)                          - Rate limiting for flask
                                                 applications
Flask-Wizard (0.5.9)                           - Rapid and easy chatbot
                                                 development in Python for
                                                 multiple channels
flask-restaction (0.25.3)                      - A web framwork born to create
                                                 RESTful API
Flask-SocketIO (2.9.2)                         - Socket.IO integration for
                                                 Flask applications
Flask-Potion (0.14.1)                          - Powerful REST API framework
                                                 for Flask and SQLAlchemy
Flask-Restler (1.10.3)                         - Build REST API for Flask
                                                 using Marshmallow.
flask-xxl (0.9.20)                             - quick way to design large
                                                 flask projects
microcosm-flask (0.83.0)                       - Opinionated persistence with
                                                 FlaskQL
flask2postman (1.4.3)                          - Generate a Postman collection
                                                 from your Flask application
flask_accept (0.0.3)                           - Custom Accept header routing
                                                 support for Flask
flask_aide (0.0.1)                             - demo
flask_alcohol (0.2.2)                          - Automatically generate API
                                                 routes from Flask-SQLAlchemy
                                                 models
flask_ample (0.0.1)                            - basic setup of ample for
                                                 flask
flask_api_builder (0.2.0)                      - A shortcut for stubbing out
                                                 your RESTful Flask APIs
flask_app_generator (0.1.0)                    - Flask Project Generator
flask_autorest (0.1.5)                         - auto create restful apis for
                                                 database, with the help of
                                                 dataset.
flask_backstage (0.2.1)                        - A backstage framework with
                                                 very few code.
flask_base64_msm_session (1.0.2)               - Use base64 encoder on
                                                 memcached server. And it will
                                                 use memcached on session
flask_basic_roles (0.2)                        - A plugin for adding very
                                                 simple users + roles to a
                                                 flask app
flask_cache_external_assets (0.2.0)            - Flask extension for caching
                                                 external assets
flask_checkargs (0.1.2)                        - A module to simplify checking
                                                 arguments in Flask apps
flask_chip (0.1.2)                             - A token generator for Flask
                                                 apps.
flask_clapi (0.2.0)                            - CLAPI wrapper
flask_cm (0.8.1)                               - Cloud Mesh: managing multiple
                                                 virtual machines in Clouds
flask_datatables (0.6.17)                      - Integrates SQLAlchemy with
                                                 DataTables (framework Flask)
flask_dino_utils (0.1.13)                      - Flask utils package to use it
                                                 among with Flask-Classy and
                                                 marshmallow
flask_doc (0.2.5)                              - Write API document when you
                                                 coding, Test your API when
                                                 you press last word
                                                 immediately
flask_error (0.1)                              - A simple and extensible way
                                                 of displaying error messages.
flask_ext_migrate (1.0.1)                      - A sourcecode manipulation
                                                 tool for converting imports.
flask_extras (4.0.3)                           - Assorted useful flask views,
                                                 blueprints, Jinja2 template
                                                 filters, and templates/macros
flask_flaskwork (0.1.11)                       - A Flask plugin to talk with
                                                 the Flaskwork Chrome
                                                 extension.
flask_frink (0.0.1)                            - Add Flask-Security datastore
                                                 functionality to Frink.
flask_github_proxy (0.0.2)                     - Plugin to build services to
                                                 push data from a website to
                                                 github with PullRequests
                                                 confirmation
flask_helpers (0.1)                            - Useful stuff for Flask
                                                 application
flask_introspect (0.0.1)                       - basic setup of ample for
                                                 flask
flask_json_multidict (1.0.0)                   - Convert Flask's
                                                 `request.get_json` dict into
                                                 a MultiDict like
                                                 `request.form`
flask_json_resource (0.2.18)                   - UNKNOWN
flask_jsondash (6.2.3)                         - Easily configurable, chart
                                                 dashboards from any arbitrary
                                                 API endpoint. JSON config
                                                 only. Ready to go.
flask_jsontools (0.1.1-0)                      - JSON API tools for Flask
Flask_LDAP_View (0.3)                          - A library to restrict your
                                                 flask pages by LDAP groups
flask_locust (0.0.2-alpha)                     - SQL-Migrations for your
                                                 Application
flask_markdown2 (0.0.3)                        - A flask extension that adds a
                                                 {% markdown %} tag to
                                                 templates.
flask_nameko (1.4.0)                           - A wrapper for using nameko
                                                 services with Flask
flask_neglog (0.0.2)                           - demo
flask_nemo (1.0.1)                             - Flask Extension to browse CTS
                                                 Repository
flask_ogm (1.1.0a9)                            - Add support for the py2neo
                                                 Object Graph Mapper to your
                                                 app
flask_open_directory (0.1.1)                   - MacOS OpenDirectory
                                                 Authorization Middleware for
                                                 Flask
flask_params (1.0.1)                           - Processes the Request params
                                                 for Flask served as a Python
                                                 library
flask_profiler (1.6)                           - API endpoint profiler for
                                                 Flask framework
flask_raven (0.0.4)                            - A flask extension for the
                                                 University of Cambridge's
                                                 authentication system
flask_rdf (0.2.0)                              - Flask decorator to output RDF
                                                 using content negotiation
flask_react (0.0.5)                            - Auto setup tool for flask and
                                                 react project
flask_render_specific_template (1.0)           - This library allows Flask
                                                 developers to dynamically
                                                 select the template directory
                                                 used for rendering
flask_replicated (1.2)                         - Flask SqlAlchemy router for
                                                 stateful master-slave
                                                 replication
flask_reqparse (2.2.1)                         - flask_reqparse is a simple
                                                 wrapper around flask request
                                                 module that helps to parse
                                                 args efficently.
flask_rest_toolkit (0.0.1)                     - A set of tools to create
                                                 simple Flask REST web
                                                 services and APIs
flask_restframework (0.1.1)                    - Web APIs for Flask, made
                                                 easy, inspired from Django
                                                 DRF.
flask_restful_jsonschema (0.1.1)               - Provides a wrapper which
                                                 provides valid json to
                                                 Resource methods.
flask_restful_url_generator (0.0.4)            - flask-restful URLs list
flask_resty_swagger (0.1.3)                    - Generate swagger
                                                 documentation from flask-
                                                 resty service
flask_sandboy (0.0.3)                          - Automated REST APIs for
                                                 SQLAlchemy models
flask_script_extras (0.1.4)                    - extras commands to Flask-
                                                 Script.
flask_servatus (0.1.3)                         - A port of djangos storages
                                                 framework for use with flask
                                                 applications
flask_servicenow (0.1.1)                       - ServiceNow REST API Flask
                                                 extension
flask_siilo (0.1.2)                            - A simple storage for Flask
                                                 based on siilo.
flask_simple_sitemap (0.0.3)                   -
flask_simplelogin (0.0.6)                      - Flask Simple Login - Login
                                                 Extension for Flask
flask_simplerest (1.0.3)                       - A Flask extension for easy
                                                 ReSTful API generation
flask_singleview (0.2.1)                       - A flask micro extension for
                                                 building single-view web
                                                 apps.
flask_slackbot (0.2.1)                         - Deal with slack outgoing
                                                 webhook
flask_sqla_debug (0.2)                         - Helpers for debugging flask
                                                 and sqlalchemy performance
flask_tlsauth (0.1.3)                          - Flask extension implementing
                                                 TLS Authentication - simple
                                                 client certificate CA
                                                 inclusive
flask_trace (0.0.4)                            - Log trace decorator function
                                                 for Flask
flask_tryton (0.6)                             - Adds Tryton support to Flask
                                                 application
flask_typed_mounter (0.2.1)                    - Decorator to mount a function
                                                 to a Flask endpoint
flask_util_js (0.2.25)                         - flask's util in javascript.
                                                 such as url_for etc.
flask_voluptuous (0.1.2)                       - A simple flask extension for
                                                 data validation with
                                                 Voluptuous
flask_web_args (0.1.2)                         - A library to help easily
                                                 parse/validate web arguments
                                                 with Flask
flask_wx (0.0.1)                               - A simple and brief utility
                                                 tools framework
flask_yamlpage (0.0.6)                         - Flatpages in yaml syntax
flaskcbv (1.4.11)                              - FlaskCBV is Alternative
                                                 Framework for working with
                                                 flask with the class Based
                                                 Views approach (CBV)
flaskchatterbot (0.1.0)                        - An open-source web based
                                                 Python chat bot in Flask.
flaskckeditor (1.6)                            - flask后台快速集成ckeditor编辑器
FlaskCms (0.0.4)                               - UNKNOWN
FlaskDeferredHandler (0.1)                     - A Flask handler for the
                                                 Google Appengine's deferred
                                                 library
flasker (0.1.45)                               - Flask, SQLAlchemy, and Celery
                                                 integration
FlaskEx (0.0.66)                               - UNKNOWN
flaskfilemanager (0.0.4)                       - RichFilemanager blueprint for
                                                 Flask web applications - adds
                                                 a ckeditor compatible file
                                                 manager / browser
flaskhmac (1.2.1)                              - Provides easy integration of
                                                 the HMAC signatures for your
                                                 REST Flask Applications.
flaskinit (0.0.1)                              - Bootstraps Flask projects
flaskit (0.1.0)                                - Utilies for Flask
                                                 application.
flaskJSONRPCServer (0.9.3)                     - A Python JSON-RPC over HTTP
                                                 with flask and gevent
flaskle (0.4)                                  - bottle-like utility
                                                 decorators for flask
pumpwood-flaskmisc (0.0.0.2)                   - Misceletiuns fucntions and
                                                 class to help development of
                                                 PumpWood on Flash
flaskmogrify (0.0.9)                           - Flaskmogrify, a simple Flask
                                                 single pageapplication to
                                                 convert (w/ Ajax) user-pasted
                                                 text using an arbitrary text
                                                 conversion function.
flaskpress-themes (0.1.5)                      - Provides infrastructure for
                                                 theming FlaskPress
                                                 applications
flaskpress (0.0.1)                             - Python Flask CMS
flaskpress-speaklater (1.3.0)                  - Implements a lazy string for
                                                 python for use with gettext
FlaskPusher (1.0.1)                            - Adds Pusher support for your
                                                 Flask application.
flaskrestframework (0.1.4)                     - Web APIs for Flask, made
                                                 easy.
flaskrestgen (0.4)                             - A restful API generator for
                                                 flask/sqlalchemy declarative
                                                 models.
FlaskSearch (0.1)                              - Powerful search functionality
                                                 for Flask apps via
                                                 ElasticSearch
flaskserver (0.1.1)                            - simple web server with Flask
flasksr (0.6)                                  - Start streaming HTTP
                                                 Responses based on your page
                                                 layout for Flask and improve
                                                 Time for First Paint.
flaskstrap (0.3.6)                             - Easily create a flask, nginx,
                                                 uwsgi and bootstrap project
                                                 ready for deployment
flaskup (0.3.2)                                - A simple Flask application to
                                                 share files.
FlaskWarts (0.1a8)                             - Assortment of various
                                                 utilities for Flask
                                                 applications
flaskwork (0.1.1)                              - UNKNOWN
Flasky (0.1.0)                                 - Lazy man's Flask Application
FlaskyTornado (0.0.45)                         - A microframework based on
                                                 Tornado and Flask and good
                                                 intentions
flatly (0.3)                                   - Pyramid scaffold that is
                                                 flat.  Kind of like Flask.
flatpages_index (0.1)                          - A small extension for
                                                 flask_flatpages
fleaker (0.4.3)                                - Tools and extensions to make
                                                 Flask development easier.
flekky (0.4.1)                                 - Static website generator
                                                 inspired by jekyll based on
                                                 flask.
flexrest (0.1.9)                               - Flexible Flask Rest Api
FliKISS (0.1)                                  - Wiki engine based on Markdown
                                                 flat files powered by Flask
flump (0.11.1)                                 - REST API builder using Flask
                                                 routing and Marshmallow
                                                 schemas.
flymph (0.1.3)                                 - Flask as Lymph Web API
gitlab-freak (1.0.0a1)                         - A Flask server that allows
                                                 you to interact with Trello
                                                 from your own Gitlab, and
                                                 keep track of your projects
                                                 dependencies.
Fregger (0.10.6)                               - Automatically generate
                                                 Swagger docs for Flask-
                                                 Restful.
frl (0.0.4)                                    - flask/requests logging
froth (0.0.1)                                  - Data Visualization Template
                                                 Engine for Django/Flask=
frs (0.0.0.dev12)                              - Flask-RESTful
                                                 Swagger(-driven) Validation
fss (0.2.1)                                    - Compile Flask/Jinja2 site
                                                 into static html content
funkyserver (0.1)                              - FunkyServer is simple package
                                                 to create Flask servers in
                                                 background processes.
Funnel (0.1)                                   - Flask extension for Beaker
fuser (1.0.4)                                  - A library to handle user
                                                 related tasks in Flask
fvsd (1.0.3)                                   - Flask+VueJS+SemanticUI+Docker
                                                 CLI boilerplate.
gdbgui (0.8.0.3)                               - browser-based gdb frontend
                                                 using Flask and JavaScript to
                                                 visually debug C, C++, Go, or
                                                 Rust
getolaf (1.0.2)                                - A static site generator based
                                                 on flask and markdown
git-golem (0.1)                                - Git web interface using
                                                 libgit2 and flask
git-webhook (0.0.6)                            - 使用 Python Flask + SQLAchemy +
                                                 Celery + Redis + React
                                                 开发的用于迅速搭建并使用 WebHook
                                                 进行自动化部署和运维，支持 Github / GitLab
                                                 / Gogs / GitOsc。
Glask (0.0.23)                                 - An extension for flask
                                                 applications with best
                                                 practices.
glassblower (0.2.5)                            - The Best Flask Boilerplate
                                                 Framework
Gluino (0.4)                                   - port of web2py libs to
                                                 bottle, flask, pyramid,
                                                 tornado (includes copy of
                                                 modules from the web2py
                                                 framework)
goblet (0.3.5)                                 - Git web interface using
                                                 libgit2 and flask
google_forms (0.3)                             - Flask web proxy for Google
                                                 forms
graphscraper (0.1.1)                           - Graph implementation that
                                                 loads graph data (nodes and
                                                 edges) from external sources
                                                 and caches the loaded data in
                                                 a database using sqlalchemy
                                                 or flask-sqlalchemy.
groundwork-sphinx-theme (1.0.8)                - Sphinx theme for groundwork
                                                 projects (Based on
                                                 flask_theme)
halef-SETU (0.0.5)                             - halef-SETU provides an easy
                                                 wrapper around SKLL models
                                                 for statistical language
                                                 understanding as well as an
                                                 easy to API based on Flask
happymongo (0.1.1)                             - Python module for making it
                                                 easy and consistent to
                                                 connect to MongoDB via
                                                 PyMongo either in Flask or in
                                                 a non-flask application
Harambe (0.10.0)                               - A mid stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha, Cors.
                                                 Supports HTML, Markdown and
                                                 Jade and more
haven (1.1.107)                                - flask's style binary server
                                                 framework
py-healthcheck (1.7.0)                         - Adds healthcheck endpoints to
                                                 Flask or Tornado apps
healthcheck (1.3.2)                            - Adds healthcheck endpoints to
                                                 Flask apps
hflossk (0.5.10)                               - HFOSS course materials via
                                                 flask
highfield (1.0.21)                             - Structured flask with mongo
HipPocket (0.1.2a)                             - A wrapper around Flask to
                                                 ease the development of
                                                 larger applications
horn ((latest release))                        - Hy Macros for Flask
http-server-livereload (1.1.0)                 - A monkey patch of http.server
                                                 to call livereload when
                                                 server_forever is called.
                                                 This is compatible with flask
                                                 reload and tiny-lr (grunt
                                                 watch).
hxl-proxy (1.3)                                - Flask-based web proxy for HXL
jac (0.16.3)                                   - A Jinja extension (compatible
                                                 with Flask and other
                                                 frameworks) to compile and/or
                                                 compress your assets.
Jalapeno (0.1.4)                               - Static Site Generator based
                                                 on Flask
jiac (0.2.1)                                   - A Jinja extension (compatible
                                                 with Flask) to compile and/or
                                                 compress your assets inline.
jobmonitor (0.0.5)                             - Physics-orientated job
                                                 monitoring over HTTP with
                                                 Flask.
json-validator (1.0)                           - Provide decorator for
                                                 validating json parameters
                                                 passed to function. Can be
                                                 used for validation of json
                                                 parameters sent to Flask.
py-json-rpc (0.0.3)                            - Decorator based toolkit to
                                                 use JSONRPC easy like Flask
Juice (0.0.23)                                 - A full stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
JYFlask (0.1)                                  - Jing Yun Flask
Keg (0.6.0)                                    - A web framework built on
                                                 Flask & SQLAlchemy.
                                                 Somewhere North of Flask but
                                                 South of Django.
KegBouncer (2.2.3)                             - A three-tiered permissions
                                                 model for KegElements built
                                                 atop Flask-User
kipavois (0.1.2)                               - Flask proxy over Kibana with
                                                 KiPavois
kit (0.2.15)                                   - Flask, Celery, SQLAlchemy
                                                 integration framework.
kola (1.5.6)                                   - flask's style json server
                                                 framework
kube_shields (0.0.6)                           - kube shields flask frontend.
zeus-lab804 (0.1.2)                            - Fast create scaffold of
                                                 flask.
Lagring (0.2.7.1)                              - Asset storage for Flask
lanfit-resp (0.1.2)                            - requests to flask response
                                                 with Link header.
Lapin (0.01a1)                                 - A flask-based web framework
lapti (0.0.1)                                  - Simple utils for flask and
                                                 peewee projects
latexrender (0.3.6)                            - A simple Flask app for
                                                 rendering latex snippets into
                                                 images.
lever (0.2.6)                                  - A tool for exposing
                                                 SQLAlchemy models in Flask
                                                 via REST
littlefish (0.0.15)                            - Flask webapp utility
                                                 functions by Little Fish
                                                 Solutions LTD
python-rabbitmq-logging (0.0.3)                - Send logs to RabbitMQ from
                                                 Python/Flask
logy (0.1)                                     - A flask based web application
                                                 for central logging
lraudit (0.1.1)                                - Adds auditing to LR Flask
                                                 apps
lrutilities (0.1.2)                            - Utilities for LR Flask apps
lrutils (0.1.4)                                - Utilities for LR Flask apps
mack (0.1.1)                                   - A simple Flask project
                                                 generator
madame (0.1.2.a)                               - RESTful API for MongoDB built
                                                 on Flask
magic-xxl (0.6.1)                              - A collection librairies to
                                                 work with Flask-Magic
tornado-mail (0.4.0)                           - A email plugin for tornado.
                                                 It is a fake Flask_mail.
Mambo (1.0.0b21)                               - A mid stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
mana (4.8)                                     - the missing startproject
                                                 command for Flask
mana0 (0.10)                                   - my flask toolkit
mana2 (0.15)                                   - my flask toolkit
mana3 (0.15)                                   - my flask toolkit
mana4 (0.15)                                   - my flask toolkit
simple-site-manager (0.1.7)                    - Manage multiple lighttpd and
                                                 Django or Flask websites on a
                                                 single machine.
script-manager (0.1.0)                         - A command-line interface.
                                                 Just a simple and crude
                                                 implementation of Flask-
                                                 Script.
mandrill_webhooks (0.1.0)                      - Flask Webhooks
manhattan_dispatch (0.0.4)                     - A middleware dispatcher for
                                                 Flask based on             we
                                                 rkzeug.wsgi.DispatcherMiddlew
                                                 are.
markov_autocomplete (1.0.1)                    - Autocomplete model easy to
                                                 integrate with Flask apps
mediaflask (0.2.1)                             - Download audio from online
                                                 videos.
mediatumbabel (0.1.1)                          - flask-babel port to provide
                                                 i18n for mediaTUM (+jinja2)
                                                 with some improvements
meteorpi_server (0.1.5)                        - HTTP server based on Flask
                                                 providing a remote API
Microbe (1.2)                                  - Micro Blog Engine inspired by
                                                 Pelican and powered by Flask
oauth-middleware (0.3.3)                       - Simple flask_oauthlib based
                                                 middleware for WSGI app to
                                                 preform oauth
simple-migrate (0.0.3)                         - A simple database migrate
                                                 tool for flask
mimerender (0.6.0)                             - RESTful HTTP Content
                                                 Negotiation for Flask,
                                                 Bottle, web.py and webapp2
                                                 (Google App Engine)
mkflask_module (0.1.1)                         - Python module
Mlask (0.2)                                    - manage.py for Flask
Mocha (0.10.1)                                 - A mid stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha, Cors.
                                                 Supports HTML, Markdown and
                                                 Jade and more
moesifwsgi (1.1.1)                             - Moesif Middleware for Python
                                                 WSGI based flatforms (Flask,
                                                 Bottle & Others)
moflask (0.1)                                  - Re-usable flask utilities.
pyramid-mongoengine (0.0.9)                    - Mongoengine Pyramid extension
                                                 based in flask-mongoengine
redis-monitor (1.0.3)                          - 使用Flask开发的一个 web 可视化的 redis
                                                 监控程序，可以查看 redis 的服务器信息、实时监控
                                                 redis 的消息处理 ops、内存占用、cpu
                                                 消耗，以及 redis 联通时间。 A web
                                                 visualization redis
                                                 monitoring program.
                                                 Performance optimized and
                                                 very easy to install and
                                                 deploy. the monitor data come
                                                 from redis.info().
myflaskr (0.0.1)                               - A test upload for PyPI
nails (0.2.0)                                  - A python MVC framework built
                                                 with Flask
NCTU-Oauth (0.1.0)                             - adds NCTU-Oauth support to
                                                 flask
notes-pico (0.8.6)                             - A note-taking example web
                                                 application for Picoweb web
                                                 pico-framework. (Ported from
                                                 Flask original)
nyt-pyiap (0.0.11)                             - Python utility functions and
                                                 Django/Flask middlewares for
                                                 validating JWT tokens from
                                                 Google's Identity-Aware Proxy
odinweb.flask (0.4.0)                          - Toolkit for building web
                                                 API's using Odin and Flask.
ofcourse (0.2.5)                               - Python courseware with Flask
                                                 on OpenShift
onyx_sqlalchemy (3.2)                          - flask_sqlalchemy for Onyx
onyxbabel (0.0.3)                              - Ramake of the Flask_BabelEX
                                                 for Onyx
Openedoo-Script-Test (0.1.2)                   - Scripting support for Flask
openedoo (1.1.0.19)                            - openedoo is backend service
                                                 for education base on flask
palmer (0.0.4)                                 - Redice Flask Boost Library.
                                                 Inspired by flask-api.
paqmind.flask-paqforms (1.0.0)                 - UNKNOWN
paqmind.flask-routes (0.2.4)                   - Class-based routes for Flask
paqmind.flask-views (0.5.1)                    - Class-based views for Flask
sanic-patched (0.4.1)                          - A microframework based on
                                                 uvloop, httptools, and
                                                 learnings of flask
perfume (0.2)                                  - Simple Object Oriented layer
                                                 for Flask.
permission (0.4.1)                             - Simple and flexible
                                                 permission control for Flask
                                                 app.
phial (0.2.0)                                  - A static website generator
                                                 that takes motivation from
                                                 Flask and Jekyll.
Phial-Toolset (1.0.2)                          - Non-intrusive toolset to
                                                 easily use
                                                 Flask/Peewee/Celery
phovea_security_flask (0.1.0)                  - UNKNOWN
PlatformoClient (0.0.7)                        - 收集Flask的请求响应时间并发送至logstash
plush_web (0.1.0)                              - Micro framework inspirated by
                                                 Sinatra, Express and Flask.
podhub.meh (0.1.12)                            - Flask framework with
                                                 defaults.
Pontus (0.2.1)                                 - Flask utility for Amazon S3.
ponywhoosh (1.7.6)                             - Your database now searchable.
                                                 The backend behind the Flask-
                                                 PonyWhoosh.
Portfolio-py (0.0.1)                           - Portfolio is a Flask based
                                                 framework that adds structure
                                                 and map your views and
                                                 templates together for rapid
                                                 application development
pour (0.2.1)                                   - A lightweight Flask app
                                                 generator.
preflask (0.2)                                 - flask & preprocessors,
                                                 together, forever <3
Prestige (0.0.1)                               - Pylot is a Flask extension
                                                 that adds structure and map
                                                 your views and templates
                                                 together for rapid
                                                 application development
proxapy (0.1.5)                                - Simple API proxy that uses
                                                 Flask/requests/gunicorn.
py3web (0.3.14)                                - Django lets you write web
                                                 apps in Django. Flask lets
                                                 you write web apps in Flask.
                                                 Py3web lets you write web
                                                 apps in Python.
py_blueprints (1.0.1)                          - Flask ready to go blueprints
pygrest (0.3)                                  - Build REST APIs with Neo4j
                                                 and Flask, as quickly as
                                                 possible!
Pylot (0.0.4)                                  - Pylot is a Flask extension
                                                 that adds structure and map
                                                 your views and templates
                                                 together for rapid
                                                 application development
PyMessager (1.0.1)                             - A Python SDK and Flask API to
                                                 develop Facebook Messenger
                                                 application
pyros_config (0.2.0)                           - Classes to manage a server
                                                 configuration. Heavily
                                                 inspired by flask
python-thumbnails (0.5.1)                      - Thumbnails for Django, Flask
                                                 and other Python projects.
PyTyrion (1.0.1)                               - 支持Tornado、Django、Bottle、Flask
                                                 的Web表单验证
pyxley (0.1.0)                                 - Python tools for building
                                                 Flask-based web applications
qiniufs (1.0.2)                                - qiniu file uploader for
                                                 flask!
Quart (0.3.1)                                  - A Python asyncio web
                                                 microframework with the same
                                                 API as Flask
quorum (0.5.12)                                - Quorum Extensions for Flask
rapidserv (2.0.0)                              - A non-blocking Flask-like Web
                                                 Framework in python.
Redberry (0.0.7.5)                             - Flask Blueprint for adding
                                                 simple CMS functionality
relask (0.1.0)                                 - A Relay-based web development
                                                 kit on Flask
reportexport (0.0.3)                           - A Flask microservice that
                                                 produces reports out of a
                                                 database in xml and pdf
                                                 format.
RESTfulEf (0.1.1)                              - A generic restful api
                                                 generator based on elixir and
                                                 flask
Tornado-Restless (0.4.5)                       - flask-restless adopted for
                                                 tornado
restpager (0.1)                                - A RESTful pager class for
                                                 Flask
revise (0.0.3)                                 - Simple Schemas for Flask JSON
                                                 Validation
ripozo (1.3.0)                                 - ReSTful API framework with
                                                 HATEOAS support and
                                                 compatibility with Flask,
                                                 Django, SQLAlchemy and more.
rororo (1.1.1)                                 - Collection of utilities,
                                                 helpers, and principles for
                                                 building Python backend
                                                 applications. Supports
                                                 aiohttp.web, Flask, and your
                                                 web-framework
serverless-runlocal (0.1.2)                    - Serverless configuration
                                                 parser to run your serverless
                                                 function as Flask.
safrs (0.1.1)                                  - safrs : SqlAlchemy Flask-
                                                 Restful Swagger2
sanic-win (0.6.1)                              - A microframework based on
                                                 uvloop, httptools, and
                                                 learnings of flask
Sanic (0.6.0)                                  - A microframework based on
                                                 uvloop, httptools, and
                                                 learnings of flask
sbswebsite (0.0.23)                            - Flask based project to create
                                                 a personal site
sga (0.1.39)                                   - make it easier to use pyga
                                                 for web develop. and make
                                                 pyga compatible with flask
                                                 and django.
Shaft (0.0.8)                                  - A mid stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha, Cors.
                                                 Supports HTML, Markdown and
                                                 Jade and more
Shake (1.6.4)                                  - A lightweight web framework
                                                 based on Werkzeug and Jinja2
                                                 as an alternative to Flask
ShelfCMS (0.12.25)                             - Enhancing flask
                                                 microframework with beautiful
                                                 admin and cms-like features
shiftboiler (0.1.7)                            - Best practices setup for
                                                 webapps, apis and cli
                                                 applications with flask
simple_flask_server (0.0.2)                    - Flask equivalent of python -m
                                                 SimpleHTTPServer.
simple_openid (1.0.6)                          - Simple OpenID. One-line setup
                                                 for OpenID login for Flask.
simpleapi (0.0.9)                              - A simple API-framework to
                                                 provide an easy to use,
                                                 consistent and portable
                                                 client/server-architecture
                                                 (for django, flask and a lot
                                                 more).
SimpleFlask (0.1.0)                            - Simple Flask application.
SimpleFlaskBlueprint (0.1.1)                   - Simple Flask blueprint.
SimpleSQLProxy (1.0)                           - A simple sqlproxy for SQL
                                                 LITE databases based on flask
skaffold (0.1)                                 - Flask/SQLAlchemy Admin
                                                 Scaffold
slask (0.1.1)                                  - A Flask app to republish to
                                                 Slack
Slingr (0.0.13)                                - Web development framework
                                                 that builds and serves Cobs
                                                 (deployable web
                                                 applications), running on top
                                                 of Flask
SmallScrewdriver (1.0.2)                       - SmallScrewdriver is python
                                                 texture packer library, with
                                                 frontend's on PySide GUI,
                                                 Flask/React.js, and console
solidwebpush (1.2.1)                           - This package lets your server
                                                 send Web Push Notifications
                                                 to your clients. NOTE: No
                                                 particular web framework are
                                                 required (e.g. Django, Flask,
                                                 Pyramid, etc.), since it was
                                                 originally designed to run on
                                                 a Raspberry Pi with no web
                                                 server installed (only a bare
                                                 Python program listening on a
                                                 port for HTTP requests).
spill (0.0.1a0)                                - A utility for generating
                                                 Flask scaffolding and
                                                 boilerplate.
spouk_utils (0.1)                              - some utils for flask
                                                 distributions
StasFliKISS (0.1.2)                            - Wiki engine based on Markdown
                                                 flat files powered by Flask.
                                                 Fork from StasEvseev.
StatesofUSA (0.1)                              - An API built on  Flask-
                                                 RESTful that returns with the
                                                 names of all the states in
                                                 USA.
sucrose (0.1)                                  - mircroservice library using
                                                 flask and rabbitmq
tahoe (1.0.3.1)                                - A Flask-based framework that
                                                 handles the tedious things
talisman (0.1.0)                               - HTTP security headers for
                                                 Flask.
teleflask (0.0.8)                              - Easily create Telegram bots
                                                 with pytgbot and flask.
                                                 Webhooks made easy.
testflask (0.5)                                - Test flask applications
                                                 easily.
testflask1 (0.1)                               - testflask1 dependency
Thorium (0.2.16)                               - A Python framework for
                                                 RESTful API interfaces in
                                                 Flask
tiddly (1.0.11)                                - Flask-Tiddly is a minimal,
                                                 prototype RESTful server for
                                                 basic CRUD transactions.
tifa (0.2.9)                                   - a modern flask scaffolding
tinflask (0.0.2)                               - Simple wrapper around flask
                                                 that uses environment
                                                 variables for host, port,
                                                 endpoint prefix. Also uses
                                                 the py-hancock library for
                                                 the ability to sign
                                                 endpoints. Endpoints for
                                                 `time`, `ping`, and `status`
                                                 are automatically added as
                                                 well.
tinysmtp (0.1.2)                               - Basically Flask-Mail without
                                                 the Flask part
Toucan (0.0.0)                                 - A full stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
trappist (0.2.0)                               - Mount your Flask or WSGI app
                                                 in your Django app.
tumbler (0.0.23)                               - Tumbler is a simple layer
                                                 that leverage flask with nice
                                                 logs and automated settings
                                                 management
txflask (0.1)                                  - txflask makes working with
                                                 Twisted Web as easy as
                                                 working with flask
tyron (0.2.4)                                  - Gevent redis/pubsub event
                                                 notifier written in flask and
                                                 gevent
update_checker_app (0.6)                       - Flask Application that
                                                 provides the interface to the
                                                 update_checker package.
uppsell (0.1)                                  - A Flask-based e-commerce API
                                                 and a django-backed admin for
                                                 managing them.
vassal_deployer (0.0.2)                        - uwsgi and nginx flask app
                                                 vassal manager for containers
vuuvv (0.0.1)                                  - A web framework using flask,
                                                 like ror.
webargs (1.8.1)                                - A friendly library for
                                                 parsing and validating HTTP
                                                 request arguments, with
                                                 built-in support for popular
                                                 web frameworks, including
                                                 Flask, Django, Bottle,
                                                 Tornado, Pyramid, webapp2,
                                                 Falcon, and aiohttp.
webdeployer (0.0.4)                            - Personal Deployer for site
                                                 created with Flask and Django
weber_utils (1.2.2)                            - Utilities for the Weber flask
                                                 template
Webmaster (0.0.2)                              - A full stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
WebPortfolio (0.2.6)                           - A full stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
webspanner (0.1.0)                             - Spanner is a micro web
                                                 framework based on asyncio
                                                 inspired by Flask &
                                                 Express.js.
webstarts (2.9.0)                              - Entry point for modern
                                                 flask/gunicorn/sentry/celery
                                                 web applications
wfgfw (0.0.6)                                  - word filter for gfw, include
                                                 plugin for flask. download
                                                 keywords: https://github.com/
                                                 observerss/textfilter
wheelshop (0.1)                                - your python wheels on a PyPI
                                                 compatible server using flask
                                                 and S3
whs.utils.flask (0.2.0)                        - Some Flask utils, targeting
                                                 REST services
WTCrud (0.1dev)                                - CRUD forms for WTForms using
                                                 Flask, Jinja2, SQLAlchemy
xstat (0.1.9)                                  - make statsd work with flask,
                                                 django, maple or other server
yell (0.3.2)                                   - User notification library
                                                 with pluggable backends.
                                                 Compatible with popular
                                                 frameworks such as Django,
                                                 Flask, Celery.
Zask (1.9.5)                                   - Basic framework to use with
                                                 ZeroRPC inspired by Flask
zforms (1.8)                                   - Tiny Flask form validation
                                                 library.
Zolenmeyer (0.1)                               - Stupid personally customized
                                                 Flask
Rodneys-MBP:Desktop rodneyvictornjii$ python
Python 2.7.10 (default, Feb  7 2017, 00:08:15)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4+5
9
>>> 9.0/4
2.25
>>> my_string = "This is a string in the my_string variable"
>>> my_num = 5
>>> my_sting = "I can change my value whenever i like"
>>> my_list = [4,2,9,7
... my_list = [4,2,9,7
