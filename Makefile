build:

install:
	sudo install -m 755 startup_hook.py /usr/local/bin/startup_hook.py
	sudo install -m 644 startup_hook.service /etc/systemd/system/startup_hook.service
	sudo touch /etc/default/startup_hook
	sudo systemctl daemon-reload
	sudo systemctl enable startup_hook

uninstall:
	sudo systemctl disable startup_hook || true
	sudo rm /usr/local/bin/startup_hook.py
	sudo rm /etc/systemd/system/startup_hook.service
	sudo systemctl daemon-reload

