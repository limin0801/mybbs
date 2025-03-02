from pecan import rest
from pecan import expose

from mybbsbackend.database.api import topic as api_topic
from mybbsbackend.database.model import topic as model_topic


class TopicController(rest.RestController):
    def __init__(self):
        self.topic = api_topic.TopicAPI()

    @expose('json')
    def get_one(self, title):
        return self.topic.get_one_by_title(title)

    @expose('json')
    def get_all(self):
        return self.topic.get_all()

    @expose('json')
    def post(self, topic):
        topic = model_topic.TopicModel(**topic)
        return self.topic.add_one(topic)

    @expose('json')
    def put(self, topic):
        return self.topic.update_topic(topic)

    @expose('json')
    def delete(self, topic):
        self.topic.delete_topic_by_id(topic)
        return None
