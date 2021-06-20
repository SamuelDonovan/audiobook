.ONESHELL:

make m4b_tool:
	# install all dependencies
	sudo apt install ffmpeg mp4v2-utils php-cli php-intl php-json php-mbstring php-xml -y
	
	# install / upgrade m4b-tool
	sudo wget https://github.com/sandreas/m4b-tool/releases/download/v.0.4.2/m4b-tool.phar -O /usr/local/bin/m4b-tool && sudo chmod +x /usr/local/bin/m4b-tool
	
	# check installed m4b-tool version
	m4b-tool --version