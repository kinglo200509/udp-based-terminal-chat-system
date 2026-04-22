# UDP-Based Terminal Chat System

> ⚠️ **STATUS: This project is currently under development/process**

A simple yet powerful UDP-based chat application that allows multiple clients to communicate with a central server using terminal interface.

## Features

- **UDP Protocol**: Lightweight and fast communication using UDP sockets
- **Server-Client Architecture**: Centralized server handling multiple clients
- **Broadcast Messaging**: Support for broadcasting messages across clients
- **Terminal Interface**: Simple command-line interface for easy interaction
- **Message Tracking**: Server tracks messages and client information


## Project Structure

```
udp-based-terminal-chat-system/
├── Client/
│   ├── udp_client.py      # Basic UDP client for sending/receiving messages
│   ├── user_2.py          # Alternative client implementation
│   └── broadcast.py       # Broadcast client for multi-client messaging
├── Server/
│   └── upd_server.py      # UDP server handling client connections
├── README.md
├── LICENSE
└── .gitignore
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python's built-in `socket` module)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/udp-based-terminal-chat-system.git
   cd udp-based-terminal-chat-system
   ```

2. No additional dependencies required - uses Python's standard library

## Usage

### Starting the Server

1. Navigate to the Server directory:
   ```bash
   cd Server
   ```

2. Run the server:
   ```bash
   python upd_server.py
   ```

The server will start listening on the configured IP address and port (default: 192.168.1.4:9999)

### Starting a Client

In a separate terminal, navigate to the Client directory and run:

```bash
# Using the basic UDP client
cd Client
python udp_client.py
```

Or use the alternative client:
```bash
python user_2.py
```

### Broadcast Messaging

For broadcast messaging across multiple clients:
```bash
python broadcast.py
```

## How It Works

1. **Server**: Listens for incoming UDP messages, stores client information, and sends acknowledgments
2. **Client**: Connects to the server and sends/receives messages in a loop
3. **Broadcast**: Sends messages to all interfaces on a specific port

### Message Flow

```
Client sends message → Server receives → Server stores data → Server sends acknowledgment → Client receives acknowledgment
```

## Example Session

### Terminal 1 - Server:
```
listening to the loopback address:192.168.1.4 at port number: 9999
Received:- Hello from Client
ip-: 192.168.1.5
port-: 54321
```

### Terminal 2 - Client:
```
What to send:- Hello from Client
This is the received msg:- b'Hello from Client'
This is the Server Address:- ('192.168.1.4', 9999)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created as a networking project to demonstrate UDP socket programming in Python.

## Disclaimer

This is an educational project. For production use, consider using established messaging systems with proper security measures.

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.

---

**Happy Chatting! 💬**
