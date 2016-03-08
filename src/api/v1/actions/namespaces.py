import logging

from tornado.gen import coroutine, Return

from data.query import Query


class NamespacesActions(object):

    def __init__(self, settings, user):
        logging.info("Initializing NamespacesActions")

        self.kube = settings['kube']
        self.database = settings["database"]
        self.user = user

    def check_permissions(self, operation, _document):
        logging.debug("check_permissions for user %s and operation %s on namespaces", self.user["username"], operation)
        return True

    @coroutine
    def create(self, namespace):
        logging.info("Creating namespace")
        body = {
            'kind': 'Namespace',
            'apiVersion': 'v1',
            'metadata': {
                'name': namespace['name'],
                'labels': [
                    {'name': namespace['name']}
                ]
            }
        }
        response = yield self.kube.namespaces.post(body)
        raise Return(response)

    @coroutine
    def update(self, document):
        logging.info("Updating namespace")

        user = yield Query(self.database, "Users").find_one(document['_id'])
        yield Query(self.database, "Users").update(user)

        raise Return(user)

    @coroutine
    def delete(self, document):
        logging.info("Deleting namespace")

        namespace = yield Query(self.database, "Namespaces").find_one(document["_id"])
        raise Return(namespace)
