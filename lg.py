__author__ = 'Luka.Grah'


# Main file for loggeter command line


from da_package import da_package
import argparse


def main():
    db = da_package.connect_database('disco.db')
    host_discovery = da_package.host_discovery('1.1.1.1','a','a',db)
    if host_discovery is not None:
        print host_discovery[0]
        print host_discovery[1]
        print host_discovery[2]
        ssh = da_package.connect_ssh('a','a','1.1.1.1')
        da_package.get_log(ssh,'/var/log/messages','c://razvoj//github/LogGatherer/messages.txt')
        da_package.get_command(ssh,'ls -al /','c://razvoj//github/LogGatherer/lsla.txt')
    else:
        print "jeba"






if __name__ == "__main__":
    main()


