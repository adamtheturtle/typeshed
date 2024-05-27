import datetime
from _typeshed import Incomplete
from typing import Literal, NamedTuple, overload

from docker.types.daemon import CancellableStream

from .images import Image
from .resource import Collection, Model

class Container(Model):
    @property
    def name(self) -> str | None: ...
    @property
    def image(self) -> Image | None: ...
    @property
    def labels(self): ...
    @property
    def status(self) -> str: ...
    @property
    def health(self) -> str: ...
    @property
    def ports(self) -> dict[Incomplete, Incomplete]: ...
    def attach(self, **kwargs): ...
    def attach_socket(self, **kwargs): ...
    def commit(self, repository: str | None = None, tag: str | None = None, **kwargs): ...
    def diff(self): ...
    def exec_run(
        self,
        cmd,
        stdout: bool = True,
        stderr: bool = True,
        stdin: bool = False,
        tty: bool = False,
        privileged: bool = False,
        user: str = "",
        detach: bool = False,
        stream: bool = False,
        socket: bool = False,
        environment: Incomplete | None = None,
        workdir: Incomplete | None = None,
        demux: bool = False,
    ) -> ExecResult: ...
    def export(self, chunk_size: int | None = 2097152) -> str: ...
    def get_archive(
        self, path, chunk_size: int | None = 2097152, encode_stream: bool = False
    ) -> tuple[Incomplete, Incomplete]: ...
    def kill(self, signal: Incomplete | None = None): ...
    @overload
    def logs(
        self,
        stdout: bool = True,
        stderr: bool = True,
        *,
        stream: Literal[True],
        timestamps: bool = False,
        tail: Literal["all"] | int = "all",
        since: datetime.datetime | float | None = None,
        follow: bool | None = None,
        until: datetime.datetime | float | None = None,
    ) -> CancellableStream: ...
    @overload
    def logs(
        self,
        stdout: bool,
        stderr: bool,
        stream: Literal[True],
        timestamps: bool = False,
        tail: Literal["all"] | int = "all",
        since: datetime.datetime | float | None = None,
        follow: bool | None = None,
        until: datetime.datetime | float | None = None,
    ) -> CancellableStream: ...
    @overload
    def logs(
        self,
        stdout: bool = True,
        stderr: bool = True,
        stream: Literal[False] = False,
        timestamps: bool = False,
        tail: Literal["all"] | int = "all",
        since: datetime.datetime | float | None = None,
        follow: bool | None = None,
        until: datetime.datetime | float | None = None,
    ) -> bytes: ...
    def pause(self): ...
    def put_archive(self, path: str, data) -> bool: ...
    def remove(self, **kwargs) -> None: ...
    def rename(self, name: str): ...
    def resize(self, height: int, width: int): ...
    def restart(self, **kwargs): ...
    def start(self, **kwargs) -> None: ...
    def stats(self, **kwargs): ...
    def stop(self, **kwargs) -> None: ...
    def top(self, **kwargs): ...
    def unpause(self): ...
    def update(self, **kwargs): ...
    def wait(self, **kwargs): ...

class ContainerCollection(Collection[Container]):
    model: type[Container]
    def run(
        self,
        image: str | Image,
        command: str | list[str] | None = None,
        stdout: bool = True,
        stderr: bool = False,
        remove: bool = False,
        **kwargs,
    ): ...
    def create(self, image: str, command: str | list[str] | None = None, **kwargs) -> Container: ...  # type:ignore[override]
    def get(self, container_id: str) -> Container: ...
    def list(
        self,
        all: bool = False,
        before: str | None = None,
        filters: Incomplete | None = None,
        limit: int = -1,
        since: str | None = None,
        sparse: bool = False,
        ignore_removed: bool = False,
    ): ...
    def prune(self, filters: Incomplete | None = None): ...

RUN_CREATE_KWARGS: list[str]
RUN_HOST_CONFIG_KWARGS: list[str]

class ExecResult(NamedTuple):
    exit_code: Incomplete
    output: Incomplete
