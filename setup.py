# ======================================================================
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ======================================================================

import setuptools
import pkg_resources
import sys

try:
	if int(pkg_resources.get_distribution("pip").version.split('.')[0]) < 9:
		print('Sorry, pip versions older than 9.0 are not supported, please upgrade pip with "pip install -U pip"')
		sys.exit(-1)
except pkg_resources.DistributionNotFound:
	pass

if tuple(sys.version_info)[:2] < (3, 10):
	print('Sorry, Python versions older 3.10 are not supported, please install a later version of Python')
	sys.exit(-1)


def readme() -> str:
	try:
		with open('README.md') as f:
			return f.read()
	except IOError:
		return ''


setuptools.setup(
	name='AWP',
	version='v0.0.1-beta',
	description='Automated Wildfire Prediction with AI',
	author='Valentina Banner, Alicia Yuen, Maya Yan',
	author_email='valentinavbanner@gmail.com, yuena945@gmail.com, yanm1@kgv.hk',
	long_description=readme(),
	long_description_content_type='text/markdown',
	keywords='AI ML NeuralNetwork fire forest wildfire environment tensorflow tkinter',
	url='https://github.com/realhuman101/AWP',
	package_dir={'': 'src'},
	packages=setuptools.find_packages('src'),
	include_package_data=True,
	python_requires='>=3.10.0, <=3.10.9',
	license_files=('LICENSE', 'COPYING'),
	license='GPL v3',
	install_requires=[
		"tensorflow==2.10.0",
		"keras==2.10.0",
		"numpy>=1.24.1",
		"pandas>=1.5.2",
		"requests>=2.28.1",
		"matplotlib>=3.5.1",
		"scikit-learn>=1.2.1",
		"scipy>=1.10.0",
		"pyglet>=2.0.dev18"
	],
	entry_points={
		'gui_scripts': [
			'AWP = gui:start'
		]
	}
)
