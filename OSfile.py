import argparse,os

parser = argparse.ArgumentParser(prog="Show system file for Mac OS")
parser.add_argument('-v',"--version",action="version",version="%(prog)s v1.0")
parser.add_argument("-s","--show",action="store_true",
	help="show the unvisible file for Mac OS")
parser.add_argument("-n","--notshow",action="store_true",
	help="hide the unvisible file for Mac OS")
args=parser.parse_args()

if args.show:
	os.system('defaults write com.apple.finder AppleShowAllFiles -bool true')
	os.system('killall Finder')
	pass
if args.notshow:
	os.system('defaults write com.apple.finder AppleShowAllFiles -bool false')
	os.system('killall Finder')
	pass
if args.version:
	parser.parse_args(['--version'])
	pass
	

