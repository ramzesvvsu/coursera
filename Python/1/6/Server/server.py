import asyncio

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    dict = {}
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

def process_data(encoding_data, csp):
    encoding_data_split = encoding_data.split(' ')
    if encoding_data_split[0] == 'put' \
            and len(encoding_data_split) == 4:
        #print(encoding_data)
        key = encoding_data_split[1]
        timestamp = int(encoding_data_split[3])
        value = float(encoding_data_split[2])
        if key not in csp.storage:
            csp.storage[key] = []
        if not (timestamp, value) in csp.storage[key]:
            csp.storage[key].append((timestamp, value))
        return "ok\n\n"
    elif encoding_data_split[0] == 'get' \
            and len(encoding_data_split) == 2:
        #print(encoding_data)
        key = encoding_data_split[1].strip()
        if len(csp.storage) == 0:
            return "ok\n\n"
        else:
            str_return = 'ok'
            for current_key in csp.storage:
                if key == current_key or key == '*':
                    for current_value in csp.storage[current_key]:
                        str_return += \
                            f'\n {current_key} {current_value[1]} {current_value[0]}'
            str_return += '\n\n'
            return str_return
    else:
        return 'error\nwrong command\n\n'


class ClientServerProtocol(asyncio.Protocol):
    storage = {}
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = process_data(data.decode(), self)
        self.transport.write(resp.encode())


