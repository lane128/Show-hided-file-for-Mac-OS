import argparse,os

parser = argparse.ArgumentParser(description="Show system file for Mac OS by Lane128.",
	formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-v',"--version",action="version",version="%(prog)s v1.1",default=None)
parser.add_argument("-s","--show",action="store_true",default=None,
	help="show the unvisible file for Mac OS")
parser.add_argument("-n","--notshow",action="store_true",default=None,
	help="hide the unvisible file for Mac OS")
args=parser.parse_args()

if args.show==None and args.notshow==None and args.version==None:
	print parser.print_help()
if args.show:
	os.system('defaults write com.apple.finder AppleShowAllFiles -bool true')
	os.system('killall Finder')
	print 'Process done!'
if args.notshow:
	os.system('defaults write com.apple.finder AppleShowAllFiles -bool false')
	os.system('killall Finder')
	print 'Process done!'
if args.version:
	parser.parse_args(['--version'])
	
	

