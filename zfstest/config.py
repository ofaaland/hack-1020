import ConfigParser
import os

# anticipated sources of configuration information:
#  (highest priority) command line arguments
#                     user config file (via cmd line or /etc/zfstest.ini)
#  (lowest priority)  default configuration in this project

config_filename='zfs-test.cfg'
config_section = 'ZFS-test'
config_list_prefix = 'list:'
configuration_description = {
	'test_disks'	: config_list_prefix + ' disks used for DESTRUCTIVE testing, comma delimited',
	'test_duration'	: '"short" or "long", determines subset of tests executed'
}

def comma_delim_list(in_string):
	tmp = []
	for item in in_string.split(','):
		tmp.append(item)
	return tmp

def load_config_file(config_file, config_dict):
	try:
		f = open(config_file)
		f.close()
	except IOError as (errno,strerr):
		return

	config_from_file = ConfigParser.RawConfigParser()
	config_from_file.read(config_file)

	# record values for keys defined above
	# replace any existing value for keys specified
	for key in configuration_description.keys():
		try:
			value = config_from_file.get(config_section,key)
		except ConfigParser.NoOptionError:
			pass
		else:
			if configuration_description[key].startswith(config_list_prefix):
				config_dict[key] = comma_delim_list(value)
			else:
				config_dict[key] = value

def load_config():
	configuration = {}
	path_to_this_module_file = os.path.dirname(os.path.realpath(__file__)) + "/"

	load_config_file(path_to_this_module_file + config_filename, configuration)
	load_config_file('/etc/' + config_filename, configuration)
	# config specified via cli options to be processed here

	return configuration

def print_config(config_dict):
	for key in config_dict.keys():
		if isinstance(config_dict[key], list):
			print key + " => " + ','.join(config_dict[key])
		else:
			print key + " => " + config_dict[key]

#test_config = load_config()
#print_config(test_config)
