import simple_func

import mlflow

from mlflow.models.signature import ModelSignature
from mlflow.types import DataType, Schema, ColSpec, TensorSpec


# Define custom Python model class
class AddModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        pass

    def predict(self, context, inputs):
        output = simple_func.simple_add(inputs["input"][0])
        return output


# Define input and output schema
input_schema = Schema([
    ColSpec(DataType.string, "input"),
])
output_schema = Schema([ColSpec(DataType.string, "output")])
signature = ModelSignature(inputs=input_schema, outputs=output_schema)

# Define input example
input_example = {"input": "123"}

# Log the model with its details such as artifacts, pip requirements and input example
with mlflow.start_run() as run:
    mlflow.pyfunc.log_model("model",
                            python_model=AddModel(),
                            artifacts={},
                            pip_requirements=["numpy"],
                            input_example=input_example,
                            signature=signature)

# Register model in MLflow Model Registry
result = mlflow.register_model("runs:/" + run.info.run_id + "/model",
                               "simple_func")

# Load the logged model
loaded_model = mlflow.pyfunc.load_model('runs:/' + run.info.run_id + '/model')

# Make a prediction using the loaded model
result = loaded_model.predict(input_example)

print(f"[mlflow_test] {result}")
