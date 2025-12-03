Uses the Kubernetes [Gateway API](https://gateway-api.sigs.k8s.io/) for authorization.

The first version always passes through a `200` unless the route is `/unauthorized`.