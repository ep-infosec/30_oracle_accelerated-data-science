score.py
--------

In the prepare step, the service automatically generates a ``score.py`` file in the artifact directory.


``score.py`` is used by the Data Science Model Deployment service to generate predictions in the input feature. Here is a minimal ``score.py`` implementation - 

.. code-block:: python3

    import joblib
    model_name = "model.joblib"

    def load_model(): # load_model must mandatorily return ``not None`` object.
      
      model = None
      with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), model_file_name), "rb") as mfile:
        model = joblib.load(mfile)
      return model

    def predict(data, model=load_model()):
      return model.predict(data).tolist()


ADS autogenerates framework specific score.py which provides following functionality - 

* Parse the input data and convert to pandas dataframe/numpy array/list
* Ensure the data type after converting to pandas dataframe matches the training time. This is achieved using the schema definition generated during ``prepare`` step.
* Serialize prediction generated by the model such that it is json serializable to avoid deployment runtime errors

You could customize the score.py to fit your use case. The most common use case for changing the ``score.py`` file is to add preprocessing and postprocessing steps to the ``predict()`` method. 

Refer Cusotmization section for how to change and verify the model artifacts.

The ``score.py`` consists of multiple functions among which the ``load_model`` and ``predict`` are most important.

load_model
~~~~~~~~~~

During deployment, the ``load_model`` method loads the serialized model. The ``load_model`` method is always fully populated, except when you set ``serialize=False`` for ``GenericModel``.

- For the ``GenericModel`` class, if you choose ``serialize=True`` in the init function, the model is pickled and the ``score.py`` is fully auto-populated to support loading the pickled model. Otherwise, the user is responsible to fill the ``load_model``. 
- For other frameworks, this part is fully populated.

**Note**: ``load_model`` should return ``not None`` value for successful deployment. 

predict
~~~~~~~

The ``predict`` method is triggered every time a payload is sent to the model deployment endpoint. The method takes the payload and the loaded model as inputs. Based on the payload, the method returns the predicted results output by the model.

pre_inference
~~~~~~~~~~~~~

If the payload passed to the endpoint needs preprocessing, this function does the preprocessing step. The user is fully responsible for the preprocessing step.

post_inference
~~~~~~~~~~~~~~

If the predicted result from the model needs some postprocessing, the user can put the logic in this function.

deserialize
~~~~~~~~~~~

When you use the ``.verify()`` or ``.predict()`` methods from model classes such as ``GenericModel`` or ``SklearnModel``, if the data passed in is not in bytes or JsonSerializable, the models try to serialize the data. For example, if a pandas dataframe is passed and not accepted by the deployment endpoint, the pandas dataframe is converted to JSON internally. When the ``X_sample`` variable is passed into the ``.prepare()`` function, the data type of pandas dataframe is passed to the endpoint, and the schema of the dataframe is recorded in the ``input_schema.json`` file. Then, the JSON payload is sent to the endpoint. Because the model expects to take a pandas dataframe, the ``.deserialize()`` method converts the JSON back to the pandas dataframe using the schema and the data type. For all frameworks except for the ``GenericModel`` class, the ``.deserialize()`` method is auto-populated. Note that for each framework, only specific data types are supported.

Starting from .. versionadded:: 2.6.3, you can send the bytes to the endpoint directly. If the bytes payload is sent to the endpoint, bytes are passed directly to the model. If the model expects a specific data format, you need to write the conversion logic yourself.

fetch_data_type_from_schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This function is used to load the schema from the ``input_schema.json`` when needed.
