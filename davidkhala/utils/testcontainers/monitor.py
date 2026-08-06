from testcontainers.core.container import DockerContainer


def get(container:DockerContainer):
    wrapped = container.get_wrapped_container()
    wrapped.reload()
    return wrapped