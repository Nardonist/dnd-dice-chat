def convert_host_to_int(host: str) -> int:
    try:
        parts = host.split(".")
        if len(parts) == 4:
            return (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])
        else:
            return abs(hash(host)) % (1 << 31)
    except Exception:
        return abs(hash(host)) % (1 << 31)


def convert_int_to_host(value: int) -> str:
    # Try to convert a 32-bit int to IPv4 dotted string
    try:
        if 0 <= value <= 0xFFFFFFFF:
            return ".".join(str((value >> (8 * i)) & 0xFF) for i in reversed(range(4)))
        else:
            return str(value)
    except Exception:
        return str(value)
