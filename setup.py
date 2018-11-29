from setuptools import setup, find_packages
import subprocess
import sys

res = subprocess.run(["env/setup_primitiv.sh"], stdout=subprocess.PIPE)
sys.stdout.buffer.write(res.stdout)

sys.path.append('./src')
sys.path.append('./test')

setup(
	name = 'Hoge',
	version = '0.1',
	description = 'This is test codes for Travis CI',
	packages = find_packages(),
	test_suite = 'hogetest.suite'
)

