import socket
import time

class ClientError(Exception):
    pass
'''    def __init__(self, value):
        self.msg = value

    def __str__(self):
        return self.msg
'''
class Client():
    def __init__(self, adress, port, timeout=None):
        self.adress = adress
        self.port = port
        self.timeout = timeout
        #self.sock = socket.create_connection((adress,port), timeout)
        #self.dict = {}

    def get(self, filter):
        #print(f'get filter {filter} class {self}')

        def str_to_dict(str):
            val = {}
            for current_row in str:
                val_list = current_row.split(' ')
                if val_list[0] in val:
                    val[val_list[0]].append((int(val_list[2]), float(val_list[1])))
                else:
                    val[val_list[0]] = [(int(val_list[2]), float(val_list[1]))]
            for key in val:
                val[key] = sorted(val[key], key=lambda x:x[0])
            return val

        with socket.create_connection((self.adress, self.port), self.timeout) as sock:
            try:
#                if filter == '*':
#                    return_val = {}
#                    for key in self.dict.keys():
#                        return_val[key] = [x for x in self.dict[key].items()]
                sock.send(f'get {filter}\n'.encode('utf-8'))
                answer = sock.recv(1024)
                if answer == "error\nwrong command\n\n":
                    raise ClientError
                dict = str_to_dict(answer.decode('utf-8').split('\n')[1:-2])
                return dict
            #                    return return_val
#                else:
#                    if filter in self.dict:
#                        return {filter : [x for x in self.dict[filter].items()]}
#                    else:
                        #raise ClientError()
#                        return {}
            except:
                raise ClientError

    def put(self, key, value, timestamp=None):
        #print(f'add value {value} for key {key} and class {self}')

        if timestamp is None:
            timestamp = int(time.time())

#        value = {timestamp: value}
#        if not key in self.dict:
#            self.dict.update({key: value})
#        else:
#            self.dict[key].update(value)
        with socket.create_connection((self.adress, self.port), self.timeout) as sock:
            try:
                sock.send(f'put {key} {value} {timestamp}\n'.encode('utf-8'))
                answer = sock.recv(1024)
                if answer == "error\nwrong command\n\n":
                    raise ClientError
            except:
                raise ClientError

if __name__ == '__main__':
    client = Client("127.0.0.1", 8888, timeout=15)

    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 2.0, timestamp=1150864248)
    client.put("palm.cpu", 0.5, timestamp=1150864248)

    client.put("eardrum.cpu", 3, timestamp=1150864250)
    client.put("eardrum.cpu", 4, timestamp=1150864251)
    client.put("eardrum.memory", 4200000)

    print(client.get("*"))
    print(client.get('get_client_error'))