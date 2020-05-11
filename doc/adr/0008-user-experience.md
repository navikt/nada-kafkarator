# 8. User experience

Date: 2020-05-11

## Status

Under discussion

See also [6. Kafkarator API is focused around dedicated CRDs](0006-kafkarator-api-is-focused-around-dedicated-crds.md)

## Context

While CRDs are a good API for Kubernetes Operators, they are not in common use for most developers, and a better
user experience is wanted.

Users today are used to creating an Application object to deploy their application. For users who are not owning a
topic, it would be easier if they can declare their topics as part of the Application resources.

There are other use cases where parts of the Application object are translated into a specific CRD handled by a separate
operator. This model can also be used here. This will move some of the responsibility from Kafkarator to Naiserator,
but the user experience will be better. The added complexity in Naiserator is acceptable.

## Decisions

- We will keep the CRDs as detailed in [6. Kafkarator API is focused around dedicated CRDs](0006-kafkarator-api-is-focused-around-dedicated-crds.md)
- Naiserator will create the CRDs based on configuration in Application
- Kafkarator will create topic and provide credentials as Secrets based on CRDs
- Naiserator will inject the Secrets in the Deployment

## Consequences

With this decision, the user experience is simpler. All they have to do is add some fields to their Application object,
and we will make sure they have everything they need to produce/consume kafka messages.

Naiserator will grow additional responsibilities, but the NAIS team are not concerned about increased complexity.
