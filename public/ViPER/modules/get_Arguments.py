import argparse


class arguments():
    def get_arguments(self):
        parser = argparse.ArgumentParser(description="Web Recon Script")
        parser.add_argument('-u', '--url', type=str, help='URL', required=True)
        args = parser.parse_args()
        target = args.url
        return target
