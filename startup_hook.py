#!/bin/env python3

import datetime, zoneinfo, os, requests, socket, subprocess, json


def main():
    hostname = socket.gethostname()

    def get_address(addr_info):
        for row in addr_info:
            if row["family"] == "inet":
                return "{}/{}".format(row["local"], row["prefixlen"])
        return "-"

    inet_address_message = ""

    outputs = subprocess.check_output(["ip", "-j", "address", "show"])

    for row in json.loads(outputs):
        inet_address_message += "{} ({}) {} {}\n".format(row["ifname"], row["link_type"], row["address"], get_address(row["addr_info"]))

    now = datetime.datetime.now(zoneinfo.ZoneInfo("Asia/Tokyo"))
    nowstr = now.strftime('%Y.%m.%d-%H:%M:%S (%Z)')
    message = "Startup {}: {}\n{}\n".format(nowstr, hostname, inet_address_message)

    main_content = {'content': message}
    headers = {'Content-Type': 'application/json'}
    discord_webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    requests.post(discord_webhook_url, json.dumps(main_content), headers=headers)


if __name__ == '__main__':
    main()
