{
	"servers": [
		{
		// Used in menu and as tree panel title
		// "display_name": "My Server",
		
		// IP or hostname (Required)
		"host": "example.com",
		
		// Default is 22
		 "port": 22,
		
		// Root directory at the server ("/" by default)
		 "remote_path": "/home/www/",
		
		// Directory at this computer to map to remote root (Required)
		// When you edit files on server they will be downloaded here first.
		// All files saved in this directory (or its subdirectories) will be uploaded to the appropriate paths on the server.
		"local_path": "E:\\phpstudy2018\\PHPTutorial\\tmp\\tmp_WWW",

		// Username
		"user": "",

		// Password (comment out if you're using private keys)
		"password": "",

		// Location of the private key file to use for authentication
		// Keys located at ~/.ssh are loaded automatically, you don't need to specify them here.
		// "ssh_key_file": "",

		// Password for the private key
		// "ssh_key_pass": "",

		// If true, ignores modification times of files and downloads them even if they are unchanged.
		 "always_download": true,

		// Timeout in seconds (5 seconds by default), 0 to disable
		"timeout":0,
	},
	]
}
