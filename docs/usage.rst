=====
Usage
=====

Define container with the :class:`zsl_openapi.module.OpenAPIModule`.

::

    class MyContainer(WebContainer):
        open_api = OpenAPIModule

Then you may use CLI `open_api` command.

::

    python app.py \
        open_api generate \
        --package storage.models.persistent \
        --output api/openapi_spec_full.yml \
        --description api/openapi_spec.yml
