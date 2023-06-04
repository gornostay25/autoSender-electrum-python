import multiprocessing
import time
import os
from electrum import daemon, SimpleConfig
from electrum import constants
from electrum.util import create_and_start_event_loop


def init_plugins(config, gui_name):
    from electrum.plugin import Plugins
    return Plugins(config, gui_name)


def run_daemon():
    print("Starting daemon")
    create_and_start_event_loop()

    configOptionst = {'cmd': 'daemon', 'verbosity': '', 'verbosity_shortcuts': '', 'portable': False, 'testnet': True,
                      'regtest': False, 'simnet': False, 'signet': False, 'offline': False, 'forget_config': False}
    configOptionst['cwd'] = os.getcwd()
    config = SimpleConfig(configOptionst)

    if config.get('testnet'):
        constants.set_testnet()

    fd = daemon.get_file_descriptor(config)
    if fd is not None:
        init_plugins(config, 'cmdline')
        d = daemon.Daemon(config, fd)
        print("started")
        d.run_daemon()
    else:
        print("Daemon already running")
        exit(1)


class ElectrumService:
    def __init__(self, wallet_pass, is_test_network):
        self.wallet_pass = wallet_pass
        self.defaultConfigOptionst = {'cmd': '', 'verbosity': '', 'verbosity_shortcuts': '', 'portable': False,
                                      'testnet': is_test_network, 'regtest': False, 'simnet': False, 'signet': False, 'offline': False, 'forget_config': False}

        self.defaultConfigOptionst['cwd'] = os.getcwd()
        config = SimpleConfig(self.defaultConfigOptionst)

        if config.get('testnet'):
            constants.set_testnet()

        self.wallet_path = config.get_wallet_path()
        self.loop, self.stop_loop, self.loop_thread = create_and_start_event_loop()

        self.daemon_process = multiprocessing.Process(target=run_daemon)
        self.daemon_process.start()
        time.sleep(5)
        self.load_wallet()

    def request_cmd(self, config, config_options):
        timeout = config.get('timeout', 60)
        if timeout:
            timeout = int(timeout)
        try:
            return daemon.request(config, 'run_cmdline', (config_options,), timeout)
        except daemon.DaemonNotRunning:
            print(
                "Daemon not running")
            self.stop_eventloop()
            exit(1)
        except Exception as e:
            print(str(e) or repr(e))

        return False

    def load_wallet(self):
        config_options = self.defaultConfigOptionst
        config_options['cmd'] = "load_wallet"
        config_options["password"] = self.wallet_pass
        config = SimpleConfig(config_options)

        result = self.request_cmd(config, config_options)

        if not result:
            print("Error load wallet")
            self.stop_eventloop()
            exit(1)
        else:
            print("Load wallet")

    def stop_eventloop(self):
        self.loop.call_soon_threadsafe(self.stop_loop.set_result, 1)
        self.loop_thread.join(timeout=1)

        self.daemon_process.terminate()
        self.daemon_process.join()

        exit(0)

    def getBalance(self):
        config_options = self.defaultConfigOptionst
        config_options['cmd'] = "getbalance"
        config = SimpleConfig(config_options)
        result = self.request_cmd(config, config_options)
        return result

    def payTo(self, destination, amount):
        # {'cmd': 'payto', 'verbosity': '', 'verbosity_shortcuts': '', 'portable': False, 'testnet': True, 'regtest': False, 'simnet': False, 'signet': False, 'offline': False, 'forget_config': False, 'nocheck': False, 'unsigned': False, 'rbf': True, 'addtransaction': False, 'destination': 'tb1qdvuczlvsqfud40wl7sujpad5qnfzatkgjglmhx', 'amount': '0.00001', 'cwd': 'C:\\Users\\gornostay25\\work\\wbl-1209958-electrum-python'}
        config_options = self.defaultConfigOptionst
        config_options['cmd'] = "payto"
        config_options["password"] = self.wallet_pass
        config_options['destination'] = destination
        config_options['description'] = "destination"
        config_options['amount'] = amount

        config_options['nocheck'] = False
        config_options['unsigned'] = False
        config_options['rbf'] = False
        config_options['addtransaction'] = True
        config = SimpleConfig(config_options)

        result = self.request_cmd(config, config_options)

        return result
