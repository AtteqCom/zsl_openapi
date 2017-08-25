from zsl_openapi.api import ApiDescription, ApiPathItem, ApiOperation

from zsl import inject
from zsl.router.task import TaskConfiguration

from zsl_openapi.builders import ApiDescriptionBuilder


class TaskApiDescriptionBuilder(ApiDescriptionBuilder):
    @inject(task_configuration=TaskConfiguration)
    def __init__(self, task_configuration):
        # type: (TaskConfiguration)->None
        self._task_configuration = task_configuration  # type: TaskConfiguration

    def build(self, api_description):
        # type: (ApiDescription)->None

        for namespace in self._task_configuration.namespaces:
            for route, task in namespace.get_routes().items():
                path = namespace.namespace + '/' + route
                # api_description
                print(path + ' -> ' + str(task))
                path_item = ApiPathItem()
                path_item.post = ApiOperation()
                path_item.post.description = task.__doc__
                path_item.post.parameters
                api_description.add_path(path_item)
