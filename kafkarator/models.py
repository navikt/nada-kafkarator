from k8s.base import Model
from k8s.fields import Field, ListField
from k8s.models.common import ObjectMeta


class TopicSpec(Model):
    name = Field(str)
    config = Field(dict)


class Topic(Model):
    """Configures a topic"""

    class Meta:
        list_url = "/apis/kafkarator.nais.io/v1/topic"
        url_template = "/apis/kafkarator.nais.io/v1/namespaces/{namespace}/topic/{name}"
        watch_list_url = "/apis/kafkarator.nais.io/v1/watch/topics"
        watch_list_url_template = "/apis/kafkarator.nais.io/v1/watch/namespaces/{namespace}/topics"

    apiVersion = Field(str, "kafkarator.nais.io/v1")
    kind = Field(str, "Topic")
    metadata = Field(ObjectMeta)
    spec = Field(TopicSpec)


class TopicAccessUsers(Model):
    producers = ListField(str)
    consumers = ListField(str)


class TopicReference(Model):
    name = Field(str)
    namespace = Field(str)
    cluster = Field(str)


class TopicAccessSpec(Model):
    topic = Field(TopicReference)
    granted = Field(TopicAccessUsers)
    requested = Field(TopicAccessUsers)


class TopicAccess(Model):
    """Manages access to a topic"""

    class Meta:
        list_url = "/apis/kafkarator.nais.io/v1/topic-access"
        url_template = "/apis/kafkarator.nais.io/v1/namespaces/{namespace}/topic-access/{name}"
        watch_list_url = "/apis/kafkarator.nais.io/v1/watch/topic-accesses"
        watch_list_url_template = "/apis/kafkarator.nais.io/v1/watch/namespaces/{namespace}/topic-accesses"

    apiVersion = Field(str, "kafkarator.nais.io/v1")
    kind = Field(str, "TopicAccess")
    metadata = Field(ObjectMeta)
    spec = Field(TopicAccessSpec)


class ApplicationTopicSpec(Model):
    application = Field(str)
    produces = ListField(TopicReference)
    consumes = ListField(TopicReference)


class ApplicationTopic(Model):
    """Maps Application to the topics it produces to or consumes from"""

    class Meta:
        list_url = "/apis/kafkarator.nais.io/v1/application-topic"
        url_template = "/apis/kafkarator.nais.io/v1/namespaces/{namespace}/application-topic/{name}"
        watch_list_url = "/apis/kafkarator.nais.io/v1/watch/application-topics"
        watch_list_url_template = "/apis/kafkarator.nais.io/v1/watch/namespaces/{namespace}/application-topics"

    apiVersion = Field(str, "kafkarator.nais.io/v1")
    kind = Field(str, "ApplicationTopic")
    metadata = Field(ObjectMeta)
    spec = Field(ApplicationTopicSpec)
