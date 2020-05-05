# nada-kafkarator

## Overview

Kafkarator has two responsibilities:

1. Create Kafka topics based on configuration provided by an application developer
2. Provide credentials needed for an application to connect to Kafka

The following are initial thoughts on how to go about this, but will probably need updating as we get around to
implementation.

### Topics

When an application needs to create a topic, developers create a Topic resource in Kubernetes. Kafkarator will detect 
this and create the topic with the given configuration.

### Credentials

When an application needs to produce or consume from a topic, it will indicate this by creating an AppTopic resource.
Kafkarator will then procure the required credentials, and provide them to the application.

## Contributing

### ADR

This project uses ADR to record architectural decisions. If you are wondering about choices we have made, explore the
`doc/adr` directory.

### Development

We use Poetry to manage dependencies. Preferably all code should be reviewed before committing to master, so please
create Pull Requests for your contributions. It is always wise to discuss the feature you want to implement in an issue
first, before starting to write code. That way you know that you are moving in the right direction.
