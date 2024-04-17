{% macro my_model() %}
{{
    config(
        materialized='table'
    )
}}

{% set my_python_script = '/Users/jakemaund/Desktop/final_project/final_project_DEz/macros/ELT_Python_Script.py' %}

{{ run-operation(
    python_script=my_python_script,
    args={
        'project_id': 'praxis-wall-411617',
        'dataset_id': 'final_project_DEz_BQ',
        'table_id': 'final_project_JM'
    }
) }}
{% endmacro %}
