.. _Data_Catalog_Metastore:

######################
Data Catalog Metastore
######################

This section demonstrates how to configure the ``spark-defaults.conf`` file so that you can connect with the Oracle Cloud Infrastructure (OCI) `Data Catalog Metastore <https://docs.oracle.com/en-us/iaas/data-catalog/using/metastore.htm>`__. This connection is used to run a `PySpark <https://spark.apache.org/docs/latest/api/python/>`__ application using OCI `Data Flow <https://docs.oracle.com/en-us/iaas/data-flow/using/home.htm>`__ and `Data Science Jobs <https://docs.oracle.com/en-us/iaas/tools/ads-sdk/latest/user_guide/jobs/overview.html>`__. The data will be stored in OCI `Object Storage <https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm>`__. Thus, you will work with data that is stored in Object Storage, information about the location and structure of that data will be managed by Data Catalog Metastore, compute will be provided by Data Flow and all of this will be run in a Job.

OCI `Data Catalog <https://docs.oracle.com/en-us/iaas/data-catalog/home.htm>`__ is a metadata management service that helps data professionals discover data and support data governance. The `Data Catalog Metastore <https://docs.oracle.com/en-us/iaas/data-catalog/using/metastore.htm>`__ provides schema definitions for objects in structured and unstructured data assets that reside in Object Storage.  Use the metastore as a central metadata repository to manage data tables that are backed by files in Object Storage.

OCI `Data Flow <https://docs.oracle.com/en-us/iaas/data-flow/using/home.htm>`__ is a fully managed `Apache Spark <https://spark.apache.org/>`__ service. This section demonstrates how to use PySpark to create Spark applications.

`Data Science Jobs <https://docs.oracle.com/en-us/iaas/tools/ads-sdk/latest/user_guide/jobs/overview.html>`__ allows you to run customized tasks outside of a notebook session. A Job is a template that describes a task that you want to perform. In this section, that task is to run a PySpark application using Data Flow. Since the Job is run outside of a notebook, command-line arguments can be passed to the Job such that it performs customized activities. OCI `Logging <https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/loggingoverview.htm>`__ is used to capture events. You can also read and write data to Object Storage directly or with the aid of Data Catalog.

Data Flow can access the Data Catalog Metastore to securely store and retrieve schema definitions for unstructured and structured data assets in Object Storage. For integration with Data Flow, the metastore provides an invocation endpoint. This endpoint is a Hive Metastore interface. 

`Apache Hive <https://hive.apache.org/>`__ is a data warehousing framework that facilitates read, write, or manage operations on large datasets residing in distributed file systems. The Data Catalog Metastore is backed by the Apache Hive Metastore. A Hive Metastore is the central repository of metadata for a Hive cluster.  It stores metadata for data structures such as databases, tables, and partitions in a relational database, backed by files maintained in Object Storage. `Apache Spark SQL <https://spark.apache.org/sql/>`__ makes use of a Hive Metastore for this purpose. 


.. toctree::
    :hidden:
    :maxdepth: 1

    prerequisite
    quick_start
    data_flow
    interactive_spark

