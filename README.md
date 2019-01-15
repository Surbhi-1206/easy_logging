# easy_logging_conifg
An easy to use logging library which returns a basic logging configuration for any python application.

- Class LogConfiguration accepts the root path of location to store log records
- On Initialization, the default components(filters, formatters, handlers and loggers) are populated. The get() method fetches   the complete configuration.
- The class has four methods to fetch logging components. These methods can be overridden by the class which extends
  "LogConfiguration", to add custom components to existing default components. 
  
  "pip install easy-logging-config" - Run this command to install the package
