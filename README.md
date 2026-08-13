# TCP Port Scanner

A simple Python-based TCP port scanner that checks whether a range of ports is open on a target host and prints the status along with common service names.

## Features

- Scans a specified host and port range
- Uses TCP connection attempts to detect open ports
- Displays common service names for well-known ports
- Uses multithreading to speed up scanning
- Works as a lightweight command-line utility

## Requirements

- Python 3.x
- Standard library modules only: `socket`, `threading`

## Usage

1. Run the script:

```bash
python Main.py
```

2. Enter the target host:

```text
Enter host to scan: example.com
```

3. Enter the starting and ending ports:

```text
Enter starting port: 1
Enter ending port: 100
```

The program will scan each port in the given range and print open ports like this:

```text
[OPEN]   80     HTTP
[OPEN]   443    HTTPS
```

## Example

```bash
python Main.py
```

## Notes

- Use this tool responsibly and only on systems you own or have explicit permission to test.
- Some networks may block or rate-limit port scans.
- The script uses a timeout of 1 second per connection attempt.

## License

This project is provided for educational and learning purposes.
