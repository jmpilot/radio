import subprocess
import sys

#key,value are radio{<command>:<stream URL>}
#should probably decouple this logic
master_stream_urls = {
'WCPE':
'https://playerservices.streamtheworld.com/api/livestream-redirect/WCPE_FM.mp3',
'WFMU':
'http://stream0.wfmu.org/freeform-high.aac',
'WKNC':
'https://streaming.live365.com/a45877',
'WNCW':
'https://ice64.securenetsystems.net/WNCW',
'WUNC':
'https://wunc-ice.streamguys1.com/wunc-128-mp3'
}


def build_command(user_choice_dict_key):
		
	for k,v in master_stream_urls.items():
			if k.lower() == user_choice_dict_key:
				url = master_stream_urls[k]
				command = ['ffplay','-vn','-nodisp', '-i', url]
				return command
			else:
				continue
	

def play_station():

	user_arg = sys.argv[1].lower()
	command = build_command(user_arg)

	try:
		subprocess.run(command)

	except Exception as e:
		print(f'!!subprocess ffmpeg run error: {e}')

def main():

	play_station()
	

if __name__ == '__main__':
	main()