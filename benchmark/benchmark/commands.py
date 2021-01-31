from os.path import join


class CommandMaker:

    @staticmethod
    def cleanup():
        return ('rm -r .db-* ; rm .*.json ; rm -r logs ; '
                'rm node ; rm client ; mkdir -p logs')

    @staticmethod
    def compile():
        return 'cargo build --quiet --release --features benchmark'

    @staticmethod
    def generate_key(filename):
        assert isinstance(filename, str)
        return f'./node keys --filename {filename}'

    @staticmethod
    def run_node(keys, committee, store, parameters, debug=False):
        assert isinstance(keys, str)
        assert isinstance(committee, str)
        assert isinstance(parameters, str)
        assert isinstance(debug, bool)
        v = '-vvv' if debug else '-vv'
        return (f'./node {v} run --keys {keys} --committee {committee} '
                f'--store {store} --parameters {parameters}')

    @staticmethod
    def run_client(address, txs, size, rate, timeout, nodes=[]):
        assert isinstance(address, str)
        assert isinstance(txs, int)
        assert isinstance(size, int) and size > 0
        assert isinstance(rate, int) and rate >= 0
        assert isinstance(nodes, list) 
        assert all(isinstance(x, str) for x in nodes)
        nodes = f'--nodes {" ".join(nodes)}' if nodes else ''
        return (f'./client {address} --transactions {txs} --size {size} '
                f'--rate {rate} --timeout {timeout} {nodes}')

    @staticmethod
    def kill():
        return 'tmux kill-server'

    @staticmethod
    def alias_binaries(origin):
        assert isinstance(origin, str)
        node, client = join(origin, 'node'), join(origin, 'client')
        return f'ln -s {node} . ; ln -s {client} .'