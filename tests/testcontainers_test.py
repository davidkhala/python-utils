import platform
import unittest
from time import sleep

from docker.errors import NotFound

from davidkhala.utils.testcontainers import persistent

_is_windows = platform.system() == "Windows"


class PersistTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        persistent()

    @unittest.skipIf(_is_windows, "Linux containers are not available on Windows runners")
    def test_redis(self):

        from testcontainers.core.container import DockerContainer
        from davidkhala.utils.testcontainers.monitor import get
        container = DockerContainer("redis:latest")
        container.start()
        sleep(20)
        wrapped = get(container)

        self.assertEqual(wrapped.status, "running")
        container.stop()
        try:
            wrapped.reload()
            # 如果 reload 成功，说明容器还在 → 失败
            self.fail("Container still exists after stop()")
        except NotFound:
            # 404 → 容器已删除 → 成功
            return

    @unittest.skipUnless(_is_windows, "Windows containers are only available on Windows runners")
    def test_windows_container(self):
        from testcontainers.core.container import DockerContainer
        from davidkhala.utils.testcontainers.monitor import get
        container = DockerContainer("mcr.microsoft.com/windows/servercore:ltsc2025")
        container.with_command(["cmd", "/c", "ping -t localhost"])
        container.start()
        sleep(20)
        wrapped = get(container)

        self.assertEqual(wrapped.status, "running")
        container.stop()
        try:
            wrapped.reload()
            # 如果 reload 成功，说明容器还在 → 失败
            self.fail("Container still exists after stop()")
        except NotFound:
            # 404 → 容器已删除 → 成功
            return


if __name__ == '__main__':
    unittest.main()
