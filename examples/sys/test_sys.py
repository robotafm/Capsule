import sys
import hashlib
import socket

def get_current_server_hash():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    platform = sys.platform
    hasher_sha3_512 = hashlib.sha3_512()
    text = (hostname+'|'+ip_address+'|'+platform).encode()
    hasher_sha3_512.update(text)
    return(hasher_sha3_512.hexdigest())

def main():
    print("sys.argv=", sys.argv)
    print("sys.byteorder=", sys.byteorder)
    print("sys.builtin_module_names=", sys.builtin_module_names)
    print("sys.copyright=", sys.copyright)
    print("sys.dllhandle=", sys.dllhandle)
    print("sys.exc_info()=", sys.exc_info())
    print("sys.exec_prefix=", sys.exec_prefix)
    print("sys.executable=", sys.executable)
    print("sys.flags=", sys.flags)
    print("sys.float_info=", sys.float_info)
    print("sys.getdefaultencoding()=", sys.getdefaultencoding())
    print("sys.getswitchinterval()=", sys.getswitchinterval())
    print("sys.getwindowsversion()=", sys.getwindowsversion())
    print("sys.hash_info=", sys.hash_info)
    print("sys.path=", sys.path)
    print("sys.path_importer_cache=", sys.path_importer_cache )
    print("sys.platform=", sys.platform)
    print("sys.prefix=", sys.prefix)
    print("sys.dont_write_bytecode=", sys.dont_write_bytecode)
    print("sys.version=", sys.version )
    print("sys.api_version=", sys.api_version )
    print("sys.version_info=", sys.version_info )
    print("sys.warnoptions=", sys.warnoptions)
    print("sys.winver=", sys.winver)

    # sys.setdlopenflags(flags) - установить значения флагов для вызовов dlopen().
    # sys.setrecursionlimit(предел) - установить максимальную глубину рекурсии.
    # sys.setswitchinterval(интервал) - установить интервал переключения потоков.
    # sys.settrace(tracefunc) - установить "след" функции.
    # sys.stdin - стандартный ввод.
    # sys.stdout - стандартный вывод.
    # sys.stderr - стандартный поток ошибок.
    # sys.__stdin__, sys.__stdout__, sys.__stderr__ - исходные значения потоков ввода, вывода и ошибок.

    print(get_current_server_hash())


if __name__ == '__main__':
    main()