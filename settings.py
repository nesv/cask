# Bourbon's settings module.
# 
# To see a complete list of options that are supported by Flask (and in-turn,
# Bourbon), see the following:
#
#    http://flask.pocoo.org/docs/config/#builtin-configuration-values

# Set the hostname/IP address and port that Flask/Bourbon should listen on.
# For production, un-comment this line
#SERVER_NAME = "my.domain.com:8008"

# Enable debugging?
# 
# If you set DEBUG = True, then Flask will automatically reload every time you
# change a file. So, if you are developing Bourbon, it is usually a good idea
# to set this to True.
DEBUG = False

# Enable/disable testing mode.
TESTING = False

# The SQLALCHEMY_DATABASE_URI setting lets you specify the connection URI used
# to connect to an SQL database.
#
# For some reference material as to how to properly concoct a connection URI
# for SQLAlchemy:
#
#     http://docs.sqlalchemy.org/en/rel_0_8/core/engines.html#sqlalchemy.create_engine
SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/bourbon.db"
