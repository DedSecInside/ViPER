import argparse


class arguments():
    def get_arguments(self):
        parser = argparse.ArgumentParser(description="Web Recon Script")
        parser.add_argument('-u', '--url', type=str, help='URL', required=True)
        parser.add_argument('-A1', '--info', type=str, help='Injection Attacks')
        parser.add_argument('-A3', '--sql', type=str, help='XSS')
        args = parser.parse_args()
        target = args.url
        return target
