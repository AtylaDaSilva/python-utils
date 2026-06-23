from typing import TypeVar, Type, Any
from collections.abc import Callable
from time import sleep
import re


def remover_pontuacao_cnpj(cnpj: str) -> str:
    """
        Remove toda a pontuação de um CNPJ.
    Args:
        cnpj: string do CNPJ a remover pontuação

    Returns:
        Nova string de *cnpj* com toda a pontuação removida.
    """
    return re.sub(r"[.\-/]", "", cnpj)


def aplicar_mascara_cnpj(numeros: str) -> str:
    n = numeros.strip().replace(".", "")
    len_numeros = len(n)
    if len_numeros != 14:
        raise ValueError(f"A string deve conter exatamente 14 dígitos, ´{n}´ contém {len_numeros}.")

    return f"{n[:2]}.{n[2:5]}.{n[5:8]}/{n[8:12]}-{n[12:]}"


T = TypeVar("T")


def safe_cast(value: Any, target_type: Type[T]) -> T:
    """
    Casts a value to the target type only if it's not already an instance of that type.

    Args:
        value: The value to potentially cast.
        target_type: The type to cast to.

    Returns:
        The value as the target type, either cast or unchanged.

    Raises:
        TypeError: If the value cannot be cast to the target type.
        ValueError: If the value is incompatible with the target type.
    """
    if isinstance(value, target_type):
        return value
    return target_type(value)


def retry_on_exception(
        func: Callable,
        max_attempts: int = 1,
        exception: type[Exception] | tuple[type[Exception], ...] = Exception,
        polling_seconds: float | None = 0.5,
        *args,
        **kwargs
) -> Any:
    """
        Invoke ``func``, retrying up to ``max_attempts`` times if it raises ``exception``.
        Returns whatever ``func`` returns on the first successful attempt.

        Args:
            func: Callable with zero or more arguments.
            max_attempts: Maximum number of execution attempts. Defaults to 1
                (invokes ``func`` at least once).
            exception:
                Re-invokes ``func`` if ``exception`` is raised.
            polling_seconds:
                Amount of seconds to wait before invoking ``func`` again.
                If ``polling_seconds`` is None, retries ``func`` immediately.
            *args, **kwargs:
                Any positional or keyword arguments to be passed to ``func``.
        Returns:
            Whatever ``func()`` returns on the first successful attempt.
        Raises:
            Exception: Re-raises the last caught exception (of the type(s) passed via ``exception``)
            when all attempts are exhausted.
            ValueError: If ``max_attempts`` is less than 1.
        Example:
            >>> def flaky():
            ...     ...
            >>> retry_on_exception(func=flaky, max_attempts=3)
        """
    if max_attempts < 1:
        raise ValueError(f"max_attempts must be >= 1, got {max_attempts}")

    for attempt in range(max_attempts):
        try:
            return func(*args, **kwargs)
        except exception as exc:
            if attempt == max_attempts - 1:
                raise
            if polling_seconds:
                sleep(polling_seconds)

    return None  # If max_attempts <= 0
