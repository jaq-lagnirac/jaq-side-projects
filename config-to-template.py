# Justin Caringal
# A tool to take a config.json file and output a
# template .json config file

import os
import sys
import json
import argparse
import logging

SCRIPT_PATH = os.path.abspath(__file__)
FORMAT = '[%(asctime)s] %(levelname)s %(message)s'
l = logging.getLogger()
lh = logging.StreamHandler()
lh.setFormatter(logging.Formatter(FORMAT))
l.addHandler(lh)
l.setLevel(logging.INFO)
debug = l.debug; info = l.info; warning = l.warning; error = l.error

DESCRIPTION = '''

A tool to take a config.json file and outputs a template
JSON file that takes out all of the sensitive information
and replaces it with data types. Works with any JSON file.

'''

EPILOG = '''
'''

class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter,
    argparse.RawDescriptionHelpFormatter):
  pass
parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG,
  formatter_class=CustomFormatter)

parser.add_argument('config',
                    help='.json file to be converted')
parser.add_argument('-i', '--indent',
                    type=int,
                    default=4,
                    help='Set indent for JSON file, for one line set to -1')
parser.add_argument('-o', '--output-dir',
                    default='.',
                    help='Set output directory, defaults to current working directory')
parser.add_argument('-f', '--force',
                    action='store_true',
                    help='Forces overwrite of template if file already exists')
parser.add_argument('-v', '--verbose',
                    action='store_true',
                    help='Set logging level to DEBUG')

args = parser.parse_args()

if args.verbose:
  l.setLevel(logging.DEBUG)


def force_exit(msg):
  '''Shortcut for exception handling message'''
  error(msg)
  info('Exiting program.')
  sys.exit(1)

def extract_type(value):
  '''Extracts variable type'''
  var_type = str(type(value))
  start_indx = var_type.index('\'') + 1 # finds first '
  end_indx = var_type.index('\'', start_indx) # finds second '
  extracted_var_type = var_type[start_indx : end_indx]
  return extracted_var_type


debug('%s begin', SCRIPT_PATH)


# ensures output dir valid, exits program otherwise
if not os.path.exists(args.output_dir):
  force_exit(f'Output directory does not exist: {args.output_dir}')

# opens template file into dict
with open(args.config, 'r') as config:
  config_dict = json.loads(config.read())

# iterates through dict
for key, value in config_dict.items():
  
  # extracts variable type
  var_type = extract_type(value)
  debug(f'{key}\t\t\t{value}\t\t\t{var_type}')

  # replaces value at key with var_type
  config_dict[key] = var_type

# extracts extension, generates new file name
basename = os.path.basename(args.config)
extension_indx = basename.rindex('.')
extension = basename[extension_indx : ]
debug(f'Extension - {extension}')
# generates new file name
template_name = basename.replace(extension, f'.template{extension}')
info(f'Filename generated: {template_name}')
# generates full path
template_path = os.path.join(args.output_dir, template_name)
info(f'File path generated: {template_path}')

# checks if config file exists in template_path, notifies user
path_exists = os.path.exists(template_path)
if not args.force and path_exists:
  force_exit('Template config file already exists. Use --force to overwrite existing file.')
elif path_exists: # force flag used
  info('Template config file already exists. Overwriting.')
else: # path does not exist
  info('Creating new template config file.')

# creates new template json file
with open(template_path, 'w') as template:
  indent = args.indent
  if indent > 0: # prints with indent
    template.write(json.dumps(config_dict, indent = args.indent))
  else: # one single line
    template.write(json.dumps(config_dict))

info('Template file created. Info dumped.')


debug('%s end', SCRIPT_PATH)
