__author__ = 'Luka.Grah'


# Main file for loggeter command line


from da_package import da_package
import argparse


def main():
    db = da_package.connect_database('disco.db')
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--add_host',  nargs=3, metavar=('HOSTNAME','USERNAME','PASSOWRD'))
    group.add_argument('--delete_host',nargs=1, metavar=('HOSTNAME'))
    group.add_argument('--register_host',nargs=1, metavar=('HOSTNAME'))
    group.add_argument('--list_hosts')
    group.add_argument('--get_all_logs')


    #parser.add_argument("hostname", type=str, help="hostname")
    #parser.add_argument("username", type=str, help="username")
    #parser.add_argument("password", type=str, help="password")
    args = parser.parse_args()


    if args.add_host:
         if args.add_host[0] is not None and args.add_host[1] is not None and args.add_host[2] is not None:
             hostname_id = da_package.add_server(args.add_host[0],args.add_host[1],args.add_host[2],db)
             print hostname_id

    if args.delete_host:
        if args.delete_host[0] is not None:
            da_package.delete_server(args.delete_host[0],db)
    if args.register_host:
        if args.register_host[0] is not None:
            da_package.register_host(args.register_host[0]












if __name__ == "__main__":
    main()


