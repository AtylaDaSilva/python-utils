from typing import TypeVar, Type, Any
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
    if len(numeros) != 14:
        raise ValueError("A string deve conter exatamente 14 dígitos.")

    return f"{numeros[:2]}.{numeros[2:5]}.{numeros[5:8]}/{numeros[8:12]}-{numeros[12:]}"


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
